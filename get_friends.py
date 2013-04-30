'''
This is a test for getting a user and his friends.
Next step is caching those objects in the db so we don't have to
ask for them every time we need them.
'''
import twitter
from oauth import Auth
from user  import User
from models import Friend
from searchem import db

api  = Auth().api
user = User(api)

# fetch user friends and store in the database:
friends = user.get_friends('wa3l')
for user in friends:
  model = Friend(user)
  db.session.add(model)
  print user
db.session.commit()
