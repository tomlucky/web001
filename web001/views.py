#!/usr/bin/python
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.contrib import auth


def index(req):
    myList = ["1"] * 10
    return render(req, 'index.html', {'myList': myList})
