from django.contrib import admin
from .models import Project
# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','description', 'image', 'created')
    list_display_links = ('id', 'title')

    list_filter = ('created', 'updated')
    search_fields = ('title', 'description')

    readonly_fields = ('created', 'updated')