from django.shortcuts import render
from .models import Project
from django.contrib.auth.decorators import login_required

# DEUD: ! NOT GONNA CAP THE NUMBER OF PROJECTS DISPLAYED FOR NOW !
@login_required(login_url='users:login')
def show_hub(request):
    project_list = Project.objects.all()
    return render(request, 'projecthub/hub.html', {'project_list': project_list}) 



@login_required(login_url='users:login')
def show_project(request, slug):
    project = Project.objects.get(slug=slug)
    return render(request, 'projecthub/project_detail.html', {'project': project})