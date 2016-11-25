# coding=utf8
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __unicode__(self):  # __str__ on Python 3
        return self.name  # 在admin配置页面，可以容易的看到名


class Titles(models.Model):
    enName = models.CharField(max_length=10)
    cnName = models.CharField(max_length=10)

    def __unicode__(self):  # __str__ on Python 3
        return self.enName  # 在admin配置页面，可以容易的看到名


post_date = models.IntegerField()
meta_key = models.CharField(max_length=255)


class Posts(models.Model):
    post_author = models.CharField(max_length=255)
    post_date = models.CharField(max_length=255)
    post_date_gmt = models.CharField(max_length=255)
    post_content = models.TextField()
    post_title = models.CharField(max_length=255)
    post_excerpt = models.CharField(max_length=255)
    post_status = models.CharField(max_length=255)
    comment_status = models.CharField(max_length=255)
    ping_status = models.CharField(max_length=255)
    post_password = models.CharField(max_length=255)
    post_name = models.CharField(max_length=255)
    to_ping = models.CharField(max_length=255)
    pinged = models.CharField(max_length=255)
    post_modified = models.CharField(max_length=255)
    post_modified_gmt = models.CharField(max_length=255)
    post_content_filtered = models.CharField(max_length=255)
    guid = models.CharField(max_length=255)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=255)
    post_mime_type = models.CharField(max_length=255)
    comment_count = models.IntegerField()


def __unicode__(self):  # __str__ on Python 3
    return self.post_title  # 在admin配置页面，可以容易的看到名
