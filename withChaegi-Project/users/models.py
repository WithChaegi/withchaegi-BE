from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(verbose_name='전화번호', max_length=11)

# class UserInfo(models.Model):
#     phone_sub = models.CharField(verbose_name='보조 전화번호', max_length=11)

#     user = models.ForeignKey(to='User', on_delete=models.CASCADE)