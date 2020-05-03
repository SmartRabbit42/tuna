from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("fish are stronger in a shoal")

def add_fish(request):
    return HttpResponse("another one joins the shoal")
