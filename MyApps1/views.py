from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def f1(request):
    return HttpResponse("hello world")
def f2(request):
    return HttpResponse("hello world")
