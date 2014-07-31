import tweepy
import json
import cPickle
import zmq

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'PUpKEozSrCV5x06mc1uNDMgMN'
consumer_secret = 'q0W7N8wDCD41O9pPu8yej42BnJ138Gwpl2wQsB5wvxLqvciKQy'
access_token = '1315274378-RxFpa0iNmDucPaxMCENLaeeky9k4rL9JN0Zjn60'
access_token_secret = 'fjCiFRyXbIMFSGlykJMEhPxNxpj7YnbFreWoeCJBCLQCG'

tweet_list = ""

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        print ''
        # f = open('tweets.txt', 'a')
        # f.write(decoded['text'].encode('ascii', 'ignore'))
        # f.write('\n+++++++++++++')
        # f.close()
        socket.send_string(u"%i %s" % (10, unicode(decoded['text'].encode('ascii', 'ignore'))))
        print "Tweet Sent"
        # tweet_list = decoded['text'].encode('ascii', 'ignore')
        # f = open('tweet_pickle', 'wb')
        # cPickle.dump(tweet_list,f)
        # f.close()
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5556")

    print "Beginning Stream:"

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l)
    stream.filter(track=['macklemore', 'fries'])