#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from pelicanconf import *

SITEURL = 'https://www.nonatomiclabs.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "nonatomic.blog"
GOOGLE_ANALYTICS = "UA-64506480-3"

EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/travis.yml': {'path': '.travis.yml'}}
