from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import Post 
# Create your views here.
def posts(request):
    first_post = Post.objects.first()
    posts = Post.objects.all()
    return render(request, 'blogs.html', {'posts':posts,'first_post':first_post})
    # return HttpResponse(blogs)
def post(request, id):
    post = Post.objects.get(id=id)
    return render(request,'blog.html',{'post':post})
    # blog = Post.objects.get(id=id)
    # content = f'{blog.title}-{blog.desc}'
    # return render(request, 'blog.html')
    # return HttpResponse(content)