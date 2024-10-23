from .models import Orderitem
from rest_framework import serializers


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orderitem
        fields = [
            'oreder'
            'product'
            'qty'
        ]
        read_only_fields = [
            'order'
        ]