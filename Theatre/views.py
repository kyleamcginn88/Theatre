from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
# Palmer said to change location to Location for better naming conventions
from Theatre.models import Info, MovieInfo , Store, location


def home(request):
    return render(request, 'home.html', {'all_movies': Info.objects.all()})

def store(request):
    return render(request,'store.html', {'store_item': Store.objects.all()})

def location(request):
    return render(request, 'location.html', {'store_item': Info.objects.all()})

def movies(request):
    return render(request,'movies.html', {'movies': MovieInfo.objects.all()})

def performances(request):
    return render(request, 'performances.html', {})