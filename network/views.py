from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Post, Like, Follow


def index(request):
    # get all posts
    all_posts = get_all_posts()

    context = {
        "all_posts": all_posts,
    }
    return render(request, "network/index.html", context)


def get_all_posts():
    # get all posts
    all_posts = Post.objects.all().values()
    
    # convert to list, in order to then sort
    all_posts = list(all_posts)
    all_posts.sort(key=lambda post:post['created'], reverse=True)

    # get poster's name and likes for each post and add to post data
    for post in all_posts:
        # get poster info
        poster_id = post['poster_id']
        poster = User.objects.get(pk=poster_id).username
        post['poster'] = poster
        # get like info
        post_id = post['id']
        likes = Like.objects.filter(liked_post=post_id)
        #### convert to list?
        likes = likes.count()
        post['likes'] = likes

    return all_posts


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
