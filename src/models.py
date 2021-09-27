from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, Table, Numeric, Enum
import os
import sys

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique = True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)    
    description = db.Column(db.String, nullable = True)
    profile_img = db.Column(db.String, nullable=True)

    have_followers = relationship("Followers", backref="user")#usamos backref porque back_populates no funciona
    #es one to one, asi que cada usuario va a tener su tabla de followers, que esta la unica
    have_post = relationship("Post")
    have_comment = relationship("Comment")



class Followers(db.Model):
    __tablename__ = 'followers'
    
    id = db.Column(db.Integer, primary_key=True)
    user_from_id = db.Column(db.Integer, nullable=False)
    user_to_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))

    have_user = relationship("User", backref="followers")


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50), nullable = True)
    location = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))

    have_media = relationship("Media", backref="post")
    have_comment = relationship("Comment", backref="post")


class Media(db.Model):
    __tablename__ = 'media'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, unique=True)
    type_media = db.Column(db.Enum, unique=False) 
    post_id = Column(Integer, ForeignKey('post.id'))



class Comment(db.Model):
    __tablename__ = 'comment'
    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, unique=False)

    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    