import tweepy
import webbrowser
import time
import sys

consumer_key = 'CoepSUu9aTBDacbsSvyFdQ'
consumer_secret = 'HfCJmpnP4kdVyl4ToBXLRu9Him5O4QrPoB3gNWYWlM'


## Getting access key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth_url = auth.get_authorization_url()
print 'From your browser, please click AUTHORIZE APP and then copy the unique PIN: ' 
webbrowser.open(auth_url)
verifier = raw_input('PIN: ').strip()
auth.get_access_token(verifier)
access_key = '108510830-gSiBhqpAd3gZLm0fcL5ht5Yn26v20fAF0a3CiXmp'
access_secret = 'OoZpY2yg6t7guh8QTGQP6rjVvJz1VEhQ8CwpFiQ'


## Authorizing account privileges
auth.set_access_token(access_key, access_secret)


## Get the local time
localtime = time.asctime( time.localtime(time.time()) )


## Status changes
api = tweepy.API(auth)
#api.update_status('It worked - Current time is %s' % localtime)
print 'It worked - now go check your status!'


## Filtering the firehose
user = []
print 'Follow tweets from which user ID?'
handle = raw_input(">")
user.append(handle)

keywords = []
print 'What keywords do you want to track? Separate with commas.'
key = raw_input(">")
keywords.append(key)

class CustomStreamListener(tweepy.StreamListener):

    def on_status(self, status):

        # We'll simply print some values in a tab-delimited format
        # suitable for capturing to a flat file but you could opt 
        # store them elsewhere, retweet select statuses, etc.



        try:
            print "%s\t%s\t%s\t%s" % (status.text, 
                                      status.author.screen_name, 
                                      status.created_at, 
                                      status.source,)
        except Exception, e:
            print >> sys.stderr, 'Encountered Exception:', e
            pass

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

# Create a streaming API and set a timeout value of ??? seconds.

streaming_api = tweepy.streaming.Stream(auth, CustomStreamListener(), timeout=None)

# Optionally filter the statuses you want to track by providing a list
# of users to "follow".

print >> sys.stderr, "Filtering public timeline for %s" % keywords

streaming_api.filter(follow=handle)