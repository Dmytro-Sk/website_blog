from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.ImageField(default='images/profile/unknown_user.png', upload_to='profile/images')
    website_url = models.CharField(max_length=255, blank=True)
    facebook_url = models.CharField(max_length=255, blank=True)
    twitter_url = models.CharField(max_length=255, blank=True)
    instagram_url = models.CharField(max_length=255, blank=True)
    pinterest_url = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self):
        super().save()

        img = Image.open(self.user_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.user_image.path)
