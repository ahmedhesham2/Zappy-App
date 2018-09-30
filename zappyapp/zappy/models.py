from __future__ import unicode_literals

from django.db import models
from mongoengine import *

connect('zappyapp-db')

class Tweet(Document):
    tweet_id = IntField(required = True)
    tweet_text = StringField(max_length = 280,required = True)
    tweet_time = DateTimeField(required = True)

