from rest_framework import serializers
from .models import Profile, Post, Like, Unlike


class ProfileSerializer(serializers.ModelSerializer):
    """
    Profile Serializer
    """
    class Meta:
        model = Profile
        fields = ['user', 'bio']


class PostSerializer(serializers.ModelSerializer):
    """
    Post Serializer
    """
    class Meta:
        model = Post
        fields = ['author', 'title', 'body', 'publication_date']

    # Make representation instead of id we will have author real name
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['author'] = instance.author.username
        return ret


class LikeSerializer(serializers.ModelSerializer):
    """
    Like Serializer
    """
    class Meta:
        model = Like
        fields = ['user', 'post', 'like', 'publication_date']


class UnlikeSerializer(serializers.ModelSerializer):
    """
    Unlike Serializer
    """
    class Meta:
        model = Unlike
        fields = ['user', 'post', 'unlike', 'publication_date']