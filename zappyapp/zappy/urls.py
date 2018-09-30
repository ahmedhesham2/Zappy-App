from django.conf.urls import url
from views import *

urlpatterns = [ 
    url(r'^$', Slack_Events.as_view()),
    url(r'^gettweets$',getTweets)
]