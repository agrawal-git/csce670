from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy

tweet_list = []

# Go to http://dev.twitter.com and create an app. 
# The consumer key and secret will be generated for you after
consumer_key="CoepSUu9aTBDacbsSvyFdQ"
consumer_secret="HfCJmpnP4kdVyl4ToBXLRu9Him5O4QrPoB3gNWYWlM"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="108510830-gSiBhqpAd3gZLm0fcL5ht5Yn26v20fAF0a3CiXmp"
access_token_secret="OoZpY2yg6t7guh8QTGQP6rjVvJz1VEhQ8CwpFiQ"

class StdOutListener(StreamListener):
	""" A listener handles tweets are the received from the stream. 
	This is a basic listener that just prints received tweets to stdout.

	"""
	def on_data(self, data):
		tweet_list.append(data)
		#print len(tweet_list)
		print data
		
		return True

	def on_error(self, status):
		print status
		
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



if __name__ == '__main__':
	
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)


    # If the authentication was successful, you should
    # see the name of the account print out
    

	stream = Stream(auth, l)
	
	#streaming_api = tweepy.streaming.Stream(auth, CustomStreamListener(), timeout=None)
	#streaming_api.filter(follow='@javastudy')	
	list_users = ['324915622091816962','324915621550751744'] 
	
	stream.filter(follow=list_users)
	#stream.sample()
	
	#print tweet_list
	
	#stream.filter(track=['google'])
