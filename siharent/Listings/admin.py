from django.contrib import admin
from .models import Listings
# Register your models here.

class ListingsAdmin(admin.ModelAdmin):
    list_display = ('id','sihas','title','country','took_off','price','is_published')
    list_display_links = ('id','sihas')
    list_filter = ('sihas','company','country')
    list_editable = ('is_published',)
    search_fields = ('title','company','flight_time','altitude')
admin.site.register(Listings,ListingsAdmin)