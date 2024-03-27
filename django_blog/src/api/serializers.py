from rest_framework import serializers
from post.models import Post

# class PostListSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     status = serializers.CharField()

# class PostCreateSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     status = serializers.CharField()
#     user = serializers.IntegerField()
#     categories = serializers.ListField()

class PostDeleteModelSerializer(serializers.ModelSerializer):
     class Meta:
        model = Post
        fields = ['id']


class PostCreateModeltSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields=('title', 'status', 'user', 'categories', 'text')



class PostLisCreatetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields=('title', 'status', 'user','text')

class PostListModelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields=('title', 'status','text')
        




