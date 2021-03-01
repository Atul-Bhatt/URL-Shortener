from flask import Flask, render_template, request, redirect, url_for, flash, abort, session
import json
import os.path
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'h432hi5ohi3h5i5hi3o2hi'


@app.route('/')
def home():
    return render_template('home.html', codes=session.keys())


@app.route('/short-url', methods=['GET', 'POST'])
def short_url():
    urls = {}

    if os.path.exists('urls.txt'):
        with open('urls.txt', mode='r', encoding='utf-8') as open_file:
            urls = json.load(open_file)
            if request.form['code'] in urls.keys():
                flash('Short Name Already Exists...')
                return redirect(url_for('home'))

    # if the URL doesn't exist then add it to the file
    urls[request.form['code']] = request.form['url']

    with open('urls.txt', mode='w', encoding='utf-8') as file:
        json.dump(urls, file)
        session[request.form['code']] = True

    return render_template('short_url.html', code=request.form['code'], url=request.form['url'])


# Redirect the user to the resource

@app.route('/<string:code>')
def redirect_route(code):
    if os.path.exists('urls.txt'):
        with open('urls.txt', mode='r', encoding='utf-8') as file:
            urls = json.load(file)
            if code in urls.keys():
                return redirect(urls[code])
            else:
                abort(404)
