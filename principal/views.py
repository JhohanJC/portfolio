from django.shortcuts import render, HttpResponse
from blog.models import Post
# Create your views here.
def index(request):
    return render(request,'indexr.html')
    # return HttpResponse('<h1>Pagina de inicio<h1>')
    # return render(request,'index.html')
def blogss(request):
    return render(request,'home.html')