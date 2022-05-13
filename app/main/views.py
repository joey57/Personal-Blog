from flask import render_template, request, redirect, url_for, abort,flash
from . import main
from ..models import User,Post
from flask_login import login_required, current_user
from datetime import datetime
from .. import db
from .forms import UpdateProfile

@main.route('/home')
@login_required
def home():
  return render_template("home.html" , user=current_user)

@main.route('/create-post', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        text = request.form.get('text')
        if not text:
            flash('Post cannot be empty', category='error')
        else:
            flash('Post created!', category='success')

    return render_template('create_post.html', user=current_user)  


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

