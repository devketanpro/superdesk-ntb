#!/usr/bin/env python
# -*- coding: utf-8; -*-
#
# This file is part of Superdesk.
#
# Copyright 2013, 2014, 2015 Sourcefabric z.u. and contributors.
#
# For the full copyright and license information, please see the
# AUTHORS and LICENSE files distributed with this source code, or
# at https://www.sourcefabric.org/superdesk/license


import os
import json
from ntb.io.feed_parsers import ntb_nitf
from ntb.io.feed_parsers import stt_newsml  # NOQA


try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


def env(variable, fallback_value=None):
    env_value = os.environ.get(variable, '')
    if len(env_value) == 0:
        return fallback_value
    else:
        if env_value == "__EMPTY__":
            return ''
        else:
            return env_value


ABS_PATH = os.path.abspath(os.path.dirname(__file__))
INIT_DATA_PATH = os.path.join(ABS_PATH, 'data')
LOCATORS_DATA_FILE = os.path.join(ABS_PATH, 'data', 'locators.json')

LOG_CONFIG_FILE = env('LOG_CONFIG_FILE', 'logging_config.yml')

APPLICATION_NAME = env('APP_NAME', 'Superdesk')
server_url = urlparse(env('SUPERDESK_URL', 'http://localhost:5000/api'))
CLIENT_URL = env('SUPERDESK_CLIENT_URL', 'http://localhost:9000')
URL_PROTOCOL = server_url.scheme or None
SERVER_NAME = server_url.netloc or None
URL_PREFIX = server_url.path.lstrip('/') or ''
if SERVER_NAME.endswith(':80'):
    SERVER_NAME = SERVER_NAME[:-3]

INSTALLED_APPS = [
    'apps.auth',
    'superdesk.roles',
    'ntb.scanpix',
    'ntb.io',
    'ntb.publish',
]

# LDAP settings
LDAP_SERVER = env('LDAP_SERVER', '')  # Ex: ldap://sourcefabric.org
LDAP_SERVER_PORT = env('LDAP_SERVER_PORT', 389)

# Fully Qualified Domain Name. Ex: sourcefabric.org
LDAP_FQDN = env('LDAP_FQDN', '')

# LDAP_BASE_FILTER limit the base filter to the security group. Ex: OU=Superdesk Users,dc=sourcefabric,dc=org
LDAP_BASE_FILTER = env('LDAP_BASE_FILTER', '')

# change the user depending on the LDAP directory structure
LDAP_USER_FILTER = env('LDAP_USER_FILTER', "(&(objectCategory=user)(objectClass=user)(sAMAccountName={}))")

# LDAP User Attributes to fetch. Keys would be LDAP Attribute Name and Value would be Supderdesk Model Attribute Name
LDAP_USER_ATTRIBUTES = json.loads(env('LDAP_USER_ATTRIBUTES',
                                      '{"givenName": "first_name", "sn": "last_name", '
                                      '"displayName": "display_name", "mail": "email", '
                                      '"ipPhone": "phone"}'))

if LDAP_SERVER:
    INSTALLED_APPS.append('apps.ldap')
else:
    INSTALLED_APPS.append('superdesk.users')
    INSTALLED_APPS.append('apps.auth.db')


INSTALLED_APPS.extend([
    'superdesk.upload',
    'superdesk.sequences',
    'superdesk.notification',
    'superdesk.activity',
    'superdesk.vocabularies',
    'superdesk.profiling',
    'superdesk.backend_meta',
    'apps.comments',

    'superdesk.io',
    'superdesk.io.feeding_services',
    'superdesk.io.feed_parsers',
    'superdesk.io.subjectcodes',
    'superdesk.io.iptc',
    'apps.io',
    'apps.io.feeding_services',
    'superdesk.publish',
    'superdesk.commands',
    'superdesk.locators',

    'apps.auth',
    'apps.archive',
    'apps.stages',
    'apps.desks',
    'apps.tasks',
    'apps.preferences',
    'apps.spikes',
    'apps.prepopulate',
    'apps.legal_archive',
    'apps.search',
    'apps.saved_searches',
    'apps.privilege',
    'apps.rules',
    'apps.highlights',
    'apps.products',
    'apps.publish',
    'apps.publish.enqueue',
    'apps.publish.formatters',
    'apps.content_filters',
    'apps.content_types',
    'apps.dictionaries',
    'apps.duplication',
    'apps.spellcheck',
    'apps.templates',
    'apps.archived',
    'apps.validators',
    'apps.validate',
    'apps.workspace',
    'apps.macros',
    'apps.archive_broadcast',
    'apps.search_providers',
    'apps.feature_preview',
    'apps.workqueue',
    'apps.picture_crop',
    'apps.languages',

    'ntb.macros',
    'planning'
])

