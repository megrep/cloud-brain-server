from flask import Flask, request
from flask_classy import FlaskView

from model import Conversation
from model import session


from setting import PLUGINS

USE_IBM = True

import base64
import dateutil.parser
import julius.recognition as recognition
import threading
import os
import sys

if USE_IBM:
    import ibm
    recognizer = ibm
else:
    import julius.recognition as julius
    recognizer = julius

app = Flask(__name__)

class IndexView(FlaskView):
    def index(self):
        return "hello world"


IndexView.register(app)

def recognize(voice, speaked_at):
    voice = recognition.recognize(voice)
    print('****** voice *******')
    print(voice)
    print('*** ************ ***')

    conversation = Conversation(content=voice, speaked_at=speaked_at)

    session.add(conversation)
    session.commit()

class ApiView(FlaskView):
    def post(self):
        voice = request.json['data']
        speaked_at = request.json['speaked_at']

        print('*** request.json ***')
        # print(request.json)
        print('*** ************ ***')

        voice = base64.b64decode(voice)

        speaked_at = dateutil.parser.parse(speaked_at)
        print('**** speaked_at ****')
        print(speaked_at)
        print('*** ************ ***')

        # voiceを認識
        voice = recognizer.recognize(voice)
        print('****** voice *******')
        print(voice)
        print('*** ************ ***')

        conversation = Conversation(content=voice, speaked_at=speaked_at)

        session.add(conversation)
        session.commit()

        return "ok"


ApiView.register(app)

print('--- LOAD PLUGINS ---')
for plugin in PLUGINS:
    print(f'load {plugin.plugin_name}')
    plugin.register(app)

print('--------------------')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=False, ssl_context=(
        'cert/server.crt', 'cert/server.key'))
