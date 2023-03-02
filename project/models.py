from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=10)
    description = RichTextField()
    image = models.ImageField(upload_to = 'projects', blank=True)
    url = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'project'
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['-created']
    def __str__(self):
        return self.title