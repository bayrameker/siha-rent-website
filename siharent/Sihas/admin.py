from django.contrib import admin
from .models import Sihas
# Register your models here.

class SihasAdmin(admin.ModelAdmin):
    list_display = ('id','name','category','brand','weight')
    list_display_links = ('id','name')
    search_fields = ('name',)
admin.site.register(Sihas,SihasAdmin)