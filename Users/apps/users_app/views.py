# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from . import models

# Create your views here.
def home(request):
    context = {"User": User.objects.all()}
    return render(request, "users_app/home.html")