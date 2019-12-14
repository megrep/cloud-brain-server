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
        speaked_at_start = request.args.get("speaked_at_start")
        speaked_at_end = request.args.get("speaked_at_end")

        if speaked_at_start and speaked_at_end:
            if not content:
                content = ''

            speaked_at_start = dateutil.parser.parse(speaked_at_start)
            speaked_at_end = dateutil.parser.parse(speaked_at_end)

            conversations = session.query(Conversation) \
                .filter(
                    Conversation.content.like(f'%{content}%'),
                    Conversation.speaked_at >= speaked_at_start,
                    Conversation.speaked_at <= speaked_at_end
            )

        else:
            return render_template('plugins/search/index.html', title="this is search title")

        print(f"=== conversation ===", file=sys.stderr)

        for conversation in conversations:
            print(f"{conversation.content}, {conversation.speaked_at}",
                  file=sys.stderr)
        print(f"=== ============ ===", file=sys.stderr)

        return render_template('plugins/search/result.html', conversations=conversations)
