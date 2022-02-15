from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product


@api_view(['GET', 'POST'])
def products_list(request):

    if request.method == 'GET':
        products = Product.objects.all()
        serializers = ProductSerializer(products, many=True) #this is going to take our product table and convert to json
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializers = ProductSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)  #this validates that API user input is true or accurate to the database
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def products_detail(request, pk): #this pk allows for input for the product id

    product = get_object_or_404(Product, pk=pk)  #since I imported django shortcut (above) we can use this function to check for errors. Just have to enter (Model, Value)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data) #this compares current product data and takes in requested data from user
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
