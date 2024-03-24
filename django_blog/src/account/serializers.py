from rest_framework import serializers

class PostListSerializer(serializers.Serializer):
    title = serializers.CharField()
    is_actual = serializers.BooleanField()


class PostCreateSerializer(serializers.Serializer):
    title = serializers.CharField()
    is_actual = serializers.BooleanField()
    user = serializers.IntegerField()
    categories = serializers.ListField()


class PostDeleteSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
