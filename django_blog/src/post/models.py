import random
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


status_choices = (
    ('ACTIVE', 'Active'),
    ('DRAFT', 'Draft'),
)

class Post(models.Model):
    title = models.CharField(verbose_name='Заголовок поста', max_length=225)
    text = models.TextField(verbose_name='Текст поста', max_length=2048)

    status = models.CharField(
        verbose_name='Статус поста',
        max_length=6,
        choices=status_choices,
        default='DRAFT'
    )

    image = models.ImageField(
        verbose_name='Изображение поста',
        upload_to='imgs/posts', 
        null=True, 
        blank=True)
    
    created_at=models.DateTimeField(auto_now_add=True, null=True) #дата создания
    updated_at=models.DateTimeField(auto_now=True, null=True) #дата последнего обновления записи
 
    
    user = models.ForeignKey(
        verbose_name='Автор поста',
        to=User, 
        related_name='post', 
        on_delete=models.CASCADE)

    categories=models.ManyToManyField(
        verbose_name='Категории',
        to='Category',
        related_name='posts',
    )
    
    def __str__(self) -> str:
        return f'{self.id} --- {self.title}'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})


    class Meta:
        db_table='post_post'
        ordering =['-created_at']
        verbose_name='Пос'
        verbose_name_plural='Посты'



class Category(models.Model):
    title = models.CharField(
        verbose_name='Название категории',
        max_length=255,
        unique = True,
        )

    is_active = models.BooleanField(
        verbose_name='Статус категории',
        default=False)


    created_at=models.DateTimeField(auto_now_add=True, null=True) 
    updated_at=models.DateTimeField(auto_now=True, null=True) 
    
    def __str__(self) -> str:
            return f'{self.id} --- {self.title}'

    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

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