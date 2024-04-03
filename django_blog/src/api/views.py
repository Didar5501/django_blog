from django.shortcuts import render

# from .serializers import PostListSerializer, PostCreateSerializer, PostDeleteSerializer
from .serializers import PostCreateModeltSerializer, PostDetailModelSerializer, PostDeleteModelSerializer, PostListModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from post.models import Post
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer, MultiPartRenderer, HTMLFormRenderer

from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from rest_framework.authentication import TokenAuthentication


# class PostListAPIView(APIView):
#     def get(self, request):
#         return Response (
#             {
#                 'data': 1
#             }
#         )

# class PostDetailAPIView(APIView):
#     def get(self, request):
#         {
#             'data': 2
#         }


#Generics

class PostCreate(CreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostCreateModeltSerializer
    # renderer_classes=[HTMLFormRenderer,MultiPartRenderer]
    permission_classes=[IsAuthenticatedOrReadOnly]


    


class PostList(ListAPIView):
    # permission_classes=[]
    queryset=Post.objects.all()
    serializer_class=PostListModelSerializer
    # renderer_classes=[JSONRenderer]
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]




class PostDetail(RetrieveUpdateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostDetailModelSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]



    


from rest_framework.generics import DestroyAPIView

class PostDelete(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDeleteModelSerializer
    permission_classes=[IsAdminUser]

 