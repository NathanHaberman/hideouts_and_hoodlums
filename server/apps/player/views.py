# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from models import *


# Create your views here.
def index(request):
    errors = messages.get_messages(request)
    if len(errors) > 0:
        context = {}
        for error in errors:
            context[error] = True

        #TODO Figure out how to get context to the template/Use it right

        return render(request, 'player/index.html', context)
    else:
        return render(request, 'player/index.html')


def register(request):
    if request.method == 'POST':
        # Validation Errors
        errors = []
        if len(request.POST['first_name']) > 75 or len(request.POST['first_name']) < 1:
            errors.append('first_name')
        if len(request.POST['last_name']) > 75 or len(request.POST['last_name']) < 1:
            errors.append('last_name')
        if len(request.POST['email']) > 75 or len(request.POST['email']) < 1:
            errors.append('email')
        if len(request.POST['username']) > 75 or len(request.POST['username']) < 1:
            errors.append('username')
        if len(request.POST['password']) > 75 or len(request.POST['password']) < 8:
            errors.append('password')
            if (request.POST['password'] != request.POST['confirm_password']):
                erors.append('confirm_password')
        if (len(errors) > 0):
            for error in errors:
                messages.error(request, error)
            return redirect('/')
    else:
        return redirect('/')