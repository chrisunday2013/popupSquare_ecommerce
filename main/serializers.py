from rest_framework import serializers 
from . import models 


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Vendor
        fields=['id', 'user', 'address']


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ProductCategory
        fields=['id', 'title', 'detail' , 'address' , 'address']      


class Productr(serializers.ModelSerializer):
    class Meta:
        model=models.Product
        fields=['id', 'title', 'detail' , 'price']             
