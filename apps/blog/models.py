from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return f'{self.title} (by {self.author})'

    @staticmethod
    def get_absolute_url():
        return reverse('blog:blog-page')
