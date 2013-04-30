'''
User module.
Handles fetching individual users as well as all friends of a user.
'''

class User:
  api   = None
  limit = 100

  def __init__(self, api):
    self.api  = api

  def get_user(self, screen_name):
    '''Return user dictionary object with required attributes'''
    user = self.api.users.show(id=screen_name)
    return self.get_user_dict(user)


  def get_friends(self, name):
    '''Return a list of user dicts with only needed attributes'''
    ids = self.fetch_friend_ids(name)
    i   = self.limit
    friends = []
    while i < len(ids) + self.limit - 1:
      batch = self.api.users.lookup(user_id=self.id_string(ids, i))
      friends.extend(self.process_batch(batch))
      i += self.limit
    return friends


  def get_user_dict(self, user):
    '''Return a user dict with only the needed attributes'''
    return {
      'user_id':      user['id_str'],
      'screen_name':  user['screen_name'],
      'follow_count': user['followers_count'],
      'tweets_count': user['statuses_count']
    }


  def fetch_friend_ids(self, name):
    '''Fetch a user's list of friends ids from twitter'''
    friends = self.api.friends.ids(screen_name=name, stringify_ids=True)
    return friends['ids']


  def id_string(self, ids, index):
    '''Return a comma-separated list of 100 friend ids'''
    return ", ".join(ids[index-self.limit:index])


  def process_batch(self, batch):
    '''Build user dicts from raw user objects and return a list of them'''
    friends = []
    for user in batch:
      friends.append(self.get_user_dict(user))
    return friends

