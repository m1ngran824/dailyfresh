from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    class Meta:
        db_table = 'df_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Address:
    receiver = models.CharField(max_length=20, verbose_name='收件人')
    phone_number = models.CharField(max_length=11, verbose_name='手机号')
    delivery_address = models.CharField(max_length=200, verbose_name='收货地址')
    post_code = models.CharField(max_length=10, blank=True, null=True, verbose_name='邮编')
    is_default = models.BooleanField(default=False, verbose_name='是否默认')
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=False, null=False, verbose_name='所属账户')

    class Meta:
        db_table = 'df_address'
        verbose_name = '地址'
        verbose_name_plural = verbose_name
