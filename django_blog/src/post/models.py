from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=128)
    photo = models.ImageField(upload_to='post/imgs/', null=True)