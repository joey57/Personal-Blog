from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    posts = db.relationship('Post', backref='user', passive_deletes=True)
    comments = db.relationship('Comment', backref ='user', passive_deletes=True)
    # likes = db.relationship('Like', backref ='user', passive_deletes=True)
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Post(db.Model):
     __tablename__ = 'posts'

     id = db.Column(db.Integer, primary_key=True)
     text = db.Column(db.Text, nullable=False)
     author = db.Column(db.Integer, db.ForeignKey('users.id',ondelete='CASCADE'), nullable=False)
     comments = db.relationship('Comment', backref ='post', passive_deletes=True)
    #  likes = db.relationship('Like', backref ='posts', passive_deletes=True)

class Comment(db.Model):
     __tablename__ = 'comments'

     id = db.Column(db.Integer, primary_key=True)
     text = db.Column(db.String(200), nullable=False)
     author = db.Column(db.Integer, db.ForeignKey('users.id',ondelete='CASCADE'), nullable=False)
     post_id = db.Column(db.Integer, db.ForeignKey('posts.id',ondelete='CASCADE'), nullable=False)

# class Like(db.Model):
#      __tablename__ = 'likes'

#      id = db.Column(db.Integer, primary_key=True)
#      author = db.Column(db.Integer, db.ForeignKey('users.id',ondelete='CASCADE'), nullable=False)
#      post_id = db.Column(db.Integer, db.ForeignKey('posts.id',ondelete='CASCADE'), nullable=False)


            





