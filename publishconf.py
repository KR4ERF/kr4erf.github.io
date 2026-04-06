# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import subprocess
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://kr4erf.radio"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

# Dynamically generate the list of apps from the gh-pages branch
# This list is used by the templates to show available software.
FLATPAK_APPS = []
try:
    # Check origin/gh-pages directly as it is guaranteed to exist in CI if apps are published
    tree_out = subprocess.run(
        ['git', 'ls-tree', '-r', '--name-only', 'origin/gh-pages:dl/flatpak/repo/refs/heads/app'],
        capture_output=True, text=True
    )
    if tree_out.returncode == 0:
        for line in tree_out.stdout.strip().split('\n'):
            if line:
                # refs look like com.example.App/x86_64/stable
                app_id = line.split('/')[0]
                if app_id not in FLATPAK_APPS:
                    FLATPAK_APPS.append(app_id)
except Exception as e:
    print(f"Warning: Failed to scan FLATPAK_APPS list: {e}")

FLATPAK_APPS.sort()
