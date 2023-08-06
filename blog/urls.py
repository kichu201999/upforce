# urls.py
from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDeleteView
from blog import views

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDeleteView.as_view(), name='user-retrieve-update-delete'),
    path('posts/', views.BlogPostListCreateView.as_view(), name='blogpost-list-create'),
    path('posts/<int:pk>/', views.BlogPostRetrieveUpdateDeleteView.as_view(), name='blogpost-retrieve-update-delete'),
    path('likes/', views.LikeListCreateView.as_view(), name='like-list-create'),
    path('likes/<int:pk>/', views.LikeRetrieveUpdateDeleteView.as_view(), name='like-retrieve-update-delete'),
]
