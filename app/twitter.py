import  oauth2 as oauth
import json
def tweets(username):
    CONSUMER_KEY = "sLTmyKHtsCMeotWpz7WI90BsV"
    CONSUMER_SECRET = "93EGGV3xxqqlHGFAPutKZpIEnOeaG7M5Edw1iCL9xPgkF6z5sd"
    ACCESS_KEY = "818867834033840128-r9ra4JgFMVvYq5tXuKVK12AWBKWgm5F"
    ACCESS_SECRET = "x2btLTTKtQywVP8qFdvJAN2y6zrMABFien4KTwDKYbBX3"
    consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
    client = oauth.Client(consumer, access_token)
    timeline_endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+username+"&count=20"
    response, data = client.request(timeline_endpoint)
    tweets = json.loads(data)
    a=[]
    for tweet in tweets:
       t= tweet['text']
       a.append(t)
    return a

