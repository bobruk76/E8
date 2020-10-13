from werkzeug.utils import redirect

from api import app
from flask import Flask, request, render_template, url_for
from api.forms import MessageForm, TagCommentForm
from api.service import Message

@app.route('/')
def index():
    messages = Message().get_all()
    return render_template('index.html', messages=messages)

@app.route('/add-site', methods=['GET','POST'])
def add_site():
    message_form = MessageForm()
    message_db = Message()
    if request.method == 'POST':
        message = request.form.get('message')
        message_db.set(message)
        return redirect('/')

    return render_template('newmessage.html', form=message_form)
#
# @app.route('/message/<_id>/', methods=['GET','POST'])
# def message_get(_id):
#
#     if request.method == 'GET':
#         tag_comment_form = TagCommentForm()
#         message = Message().get(_id)
#         return render_template('message.html', message=message, form=tag_comment_form)
#
# @app.route('/message/<_id>/<obj>', methods=['POST'])
# def _set(_id, obj):
#     if obj == 'new-tag':
#         tag = request.form.get('tag')
#         Message().update_tags(_id, tag)
#     elif obj == 'new-comment':
#         comment = request.form.get('comment')
#         Message().update_comments(_id, comment)
#
#     return redirect('/message/{}/'.format(_id))
