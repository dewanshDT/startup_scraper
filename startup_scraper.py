#!/usr/bin/env python3
"""
Startup India API Scraper
Scrapes startup data from Startup India API with proper error handling and rate limiting.
"""

import json
import time
import logging
from typing import List, Dict, Optional, Any
from pathlib import Path
from datetime import datetime
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Default configuration
DEFAULT_CONFIG = {
    "listing_api_url": "https://api.startupindia.gov.in/sih/api/noauth/search/profiles",
    "details_api_url": "https://api.startupindia.gov.in/sih/api/common/replica/user/profile/",
    "cin_api_url": "https://api.startupindia.gov.in/sih/api/noauth/dpiit/services/cin/info",
    "state_id": "5f48ce592a9bb065cdf9fb25",  # Chhattisgarh
    "rate_limit_delay": 0.5,  # seconds between requests
    "retry_attempts": 3,
    "retry_backoff": 2,  # exponential backoff factor
    "checkpoint_interval": 50,  # save checkpoint every N items
    "scrape_all_states": False,
    "states": ["5f48ce592a9bb065cdf9fb25"],
}


def load_config() -> Dict[str, Any]:
    """Load configuration from config.json or use defaults."""
    config_file = Path("config.json")
    if config_file.exists():
        try:
            with open(config_file, "r") as f:
                config = json.load(f)
                logger.info("Loaded configuration from config.json")
                return config
        except Exception as e:
            logger.warning(f"Failed to load config.json: {e}. Using defaults.")
    return DEFAULT_CONFIG.copy()


# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("scraper.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


