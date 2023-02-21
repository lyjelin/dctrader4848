from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product

"""
    Django REST framework는 단일 클래스에 관련 있는 view들을 결합한 ViewSet 기능을 제공한다
    즉, ViewSet은 여러 가지 API의 기능을 통합해서 하나의 API Set로 제공한다 
"""

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()