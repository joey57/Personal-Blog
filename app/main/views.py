from flask import render_template, request, redirect, url_for, abort,flash
from requests import post
from . import main
from ..models import User,Post
from flask_login import login_fresh, login_required, current_user
from datetime import datetime
from .. import db
from .forms import UpdateProfile

@main.route('/')
@main.route('/home')
@login_required
def home():
    posts = Post.query.all()
    return render_template("home.html" , user=current_user,posts=posts)

@main.route('/create-post', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        text = request.form.get('text')
        if not text:
            flash('Post cannot be empty', category='error')
        else:
            post = Post(text=text, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('Post created!', category='success')
            return redirect(url_for('main.home'))

    return render_template('create_post.html', user=current_user) 

@main.route('/delete-post/<int:id>', methods=['GET','POST'])
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        flash("Post does not exist.", category='error')
    elif current_user.id != post.id:
        flash("You do not have permission to delete this post.", category='error')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted', category='success')
    return redirect(url_for('main.home')) 

@main.route('/posts/<username>')
@login_required
def posts(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        flash('No user with that username exists.', category='error')
        return redirect(url_for('main.home'))

    posts = Post.query.filter_by(author=user.id).all()
    return render_template('posts.html', user=current_user, posts=posts, username=username)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

