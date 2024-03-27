from django.shortcuts import render

# from .serializers import PostListSerializer, PostCreateSerializer, PostDeleteSerializer
from .serializers import PostCreateModeltSerializer, PostLisCreatetModelSerializer, PostListModelDetailSerializer, PostDeleteModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from post.models import Post

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

class PostList(ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostLisCreatetModelSerializer

class PostDetail(RetrieveUpdateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostListModelDetailSerializer
    


from rest_framework.generics import DestroyAPIView

class PostDelete(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDeleteModelSerializer
 