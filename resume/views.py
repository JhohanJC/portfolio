from django.shortcuts import render
from .models import Profile
def index(request, id=1):
    id_user = 1
    date = Profile.objects.get(id=1)
    return render(request, 'index.html', {'date': date})