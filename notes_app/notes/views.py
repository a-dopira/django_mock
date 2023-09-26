from django.http import HttpResponse
from django.shortcuts import render


def simple_view(request):
    return HttpResponse('<h1>Here is simple view with 1 h1 header</h1>')
