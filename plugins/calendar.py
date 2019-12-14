from flask import render_template, Flask, request
from flask_classy import FlaskView, route
from model import Conversation, session
from jinja2 import Environment, FileSystemLoader

import dateutil.parser
import jaconv

import sys


class CalendarView(FlaskView):
    plugin_name = 'search'

    def get(self):
        _id = request.args.get("id")

        conversations = session.query(Conversation) \
            .filter(
            Conversation.content.like('%月%'),
            Conversation.content.like('%日%')
        )

        if not _id:
            return render_template('plugins/calendar/index.html', conversations=conversations)

        conversation = session.query(Conversation) \
            .filter(Conversation.id == _id) \
            .first()

        content = conversation.content
        content = jaconv.z2h(content, digit=True, ascii=True)

        content = content.replace('　', '')
        content = content.replace(' ', '')

        month = 0
        date = 0

        try:
            tsuki_index = content.find('月')
            month = content[tsuki_index - 1]

            nichi_index = content.find('日')
            date = content[nichi_index - 1]
        except:
            pass

        if month and date:
            print(month + '/' + date, file=sys.stderr)

        # s = '2018-12-31T05:00:30.001000'
        # speaked_at = dateutil.parser.parse(s)
        # conversation = Conversation(content='8月8日 学校ね', speaked_at=speaked_at)

        # session.add(conversation)
        # session.commit()

        return render_template('plugins/calendar/index.html', conversations=conversations)
