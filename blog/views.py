# views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import User, BlogPost, Like
from .serializers import UserSerializer, BlogPostSerializer, LikeSerializer
from django.core.exceptions import PermissionDenied


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        user = self.get_object()
        if user == self.request.user:
            serializer.save()
        else:
            raise PermissionDenied("You are not allowed to update this user.")

    def perform_destroy(self, instance):
        if instance == self.request.user:
            instance.delete()
        else:
            raise PermissionDenied("You are not allowed to delete this user.")


class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BlogPostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        post = self.get_object()
        if post.user == self.request.user:
            serializer.save()
        else:
            raise PermissionDenied("You are not allowed to edit this blog post.")

    def perform_destroy(self, instance):
        if instance.user == self.request.user:
            instance.delete()
        else:
            raise PermissionDenied("You are not allowed to delete this blog post.")
        

class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        like = self.get_object()
        if like.user == self.request.user:
            serializer.save()
        else:
            raise PermissionDenied("You are not allowed to update this like.")

    def perform_destroy(self, instance):
        if instance.user == self.request.user:
            instance.delete()
        else:
            raise PermissionDenied("You are not allowed to delete this like.")