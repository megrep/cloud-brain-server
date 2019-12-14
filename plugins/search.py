from flask import render_template
from flask_classy import FlaskView
from model import Conversation
from jinja2 import Environment, FileSystemLoader


class SearchView(FlaskView):
    plugin_name = 'search'

    def index(self):
        return render_template('plugins/search/index.html', title="this is search title")
