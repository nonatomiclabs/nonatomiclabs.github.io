#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jean Cruypenynck'
SITENAME = u'nonatomic.blog'
SITEURL = 'http://nonatomiclabs.github.io'

PATH = 'content'
STATIC_PATHS = ['blog', 'extra/CNAME']
ARTICLE_PATHS = ['blog']

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
MD_EXTENSIONS = ['codehilite(css_class=codehilite)', 'extra',
                 'figureAltCaption']

PLUGIN_PATHS = ['.']
PLUGINS = ['render_math']

DISQUS_SITENAME = "nonatomicblog"
TWITTER_USERNAME = 'nonatomiclabs'
