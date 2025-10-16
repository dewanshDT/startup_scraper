# 🚀 START HERE - Startup India API Scraper

Welcome! This is your complete scraping solution for the Startup India API.

## ⚡ Quick Start (3 Commands)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the scraper
python3 startup_scraper.py

# 3. Analyze the data
python3 analyze_data.py
```

That's it! You'll have all startup data in `startups_data.json`

## 📚 Documentation Files

Read these in order:

1. **INSTALL.md** - Installation instructions
2. **QUICKSTART.md** - Get started in 5 minutes
3. **README.md** - Complete documentation
4. **PROJECT_OVERVIEW.md** - Architecture and design
5. **STATE_IDS.md** - Reference for configuring states

## 📁 Main Files

### Core Scripts

- **`startup_scraper.py`** - Main scraper (run this first)
- **`analyze_data.py`** - Data analysis tool (run after scraping)
- **`config.json`** - Configuration (edit to customize)
- **`requirements.txt`** - Python dependencies

### Documentation

- **`00_START_HERE.md`** - This file
- **`INSTALL.md`** - Installation guide
- **`QUICKSTART.md`** - Quick start guide
- **`README.md`** - Full documentation
- **`PROJECT_OVERVIEW.md`** - Technical overview
- **`STATE_IDS.md`** - State ID reference

### Reference Files (Examples)

- `listing_api_example_response.json`
- `details_api_example_response.json`
- `cin_details_api_example_response.json`

## 🎯 What This Does

### The Scraper:

1. ✅ Fetches all startup IDs from Startup India API
2. ✅ Gets detailed information for each startup
3. ✅ Retrieves contact information (email, phone) via CIN
4. ✅ Saves everything to a rich JSON file
5. ✅ Handles errors, retries, and progress tracking

### The Output:

- Complete startup data with contact info
- Location, industry, stage, funding status
- Recognition details, badges, websites
- All in a structured JSON format

## 🔧 Configuration

Edit `config.json` to customize:

```json
{
  "state_id": "5f48ce592a9bb065cdf9fb25", // Change state
  "rate_limit_delay": 0.5, // Faster/slower scraping
  "scrape_all_states": false // Set to true for all India
}
```

See `STATE_IDS.md` for all available state IDs.

## 📊 Features

- ⚡ **Fast**: Scrapes 1,400 startups in ~10-15 minutes
- 🛡️ **Robust**: Automatic retries, error handling
- 💾 **Resumable**: Interrupt anytime, resume later
- 📝 **Logged**: Everything logged to `scraper.log`
- 🎯 **Accurate**: 3-phase process ensures complete data
- 🔄 **Flexible**: Configurable for any state or all of India

## 📈 Expected Results

For Chhattisgarh (default):

- **~1,400 startups**
- **~10-15 minutes**
- **~3 MB data**
- **Contact info for ~60-70% of startups**

For all of India:

- **~50,000 startups**
- **~5-6 hours**
- **~100-150 MB data**

## 🎨 Data Analysis

After scraping, use `analyze_data.py` to:

- View statistics and distributions
- Export to CSV for Excel/Sheets
- Filter by stage, industry, city, etc.
- Generate insights

## ⚠️ Important Notes

1. **Internet Required**: Stable connection needed
2. **Rate Limiting**: Default 0.5s delay between requests
3. **Progress Saved**: Can interrupt anytime (Ctrl+C)
4. **Resume Auto**: Just run again to continue
5. **Public Data**: Uses public government APIs

## 🆘 Troubleshooting

**Dependencies not installed?**

```bash
pip install -r requirements.txt
```

**Script stops unexpectedly?**

- Check `scraper.log`
- Simply run again - it resumes automatically

**Need faster scraping?**

- Edit `config.json`, set `rate_limit_delay: 0.3`

**Want different state?**

- Check `STATE_IDS.md`
- Update `config.json`

## 📦 Output Files

After running:

- ✅ `startups_data.json` - Your main output
- 📋 `checkpoint_ids.json` - Backup of IDs
- 📍 `progress.json` - Progress tracker
- 📝 `scraper.log` - Detailed logs

## 🎓 Learning Resources

This project demonstrates:

- API scraping best practices
- Error handling and retries
- Progress tracking systems
- Rate limiting implementation
- Data extraction and transformation
- Logging and debugging

## 💡 Next Steps

1. ✅ Install: `pip install -r requirements.txt`
2. ✅ Scrape: `python3 startup_scraper.py`
3. ✅ Analyze: `python3 analyze_data.py`
4. ✅ Export: Choose CSV option in analysis
5. ✅ Use: Import into your systems

## 🎯 Common Use Cases

- **Market Research**: Analyze startup ecosystem
- **Lead Generation**: Extract contact information
- **Competitive Analysis**: Filter by industry
- **Investment Research**: Find investment opportunities
- **Geographic Analysis**: State/city distributions
- **Trend Analysis**: Track stages and sectors

## 📞 Support

- 📝 Check `scraper.log` for errors
- 📖 Read the relevant documentation
- 🔍 All code is commented and documented
- 🎯 Example responses included for reference

---

## 🚀 Ready to Start?

```bash
pip install -r requirements.txt
python3 startup_scraper.py
```

**That's all you need!**

For detailed instructions, see `QUICKSTART.md`

---

Built with ❤️ for data-driven insights into the Indian startup ecosystem.

**Happy Scraping! 🎉**
