
from django.urls import path, re_path
# from django.shortcuts import redirect
from . import views 



urlpatterns = [
    path('', views.PostList.as_view(), name='posts'),
    path('create/', views.CreatePostView.as_view(), name='new_post'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('get_post/', views.get_post_handler),
    path('<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'), 
    #drf views
    ]