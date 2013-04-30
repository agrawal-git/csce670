'''
This is a test for getting a user and his friends.
Next step is caching those objects in the db so we don't have to
ask for them every time we need them.
'''
import twitter
from oauth import Auth
from user  import User

api  = Auth().api
user = User(api)
wa3l = user.get_user('wa3l')

friends = user.get_friends('wa3l')
for user in friends:
  print user
