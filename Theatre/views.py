from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
# Palmer said to change location to Location for better naming conventions
from Theatre.models import Info, MovieInfo , Store, Location


def home(request):
    return render(request, 'home.html', {'all_movies': Info.objects.all()})

def store(request):
    return render(request,'store.html', {'store_item': Store.objects.all()})

def location(request):
    return render(request, 'location.html', {'store_item': Info.objects.all()})

def movies(request):
    return render(request,'movies.html', {'movies': MovieInfo.objects.all()})

def performances(request):
	#list_performances = [('1/15/15', 'Fish Pump', 'Dance' ),
	#('2/25/15', '7pac' ,'Hip-Hop'),
	#('3/1/15', 'J-ci and Jolow','R&B' ),
	#('4/18/15', 'King of Lions', 'Alternative Rock'),
	#('5/5/15', 'Dr Jays', 'Rap' ),
	#('6/7/15', 'Nerdvana' , 'Grunge'),
	#('7/11/15', 'My Chemical Love' , 'Punk'),
	#('8/21/15', 'T.I. Guy' , 'Hip-Hop'),
	#('9/13/15', 'RUN D & C' ,'Hip-Hop'),
	#('10/16/15', 'Food Thrower', 'Alternative Rock' ),
	#('11/23/15', 'Dark Keys' ,'Alternative Rock'),
	#('12/11/15', 'IceBox','Rap' ),
	#('12/31/15', 'boyz II Gentlemen', 'R&B' )]
	return render(request, 'performances.html', {'performances': list_performances})