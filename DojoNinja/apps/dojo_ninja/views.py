# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
# from .models import

# Create your views here.

def home(request):
    return HttpResponse('This is a temporary')


