from django.contrib import admin
from rango.models import Category, Page


admin.site.register(Category)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.unregister(Category)
admin.site.register(Category, CategoryAdmin)