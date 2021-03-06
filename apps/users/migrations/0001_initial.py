# Generated by Django 3.2.4 on 2021-06-14 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.ImageField(default='image/profile/unknown_user.png', upload_to='profile/image')),
                ('website_url', models.CharField(blank=True, max_length=255)),
                ('facebook_url', models.CharField(blank=True, max_length=255)),
                ('twitter_url', models.CharField(blank=True, max_length=255)),
                ('instagram_url', models.CharField(blank=True, max_length=255)),
                ('pinterest_url', models.CharField(blank=True, max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
