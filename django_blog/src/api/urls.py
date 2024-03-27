from django.urls import path, re_path
from . import views 

urlpatterns = [
    path('post/', views.PostList.as_view(), name='post_list') ,
    path('post/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),


 
]