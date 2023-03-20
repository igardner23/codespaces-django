from django.db import models
import os
import tweepy

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=200)
    profile_pic = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tweet(models.Model):
    content = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name="tweets", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Community(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(User, related_name="communities")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    
def populate_models():
    auth = tweepy.OAuthHandler(os.environ['TWITTER_API_KEY'], os.environ['TWITTER_API_SECRET'])
    auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN'], os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
    api = tweepy.API(auth)
    user = api.get_user('twitter')
    user_model = User.objects.create(username=user.screen_name, password='password', email=user.email, first_name=user.name, last_name=user.name, bio=user.description, profile_pic=user.profile_image_url)
    for tweet in tweepy.Cursor(api.user_timeline, id=user.id).items(10):
        Tweet.objects.create(content=tweet.text, user=user_model)
    community = Community.objects.create(name='Twitter')
    community.users.add(user_model)
    community.save()