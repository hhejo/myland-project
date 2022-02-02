from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('제목', validators=[DataRequired('제목을 입력하세요.')])
    content = TextAreaField('내용', validators=[DataRequired('내용을 입력하세요.')])
