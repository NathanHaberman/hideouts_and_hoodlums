# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pprint

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from models import *

# Create your views here.
def index(request):
    if 'active_user' in request.session:
        return redirect('/user/' + request.session['active_user'])
    else:
        errors = messages.get_messages(request)
        if len(errors) > 0:
            context = {}
            for error in errors:
                context[str(error)] = True

            return render(request, 'player/index.html', context)
        else:
            return render(request, 'player/index.html')


def register(request):
    if request.method == 'POST':
        # Validation Errors
        username_in_use = User.objects.filter(username=request.POST['username'])
        errors = []
        if len(request.POST['first_name']) > 30 or len(request.POST['first_name']) < 1:
            errors.append('first_name_error')
        if len(request.POST['last_name']) > 30 or len(request.POST['last_name']) < 1:
            errors.append('last_name_error')
        if len(request.POST['username']) > 75 or len(request.POST['username']) < 1:
            errors.append('username_error')
        if username_in_use:
            errors.append('username_in_use')
        if len(request.POST['password']) > 128 or len(request.POST['password']) < 8:
            errors.append('password_error')
            if (request.POST['password'] != request.POST['confirm_password']):
                erors.append('confirm_password_error')
        if (len(errors) > 0):
            for error in errors:
                messages.error(request, error)
            return redirect('/')
        else:
            user = User.objects.create_user(first_name=request.POST['first_name'], last_name=request.POST['last_name'], username=request.POST['username'])
            user.set_password(request.POST['password'])
            user.save()
            request.session['active_user'] = user.id
            return redirect('/user/' + str(user.id))
    else:
        return redirect('/')

def login(request):
    if len(request.POST['username']) > 0:
        user = User.objects.filter(username=request.POST['username'])
        if user:
            user = User.objects.get(username=request.POST['username'])
            if user.check_password(request.POST['password']):
                request.session['active_user'] = user.id
                return redirect('/user/' + str(user.id))
            else:
                messages.error(request, 'login_password')
                return redirect('/')
    messages.error(request, 'login_username')
    return redirect('/')

def profile(request, user_id):
    return