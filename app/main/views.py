from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User, Post, Comment, Subscribers, Quote
from flask_login import login_required, current_user
from datetime import datetime
from .. import db
from .forms import UpdateProfile, PostForm, CommentForm, UpdatePostForm
from ..requests import get_quote

@main.route("/", methods = ["GET", "POST"])
def index():
    posts = Post.get_all_posts()
    quote = get_quote()

    if request.method == "POST":
        new_sub = Subscribers(email = request.form.get("subscriber"))
        db.session.add(new_sub)
        db.session.commit()
    return render_template("index.html", posts = posts, quote = quote)

@main.route("/post/<int:id>", methods = ["POST", "GET"])
def post(id):
    post = Post.query.filter_by(id = id).first()
    comments = Comment.query.filter_by(post_id = id).all()
    comment_form = CommentForm()
    comment_count = len(comments)

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        comment_form.comment.data = ""
        comment_alias = comment_form.alias.data
        comment_form.alias.data = ""
        if current_user.is_authenticated:
            comment_alias = current_user.username
        new_comment = Comment(comment = comment, comment_at = datetime.now(),comment_by = comment_alias,post_id = id)
        new_comment.save_comment()
        return redirect(url_for("main.post", id = post.id))

    return render_template("post.html",post = post,comments = comments,comment_form = comment_form,comment_count = comment_count)


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

