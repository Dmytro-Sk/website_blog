from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse('blog:blog-page')


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    add_post_date = models.DateTimeField(auto_now_add=True)
    change_post_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    likes = models.ManyToManyField(User, related_name='post_likes')
    dislikes = models.ManyToManyField(User, related_name='post_dislikes')
    like_updated_at = models.DateTimeField(auto_now=timezone.now())

    def __str__(self):
        return self.title

    @staticmethod
    def get_absolute_url():
        return reverse('blog:blog-page')

    def sum_likes(self):
        return self.likes.count()

    def sum_dislikes(self):
        return self.dislikes.count()
