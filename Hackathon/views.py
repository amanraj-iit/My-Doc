from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'base.html')

def Contact(request):
    return render(request, "contact.html")