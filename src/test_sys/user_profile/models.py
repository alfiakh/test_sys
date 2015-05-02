# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name=u'Пользователь')

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'
