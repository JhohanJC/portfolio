from django.urls import path
from .views import projects, projectd
urlpatterns = [
    path('', projects, name='projects'),
    path('<int:id>/', projectd, name='projectd'),
]