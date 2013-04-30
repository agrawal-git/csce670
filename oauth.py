from twitter import *
'''
OAuth module. Call to authenticate to Twitter.
Access OAuth.api to get an API object.
'''

class Auth:
  '''OAuth handling'''
  consumer_key        = 'f2MEow3T5KceQdSXfqA'
  consumer_secret     = 'iiy7WdQdSKbqhRCxSwwivSUidioGyOf4aQpqg7czWo'
  access_token        = '143602582-ViRwhkTAnlbtUPMc2ArykGHxOP67hX3D221iO6kq'
  access_token_secret = 'Id66ldFowHtyER7B3jUIGLtoq6zpuMsVwccUUJRug'
  api = None

  def __init__(self):
    self.api = Twitter(auth= OAuth(
      self.access_token, self.access_token_secret,
      self.consumer_key, self.consumer_secret
    ))
