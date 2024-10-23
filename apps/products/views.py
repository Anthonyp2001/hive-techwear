from django.db.models import query
from django.shortcuts import render
from rest_framework import generics, serializers
from django_filters.rest_framework import DjangoFilterBackend
from apps.user.mixins import CustomLoginRequiredMixin
from apps.products.serializers import productserializers
from rest_framework import filters

from .models import Product

class Productlist(CustomLoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = productserializers
    filter_backends = [DjangoFilterBackend, filters.searchfilter]
    filterset_fields = ['category_id', 'type']
    search_field = ['name', 'description']
