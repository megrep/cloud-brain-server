from flask import Flask
from flask_classy import FlaskView

app = Flask(__name__)

class HelloView(FlaskView):
    def index(self):
        return "hello world"

HelloView.register(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
