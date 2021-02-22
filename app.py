from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/short-url')
def short_url():
    return render_template('short_url.html', code=request.args['code'], url=request.args['url'])
