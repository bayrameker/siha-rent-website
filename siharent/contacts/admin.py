from django.contrib import admin
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','listing','phone','contact_date','user_id')
    list_display_links = ('id','name')
    search_fields = ('name','email','listing')
admin.site.register(Contact,ContactAdmin)