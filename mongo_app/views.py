from rest_framework_mongoengine import generics

from .serializers import CategorySerializer, ManufacturerSerializer, ProductSerializer
from .models import Product, ProductCategory, ProductManufacturer

# Create your views here.


class ProductList(generics.ListCreateAPIView):
    lookup_field = 'id'
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

        
class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'uid'
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()


class CategoryList(generics.ListCreateAPIView):
    lookup_field = 'uid'
    serializer_class = CategorySerializer

    def get_queryset(self):
        return ProductCategory.objects.all()


class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'uid'
    serializer_class = CategorySerializer

    def get_queryset(self):
        return ProductCategory.objects.all()


class ManufacturerList(generics.ListCreateAPIView):
    lookup_field = 'uid'
    serializer_class = ManufacturerSerializer

    def get_queryset(self):
        return ProductManufacturer.objects.all()


class ManufacturerDetails(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'uid'
    serializer_class = ManufacturerSerializer

    def get_queryset(self):
        return ProductManufacturer.objects.all()