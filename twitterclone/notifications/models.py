from django.db import models


class Notifications(models.Model):
    notification = models.BooleanField()

    def __str__(self):
        return self.name
