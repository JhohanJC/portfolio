from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=20)
    foto = models.ImageField(upload_to = 'resume', blank=True)
    profession = models.CharField(max_length=40)
    about = models.TextField(blank=True)
    file = models.FileField(upload_to='CV', verbose_name='CV File', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'profile'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ['-created']
    def __str__(self):
        return self.name