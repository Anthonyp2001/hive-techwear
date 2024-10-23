from .models import Product
from rest_framework import serializers
from cloudinary.models import CloudinaryField
from apps.categories.serializers import CategorySerializer

class productserializers(serializers.ModelSerializer):
    image = serializers.ImageField(read_only=True)
    Category= CategorySerializer(many=False, read_only=True)

    class meta:
        model = Product
        fields = '__all__'
        depth = 1
    