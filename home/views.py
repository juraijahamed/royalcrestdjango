from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def home(request):
    return render(request, "home.html", {'active_page': 'home'})

def about(request):
    return render(request, "about.html", {'active_page': 'about'})

def service(request):
    return render(request, "services.html", {'active_page': 'services'})