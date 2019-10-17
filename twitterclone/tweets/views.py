from twitterclone.twitterusers.models import TwitterUser
from django.shortcuts import HttpResponseRedirect, reverse, render

sort = True


def sort(request, *args, **kwargs):
    html = "hello.html"
    items = Tweet.objects.filter().order_by('time')
    return render(request, html, {'text': items})


def addfollow(request, id):
    currentuser = request.user.twitteruser
    try:
        twitteruser = TwitterUser.objects.get(id=id)
    except TwitterUser.DoesNotExist():
        return HttpResponseRedirect(reverse('homepage'))

    currentuser.following.add(twitteruser)
    return HttpResponseRedirect(reverse('homepage'))


def removefollow(request, id):
    currentuser = request.user.twitteruser
    try:
        twitteruser = TwitterUser.objects.get(id=id)
    except TwitterUser.DoesNotExist():
        return HttpResponseRedirect(reverse('homepage'))

    currentuser.following.remove(twitteruser)
    return HttpResponseRedirect(reverse('homepage'))
