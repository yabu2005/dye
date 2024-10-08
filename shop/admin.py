from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug', 'price']
    list_filter = ['created']
    list_editable = ['price']
    date_hierarchy = ('created')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email']
    list_filter = ['date']
    date_hierarchy = ('date')