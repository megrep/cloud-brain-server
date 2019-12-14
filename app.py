from flask import Flask
from flask_classy import FlaskView

from setting import PLUGINS


app = Flask(__name__)


class IndexView(FlaskView):
    def index(self):
        return "hello world"


IndexView.register(app)

print('--- LOAD PLUGINS ---')
for plugin in PLUGINS:
    print(f'load {plugin.plugin_name}')
    plugin.register(app)

print('--------------------')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')