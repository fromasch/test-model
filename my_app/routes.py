from flask import render_template, redirect, abort, send_from_directory, send_file
import yaml
from os import listdir

from my_app import app


# Fake Database
db = {}
db_path = 'my_app/fake_db/'
for filename in listdir(db_path):
    with open(db_path+filename, 'r') as f:
        y = yaml.full_load(f)
        db[filename.replace('.yml', '')] = y

def select_data(db, page, lang):
    data = db[page.lower()]
    if lang == 'en':
        data['text'] = data['en']
        pages = db['pages']['en']
    else:
        data['text'] = data['kr']
        pages = db['pages']['kr']
    return pages, data


# Setting Jinja2 to remove ugly whitespace
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

@app.route('/')
@app.route('/home')
def home():
    return redirect("/kr/home", code=302)


@app.route("/<lang>/home", methods=["GET", "POST"])
def index(lang):
    page = "Home"
    pages, data = select_data(db, page, lang)
    print(pages)
    return render_template("home.html", pages=pages, current_page=page, lang=lang, data=data)
