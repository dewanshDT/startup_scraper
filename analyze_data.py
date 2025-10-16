#!/usr/bin/env python3
"""
Data Analysis Utility for Scraped Startup Data
Provides statistics and insights from the scraped startup data.
"""

import json
from pathlib import Path
from collections import Counter
from typing import List, Dict


def load_data(file_path: str = "startups_data.json") -> List[Dict]:
    """Load scraped startup data."""
    with open(file_path, "r") as f:
        return json.load(f)


def analyze_data(data: List[Dict]):
    """Analyze and print statistics about the scraped data."""
    total = len(data)

    print("=" * 70)
    print("STARTUP DATA ANALYSIS")
    print("=" * 70)
    print(f"\nTotal Startups: {total}")

    # Contact information statistics
    with_cin = sum(1 for s in data if s.get("cin"))
    with_email = sum(1 for s in data if s.get("contact", {}).get("email"))
    with_phone = sum(1 for s in data if s.get("contact", {}).get("phone"))

    print("\n" + "-" * 70)
    print("CONTACT INFORMATION")
    print("-" * 70)
    print(f"Startups with CIN: {with_cin} ({with_cin/total*100:.1f}%)")
    print(f"Startups with Email: {with_email} ({with_email/total*100:.1f}%)")
    print(f"Startups with Phone: {with_phone} ({with_phone/total*100:.1f}%)")

    # Recognition status
    dipp_certified = sum(1 for s in data if s.get("dippCertified"))
    recognised = sum(1 for s in data if s.get("dippRecognitionStatus") == "RECOGNISED")

    print("\n" + "-" * 70)
    print("RECOGNITION STATUS")
    print("-" * 70)
    print(f"DIPP Certified: {dipp_certified} ({dipp_certified/total*100:.1f}%)")
    print(f"DIPP Recognised: {recognised} ({recognised/total*100:.1f}%)")

    # Funding status
    funded = sum(1 for s in data if s.get("funded"))
    print(f"\nFunded Startups: {funded} ({funded/total*100:.1f}%)")

    # Stage distribution
    stages = [s.get("stage") for s in data if s.get("stage")]
    stage_counts = Counter(stages)

    print("\n" + "-" * 70)
    print("STAGE DISTRIBUTION")
    print("-" * 70)
    for stage, count in stage_counts.most_common():
        print(f"{stage:20} : {count:4} ({count/total*100:.1f}%)")

    # Location distribution
    cities = [
        s.get("location", {}).get("city")
        for s in data
        if s.get("location", {}).get("city")
    ]
    city_counts = Counter(cities)

    print("\n" + "-" * 70)
    print("TOP 10 CITIES")
    print("-" * 70)
    for city, count in city_counts.most_common(10):
        print(f"{city:20} : {count:4} ({count/total*100:.1f}%)")

    # Industry distribution
    industries = [s.get("industry") for s in data if s.get("industry")]
    industry_counts = Counter(industries)

    print("\n" + "-" * 70)
    print("TOP 10 INDUSTRIES")
    print("-" * 70)
    for industry, count in industry_counts.most_common(10):
        print(f"{industry:30} : {count:4} ({count/total*100:.1f}%)")

    # Sector distribution
    all_sectors = []
    for s in data:
        sectors = s.get("sectors", [])
        all_sectors.extend(sectors)
    sector_counts = Counter(all_sectors)

    print("\n" + "-" * 70)
    print("TOP 10 SECTORS")
    print("-" * 70)
    for sector, count in sector_counts.most_common(10):
        print(f"{sector:40} : {count:4}")

    # Looking to connect
    all_connections = []
    for s in data:
        connections = s.get("lookingToConnectTo", [])
        all_connections.extend(connections)
    connection_counts = Counter(all_connections)

    print("\n" + "-" * 70)
    print("LOOKING TO CONNECT TO")
    print("-" * 70)
    for connection, count in connection_counts.most_common():
        print(f"{connection:15} : {count:4} ({count/total*100:.1f}%)")

    # Badges
    all_badges = []
    for s in data:
        badges = s.get("badges", [])
        all_badges.extend(badges)
    badge_counts = Counter(all_badges)

    print("\n" + "-" * 70)
    print("BADGES")
    print("-" * 70)
    for badge, count in badge_counts.most_common():
        print(f"{badge:20} : {count:4} ({count/total*100:.1f}%)")

    # Website/LinkedIn presence
    with_website = sum(1 for s in data if s.get("website"))
    with_linkedin = sum(1 for s in data if s.get("linkedInUrl"))

    print("\n" + "-" * 70)
    print("ONLINE PRESENCE")
    print("-" * 70)
    print(f"With Website: {with_website} ({with_website/total*100:.1f}%)")
    print(f"With LinkedIn: {with_linkedin} ({with_linkedin/total*100:.1f}%)")

    print("\n" + "=" * 70)


