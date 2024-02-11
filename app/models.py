from django.db import models


class API(models.Model):
    phone = models.CharField(max_length=16, verbose_name='Номер телефона')
    gender = models.CharField(max_length=16, verbose_name='Пол')
    username = models.CharField(max_length=128, verbose_name='Ник донора для фоток')
    api_id = models.CharField(max_length=32, verbose_name='ID из инструментов разработчика')
    api_hash = models.CharField(max_length=64, verbose_name='Hash из инструментов разработчика')
    is_activated = models.BooleanField(default=False, verbose_name='Был ли активирован')
