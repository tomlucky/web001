#!/usr/bin/python
from django.shortcuts import render
from django.http import HttpResponse
import qrcode
from cStringIO import StringIO
from web001 import models

from django.http import JsonResponse
from web001.models import *


#
# def index(request):
#     allPeople = models.Person.objects.all()
#     myList = ["1"] * 10
#     return render(request, 'index_test.html', {'myList': myList, 'allPeople': allPeople})

def index(request):
    titles = Titles.objects.all()
    return render(request, 'index.html', {'titles': titles})


def add(req):
    a = req.GET['a']
    d = req.GET['d']
    a = int(a)
    d = int(d)

    return JsonResponse(range(a, d, 1), safe=False)


def contexttest(req):
    return render(req, 'context.html')


def generate_qrcode(request, data):
    img = qrcode.make(data)
    buf = StringIO()
    img.save(buf)
    image_stram = buf.getvalue()
    response = HttpResponse(image_stram, content_type='image/png')
    response['Last-Modified'] = 'Mon, 27 Apr 2015 02:05:03 GMT'
    response['Cache-Control'] = 'max-age=31536000'
    return response


def bstest(req):
    return render(req, 'bstest.html')
