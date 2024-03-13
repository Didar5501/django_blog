
from django.contrib import admin
from django.urls import path, re_path, include

from post import views 

from post.views import page_404

from django.conf import settings

urlpatterns= [
        path('admin/', admin.site.urls),
        path('post/', include('post.urls')),
    ]

handler404 = page_404