RENDITIONS = {
    'picture': {
        'thumbnail': {'width': 220, 'height': 120},
        'viewImage': {'width': 640, 'height': 640},
        'baseImage': {'width': 1400, 'height': 1400},
    },
    'avatar': {
        'thumbnail': {'width': 60, 'height': 60},
        'viewImage': {'width': 200, 'height': 200},
    }
}

SERVER_DOMAIN = 'localhost'

MACROS_MODULE = env('MACROS_MODULE', 'ntb.macros')

WS_HOST = env('WSHOST', '0.0.0.0')
WS_PORT = env('WSPORT', '5100')

# Determines if the ODBC publishing mechanism will be used, If enabled then pyodbc must be installed along with it's
# dependencies
ODBC_PUBLISH = env('ODBC_PUBLISH', None)
# ODBC test server connection string
ODBC_TEST_CONNECTION_STRING = env('ODBC_TEST_CONNECTION_STRING',
                                  'DRIVER=FreeTDS;DSN=NEWSDB;UID=???;PWD=???;DATABASE=News')

DEFAULT_SOURCE_VALUE_FOR_MANUAL_ARTICLES = 'NTB'
DEFAULT_URGENCY_VALUE_FOR_MANUAL_ARTICLES = 3
DEFAULT_GENRE_VALUE_FOR_MANUAL_ARTICLES = []

# This value gets injected into NewsML 1.2 and G2 output documents.
NEWSML_PROVIDER_ID = 'ntb.no'
ORGANIZATION_NAME = env('ORGANIZATION_NAME', 'NTB')
ORGANIZATION_NAME_ABBREVIATION = env('ORGANIZATION_NAME_ABBREVIATION', 'NTB')

AMAZON_CONTAINER_NAME = env('AMAZON_CONTAINER_NAME', '')
AMAZON_ACCESS_KEY_ID = env('AMAZON_ACCESS_KEY_ID', '')
AMAZON_SECRET_ACCESS_KEY = env('AMAZON_SECRET_ACCESS_KEY', '')
AMAZON_REGION = env('AMAZON_REGION', 'us-east-1')
AMAZON_SERVE_DIRECT_LINKS = env('AMAZON_SERVE_DIRECT_LINKS', False)
AMAZON_S3_USE_HTTPS = env('AMAZON_S3_USE_HTTPS', False)

is_testing = os.environ.get('SUPERDESK_TESTING', '').lower() == 'true'
ELASTICSEARCH_FORCE_REFRESH = is_testing
ELASTICSEARCH_AUTO_AGGREGATIONS = False
SIGN_OFF_MAPPING = 'email'
DEFAULT_CONTENT_TYPE = 'Standard'
DEFAULT_LANGUAGE = 'nb-NO'
GENERATE_SHORT_GUID = True
LANGUAGES = [
    {'language': 'nb-NO', 'label': 'Bokmål', 'source': True, 'destination': False},
    {'language': 'nn-NO', 'label': 'Nynorsk', 'source': False, 'destination': True},
    {'language': 'en', 'label': 'English', 'source': False, 'destination': False},
    {'language': 'de', 'label': 'German', 'source': False, 'destination': False}
]

# NTB NITF specific behaviour
NITF_MAPPING = ntb_nitf.NITF_MAPPING

ENABLE_PROFILING = False

NO_TAKES = True

FTP_TIMEOUT = 30

DEFAULT_TIMEZONE = "Europe/Oslo"

# FIXME: temporary fix for SDNTB-344, need to be removed once SDESK-439 is implemented
INGEST_SKIP_IPTC_CODES = True

SESSION_EXPIRY_MINUTES = 12 * 60

NIFS_STAGE_MAP = {6: 'Eliteserien menn',
                  676155: 'Eliteserien menn'}
NIFS_QCODE_MAP = {1: '15054000',  # Fotball
                  3: '15029000',  # Håndball
                  }

PLANNING_EXPORT_BODY_TEMPLATE = '''
{% for item in items %}
<p><b>{{ item.name or item.headline or item.slugline }}</b></p>
<p>{{ item.description_text }}</p>
<p></p>
{% if item.get('event', {}).get('location') %}
<p>Sted: {{ item.event.location[0].name }}.</p>
{% endif %}
{% if item.get('ednote', '') != '' %}
<p>Til red: {{ item.ednote }}</p>
{% endif %}
{% if item.coverages %}
<p>Dekning: {{ item.coverages | join(', ') }}
{% endif %}
<p>---</p>
{% endfor %}
'''
