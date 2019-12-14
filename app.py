from flask import Flask, request
from flask_classy import FlaskView

from setting import PLUGINS

import base64
from datetime import datetime


app = Flask(__name__)


class IndexView(FlaskView):
    def index(self):
        return "hello world"


IndexView.register(app)


class ApiView(FlaskView):
    def post(self):
        voice = request.json['data']
        speaked_at = request.json['speaked_at']

        print('*** request.json ***')
        print(request.json)
        print('*** ************ ***')

        voice = base64.b64decode(voice)

        print('*** request.json ***')
        print(voice)
        print('*** ************ ***')

        speaked_at = datetime.fromisoformat(speaked_at)
        print('**** speaked_at ****')
        print(speaked_at)
        print('*** ************ ***')

        return "ok"


ApiView.register(app)


print('--- LOAD PLUGINS ---')
for plugin in PLUGINS:
    print(f'load {plugin.plugin_name}')
    plugin.register(app)

print('--------------------')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
