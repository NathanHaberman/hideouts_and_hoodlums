# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=75)
    role = models.CharField(max_length=75)
    level = models.IntegerField()
    specialty = models.IntegerField()
    specialty_level = models.IntegerField(default=1)
    money = models.IntegerField()
    # user_id = models.ForeignKey('User', related_name='id', on_delete=models.CASCADE)
