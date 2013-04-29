from flask import Flask, render_template, url_for, g
# request, session, redirect, abort, flash
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.heroku import Heroku
import models
from models import db

app    = Flask(__name__)
heroku = Heroku(app)
db.app = app
db.init_app(app)

@app.route('/')
def index():
  # user = models.Friend("123","wa3l", 4, 4)
  # db.session.add(user)
  # db.session.commit()
  user = models.Friend.query.first()
  if not user:
    user = models.Friend("123","wa3l", 4, 4)
  return render_template('index.html', name=user.screen_name)

@app.route('/search/')
def search():
  return "this is the search page"


if __name__ == '__main__':
    app.run(debug=True)
