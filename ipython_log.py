# IPython log file

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
    
from hello_world.core.models import *
get_ipython().run_line_magic('logstart', '')
