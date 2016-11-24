#!/usr/bin/python
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.contrib import auth

from web001 import models


def index(request):
    allPeople = models.Person.objects.all()
    myList = ["1"] * 10
    return render(request, 'index.html', {'myList': myList, 'allPeople': allPeople})
