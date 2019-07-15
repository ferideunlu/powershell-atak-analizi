from django.shortcuts import render
from django.http import HttpResponse
from . import helpers

def view(request, image):
    print(f"image: {image}")
    return render(request, 'stats/view.html', {'logs': helpers.get_logs(image=image, page=1)})