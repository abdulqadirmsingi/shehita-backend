from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "description"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name",
                  "category",
                  "description",
                  "price",
                  "stock",
                  "available",
                  "image",
                  "created",
                  "updated"]
        