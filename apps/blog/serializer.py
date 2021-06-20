from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title', 'author', 'body', 'add_post_date', 'category', 'likes', 'dislikes']
