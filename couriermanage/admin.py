from django.contrib import admin
from .models import *


class CourierAdmin(admin.ModelAdmin):
	list_display = ( 'sender_name', 'tracking_id', 'sender_phone', 'service',)
	change_list_template = 'admin/change_list.html'
	actions = None

admin.site.site_header = 'ITSOURCECODE-CMS Administration'
admin.site.site_title = 'ITSOURCECODE-CMS-Admin'
admin.site.register(Courier, CourierAdmin)

admin.site.register(Contact)