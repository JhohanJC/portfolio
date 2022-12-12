from django.urls import path 
# views 
from . import views 
# Config URL 
urlpatterns =[
    path('', views.profile, name='profile'),
    path('here/', views.presentacion, name='presentacion'),]