# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from models import *


# Create your views here.
def index(request):
    return render(request, 'player/index.html')

def register(request):
    if request.method == 'POST':
        # Validation Errors
        errors = UserManager(request.POST)
        if (len(errors) > 0):

            # TODO Pass errors to template
            
            return redirect('/')
    else:
        return redirect('/')