
from django.urls import path

from . import views

urlpatterns = [
    # Pages
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<str:profilename>", views.profile, name="profile"),

    # API Routes
    path("like/<str:postID>", views.like, name="like"),
    path("unlike/<str:postID>", views.unlike, name="unlike"),
    path("new-post-submit", views.new_post_submit, name="new-post-submit"),
    path("follow/<str:profilename>", views.follow, name="follow"),
    path("unfollow/<str:profilename>", views.unfollow, name="unfollow")
]
