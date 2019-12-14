from flask import Flask, request
from flask_classy import FlaskView

from setting import PLUGINS

import base64


app = Flask(__name__)


class IndexView(FlaskView):
    def index(self):
        return "hello world"


IndexView.register(app)


class ApiView(FlaskView):
    def post(self):
        print('*** request.json ***')
        print(request.json)
        print('*** ************ ***')

        voice = request.json['data']
        voice = base64.b64decode(voice)

        print('*** request.json ***')
        print(voice)
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
