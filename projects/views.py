from django.shortcuts import render
from .models import Project


def projects(request):
    projects=Project.objects.all().order_by('-date')
    return render(request,'index.html',{"projects":projects})
