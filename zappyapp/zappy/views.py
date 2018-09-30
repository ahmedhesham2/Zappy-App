import datetime

from django.shortcuts import render
from slackclient import SlackClient
import os
import sys
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import time
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from models import Tweet
import json
from django.http import HttpResponse

# Create your views here.
# SLACK_VERIFICATION_TOKEN = 'Q5UFq4NaMDGuoRae5mwRNpnN'
# SLACK_BOOT_TOKEN = 'xoxb-445124356224-445676911636-yo9dS2B7j0eQGyYLB0OrUpgH'

# to check if the coming request from our workspace or not
VeriFication_Token = 'Q5UFq4NaMDGuoRae5mwRNpnN'

# to create slack client to interact with our workspace
Slack_Bot_User_Token = 'xoxb-445124356224-445676911636-yo9dS2B7j0eQGyYLB0OrUpgH'

# slack client
slack_client = SlackClient(Slack_Bot_User_Token)

#Twitter Keys
consumer_key = 'YOUR-CONSUMER-KEY'
consumer_secret = 'YOUR-CONSUMER-SECRET'
access_token = 'YOUR-ACCESS-TOKEN'
access_secret = 'YOUR-ACCESS-SECRET'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class Slack_Events(APIView) :

    # method where we handle bot user request
    def post(self, request , *args , **Kwargs):

        # print "in post method"
        slack_request_msg = request.data

        # checking if request coming from correct workspace
        if slack_request_msg.get('token') != VeriFication_Token :
            return Response(status = status.HTTP_403_FORBIDDEN)

        #verification challenge
        if slack_request_msg.get('type') == 'url_verification' :
            return Response(data=slack_request_msg , status = status.HTTP_200_OK)

        # event listening
        if 'event' in slack_request_msg:
            msg_event = slack_request_msg.get('event')

            # check if msg coming from slack api
            if msg_event.get('subtype') == 'bot_message':
                return Response(status=status.HTTP_200_OK)

            # process user's message
            user = msg_event.get('user')
            text = msg_event.get('text')
            channel = msg_event.get('channel')

            # respond with hello msg
            bot_text = 'Hi <@{}> :wave:'.format(user)
            if 'go' in text.lower():
                # print "gooooooooooooooooooooooooooooooooooooooooooooooooo"
                slack_client.api_call(method='chat.postMessage',
                                channel=channel,
                                text=bot_text)

                # tweet_obj = Tweet(tweet_id=1, tweet_text="Hi Hesham", tweet_time=datetime.datetime.now())
                # tweet_obj.save()
                # x = Tweet.objects()
                # for t in x :
                #     print t.tweet_id , t.tweet_text
                #     print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

                # to get all tweets in the timeline
                All_Tweets = tweepy.Cursor(api.home_timeline).items()

                for iter in All_Tweets :
                    newTweet = Tweet.objects(tweet_id=iter.id)

                    # check if this tweet dosen't exist before
                    if not newTweet :
                        tweet_obj = Tweet(tweet_id = iter.id,tweet_text= iter.text,tweet_time = iter.created_at)
                        tweet_obj.save()
                    else :
                        pass

            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_200_OK)


    def get(self, request , *args , **Kwargs):
        # print "Hello Slack"
        return render(request, 'base.html', {})


def getTweets(request):
    tweets_res = []
    tweets = Tweet.objects()
    for tweet in tweets:
        tweets_res.append({"text":tweet.tweet_text,"time":str(tweet.tweet_time)})

    return HttpResponse(json.dumps(tweets_res))