#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Gaurav Modi'
SITENAME = 'Moonshot.in'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

DISPLAY_CATEGORIES_ON_MENU = False

# MENUITEMS = (
# #    ('About', ''),
#     ('Contact', 'https://docs.google.com/forms/d/e/1FAIpQLSd_67Y_w4mvfDw3KQQEJJygHSumOYqH-eiByDI-xUStsw0T1Q/viewform?usp=sf_link'),
# #    ('CV', ''),
#     ('GitHub', 'https://github.com/gauravmodi/')
#     )

# Theme & Style
TYPOGRIFY = True
THEME = "../pelican-themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'cosmo'
HIDE_SIDEBAR = True
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
# plugins configuration
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['i18n_subsites',]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)
#
# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Delete output folder content except git files
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".hg", ".git", ".bzr", "CNAME"]
