# -*- coding: utf-8 -*-

from airbrush import db

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
