
from django.contrib import admin
from django.urls import path, re_path

from post import views 


urlpatterns= [
        path('admin/', admin.site.urls),
        path('index/', views.index),
        re_path(r'^about/$', views.about), # начало и конец
        re_path(r'^g+', views.ggg), #1 или более раз
        re_path(r'^contact(?:s)?/$', views.contacts), # повтор либо 0 или 1 раз 
        re_path(r'^arсhive/\d{4}/$', views.arсhive),# ограничение кол-ва симоволов / цифр
        path('home/', views.home),
    ]
