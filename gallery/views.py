from django.shortcuts import render
from .forms import ImageUploadForm
from .models import Image

def image_gallery(request):
    
    images = Image.objects.all()
    return render(request, 'gallery.html', {'images': images},)