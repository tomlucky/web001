#!/usr/bin/python
from django.shortcuts import render

from web001 import models

from django.http import JsonResponse


def index(request):
    allPeople = models.Person.objects.all()
    myList = ["1"] * 10
    return render(request, 'index.html', {'myList': myList, 'allPeople': allPeople})


def add(req):
    a = req.GET['a']
    d = req.GET['d']
    a = int(a)
    d = int(d)

    return JsonResponse(range(a, d, 1), safe=False)


def contexttest(req):
    return render(req, 'context.html')
