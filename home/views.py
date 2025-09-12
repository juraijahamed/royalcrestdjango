from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from royalcrest import settings


def home(request):
    template_dir = settings.TEMPLATES[0]['DIRS']
    files = os.listdir(template_dir[0])
    return HttpResponse(f"Templates directory: {template_dir}<br>Files: {files}",{'active_page': 'home'})

def about(request):
    return render(request, "about.html", {'active_page': 'about'})

def service(request):
    return render(request, "services.html", {'active_page': 'services'})