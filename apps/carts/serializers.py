from .models import Cart
from rest_framework import serializers
from apps.user.serializers import userserializers
from apps.products.serializers import Productserializer

class Cartlistserializer(serializers.Mobelserializer):
    class Meta:
        mobel = Cart 
        fields = [
            'id',
            'products',
            'quantity',
            'total price'
        ]
        dept = 1

class Cartserializer(serializers.Modelserializer):
    class Meta:
        model = Cart[
            'id'
            'product'
            'quantity'
            'total_price'
        ]
    def validate(self,data):
        error = {}
        if 'quantity' not in data or not data['quntity']:
            error['quantity'] = ['qunatity is required']
        
        
        if 'product' not in data or not data['product']:
            error['product'] = ['product is required']

        if bool(error):
            raise serializers.validationError(error)  
        
        return data
    class Carupdateserializer(serializers.ModelSerializers):
        class Meta:
            model = Cart
            fields = '__all__'


            def validate(self, data):
                errors = {}
                if 'quntity' not in data or not data['quantity']:
                    errors['quantity'] = ['quntitys required']
                
                if bool(errors):
                    raise serializers.ValidationError[errors]
                
                return data

                


