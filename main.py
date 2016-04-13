#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import config
import datetime

consumer_key = config.twitter['consumer_key']
consumer_secret = config.twitter['consumer_secret']
access_token = config.twitter['access_token']
access_token_secret = config.twitter['access_token_secret']


class TwitaListener(StreamListener):

    def on_data(self, data):
        data = json.loads(data)
        if '' in data['text'].lower() and 'retweeted_status' not in data:
            print("\n@%s: %s" % (\
                data['user']['screen_name'],\
                data['text'],))
            dt = datetime.datetime.strptime(data['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
            print(dt.strftime('%a %d %b %Y %H:%M:%S'))
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    l = TwitaListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    streamPan = Stream(auth, l)
    streamPri = Stream(auth, l)

    streamPan.filter(track=['Tony Gali', 'Moreno Valle'], async=True)
    streamPri.filter(track=['Blanca Alcalá'], async=True)
