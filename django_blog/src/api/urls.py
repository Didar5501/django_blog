from django.urls import path, re_path
from . import views 

urlpatterns = [

    #via APIView
    # path('post_list_apiview/', views.PostListAPIView.as_view(), name = 'post_list_apiview'),
    # path('post_detail_apiview', views.PostDetailAPIView.as_view(), name = 'post_detail_apiview'),

    #via generics
    path('post_create/', views.PostCreate.as_view(), name='post_create_generic') ,
    path('post_list/', views.PostList.as_view(), name='post_list_generic') ,
    path('post_detail/<int:pk>', views.PostDetail.as_view(), name='post_detail_generic_'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete_generic_'),


 
]