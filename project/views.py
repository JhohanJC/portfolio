from django.shortcuts import render
from .models import Project
from django.shortcuts import get_object_or_404
# Create your views here.
def projects(request):
    projects = Project.objects.all()
    projectd = Project.objects.first()
    return render(request, 'projects.html', {'projects': projects, 'projectd': projectd })
def projectd(request, id):
    projectd = Project.objects.get(id=id)
    return render(request, 'project.html', {'projectd': projectd})