# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class FunFact(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=250)
  its_true =  models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title

class Tag(models.Model):
  title = models.CharField(max_length=50)
  color = models.CharField(max_length=10)
  created_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title