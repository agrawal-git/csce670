'''
User module.
Given a user_id or screen_name, return a user dictionary
'''
class User:
  api   = None
  limit = 100

  def __init__(self, api):
    self.api  = api

  def get_user(self, screen_name):
    '''Return user dictionary object with required data'''
    user = self.api.users.show(id=screen_name)
    return self.get_user_dict(user)


  def get_user_dict(self, user):
    return {
      'user_id':      user['id_str'],
      'screen_name':  user['screen_name'],
      'follow_count': user['followers_count'],
      'tweets_count': user['statuses_count']
    }


  def get_friends(self, name):
    friend_ids = self.api.friends.ids(screen_name=name, stringify_ids=True)['ids']
    friends = []
    i = self.limit
    while i < len(friend_ids) + self.limit - 1:
      ids = ", ".join(friend_ids[i-self.limit:i])
      batch = self.api.users.lookup(user_id=ids)
      i += self.limit
      for user in batch:
        friends.append(self.get_user_dict(user))
    return friends
