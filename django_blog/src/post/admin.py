from django.contrib import admin

from .models import Post, Category, UserAccount

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','created_at', 'updated_at', 'is_actual']
    readonly_fields=[
        'created_at',
        'updated_at'

    ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','title','created_at', 'updated_at', 'is_active']
    readonly_fields=[
        'created_at',
        'updated_at'
    ]

@admin.register(UserAccount)
class UserAccount(admin.ModelAdmin):
    list_display=['id','mobile_phone','user','created_at', 'updated_at']
    readonly_fields=[
        'created_at',
        'updated_at'
    ]

# Register your models here.
