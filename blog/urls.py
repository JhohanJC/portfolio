from django.urls import path 
# views 
from .views import posts, post 
# Config URL 
urlpatterns =[
    path('', posts, name='posts'),
    path('<int:id>/', post, name='post'),]