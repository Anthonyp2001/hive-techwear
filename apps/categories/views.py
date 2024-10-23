from django.shortcuts import generics 

from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer

class Catgorylist(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = None
