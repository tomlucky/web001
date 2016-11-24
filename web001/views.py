#!/usr/bin/python
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib import auth


def index(req):
    return render_to_response('index.html')
