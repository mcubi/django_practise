from django.shortcuts import render
from .models import Project

def show_hub(request):
    project_list = Project.objects.all()
    return render(request, 'projecthub/hub.html', {'project_list': project_list})

def show_project(request, slug):
    project = Project.objects.get(slug=slug)
    return render(request, 'projecthub/project_detail.html', {'project': project})