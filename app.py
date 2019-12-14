from flask import Flask, render_template, request
from flask_classy import FlaskView, route

app = Flask(__name__)
##この上まではテンプレみたいなものなので

class HelloView(FlaskView):
    @app.route('/home')
    def home(self):
        return render_template('home.html')

    def search():
        return render_template('search.html')

    @route('/result',methods=['POST','GET'])
    def result():
        return render_template('result.html')

HelloView.register(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
