from django.shortcuts import render
from django.http import HttpResponse 
def greet(request):
    return render (request,'greet.html') #("<h1>Hello Users Welcome to My First Django Site<h1>") 
