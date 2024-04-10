from django.contrib import admin
from .models import Category,Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','is_published','posted_at')
    list_filter = ('is_published','posted_at')
    list_editable = ('is_published',)






admin.site.register(Category)
admin.site.register(Post,PostAdmin)