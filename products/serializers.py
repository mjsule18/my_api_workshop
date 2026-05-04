from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' # Or list specific fields like ['id', 'name', 'description', 'price', 'stock']