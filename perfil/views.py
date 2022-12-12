from django.shortcuts import render, HttpResponse
from .models import Project
# Create your views here.
def profile(request):
    projects=Project.objects.all()
    return render(request, 'profile.html',{'projects':projects})
def presentacion(request):
    return render(request,'indexr.html')