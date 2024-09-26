from rest_framework import serializers
from app.models import Product, Material, ProductMaterials, Warehouse


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'code']


class ProductMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMaterials
        fields = ['product', 'material', 'quantity']


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'material', 'remainder', 'price']
