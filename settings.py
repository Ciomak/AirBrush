# -*- coding: utf-8 -*-

import os

from local_settings import *


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'.format(DATABASE_USER,
                                                                             DATABASE_PASS,
                                                                             DATABASE_HOST,
                                                                             DATABASE_PORT,
                                                                             DATABASE_NAME
                                                                            )

SQLALCHEMY_ECHO=True
SQLALCHEMY_MIGRATE_REPO=os.path.join(BASE_DIR, 'db_repository')

DEBUG=True
TEMPLATES_AUTO_RELOAD=True

TEMPLATE_DIR=os.path.join(BASE_DIR, 'airbrush', 'templates')
MEDIA_DIR=os.path.join(BASE_DIR, 'airbrush', 'media')
STATIC_DIR=os.path.join(BASE_DIR, 'airbrush', 'static')