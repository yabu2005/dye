from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = 'Wow Burger'
admin.site.site_title = 'Wow Burger'
admin.site.index_title = 'Wow Burger Admin Panel'

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name',
                    'email', 'city', 'sub_city', 'home_number', 'delivered', 'paid']
    list_filter = ['delivered', 'paid', 'created']
    date_hierarchy = 'created'
    inlines = [OrderItemInline]
