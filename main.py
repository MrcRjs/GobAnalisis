# coding=utf-8
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import config
import datetime
import twitterUtils

consumer_key        = config.twitter['consumer_key']
consumer_secret     = config.twitter['consumer_secret']
access_token        = config.twitter['access_token']
access_token_secret = config.twitter['access_token_secret']
candidates          = config.candidates


class TwitaListener(StreamListener):

    def on_data(self, data):
        data = json.loads(data)
        if '' in data['text'].lower() and 'retweeted_status' not in data:
            words = twitterUtils.tweetWords(data['text'],3)
            hashtags = data['entities']['hashtags']
            print("\n@%s: %s" % (\
                data['user']['screen_name'],\
                data['text']))
            dt = datetime.datetime.strptime(data['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
            print(dt.strftime('%a %d %b %Y %H:%M:%S'))
            print(words)
            print(hashtags)
        return True

    def on_error(self, status_code):
        print ('Encountered error with status code: ' + str(status_code))
        return True

    def on_timeout(self):
        print ('Timeout...')
        return True

if __name__ == '__main__':

    l = TwitaListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    streamUnique = Stream(auth, l)
    streamUnique.filter(track = candidates, async = True)