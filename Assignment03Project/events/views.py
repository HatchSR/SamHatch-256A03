from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def events(request):
    if request.method == "GET":
        if request.session.get('role') != 'Admin':
            return HttpResponse('<h1>role is not admin</h1>')
        else: 
            
            return HttpResponse('<h1>role is admin</h1>')
