# from rest_framework import serializers

# from .models import Post

# class PostListSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     status = serializers.BooleanField()




# class PostCreateSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     is_actual = serializers.BooleanField()
#     user = serializers.IntegerField()
#     categories = serializers.ListField()


# class PostDeleteSerializer(serializers.Serializer):
#     post_id = serializers.IntegerField()


# # class PostListModelSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Post
# #         fields = ('title', 'status')

# # class PostCreateModelSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Post
# #         fields = ('title', 'status', 'user', 'categories')