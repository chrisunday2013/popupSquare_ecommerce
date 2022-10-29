from . import models 
from . import serializers
from rest_framework import generics


class VendorList(generics.ListAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class=serializers.VendorSerializer
