from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class AttributesAdmin(admin.ModelAdmin):
    list_display = ['title','category','creation_date','admin_image']
    list_display_links = ['title','admin_image']
    search_fields = ['title',]
    prepopulated_fields = {'slug': ('title',)}

    def admin_image(self,other):
        if other.image:
            return mark_safe(f"<img src='{other.image.url} 'width='50'")
        else:
            return None
    admin_image.__name__='photo'

admin.site.register(Attributes,AttributesAdmin)

class AdminCategories(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category,AdminCategories)

