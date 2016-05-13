import time
import requests
import tweepy
import urllib
import os
import random
 
page = 1
# Tag.
url = 'https://danbooru.donmai.us/posts.json?tags=tachibana_marika&limit=1'
# Twi.
consumer_key =
consumer_secret =
access_key =
access_secret =
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
 
api = tweepy.API(auth)
       
while True:
    try:
        random.seed()
        jsURL = url + str(random.randint(1,1000))
        response = requests.get(jsURL)
        pageTable = response.json()
        arrayNum = random.randint(0,9)
       
        imageSource = pageTable[arrayNum]["file_url"]
        imageURL = "http://danbooru.donmai.us" + imageSource
        print imageURL
        sourceURL = "http://danbooru.donmai.us/posts/" + str(pageTable[arrayNum]["id"])
        print sourceURL
        urllib.urlretrieve(imageURL, 'image.jpg')
       
        # tweet.
        tweetString = sourceURL + " "
        api.update_with_media('image.jpg', status=tweetString)
       
        os.remove('image.jpg')
        # req in hour.
        time.sleep(1800)
       
    except tweepy.error.TweepError:
        print "Image too large, finding a different image..."
