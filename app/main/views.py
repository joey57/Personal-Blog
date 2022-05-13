from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User
from flask_login import login_required, current_user
from datetime import datetime
from .. import db
from .forms import UpdateProfile


# @main.route("/profile/<int:id>", methods = ["POST", "GET"])
# def profile(id):
#     user = User.query.filter_by(id = id).first()
#     posts = Post.query.filter_by(user_id = id).all()

#     if request.method == "POST":
        
#         db.session.add(new_sub)
#         db.session.commit()
#     return render_template("profile/profile.html",user = user, posts = posts)

# @main.route("/profile/<int:id>/update", methods = ["POST", "GET"])
# @login_required
# def update_profile(id):
#     user = User.query.filter_by(id = id).first()
#     form = UpdateProfile()
#     if form.validate_on_submit():
#         user.first_name = form.first_name.data
#         user.last_name = form.last_name.data
#         user.email = form.email.data
#         user.bio = form.bio.data

#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for("main.profile", id = id))
    
#     return render_template("profile/update.html",user = user, form = form)

