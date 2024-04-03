from rest_framework import serializers
from post.models import Post
import os
import re

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
        fields = ['id']   #Домашка


class PostCreateModeltSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'status', 'text', 'image', 'user', 'categories')
    
    def validate_status(self, value):
        if value not in ['ACTIVE', 'DRAFT']:  
            raise serializers.ValidationError("Статус должен быть 'ACTIVE' или 'DRAFT'")
        return value

    def validate(self, attrs):
        print(attrs)
        if  attrs['title'][:4] !='Post':
            raise serializers.ValidationError("Не канает: title должен начинаться с Post ")
        return attrs

    def validate_text(self, value):
        if not value.strip():  
            raise serializers.ValidationError("Текст не может быть пустым")
        return value

    def validate_image(self, value):
        file_name = value.name
        file_extension = os.path.splitext(file_name)[1].lower()
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
        if file_extension not in image_extensions:
            raise serializers.ValidationError("Формат файла изображения недопустим")
        return value

class PostDetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields=('title', 'status','text','categories')

class PostListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields=('title', 'status', 'user', 'categories', 'text')





        




