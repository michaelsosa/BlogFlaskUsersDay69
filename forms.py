from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DecimalField
from wtforms.validators import DataRequired, URL, InputRequired, length
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class CommentForm(FlaskForm):
    # title = StringField("Blog Post Title", validators=[DataRequired()])
    # subtitle = StringField("Subtitle", validators=[DataRequired()])
    # img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    text = CKEditorField("Blog Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")


class RegisterForm(FlaskForm):
    # email
    # VARCHAR(100),
    # password
    # VARCHAR(100),
    # name
    # VARCHAR(1000),
    email = StringField(label='Email', validators=[InputRequired("Email address is required."), length(max=100)])
    password = PasswordField(label='Password', validators=[InputRequired("Password is required."), length(max=100)])
    name = StringField(label='Name', validators=[InputRequired("Name is required."), length(max=1000)])
    submit = SubmitField(label="Sign me up!")

class LoginForm(FlaskForm):
    # email
    # VARCHAR(100),
    # password
    # VARCHAR(100),
    # name
    # VARCHAR(1000),
    email = StringField(label='Email', validators=[InputRequired("Email address is required."), length(max=100)])
    password = PasswordField(label='Password', validators=[InputRequired("Password is required."), length(max=100)])
    # name = StringField(label='Name', validators=[InputRequired("Name is required."), length(max=1000)])
    submit = SubmitField(label="Let me in!")


class EditMovieForm(FlaskForm):
    # name, location, opening_time, closing_time, coffee_grade, wifi_grade, power_grade
    # title = StringField(label='Book Name', validators=[InputRequired("Book Name is required.")])
    # author = StringField(label='Book Author', validators=[InputRequired("Book Author is required.")])
    new_rating = DecimalField(label='New Rating', validators=[InputRequired("Rating is required.")])
    new_review = StringField(label='Movie Review', validators=[InputRequired("required."), length(max=250)])
    submit = SubmitField(label="Update")
