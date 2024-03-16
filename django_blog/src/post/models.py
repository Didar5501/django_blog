import random
from django.contrib.auth.models import User
from django.db import models


class UserAccount(models.Model):
    mobile_phone= models.CharField(max_length=12)
    user =models.OneToOneField(to=User, related_name='account', on_delete=models.PROTECT)
    created_at=models.DateTimeField(auto_now_add=True, null=True) #дата создания
    updated_at=models.DateTimeField(auto_now=True, null=True) #дата последнего обновления записи

    class Meta:
        db_table='UserAccount'

class Post(models.Model):
    title = models.CharField(max_length=128, null=True, default=f'post{int(random.random()*100)}')
    created_at=models.DateTimeField(auto_now_add=True, null=True) #дата создания
    updated_at=models.DateTimeField(auto_now=True, null=True) #дата последнего обновления записи
    is_actual = models.BooleanField(blank=True, null=True) # True/False
    photo = models.ImageField(upload_to='imgs/posts', null=True, blank=True)
    user = models.ForeignKey(to=User, related_name='post', on_delete=models.CASCADE)
    categories=models.ManyToManyField(
        to='Category',
        related_name='posts',
    )
    
    class Meta:
        ordering =['-updated_at']

    def __str__(self) -> str:
        return f'{self.id} - {self.title}'

class Category(models.Model):
    created_at=models.DateTimeField(auto_now_add=True, null=True) 
    updated_at=models.DateTimeField(auto_now=True, null=True) 
    title = models.CharField(max_length=128)
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categoryes'

    def __str__(self) -> str:
        return self.title
  
    
   
# python manage.py makemigrations
# python manage.py migrate

# python manage.py shell
# exit() - выход из шелла

# all() - SELECT *
# filter() - Where
# get() - Where (возвращает 1 объект)

# Post.objects.filter().first() - Вытащит первую запись
# Post.objects.filter().first()

#  Post.objects.filter().last() 


#from post.models import Post



# filter(***__gt) - больше чем
# filter(***__gte )- большеили равно чем
# filter(***__lt )- меньше чем
# filter(***__lte )- меньше или равно чем