from twitter import *
'''
OAuth module. Call to authenticate to Twitter.
Access OAuth.api to get an API object.
'''

class Auth:
  '''OAuth handling'''
  consumer_key        = 'WyHTqA4Ng7ofLhgHVlZXw'
  consumer_secret     = 'GuBFv0VXya7wakRppmc0sj7Ygngr67OMEhZDNCrfGw'
  access_token        = '143602582-BBdrYTKdPmHFy7DVfGTDgMMbzWZQGJGRWfOIQ4Sl'
  access_token_secret = '5maNS11PGE4BwHJdECV1F9dZ01Us6ZMhHvNud1AaPcQ'
  api = None

  def __init__(self):
    self.api = Twitter(auth= OAuth(
      self.access_token, self.access_token_secret,
      self.consumer_key, self.consumer_secret
    ))
