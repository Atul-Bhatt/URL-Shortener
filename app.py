from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'h432hi5ohi3h5i5hi3o2hi'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/short-url', methods=['GET', 'POST'])
def short_url():
    url = {}
    url[request.form['code']] = request.form['url']

    if os.path.exists('urls.txt'):
        with open('urls.txt', mode='r', encoding='utf-8') as open_file:
            existing_urls = json.load(open_file)
            if request.form['code'] in existing_urls.keys():
                flash('Short Name Already Exists...')
                return redirect(url_for('home'))

    with open('urls.txt', mode='a', encoding='utf-8') as file:
        json.dump(url, file)

    return render_template('short_url.html', code=request.form['code'], url=request.form['url'])
