# BONUS: (5 points) As a developer, I want to add the ability to add an image link to each product. (Link to picture on the internet)
    # line 10 contains 'image_link' to allow users to make requests (e.g. PUT) from this table column

from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'inventory_quantity', 'image_link'] #these correspond to the table's columns