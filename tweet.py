'''
Tweet module.
Handles fetching individual users tweets as well as all tweets from friends of a user.
'''

class Tweets:
  api   = None
  limit = 200

  def __init__(self, api):
    self.api  = api


  def timeline(self, user_id, auth_id):
    '''Return tweet dictionary object with required attributes'''
    tweets = self.api.statuses.user_timeline(
      user_id=user_id, count=self.limit, include_rts=False
    )
    return self.tweet_dicts(tweets, auth_id)


  def tweet_dicts(self, raw_tweets, auth_id):
    '''Return a list of tweet dicts with only needed attributes'''
    tweets = []
    for tweet in raw_tweets:
      tweets.append(self.tweet_dict(tweet, auth_id))
    return tweets


  def tweet_dict(self, tweet, auth_id):
    '''Return a tweet dict with only the needed attributes'''
    own_tweet   = False
    tweet_id    = tweet['id_str']
    user_id     = tweet['user']['id_str']
    screen_name = tweet['user']['screen_name']
    if user_id == auth_id: own_tweet = True
    permalink   = "http://twitter.com/%s/status/%s" % (screen_name, tweet_id)
    return {
       'tweet_id': tweet_id,          'text': tweet['text'],
        'user_id': user_id,  'retweet_count': tweet['retweet_count'],
           'link': permalink,   'created_at': tweet['created_at'],
      'own_tweet': own_tweet,  'screen_name': screen_name,
    }
