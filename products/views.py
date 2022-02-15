#(5 points) As a developer, I want to create a GET endpoint the responds with a 200 success status code and all of the products within the Product table.
    # line 25 and lines 28-31 
#(5 points) As a developer, I want to create a GET by id endpoint that does the following things:
#Accepts a value from the request’s URL (The product ID) | Returns a 200 status code. | Responds with the product in the database that has the id that was sent through the URL.
    # line 39 and lines 43-45 
# (5 points) As a developer, I want to create a POST endpoint that does the following things:
# Accepts a body object from the request in the form of a Product model | Adds the new product to the database | Returns a 201 status code | Responds with the newly created product object.
    # line 25 and lines 32-36 
# (5 points) As a developer, I want to create a PUT endpoint that does the following things:
# Accepts a value from the request’s URL (The product ID) | Accepts a body object from the request in the form of a Product model | 
# Finds the product in the table and updates with the properties that were sent | Returns a 200 status code | Responds with the newly updated product object.
    # line 39 and lines 46-50 
# (5 points) As a developer, I want to create a DELETE endpoint that does the following things:
# Accepts a value from the request’s URL | Returns a 204 status code (NO CONTENT).
    # line 39 and lines 51-53

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
