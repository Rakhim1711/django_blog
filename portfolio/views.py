from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})

def pic(request):
    return render(request, 'portfolio/pic.html')

# Create your views here.
