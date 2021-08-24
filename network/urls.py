
from django.urls import path

from . import views

urlpatterns = [
    # Pages
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # API Routes
    path("like/<str:postID>", views.like, name="like"),
    path("unlike/<str:postID>", views.unlike, name="unlike")
]
