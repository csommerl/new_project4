from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse

# My additional modules + models
from .models import User, Post, Like, Follow
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm


def index(request):
    form = NewPostForm()

    # get user id in order to get like info
    user_id = request.user.id
    # get all posts
    all_posts = Post.objects.all().values()
    # get post data
    all_posts = get_post_data(all_posts, user_id)
    
    # pagination
    paginator = Paginator(all_posts, 10) ##### in documentation example, Paginator takes a simple `objects.all()`
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        "page_obj": page_obj,
        "form": form
    }

    return render(request, "network/index.html", context)


def get_post_data(posts, user_id):
    # convert to list, in order to then sort
    posts = list(posts)
    posts.sort(key=lambda post:post['created'], reverse=True)

    # get poster's name and likes for each post and add to post data
    for post in posts:
        # get poster info
        poster_id = post['poster_id']
        poster = User.objects.get(pk=poster_id).username
        post['poster'] = poster
        
        # get number of likes info
        post_id = post['id']
        likes = Like.objects.filter(liked_post=post_id, like_status=True)
        likes_count = likes.count() #### no need convert to list to get count?
        post['likes_count'] = likes_count

        # get whether user likes the post
        likes_by_user = list(likes.filter(liker=user_id, like_status=True))
        if likes_by_user == []:
            like_button = "Like"
        else:
            like_button = "Unlike"
        post['like_button'] = like_button

    return posts


@csrf_exempt
def like(request, postID):
    liked_post = int(postID)
    liker = request.user.pk
    if request.method == "POST":
        like = Like(liked_post=Post.objects.get(pk=liked_post), liker=User.objects.get(pk=liker))
        like.save()
        return HttpResponse(status=204)
    else:
        return JsonResponse({
            "error": "POST request required."
        }, status=400)


@csrf_exempt
def unlike(request, postID):
    unliked_post = int(postID)
    liker = request.user.pk
    if request.method == "POST":
        # need like_status=True to get only the most recent one
        like = Like.objects.get(liked_post=unliked_post, liker=liker, like_status=True)
        like.like_status = False
        like.save()
        return HttpResponse(status=204)
    else:
        return JsonResponse({
            "error": "POST request required."
        }, status=400)


def new_post_submit(request):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post = Post(
                poster = request.user,
                content = cd["content"]
            )
            post.save()
        return HttpResponseRedirect(reverse("index"))


def profile(request, profilename):
    
    # get user id in order to get like info
    user_id = request.user.id

    # try if user with profilename exists
    try:
        # get profile posts
        profile_id = User.objects.get(username=profilename).pk
        profile_posts = Post.objects.filter(poster=profile_id).values()
        profile_posts = get_post_data(profile_posts, user_id)

        # pagination
        paginator = Paginator(profile_posts, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # profile info
        followers = Follow.objects.filter(followed=profile_id, follow_status=True).count()
        follows = Follow.objects.filter(follower=profile_id, follow_status=True).count()
        
        # set follow button; maybe do it with if statement?
        try:
            Follow.objects.get(followed=profile_id, follower=user_id, follow_status=True)
            follow_button = "Unfollow"
        except:
            follow_button = "Follow"
        
        context = {
            "profilename": profilename,
            "page_obj": page_obj,
            "followers": followers,
            "follows": follows,
            "follow_button": follow_button
        }

    except:
        message = "No user with that profile name exists."

        context = {
            "profilename": profilename,
            "message": message
        }

    return render(request, "network/profile.html", context)


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
