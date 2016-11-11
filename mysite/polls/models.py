from __future__ import unicode_literals

from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    priority = models.IntegerField(default=0)
    person = models.ForeignKey('Person', default='', null=True)

class Person(models.Model):

    name = models.CharField(max_length=255)
