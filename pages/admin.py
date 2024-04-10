from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','contacted_at','is_resolved')
    list_filter = ('contacted_at','is_resolved',)
    list_editable = ('is_resolved',)


admin.site.register(Contact,ContactAdmin)

