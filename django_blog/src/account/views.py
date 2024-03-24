from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserAccount
from django.contrib.auth.models import User

from post.models import Post
from .serializers import PostListSerializer, PostCreateSerializer

from .serializers import PostDeleteSerializer

from rest_framework import status

 

class AccountAPIView(APIView):
    def get(self, request):
        accounts_mobile_phones = UserAccount.objects.all().values('mobile_phone')
        return Response (list(accounts_mobile_phones))
    
    def post(self, request):
        print(request.data)
        return Response('test')


class PostAPIView(APIView):
    def get(self, request):
        post_queryset = Post.objects.all()
        serializer = PostListSerializer(post_queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=PostCreateSerializer(data=request.data)
        serializer.is_valid()
        #Creating post
        categories = serializer.validated_data.get('categories')
        user = User.objects.get(id=serializer.validated_data.pop('user'))
        categories = serializer.validated_data.pop('categories')
        print(serializer.validated_data)
        post = Post.objects.create(user=user,**serializer.validated_data)
        print(post.categories.all())
        post.categories.add(*categories)
        return Response('Created')


    def delete(self, request):
        serializer = PostDeleteSerializer(data=request.data)
        if serializer.is_valid():
            post_id = serializer.validated_data['post_id']
            try:
                post = Post.objects.get(id=post_id)
                post.delete()
                return Response('Post deleted successfully', status=status.HTTP_204_NO_CONTENT)
            except Post.DoesNotExist:
                return Response('Post does not exist', status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)