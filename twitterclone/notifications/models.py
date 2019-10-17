from django.db import models
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.tweets.models import Tweet


class Notifications(models.Model):
    owner = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, related_name='owner')
    mentions = models.ManyToManyField(Tweet)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"to: {self.twitter_user} - {self.tweet.text} - from: {self.tweet.twitter_user.username}"
