from flask import render_template, Flask, request
from flask_classy import FlaskView, route
from model import Conversation, session
from jinja2 import Environment, FileSystemLoader


import dateutil.parser


import sys


class SearchView(FlaskView):
    plugin_name = 'search'

    def get(self):
        content = request.args.get("content")
        speaked_at = request.args.get("speaked_at")

        if not content and not speaked_at:
            return render_template('plugins/search/index.html', title="this is search title")

        elif not content:
            speaked_at = dateutil.parser.parse(speaked_at)

            conversations = session.query(Conversation) \
                .filter(Conversation.speaked_at == speaked_at)

        elif not speaked_at:
            conversations = session.query(Conversation) \
                .filter(Conversation.content.like(f'%{content}%'))

        else:
            conversations = session.query(Conversation) \
                .filter(Conversation.content.like(f'%{content}%'), Conversation.speaked_at == speaked_at) \


        print(f"=== conversation ===", file=sys.stderr)

        for conversation in conversations:
            print(f"{conversation.content}, {conversation.speaked_at}",
                  file=sys.stderr)
        print(f"=== ============ ===", file=sys.stderr)

        return render_template('plugins/search/result.html', conversations=conversations)
