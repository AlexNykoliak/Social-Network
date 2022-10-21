from .models import Profile, Post, Like, Unlike
from .serializers import PostSerializer, LikeSerializer, UnlikeSerializer
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
