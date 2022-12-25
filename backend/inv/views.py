from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Brand, Category, Product
from .serializers import BranSerializer, CategorySerializer, ProductSerializer


# Create your views here.
class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BranSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
