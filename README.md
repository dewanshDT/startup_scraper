# Startup India API Scraper

A robust Python scraper for extracting startup data from the Startup India API with comprehensive error handling, rate limiting, and progress tracking.

## Features

✅ **Three-Phase Scraping Process**

- Phase 1: Fetch all startup IDs from listing API
- Phase 2: Fetch detailed information for each startup
- Phase 3: Fetch contact information via CIN API

✅ **Robust Error Handling**

- Automatic retry logic with exponential backoff
- Graceful handling of missing/invalid data
- Detailed error logging

✅ **Progress Tracking**

- Checkpoint system to resume interrupted scraping
- Periodic saves every 50 items
- Progress tracking in `progress.json`

✅ **Rate Limiting**

- Configurable delay between requests (default: 0.5s)
- Prevents overwhelming the API

✅ **Rich Data Output**

- Comprehensive JSON output with all startup details
- Contact information (email, phone, address)
- Location, industry, sectors, stage, funding status
- Timestamps and recognition details

## Installation

1. Install Python 3.7 or higher
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Simply run the script:

```bash
python startup_scraper.py
```

### Configuration

Edit the `CONFIG` dictionary in `startup_scraper.py` to customize:

```python
CONFIG = {
    "state_id": "5f48ce592a9bb065cdf9fb25",  # Change to scrape different state
    "rate_limit_delay": 0.5,  # Seconds between requests
    "retry_attempts": 3,  # Number of retry attempts
    "retry_backoff": 2,  # Exponential backoff factor
    "checkpoint_interval": 50,  # Save every N items
}
```

### Resuming Interrupted Scraping

The scraper automatically saves progress. If interrupted:

- Run the script again - it will resume from where it left off
- Uses `checkpoint_ids.json` and `progress.json` to track state

### Output Files

- **`startups_data.json`** - Final output with all scraped data
- **`checkpoint_ids.json`** - List of all startup IDs (Phase 1 checkpoint)
- **`progress.json`** - Current progress tracker
- **`scraper.log`** - Detailed log of all operations

## Output Data Structure

```json
{
  "id": "68a9739ee4b021e0fa5be7d8",
  "name": "SHRI GANPATI INDUSTRIES",
  "legalName": "SHRI GANPATI INDUSTRIES",
  "role": "Startup",
  "cin": "2706252732",
  "pan": "AFGFS1706L",
  "dippNumber": "DIPP219300",
  "dippRecognitionStatus": "RECOGNISED",
  "dippCertified": true,
  "stage": "Validation",
  "funded": false,
  "ideaBrief": "Description of the startup...",
  "website": "https://example.com",
  "linkedInUrl": null,
  "location": {
    "country": "India",
    "state": "Chhattisgarh",
    "city": "Raipur"
  },
  "industry": "Renewable Energy",
  "sectors": ["Manufacture of Electrical Equipment"],
  "lookingToConnectTo": ["Investor", "Mentor", "Startup"],
  "badges": ["CIN_CERTIFIED"],
  "createdOn": 1755935646181,
  "publishedOn": 1756710210775,
  "contact": {
    "email": "startup@example.com",
    "phone": "9229330903",
    "registeredAddress": "Behind Arjun Enclave"
  },
  "companyStatus": "Active",
  "incorporationDate": "12-03-2025"
}
```

## API Endpoints Used

1. **Listing API** (POST): `https://api.startupindia.gov.in/sih/api/noauth/search/profiles`
2. **Details API** (GET): `https://api.startupindia.gov.in/sih/api/common/replica/user/profile/{id}`
3. **CIN API** (GET): `https://api.startupindia.gov.in/sih/api/noauth/dpiit/services/cin/info?cin={cin}`

## Error Handling

The scraper handles various error scenarios:

- Network timeouts and connection errors
- HTTP 429 (Too Many Requests) with automatic retry
- Missing or invalid CIN numbers
- API response validation
- Malformed JSON responses

## Performance

- Processes ~7,200 requests per hour (with 0.5s delay)
- Expected time for 1,391 startups: ~10-15 minutes
- Memory efficient with periodic checkpoints

## Logging

All operations are logged to both console and `scraper.log`:

- INFO: Progress updates, successful operations
- WARNING: Skipped items, missing data
- ERROR: Failed requests, exceptions

## Tips

1. **For faster scraping**: Reduce `rate_limit_delay` (but be careful not to overwhelm the API)
2. **For slower/unreliable connections**: Increase `retry_attempts`
3. **To scrape different states**: Change the `state_id` in CONFIG
4. **To scrape all of India**: Use an empty array for states: `"states": []`

## Troubleshooting

**Script stops unexpectedly:**

- Check `scraper.log` for errors
- Simply run again - it will resume automatically

**No contact information retrieved:**

- Some startups may not have valid CIN numbers
- CIN API may not have data for all CINs

**Rate limiting errors:**

- Increase `rate_limit_delay` to 1.0 or higher
- Check your internet connection

## License

MIT License - Feel free to modify and use as needed.
