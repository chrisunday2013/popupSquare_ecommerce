from . import models 
from . import serializers
from rest_framework import generics, permissions


#vendor
class VendorList(generics.ListCreateAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class=serializers.VendorSerializer


class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class=serializers.VendorDetailSerializer


#product
class ProductList(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class=serializers.ProductListSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class=serializers.ProductDetailSerializer
    

#customer 
class CustomerList(generics.ListCreateAPIView):
    queryset = models.Customer.objects.all()
    serializer_class=serializers.CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Customer.objects.all()
    serializer_class=serializers.CustomerDetailSerializer
        


#order
class OrderList(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class=serializers.OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Order.objects.all()
    serializer_class=serializers.OrderDetailSerializer
                

#order
class OrderItemList(generics.ListCreateAPIView):
    queryset = models.OrderItems.objects.all()
    serializer_class=serializers.OrderItemSerializer


class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.OrderItems.objects.all()
    serializer_class=serializers.OrderItemDetailSerializer
       