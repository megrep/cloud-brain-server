from flask import render_template, Flask, request
from flask_classy import FlaskView, route
from model import Conversation, session
from jinja2 import Environment, FileSystemLoader

import dateutil.parser
import jaconv
from datetime import datetime

import urllib.request
import urllib.parse

import sys

URL = 'https://script.google.com/macros/s/AKfycby4wd8ptsrCSiACCPo09vIVQwel-9bqD0-8GXUCI05D7y2hmAV5/exec'


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
            return render_template('plugins/calendar/index.html', conversations=conversations, use_alert=False)

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

        content = urllib.parse.quote(content)

        year = datetime.now().year

        print(type(month), file=sys.stderr)
        if datetime.now().month > int(month):
            year += 1

        _datetime = f'{year}/{month}/{date} 00:00:00'
        _datetime = urllib.parse.quote(_datetime)

        url = f'{URL}?title={content}&datetime={_datetime}'
        req = urllib.request.Request(url)

        with urllib.request.urlopen(req) as res:
            body = res.read()

        print(body, file=sys.stderr)

        # s = '2018-12-31T05:00:30.001000'
        # speaked_at = dateutil.parser.parse(s)
        # conversation = Conversation(content='8月8日 学校ね', speaked_at=speaked_at)

        # session.add(conversation)
        # session.commit()

        return render_template('plugins/calendar/index.html', conversations=conversations, use_alert=True)
