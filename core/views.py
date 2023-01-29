from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render


def index(value):
    return render(request=requests, template_name='students/index.html')


def view_with_param(request, value):
    return HttpResponse(f'With param: "{value}"')


def view_without_param(request):
    return HttpResponse('Without param')
