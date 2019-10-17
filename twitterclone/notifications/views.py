from django.shortcuts import render
from twitterclone.notifications.models import Notifications


def notification_view(request, *args, **kwargs):
    html = "notification.html"
   
    return render(request, html)

