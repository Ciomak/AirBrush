# -*- coding: utf-8 -*-

from airbrush import db

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), default=None)
    path = db.Column(db.String(150))
    rate = db.Column(db.Integer)
    gallery = db.Column(db.Integer, db.ForeignKey('gallery.id'))
    
class Gallery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    rate = db.Column(db.Integer)
    images = db.relationship('Image', backref='gallery', lazy='dynamic')