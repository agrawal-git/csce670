from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


# The friends table
class Friend(db.Model):
  id            = db.Column(db.Integer, primary_key=True)
  user_id       = db.Column(db.String(20), unique=True)
  screen_name   = db.Column(db.String(50), unique=True)
  follow_count  = db.Column(db.Integer)
  tweets_count  = db.Column(db.Integer)

  def __init__(self, user):
    self.user_id      = user['user_id']
    self.screen_name  = user['screen_name']
    self.follow_count = user['follow_count']
    self.tweets_count = user['tweets_count']

  def __repr__(self):
    return "%r" % self.screen_name


# The tweets table
class Tweet(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  tweet_id      = db.Column(db.String(20), unique=True)
  text          = db.Column(db.String(300))
  link          = db.Column(db.String(250))
  user_id       = db.Column(db.String(20))
  screen_name   = db.Column(db.String(50))
  created_at    = db.Column(db.DateTime)
  retweet_count = db.Column(db.Integer)
  own_tweet     = db.Column(db.Boolean)
  terms = db.relationship('TweetTerm', backref='tweet', lazy='dynamic')

  def __init__(self, tweet):
    self.tweet_id       = tweet['tweet_id']
    self.text           = tweet['text']
    self.link           = tweet['link']
    self.user_id        = tweet['user_id']
    self.screen_name    = tweet['screen_name']
    self.retweet_count  = tweet['retweet_count']
    self.created_at     = tweet['created_at']
    self.own_tweet      = tweet['own_tweet']


# The terms table
class Term(db.Model):
  id     = db.Column(db.Integer, primary_key=True)
  term   = db.Column(db.String(50), unique=True)
  tweets = db.relationship('TweetTerm', backref='term', lazy='dynamic')

  def __init__(self, term):
    self.term = term

  def __repr__(self):
    return "%r" % self.term


# The terms-to-tweets table
class TweetTerm(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  tweet_id = db.Column(db.Integer, db.ForeignKey('tweet.id'))
  term_id  = db.Column(db.Integer, db.ForeignKey('term.id'))
  count    = db.Column(db.Integer)

  def __init__(self, tweet_id, term_id, count):
    self.tweet_id = tweet_id
    self.term_id  = term_id
    self.count    = count
