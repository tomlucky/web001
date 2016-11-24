# coding=utf8
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __unicode__(self):  # __str__ on Python 3
        return self.name  # 在admin配置页面，可以容易的看到名
