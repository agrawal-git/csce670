from __future__ import with_statement
from contextlib import closing
from flask import Flask, render_template, url_for, g
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.heroku import Heroku
import os
# from flask import request, session, redirect, abort, flash

app    = Flask(__name__)
heroku = Heroku(app)
db     = SQLAlchemy(app)



@app.route('/')
def index():
  return render_template('index.html', name="this is the main page")

@app.route('/search/')
def search():
  return "this is the search page"


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def close_db_connection(exception):
    g.db.close()


def connect_db():
  return sqlite3.connect(app.config['DATABASE'])


def init_db():
  with closing(connect_db()) as db:
    with app.open_resource('schema.sql') as f:
      db.cursor().executescript(f.read())
    db.commit()



if __name__ == '__main__':
    app.run(debug=True)
