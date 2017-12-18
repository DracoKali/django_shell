# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)

   """ def __str__(self):
        return "%s %s" % (self.name, self.city, self.state)"""
         


class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, on_delete=models.CASCADE)

"""    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)"""
       

   
   
        