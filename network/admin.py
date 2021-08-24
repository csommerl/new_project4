from django.contrib import admin
from .models import User, Post, Like, Follow

class UserAdmin(admin.ModelAdmin):
    list_display = ("pk", "username", "email")


class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "created", "poster", "content")


class LikeAdmin(admin.ModelAdmin):
    list_display = ("pk", "created", "liked_post", "liker", "like_status")


class FollowAdmin(admin.ModelAdmin):
    list_display = ("pk", "created", "followed", "follower", "follow_status")


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Follow, FollowAdmin)