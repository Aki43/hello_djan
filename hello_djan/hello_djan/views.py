from django.http import HttpResponse
from django.shortcuts import render

def about(reqest):
    return render(reqest,'about.html', {'zalypa':'sosi'})

def home(reqest):
    return HttpResponse('come back home')