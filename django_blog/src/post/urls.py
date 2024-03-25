
from django.urls import path, re_path
from django.shortcuts import redirect
from . import views 



urlpatterns = [
    path('', views.PostList.as_view(), name='posts'),
    # path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    re_path(r'^archive/(?P<year>[0-9]{4})/$', views.post_archive),
    path('get_post/', views.get_post_handler),
    path('template_test/', views.template_test),
    #Create post
    path('create/', views.CreatePostView.as_view(), name='new_post'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'), 

]