import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask import Markup
from flask_misaka import Misaka

app = Flask(__name__)
Misaka(app, fenced_code=True)

app.config.from_pyfile("config.py")
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, app.config['DATABASE_NAME'])
))


### DATABASE FUNCTIONS ###

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database"""
    init_db()
    print('Initialized the database.')



def db_get_posts(limit=None):
    sql_query = 'select * from entries order by id desc'
    if limit:
        sql_query = ' '.join([sql_query, 'limit %d' % limit])
    db = get_db()
    cur = db.execute(sql_query)
    return cur.fetchall()


### Views ###

@app.route('/')
def homepage():
    entries = db_get_posts(limit=5)
    return render_template('homepage.html', entries=entries)


@app.route('/aboutme')
def aboutme():
    page = os.path.join(app.root_path, 'pages/aboutme.md')
    with open(page, 'r') as f:
        content = f.read()
    return render_template('aboutme.html', text = content)


@app.route('/allposts')
def allposts():
    entries = db_get_posts()
    return render_template('allposts.html', entries=entries)


@app.route('/blog/<int:blog_id>')
def post(blog_id):
    db = get_db()
    max_entry = db.execute("select Count(*) from entries").fetchone()
    if blog_id not in range(1, max_entry[0] + 1):
        abort(404)
    if type(blog_id) is not int:
        abort(404)

    sql_query = 'select * from entries where id=%d' % blog_id
    cur = db.execute(sql_query)
    blog_post = cur.fetchall()[0]

    page = os.path.join(app.root_path, 'pages/%s' % blog_post['path'])
    with open(page, 'r') as f:
        content = f.read()

    return render_template('blogpost.html', blog_post=blog_post, text=content)
