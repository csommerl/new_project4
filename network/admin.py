from django.contrib import admin
from .models import User, Post, Like, Follow

class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email")


class PostAdmin(admin.ModelAdmin):
    list_display = ("created", "poster", "content")


class LikeAdmin(admin.ModelAdmin):
    list_display = ("created", "liker", "liked_post")


class FollowAdmin(admin.ModelAdmin):
    list_display = ("created", "follower", "followed")


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Follow, FollowAdmin)