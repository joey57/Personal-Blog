from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
  bio = TextAreaField('Tell us about you', validators=[DataRequired()])
  submit = SubmitField('Submit')

class PostForm(FlaskForm):
    title = StringField("Blog title:", validators=[DataRequired()])
    post = TextAreaField("Type Away:", validators=[DataRequired()])
    submit = SubmitField("Post")

class UpdatePostForm(FlaskForm):
    title = StringField("Blog title", validators=[DataRequired()])
    post = TextAreaField("Type Away", validators=[DataRequired()])
    submit = SubmitField("Update")

class CommentForm(FlaskForm):
    comment = TextAreaField("Post Comment", validators=[DataRequired()])
    alias = StringField("Comment Alias")
    submit = SubmitField("Comment")
  