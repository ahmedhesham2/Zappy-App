# Zappyapp

# we will use mongoDB as the Database for our web Application .

download mongoDB:
install mongoDB using: sudo pip install mongoengine
install mongoDB clients: sudo apt install mongodb-clients
install mongoDB server: sudo apt install mongodb-server

# we will use django framework as the backend for our project which will interact Slack Api & Tweeter Api .

download django and slack api and twitter api:
sudo apt-get install python-django
sudo apt-get install python-pip
sudo pip install django
sudo pip install djangorestframework
sudo pip install slackclient
pip install slackeventsapi
sudo pip install tweepy

run server: python manage.py runserver 0.0.0.0:8000

download node and angular:
https://nodejs.org/en/download/
sudo npm install -g @angular/cli


create slack app and bot then change in views:
Slack verification token , Slack Bot User Token which get from slack api (OAUTh & Permissions , Basic Information)

Activate Event Subscriptions and put your URL that listen to message event
and use ngrok to generate public domain in your local system
download ngrok:
https://ngrok.com/

# to create a valid url instead of localhost
    ./ngrok http 8000

create twitter app and then change in views:
TWITTER CONSUMER KEY, TWITTER CONSUMER SECRET,
TWITTER ACCESS TOKEN, TWITTER ACCESS SECRET.
getting from twitter api .



# to build your Angular App inside static file in your django App run this command :
ng build --prod --output-path Static File Path  --watch --output-hashing none

resources :
_______________

 1- http://docs.mongoengine.org/guide/defining-documents.html

 2- https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/

 3- https://api.slack.com/apps/

 4- https://apps.twitter.com/app/15012043/keys