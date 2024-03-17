from rest_framework import serializers

class PostListSerializer(serializers.Serializer):
    title = serializers.CharField()
    is_actual = serializers.BooleanField()

