from django.shortcuts import render


def index(request, *args, **kwargs):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def addtweet(request):
    return render(request, 'addtweet.html')


def feed(request):
    return render(request, 'feed.html')


def profile(request):
    return render(request, 'profile.html')
