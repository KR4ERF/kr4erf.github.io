# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import subprocess
import sys

sys.path.append(os.curdir)
from pelican import signals
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://kr4erf.radio"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""

# If we're in GitHub Actions, fetch gh-pages to ensure we have the branch locally
if os.environ.get('GITHUB_ACTIONS') == 'true':
    print("Fetching gh-pages branch...")
    subprocess.run(['git', 'fetch', 'origin', 'gh-pages:gh-pages'], capture_output=True)

# Dynamically generate the list of apps from the gh-pages branch without extracting files
FLATPAK_APPS = []
try:
    # Use the local gh-pages branch we just fetched
    # App refs look like com.example.App/x86_64/stable
    tree_out = subprocess.run(['git', 'ls-tree', '-r', '--name-only', 'gh-pages:dl/flatpak/refs/heads/app'], capture_output=True, text=True)
    if tree_out.returncode == 0:
        for line in tree_out.stdout.strip().split('\n'):
            if line:
                parts = line.split('/')
                if parts:
                    app_id = parts[0]
                    if app_id not in FLATPAK_APPS:
                        FLATPAK_APPS.append(app_id)
except Exception as e:
    print(f"Could not read FLATPAK_APPS from gh-pages branch: {e}")

FLATPAK_APPS.sort()

