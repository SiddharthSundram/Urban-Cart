from django.contrib import admin
from .models import Product, OrderRequest

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    search_fields = ('name',)
    list_filter = ('price',)


@admin.register(OrderRequest)
class OrderRequestAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'product', 'status', 'date_ordered')
    list_filter = ('status', 'date_ordered')
    search_fields = ('customer_name', 'product__name')
