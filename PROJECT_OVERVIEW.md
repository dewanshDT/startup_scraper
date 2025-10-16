# Startup India API Scraper - Project Overview

## 📁 Project Structure

```
scrape/
├── startup_scraper.py              # Main scraper script
├── analyze_data.py                 # Data analysis and export utility
├── config.json                     # Configuration file
├── requirements.txt                # Python dependencies
│
├── QUICKSTART.md                   # Quick start guide
├── README.md                       # Full documentation
├── STATE_IDS.md                    # Reference for Indian state IDs
├── PROJECT_OVERVIEW.md             # This file
│
├── listing_api_example_response.json    # Example API responses
├── details_api_example_response.json    # (for reference)
└── cin_details_api_example_response.json
```

## 🎯 Core Components

### 1. **startup_scraper.py** - Main Scraper

The heart of the project. Features:

- **3-Phase Scraping Process**
  - Phase 1: Fetch all startup IDs
  - Phase 2: Fetch detailed information
  - Phase 3: Fetch contact information via CIN
- **Robust Error Handling**: Retries, timeouts, graceful failures
- **Rate Limiting**: Configurable delays between requests
- **Progress Tracking**: Resume from where you left off
- **Checkpoint System**: Saves progress periodically
- **Comprehensive Logging**: All operations logged to file and console

### 2. **analyze_data.py** - Data Analysis Tool

Post-scraping analysis and export utility. Features:

- Statistical analysis and insights
- Distribution charts (stage, industry, location)
- CSV export functionality
- Filtered data export (by stage, industry, city, etc.)
- Interactive command-line interface

### 3. **config.json** - Configuration File

Central configuration for all settings:

- API endpoints
- State selection
- Rate limiting parameters
- Retry logic configuration
- Checkpoint intervals

## 🔄 Workflow

```
1. Configure
   └── Edit config.json to set states and parameters

2. Scrape
   └── Run: python startup_scraper.py
   └── Outputs: startups_data.json

3. Analyze
   └── Run: python analyze_data.py
   └── View statistics and export to CSV
```

## 📊 Data Flow

```
Listing API → Startup IDs
     ↓
Details API → Full Startup Info (with CIN)
     ↓
CIN API → Contact Information
     ↓
Merged Rich Data → JSON Output
```

## 🎨 Key Features

### ✅ Resumable Scraping

- Interrupt anytime with `Ctrl+C`
- Progress automatically saved
- Resume by running script again

### ✅ Intelligent Rate Limiting

- Prevents API overwhelm
- Configurable delays
- Automatic retry on failures

### ✅ Comprehensive Data

Each startup includes:

- Basic info (name, CIN, PAN, DIPP number)
- Location (country, state, city)
- Industry and sectors
- Stage and funding status
- Contact information (email, phone, address)
- Recognition and badges
- Website and LinkedIn
- Timestamps

### ✅ Error Resilience

- Network failures handled gracefully
- Missing data doesn't break scraping
- Invalid CINs skipped automatically
- Detailed error logging

## 🚀 Quick Commands

```bash
# Install
pip install -r requirements.txt

# Scrape
python startup_scraper.py

# Analyze
python analyze_data.py
```

## 📝 Output Files

| File                  | Purpose                   | Size (approx) |
| --------------------- | ------------------------- | ------------- |
| `startups_data.json`  | Main output with all data | 2-5 MB        |
| `checkpoint_ids.json` | All startup IDs           | 50-100 KB     |
| `progress.json`       | Progress tracker          | 1 KB          |
| `scraper.log`         | Detailed logs             | 1-10 MB       |
| `*.csv`               | CSV exports (optional)    | Variable      |

## ⚙️ Configuration Options

### Rate Limiting

```json
"rate_limit_delay": 0.5  // Seconds between requests
```

- Lower = Faster (0.2-0.3)
- Higher = Safer (1.0-2.0)
- Default: 0.5

### State Selection

```json
"scrape_all_states": false,
"states": ["5f48ce592a9bb065cdf9fb25"]  // Chhattisgarh
```

### Retry Logic

```json
"retry_attempts": 3,
"retry_backoff": 2  // Exponential backoff factor
```

### Checkpoints

```json
"checkpoint_interval": 50  // Save every N startups
```

## 📈 Performance Metrics

**For ~1,400 startups (Chhattisgarh):**

- Phase 1 (IDs): ~2-3 minutes
- Phase 2-3 (Details + CIN): ~8-12 minutes
- **Total**: ~10-15 minutes
- **Requests**: ~2,800 total
- **Data Size**: ~3 MB

**Scaling:**

- All of India: ~50,000 startups
- Estimated time: 5-6 hours
- Estimated data: ~100-150 MB

## 🔍 Use Cases

1. **Market Research**: Analyze startup distribution across India
2. **Lead Generation**: Extract contact information for outreach
3. **Competitive Analysis**: Filter by industry/sector
4. **Investment Research**: Find funded vs unfunded startups
5. **Geographic Analysis**: State/city-wise distribution
6. **Trend Analysis**: Track startup stages and industries

## 🛠️ Customization

### Scrape Different States

See `STATE_IDS.md` for all state IDs

### Scrape Specific Industries

Edit the payload in `startup_scraper.py`:

```python
"industries": ["5f48ce5f2a9bb065cdfa1742"],  # Add industry IDs
```

### Change Data Fields

Modify `extract_startup_data()` in `startup_scraper.py`

### Custom Analysis

Extend `analyze_data.py` with your own functions

## 🔐 Data Privacy

**Important Notes:**

- This scraper uses public APIs
- Contact information is from public government records
- Respect data usage policies
- Consider GDPR/data protection laws if sharing data
- Use responsibly for legitimate purposes

## 📚 Documentation Files

- **QUICKSTART.md**: Get started in 3 steps
- **README.md**: Comprehensive guide with all details
- **STATE_IDS.md**: Reference for state IDs
- **PROJECT_OVERVIEW.md**: This file - high-level overview

## 🐛 Troubleshooting

| Issue             | Solution                                  |
| ----------------- | ----------------------------------------- |
| Script stops      | Check `scraper.log`, run again to resume  |
| No contact info   | Normal - not all startups have valid CINs |
| Rate limit errors | Increase `rate_limit_delay` in config     |
| Network errors    | Check internet, script will auto-retry    |
| Incomplete data   | Some fields may be null - this is normal  |

## 🎓 Learning Resources

The code is well-commented and modular. Great for learning:

- API scraping with Python
- Error handling and retry logic
- Progress tracking and checkpoints
- Data extraction and transformation
- Rate limiting implementation
- Logging best practices

## 💡 Next Steps

After scraping:

1. ✅ Analyze data with `analyze_data.py`
2. ✅ Export to CSV for Excel/Google Sheets
3. ✅ Filter for specific criteria
4. ✅ Integrate with your own systems
5. ✅ Build visualizations or dashboards

## 📞 Support

- Check `scraper.log` for detailed error messages
- Review example JSON files for data structure
- All functions have docstrings explaining their purpose
- Configuration is self-documented in `config.json`

---

**Happy Scraping! 🚀**

Built with ❤️ for the Indian startup ecosystem
