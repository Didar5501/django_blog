
from django.urls import path, re_path
from django.shortcuts import redirect
from . import views 


# urlpatterns= [
#         path('index/', views.index),
#         re_path(r'^about/$', views.about), # начало и конец
#         re_path(r'^g+/$', views.ggg), #1 или более раз
#         re_path(r'^contact(?:s)?/$', views.contacts), # повтор либо 0 или 1 раз 
#         re_path(r'^arсhive/\d{4}/$', views.arсhive),# ограничение кол-ва симоволов / цифр
#         re_path(r'^arсhive-2/1[7-9]\d{2}/$', views.arсhive_2),# входжение цифр
#         re_path(r'^group/[A-C]\d{4}/$', views.group),# входжение букв алфавита
#         path('home/', views.home),# Домашеяя работа за 22/02/24
#     ]
urlpatterns = [
    path('', views.posts, name='home'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    re_path(r'^archive/(?P<year>[0-9]{4})/$', views.post_archive),
    path('get_post/', views.get_post_handler),
    path('template_test/', views.template_test)
]