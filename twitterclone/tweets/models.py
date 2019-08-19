from django.db import models
from twitterclone.twitteruser.models import TwitterUser
from django.utils import timezone


class Tweet(models.Model):
    tweeter = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, null=True, blank=True)
    body = models.CharField(max_length=140)
    time = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.body
