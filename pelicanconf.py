#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jean Cruypenynck'
SITENAME = u'nonatomic.blog'

PATH = 'content'
STATIC_PATHS = ['blog', 'download', 'extra/CNAME', 'extra/favicon.ico', 'extra/robots.txt' 'extra/.travis.yaml', 'pages', 'cycling2017', 'titanic']
ARTICLE_PATHS = ['blog']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'}
}

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = ('%B %d, %Y')

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 6
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

THEME = "theme"
MARKDOWN = {
    'extensions' : ['markdown.extensions.codehilite', 'markdown.extensions.extra', 'markdown.extensions.meta'],
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'}
    }
}

PLUGIN_PATHS = ['.']
PLUGINS = ['render_math']

DISQUS_SITENAME = "nonatomicblog"
TWITTER_USERNAME = 'nonatomiclabs'
