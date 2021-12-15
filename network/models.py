from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):
    def __str__(self):
        return f"{self.username}"


class Post(models.Model):
    poster = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts")
    content = models.CharField(max_length=280)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Post {self.pk} ({self.poster}'s post on {self.created.date()} at {self.created.time()})"


class Like(models.Model):
    liked_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="likes")
    liker = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="liked")
    like_status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    # if different from created, this means that it is deleted
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Like {self.pk} (At {self.created.time()} on {self.created.date()}, {self.liker} liked {self.liked_post})"


class Follow(models.Model):
    followed = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followers")
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follows")
    follow_status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Follow {self.pk} ({self.follower} followed {self.followed} on {self.created.date()} at {self.created.time()})"
