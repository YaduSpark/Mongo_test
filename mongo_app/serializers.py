from rest_framework_mongoengine import serializers

from .models import Product, ProductCategory, ProductManufacturer


class CategorySerializer(serializers.DocumentSerializer):
    class Meta:
        model= ProductCategory
        fields = '__all__'


class ManufacturerSerializer(serializers.DocumentSerializer):
    class Meta:
        model=ProductManufacturer
        fields='__all__'


class ProductSerializer(serializers.DocumentSerializer):
    class Meta:
        model=Product
        fields = '__all__'
        depth = 1