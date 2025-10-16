# Installation Guide

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Internet connection

## Installation Steps

### Step 1: Install Dependencies

```bash
cd /Users/dewansh/Code/scrape
pip install -r requirements.txt
```

Or install packages individually:

```bash
pip install requests urllib3
```

### Step 2: Verify Installation

```bash
python3 -c "import requests; print('✓ Dependencies installed successfully')"
```

### Step 3: Configure (Optional)

Edit `config.json` to customize:

- States to scrape
- Rate limiting
- Checkpoint intervals

### Step 4: Run the Scraper

```bash
python3 startup_scraper.py
```

## Alternative: Virtual Environment (Recommended)

Using a virtual environment keeps dependencies isolated:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Run scraper
python startup_scraper.py

# When done, deactivate
deactivate
```

## Troubleshooting Installation

### Issue: pip not found

```bash
# Install pip
python3 -m ensurepip --upgrade
```

### Issue: Permission denied

```bash
# Use --user flag
pip install --user -r requirements.txt
```

### Issue: SSL certificate errors

```bash
# Update certificates
pip install --upgrade certifi
```

## Verify Everything Works

After installation, run this quick test:

```bash
python3 -c "
import requests
import json
from pathlib import Path
print('✓ All modules imported successfully')
print('✓ Ready to scrape!')
"
```

## Next Steps

1. **Quick Start**: See `QUICKSTART.md`
2. **Full Documentation**: See `README.md`
3. **Configure States**: See `STATE_IDS.md`
4. **Project Overview**: See `PROJECT_OVERVIEW.md`

## System Requirements

- **OS**: macOS, Linux, or Windows
- **Python**: 3.7+
- **RAM**: 512 MB minimum (2 GB recommended)
- **Disk Space**: 100 MB for data
- **Network**: Stable internet connection

## Support

If you encounter issues:

1. Check `scraper.log` after running
2. Ensure Python version: `python3 --version`
3. Update pip: `pip install --upgrade pip`
4. Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`
