# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('settings')

db = SQLAlchemy(app)

from airbrush.gallery import models