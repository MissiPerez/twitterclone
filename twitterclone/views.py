from twitterclone.tweets.models import Tweet
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from twitterclone.twitterusers.forms import SignupForm, AddUserForm
from twitterclone.tweets.forms import TweetForm
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.authentication.forms import LoginForm

from django.contrib.auth.models import User
from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required

@login_required()
def index(request, *args, **kwargs):
    html = 'home.html'
    followed_users = request.user.twitteruser.following.all()
    loggedin_tweets = Tweet.objects.filter(tweeter=request.user.twitteruser)
    following_tweets = Tweet.objects.filter(tweeter__in=followed_users)
    items = loggedin_tweets | following_tweets 
    return render(request, html, {'feed': items})


def signup(request):
    html = 'signup.html'
    form = None
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                data["username"], data["password"])
            login(request, user)
            TwitterUser.objects.create(
                handle=data["name"],
                bio=data["bio"],
                person=user
            )
            return HttpResponseRedirect(reverse("homepage"))
    else:
        form = SignupForm()
    return render(request, html, {"form": form})



@login_required()
def addtweet(request):
    html = "addtweet.html"
    form = None
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(
                body=data["body"],
                tweeter=request.user.twitteruser
            )
        return render(request, "added.html")
    else:
        form = TweetForm()
    return render(request, html, {"form": form})
    # notifications start here 


def profile_view(request, id):
    html = "profile.html"
    twitter_user = TwitterUser.objects.get(id=id)
    tweets = Tweet.objects.filter(tweeter=twitter_user)
    count = len(tweets)
    follow_count = twitter_user.following.count()
    return render(request, html, {"auth": twitter_user, "tweets": tweets, "tweetcount": count, "followcount": follow_count})


def tweet_view(request, id):
    html = 'tweetview.html'
    tweet = Tweet.objects.get(id=id)
    return render(request, html, {"tweet": tweet})


def login_view(request):
    html = 'login.html'
    form = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data["username"], password=data["password"])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get("next", "/"))
    else:
        form = LoginForm()
    return render(request, html, {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
