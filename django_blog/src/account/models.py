from django.db import models
from django.contrib.auth.models import User
from django.db import models

class UserAccount(models.Model):
    mobile_phone= models.CharField(max_length=12)
    user =models.OneToOneField(to=User, related_name='account', on_delete=models.PROTECT)
    created_at=models.DateTimeField(auto_now_add=True, null=True) #дата создания
    updated_at=models.DateTimeField(auto_now=True, null=True) #дата последнего обновления записи

    def __str__(self) -> str:
        return f'{self.id} ---{self.mobile_phone}'

    class Meta:
        db_table='UserAccount'
        ordering =['-created_at']
        verbose_name='User account'
        verbose_name_plural='Users accounts'

# Create your models here.
