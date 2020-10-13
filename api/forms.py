from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField


class MessageForm(FlaskForm):
    message = TextAreaField(u'Сообщение')

class TagCommentForm(FlaskForm):
    tag = StringField(u'Тег')
    comment = TextAreaField(u'Комментарий')
