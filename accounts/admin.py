from django.contrib import admin

from .models import *



admin.site.register(Tag)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'date_created')
    list_filter = ('date_created', )  
    search_fields = ['name','email']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'description')
    list_filter = ('category', )  
    search_fields = ['name']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'status', 'date_created')
    list_filter = ('status', 'date_created', )  
    search_fields = ['product','customer']


