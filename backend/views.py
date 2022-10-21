import json

from django.http import HttpResponse

from .models import Profile, Post, Like, Unlike
from .serializers import ProfileSerializer, PostSerializer, LikeSerializer, UnlikeSerializer
from rest_framework import generics

"""
I used generic class-based views, beacuse of pretty concise code
"""


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostLikeView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class PostUnlikeView(generics.CreateAPIView):
    queryset = Unlike.objects.all()
    serializer_class = UnlikeSerializer


class AnaliticsView(generics.ListAPIView):
    serializer_class = LikeSerializer

    def get(self, request, *args, **kwargs):
        likes_count = Like.objects.filter(publication_date__range=[kwargs['date_from'], kwargs['date_to']])
        if len(likes_count) > 0:
            mimetype = 'application/json'
            return HttpResponse(json.dumps({'For this period of time there were LIKES in ammount': len(likes_count)}), mimetype)
        else:
            return HttpResponse(json.dumps({'There were no likes': []}))

"""
need to make it
"""

class ActivityView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


