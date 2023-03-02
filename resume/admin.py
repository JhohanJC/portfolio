from django.contrib import admin
# Register your models here.
from .models import Profile 
@admin.register(Profile) 
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'updated')
    list_display_links = ('id', 'name',)
    #list_editable = ('name',)
    list_filter = ('name', 'created', 'updated')
    search_fields = ('name', )
    readonly_fields = ('created', 'updated')