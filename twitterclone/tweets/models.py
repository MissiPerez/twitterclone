from django.db import models
from twitterclone.twitterusers.models import TwitterUser
from django.utils import timezone
from django.contrib.auth.models import User


class Tweet(models.Model):
    tweeter = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, null=True, blank=True)
    body = models.CharField(max_length=140)
    time = models.DateTimeField(default=timezone.now, blank=True)
    likes = models.ManyToManyField(User, related_name="folowers")

    def __str__(self):
        return self.body

