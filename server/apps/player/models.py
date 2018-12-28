# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class CharacterManager(models.Manager):
    def validator(self, post_data):
        errors = []
        if len(post_data['first_name']) > 75 | len(post_data['first_name']) < 1:
            errors.append('first_name')
        if len(post_data['role']) > 75 | len(post_data['role']) < 1:
            errors.append('role')
        if post_data['level'] > 20 | post_data['level'] < 1:
            errors.append('level')
        if post_data['specialty'] > 10 | post_data['specialty'] < 1:
            errors.append('specialty')
        if post_data['specialty_level'] > 5 | post_data['specialty_level'] < 1:
            errors.append('specialty_level')
        if post_data['money'] != 0:
            errors.append('money')
        return errors

class Character(models.Model):
    name = models.CharField(max_length=75)
    role = models.CharField(max_length=75)
    level = models.IntegerField()
    specialty = models.IntegerField()
    specialty_level = models.IntegerField(default=1)
    money = models.IntegerField()
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

class UserManager(models.Manager):
    def validator(self, post_data):
        errors = []
        if len(post_data['first_name']) > 75 | len(post_data['first_name']) < 1:
            errors.append('first_name')
        if len(post_data['last_name']) > 75 | len(post_data['last_name']) < 1:
            errors.append('last_name')
        if len(post_data['email']) > 75 | len(post_data['email']) < 1:
            errors.append('email')
        if len(post_data['username']) > 75 | len(post_data['username']) < 1:
            errors.append('username')
        if (post_data['password'] == post_data['confirm_password']):
            if len(post_data['password']) > 75 | len(post_data['password']) < 8:
                errors.append('password')
        else:
            errors.append['confirm_password']
        return errors
        