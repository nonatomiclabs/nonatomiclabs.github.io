#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jean Cruypenynck'
SITENAME = u'nonatomic.blog'

PATH = 'content'
STATIC_PATHS = ['blog', 'download', 'extra/CNAME', 'extra/favicon.ico', 'extra/.travis.yaml', 'pages', 'cycling2017']
ARTICLE_PATHS = ['blog']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = ('%B %d, %Y')

# Feed generation is usually not desired when developing
FEED_RSS = 'rss.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 6
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

THEME = "theme"
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'codehilite'},
        'markdown.extensions.extra': {},
        'figureAltCaption': {},
    },
    'output_format': 'html5',
}

PLUGIN_PATHS = ['.']
PLUGINS = ['render_math']

DISQUS_SITENAME = "nonatomicblog"
TWITTER_USERNAME = 'nonatomiclabs'
