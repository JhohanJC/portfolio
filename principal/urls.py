from django.urls import path 
# views 
from .views import index, blogss
# Config URL 
urlpatterns =[
    path('', index, name='home'),
    path('blogss/', blogss, name='blogss'),]