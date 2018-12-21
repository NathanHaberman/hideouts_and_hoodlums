# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from apps.player import models
from django.contrib.auth.models import User


# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=75)
    # dm_id = models.ForeignKey('User', related_name='id', on_delete=models.CASCADE)
    # character_id = models.ManyToManyField(Character)
    level = models.IntegerField(default=1)
    funds = models.IntegerField(default=0)
    income = models.IntegerField(default=0)
    small_1 = models.IntegerField(default=0)
    small_2 = models.IntegerField(default=0)
    small_3 = models.IntegerField(default=0)
    small_4 = models.IntegerField(default=0)
    small_5 = models.IntegerField(default=0)
    small_6 = models.IntegerField(default=0)
    medium_1 = models.IntegerField(default=0)
    medium_2 = models.IntegerField(default=0)
    medium_3 = models.IntegerField(default=0)
    medium_4 = models.IntegerField(default=0)
    large_1 = models.IntegerField(default=0)
    large_2 = models.IntegerField(default=0)