from django.contrib import admin
from app.models import Product,Material,MaterialProduct,Warehouse





@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_qty')
    search_fields = ('product_name',)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('material_name',)
    search_fields = ('material_name',)


@admin.register(MaterialProduct)
class MaterialProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'material', 'quantity')
    list_filter = ('product', 'material')


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('material', 'remaining_quantity', 'price')
    list_filter = ('material',)
    search_fields = ('material__material_name',)