def export_filtered_data(data: List[Dict], filter_criteria: Dict, output_file: str):
    """Export filtered data based on criteria."""
    filtered = data

    if "stage" in filter_criteria:
        filtered = [s for s in filtered if s.get("stage") == filter_criteria["stage"]]

    if "industry" in filter_criteria:
        filtered = [
            s for s in filtered if s.get("industry") == filter_criteria["industry"]
        ]

    if "city" in filter_criteria:
        filtered = [
            s
            for s in filtered
            if s.get("location", {}).get("city") == filter_criteria["city"]
        ]

    if "funded" in filter_criteria:
        filtered = [s for s in filtered if s.get("funded") == filter_criteria["funded"]]

    if "has_email" in filter_criteria and filter_criteria["has_email"]:
        filtered = [s for s in filtered if s.get("contact", {}).get("email")]

    with open(output_file, "w") as f:
        json.dump(filtered, f, indent=2, ensure_ascii=False)

    print(f"Exported {len(filtered)} startups to {output_file}")


def export_to_csv(data: List[Dict], output_file: str = "startups_data.csv"):
    """Export data to CSV format."""
    import csv

    if not data:
        print("No data to export")
        return

    fieldnames = [
        "id",
        "name",
        "legalName",
        "cin",
        "pan",
        "dippNumber",
        "dippRecognitionStatus",
        "stage",
        "funded",
        "industry",
        "country",
        "state",
        "city",
        "email",
        "phone",
        "website",
        "linkedInUrl",
        "companyStatus",
        "incorporationDate",
    ]

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for startup in data:
            row = {
                "id": startup.get("id"),
                "name": startup.get("name"),
                "legalName": startup.get("legalName"),
                "cin": startup.get("cin"),
                "pan": startup.get("pan"),
                "dippNumber": startup.get("dippNumber"),
                "dippRecognitionStatus": startup.get("dippRecognitionStatus"),
                "stage": startup.get("stage"),
                "funded": startup.get("funded"),
                "industry": startup.get("industry"),
                "country": startup.get("location", {}).get("country"),
                "state": startup.get("location", {}).get("state"),
                "city": startup.get("location", {}).get("city"),
                "email": startup.get("contact", {}).get("email"),
                "phone": startup.get("contact", {}).get("phone"),
                "website": startup.get("website"),
                "linkedInUrl": startup.get("linkedInUrl"),
                "companyStatus": startup.get("companyStatus"),
                "incorporationDate": startup.get("incorporationDate"),
            }
            writer.writerow(row)

    print(f"Exported {len(data)} startups to {output_file}")


def main():
    """Main entry point for data analysis."""
    data_file = Path("startups_data.json")

    if not data_file.exists():
        print(f"Error: {data_file} not found!")
        print("Please run the scraper first: python startup_scraper.py")
        return

    print("Loading data...")
    data = load_data()

    # Display analysis
    analyze_data(data)

    # Optional: Export to CSV
    print("\n" + "=" * 70)
    response = input("\nExport to CSV? (y/n): ").strip().lower()
    if response == "y":
        export_to_csv(data)

    # Optional: Export filtered data
    print("\n" + "=" * 70)
    response = input("\nExport filtered data? (y/n): ").strip().lower()
    if response == "y":
        print("\nAvailable filters:")
        print("1. By stage")
        print("2. By industry")
        print("3. By city")
        print("4. Funded only")
        print("5. With email only")

        choice = input("\nEnter filter number (or press Enter to skip): ").strip()

        if choice == "1":
            stage = input("Enter stage: ").strip()
            export_filtered_data(
                data, {"stage": stage}, f"startups_{stage.lower()}.json"
            )
        elif choice == "2":
            industry = input("Enter industry: ").strip()
            export_filtered_data(
                data,
                {"industry": industry},
                f"startups_{industry.lower().replace(' ', '_')}.json",
            )
        elif choice == "3":
            city = input("Enter city: ").strip()
            export_filtered_data(
                data, {"city": city}, f"startups_{city.lower().replace(' ', '_')}.json"
            )
        elif choice == "4":
            export_filtered_data(data, {"funded": True}, "startups_funded.json")
        elif choice == "5":
            export_filtered_data(data, {"has_email": True}, "startups_with_email.json")


if __name__ == "__main__":
    main()
