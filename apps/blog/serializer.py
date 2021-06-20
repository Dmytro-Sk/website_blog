from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title', 'author', 'body', 'add_post_date', 'category', 'likes', 'dislikes']

    def to_representation(self, instance):
        representation = super(PostSerializer, self).to_representation(instance)
        representation['add_post_date'] = instance.add_post_date.strftime('%d-%m-%Y')
        return representation
