# serializers.py
from rest_framework import serializers
from .models import User, BlogPost, Like


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    #likes = LikeSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, obj):
        return obj.likes.count()

    class Meta:
        model = BlogPost
        fields = '__all__'
