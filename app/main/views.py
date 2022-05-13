from flask import render_template, request, redirect, url_for
from . import main
from ..models import User
from flask_login import login_required, current_user
from .. import db
