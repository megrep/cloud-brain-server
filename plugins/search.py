from flask_classy import FlaskView
from model import Conversation


class SearchView(FlaskView):
    plugin_name = 'search'

    def index(self):
        return "this is search page"