class StartupScraper:
    """Main scraper class for Startup India data."""

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.session = self._create_session()
        self.checkpoint_file = Path("checkpoint_ids.json")
        self.progress_file = Path("progress.json")
        self.output_file = Path("startups_data.json")

    def _create_session(self) -> requests.Session:
        """Create a requests session with retry logic."""
        session = requests.Session()
        retry_strategy = Retry(
            total=self.config["retry_attempts"],
            backoff_factor=self.config["retry_backoff"],
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST"],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session

    def _rate_limit(self):
        """Apply rate limiting between requests."""
        time.sleep(self.config["rate_limit_delay"])

    def get_listing_page(self, page_num: int) -> Optional[Dict]:
        """Fetch a single page from the listing API."""
        # Determine which states to scrape
        if self.config.get("scrape_all_states", False):
            states = []  # Empty array means all states
        else:
            states = self.config.get("states", [self.config.get("state_id")])

        payload = {
            "query": "",
            "focusSector": False,
            "industries": [],
            "sectors": [],
            "states": states,
            "cities": [],
            "stages": [],
            "badges": [],
            "roles": ["Startup"],
            "page": page_num,
            "sort": {"orders": [{"field": "registeredOn", "direction": "DESC"}]},
            "dpiitRecogniseUser": True,
            "internationalUser": False,
        }

        try:
            self._rate_limit()
            response = self.session.post(
                self.config["listing_api_url"], json=payload, timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching page {page_num}: {e}")
            return None

    def fetch_all_startup_ids(self) -> List[Dict[str, str]]:
        """Fetch all startup IDs from listing API."""
        logger.info("Phase 1: Fetching all startup IDs...")

        # Check if checkpoint exists
        if self.checkpoint_file.exists():
            logger.info("Loading startup IDs from checkpoint...")
            with open(self.checkpoint_file, "r") as f:
                return json.load(f)

        startup_ids = []

        # Get first page to determine total pages
        first_page = self.get_listing_page(0)
        if not first_page:
            logger.error("Failed to fetch first page. Aborting.")
            return []

        total_pages = first_page.get("totalPages", 0)
        total_elements = first_page.get("totalElements", 0)
        logger.info(f"Total pages: {total_pages}, Total startups: {total_elements}")

        # Process first page
        for startup in first_page.get("content", []):
            startup_ids.append({"id": startup.get("id"), "name": startup.get("name")})

        logger.info(
            f"Fetched page 0/{total_pages - 1}: {len(startup_ids)} startups so far"
        )

        # Fetch remaining pages
        for page_num in range(1, total_pages):
            page_data = self.get_listing_page(page_num)
            if page_data:
                for startup in page_data.get("content", []):
                    startup_ids.append(
                        {"id": startup.get("id"), "name": startup.get("name")}
                    )
                logger.info(
                    f"Fetched page {page_num}/{total_pages - 1}: {len(startup_ids)} startups so far"
                )
            else:
                logger.warning(f"Skipping page {page_num} due to error")

        # Save checkpoint
        with open(self.checkpoint_file, "w") as f:
            json.dump(startup_ids, f, indent=2)
        logger.info(
            f"Phase 1 complete: {len(startup_ids)} startup IDs saved to {self.checkpoint_file}"
        )

        return startup_ids

    def get_startup_details(self, startup_id: str) -> Optional[Dict]:
        """Fetch detailed information for a single startup."""
        try:
            self._rate_limit()
            url = f"{self.config['details_api_url']}{startup_id}"
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching details for {startup_id}: {e}")
            return None

    def get_cin_details(self, cin: str) -> Optional[Dict]:
        """Fetch CIN details including contact information."""
        if not cin or cin == "null" or cin == "":
            return None

        try:
            self._rate_limit()
            response = self.session.get(
                self.config["cin_api_url"], params={"cin": cin}, timeout=30
            )
            response.raise_for_status()
            data = response.json()
            if data.get("status"):
                return data.get("data")
            return None
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching CIN details for {cin}: {e}")
            return None

    def extract_startup_data(self, details: Dict, cin_details: Optional[Dict]) -> Dict:
        """Extract and structure relevant data from API responses."""
        user = details.get("user", {})
        startup = user.get("startup", {})
        location = startup.get("location", {})
        focus_area = startup.get("focusArea", {})

        # Extract location info
        country = location.get("country", {}).get("countryName")
        state = location.get("state", {}).get("stateName")
        city = location.get("city", {}).get("districtName")

        # Extract industry and sectors
        industry = focus_area.get("industry", {}).get("industryName")
        sectors = [
            s.get("sectionName")
            for s in focus_area.get("sectors", [])
            if s.get("sectionName")
        ]

        # Build structured data
        data = {
            "id": user.get("uniqueId"),
            "name": user.get("name"),
            "legalName": startup.get("legalName"),
            "role": user.get("role"),
            "cin": startup.get("cin"),
            "pan": startup.get("pan"),
            "dippNumber": startup.get("dippNumber"),
            "dippRecognitionStatus": startup.get("dippRecognitionStatus"),
            "dippCertified": startup.get("dippCertified"),
            "stage": startup.get("stage"),
            "funded": startup.get("funded"),
            "ideaBrief": startup.get("ideaBrief"),
            "website": startup.get("website"),
            "linkedInUrl": startup.get("linkedInUrl"),
            "location": {"country": country, "state": state, "city": city},
            "industry": industry,
            "sectors": sectors,
            "lookingToConnectTo": startup.get("lookingToConnectTo", []),
            "badges": user.get("badges", []),
            "createdOn": user.get("createdOn"),
            "publishedOn": user.get("lastPublishedOn"),
            "contact": {"email": None, "phone": None, "registeredAddress": None},
        }

        # Add CIN details if available
        if cin_details:
            data["contact"]["email"] = cin_details.get("email")
            data["contact"]["phone"] = cin_details.get("registeredContactNo")
            data["contact"]["registeredAddress"] = cin_details.get("registeredAddress")
            data["companyStatus"] = cin_details.get("companyStatus")
            data["incorporationDate"] = cin_details.get("incorpdate")

        return data

    def load_progress(self) -> Dict:
        """Load progress from file."""
        if self.progress_file.exists():
            with open(self.progress_file, "r") as f:
                return json.load(f)
        return {"processed_count": 0, "last_processed_id": None}

    def save_progress(self, processed_count: int, last_id: str):
        """Save progress to file."""
        progress = {
            "processed_count": processed_count,
            "last_processed_id": last_id,
            "timestamp": datetime.now().isoformat(),
        }
        with open(self.progress_file, "w") as f:
            json.dump(progress, f, indent=2)

    def save_data(self, data: List[Dict]):
        """Save scraped data to JSON file."""
        with open(self.output_file, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        logger.info(f"Data saved to {self.output_file}")

    def fetch_all_details(self, startup_ids: List[Dict[str, str]]) -> List[Dict]:
        """Fetch details and CIN info for all startups."""
        logger.info("Phase 2 & 3: Fetching detailed information and contact details...")

        all_data = []
        progress = self.load_progress()
        start_index = progress.get("processed_count", 0)

        # Load existing data if resuming
        if self.output_file.exists() and start_index > 0:
            logger.info(f"Resuming from startup {start_index}...")
            with open(self.output_file, "r") as f:
                all_data = json.load(f)

        total = len(startup_ids)

        for i in range(start_index, total):
            startup_ref = startup_ids[i]
            startup_id = startup_ref["id"]
            startup_name = startup_ref["name"]

            logger.info(f"Processing {i + 1}/{total}: {startup_name} ({startup_id})")

            # Fetch startup details
            details = self.get_startup_details(startup_id)
            if not details:
                logger.warning(f"Skipping {startup_name} - failed to fetch details")
                continue

            # Extract CIN and fetch CIN details
            cin = details.get("user", {}).get("startup", {}).get("cin")
            cin_details = None
            if cin:
                logger.info(f"  Fetching CIN details for {cin}")
                cin_details = self.get_cin_details(cin)
                if cin_details:
                    logger.info(f"  ✓ CIN details retrieved")
                else:
                    logger.info(f"  ✗ CIN details not available")
            else:
                logger.info(f"  No CIN available")

            # Extract and structure data
            startup_data = self.extract_startup_data(details, cin_details)
            all_data.append(startup_data)

            # Save checkpoint periodically
            if (i + 1) % self.config["checkpoint_interval"] == 0:
                self.save_data(all_data)
                self.save_progress(i + 1, startup_id)
                logger.info(f"Checkpoint saved at {i + 1}/{total}")

        # Final save
        self.save_data(all_data)
        self.save_progress(total, startup_ids[-1]["id"] if startup_ids else None)
        logger.info(f"Phase 2 & 3 complete: {len(all_data)} startups processed")

        return all_data

    def run(self):
        """Execute the complete scraping workflow."""
        logger.info("=" * 60)
        logger.info("Starting Startup India Scraper")
        logger.info("=" * 60)
        start_time = time.time()

        # Phase 1: Fetch all startup IDs
        startup_ids = self.fetch_all_startup_ids()
        if not startup_ids:
            logger.error("No startup IDs fetched. Aborting.")
            return

        # Phase 2 & 3: Fetch details and CIN info
        all_data = self.fetch_all_details(startup_ids)

        # Summary
        elapsed_time = time.time() - start_time
        logger.info("=" * 60)
        logger.info("Scraping Complete!")
        logger.info(f"Total startups processed: {len(all_data)}")
        logger.info(f"Time elapsed: {elapsed_time / 60:.2f} minutes")
        logger.info(f"Output file: {self.output_file.absolute()}")
        logger.info("=" * 60)

        # Statistics
        startups_with_cin = sum(1 for s in all_data if s.get("cin"))
        startups_with_contact = sum(
            1 for s in all_data if s.get("contact", {}).get("email")
        )
        logger.info(f"Startups with CIN: {startups_with_cin}")
        logger.info(f"Startups with contact info: {startups_with_contact}")


def main():
    """Main entry point."""
    try:
        config = load_config()
        scraper = StartupScraper(config)
        scraper.run()
    except KeyboardInterrupt:
        logger.info("\nScraping interrupted by user. Progress has been saved.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)


if __name__ == "__main__":
    main()
