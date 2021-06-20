from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # fields = '__all__'
        fields = ['user', 'user_image', 'user_image', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url',
                  'pinterest_url', ]

    def to_representation(self, instance):
        representation = super(ProfileSerializer, self).to_representation(instance)
        representation['user'] = instance.user.first_name
        return representation
