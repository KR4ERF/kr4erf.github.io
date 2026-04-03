AUTHOR = 'KR4ERF'
SITENAME = 'kr4erf.radio'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'EST'
DEFAULT_DATE = 'fs'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

IGNORE_FILES = [
    '**/.*',
    '.gitkeep',
]

STATIC_PATHS = [
    'extra',
    'images',
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
}

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ('GitHub', 'https://github.com/kr4erf'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'themes/neon-parked'
DIRECT_TEMPLATES = ['index']

MYCALL = 'KR4ERF'
