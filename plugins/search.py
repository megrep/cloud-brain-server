from flask import render_template,Flask,request
from flask_classy import FlaskView,route
from model import Conversation,session
from jinja2 import Environment, FileSystemLoader


def DB_check(word,time):
    for row in session.query(Conversation).filter(Conversation.text.like('%'+word+'%')).filter(Conversation.speaked_at == time):
        print(row.text, row.speaked_at)
        return row
    return "該当ない"

class SearchView(FlaskView):
    plugin_name = 'search'

    def home(self):
        return render_template('plugins/search/home.html', title="this is search title")

    @route('/result', methods=['GET','POST'])
    def result(self):
        #word = request.form['text']
        #time = request.form['speaked_at']
        row = DB_check()
        return render_template('plugins/search/result.html',DB = "hello")

    def w_search(self):
        return render_template('plugins/search/search.html')
