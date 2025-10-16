# Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run the Scraper

```bash
python startup_scraper.py
```

The scraper will:

- ✅ Fetch all startup IDs (Phase 1)
- ✅ Fetch detailed information for each startup (Phase 2)
- ✅ Fetch contact information via CIN (Phase 3)
- ✅ Save everything to `startups_data.json`

### Step 3: Analyze the Data

```bash
python analyze_data.py
```

This will show:

- 📊 Statistics and insights
- 📈 Distribution charts
- 💾 Option to export to CSV

---

## ⏸️ Interrupting and Resuming

**The scraper can be safely interrupted at any time!**

- Press `Ctrl+C` to stop
- Run `python startup_scraper.py` again to resume
- It will automatically continue from where it left off

---

## 📂 Output Files

| File                  | Description                             |
| --------------------- | --------------------------------------- |
| `startups_data.json`  | 🎯 Main output with all scraped data    |
| `checkpoint_ids.json` | 💾 All startup IDs (Phase 1 checkpoint) |
| `progress.json`       | 📍 Current progress tracker             |
| `scraper.log`         | 📝 Detailed logs                        |

---

## ⚙️ Configuration

Edit `startup_scraper.py` to change settings:

```python
CONFIG = {
    "state_id": "5f48ce592a9bb065cdf9fb25",  # Chhattisgarh
    "rate_limit_delay": 0.5,  # Seconds between requests
    "checkpoint_interval": 50,  # Save every N items
}
```

### Common State IDs

- Chhattisgarh: `5f48ce592a9bb065cdf9fb25`
- For all states: Set `"states": []` in the payload

---

## 🔍 Example: Finding Specific Startups

After scraping, use `analyze_data.py` to filter:

```bash
python analyze_data.py
# Choose option to export filtered data
# Filter by: stage, industry, city, funding status, or email availability
```

---

## 💡 Tips

1. **Faster scraping**: Reduce `rate_limit_delay` to `0.2` or `0.3`
2. **More reliable**: Increase `retry_attempts` to `5`
3. **Resume from scratch**: Delete `checkpoint_ids.json` and `progress.json`

---

## ❓ Troubleshooting

**Script stops unexpectedly?**

- Check `scraper.log` for errors
- Simply run again - it resumes automatically

**No contact info?**

- Some startups don't have valid CINs
- This is normal and expected

**Taking too long?**

- Reduce `rate_limit_delay` (but be careful!)
- Expected time: ~10-15 minutes for 1,400 startups

---

## 📊 Data Structure Example

```json
{
  "id": "68a9739ee4b021e0fa5be7d8",
  "name": "SHRI GANPATI INDUSTRIES",
  "cin": "2706252732",
  "contact": {
    "email": "startup@example.com",
    "phone": "9229330903"
  },
  "location": {
    "state": "Chhattisgarh",
    "city": "Raipur"
  },
  "industry": "Renewable Energy",
  "stage": "Validation"
}
```

---

## 🎉 That's it!

Your scraper is ready to use. Run `python startup_scraper.py` and watch the magic happen!

For detailed documentation, see [README.md](README.md)
