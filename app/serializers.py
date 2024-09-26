from rest_framework import serializers
from app.models import Product, Material, ProductMaterials, Warehouse


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'material_name']


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'warehouse_name', 'remaining_quantity', 'price']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_qty']


class ProductMaterialsSerializer(serializers.ModelSerializer):
    material_name = serializers.CharField(source='material.material_name', read_only=True)

    class Meta:
        model = ProductMaterials
        fields = ['product', 'material_name', 'quantity']
