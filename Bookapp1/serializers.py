from rest_framework import serializers
from .models import *
class BookappSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookappModel
        fields='__all__'