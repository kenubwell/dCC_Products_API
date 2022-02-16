#(5 points) As a developer, I want to create a GET endpoint the responds with a 200 success status code and all of the products within the Product table.
    # line 43 and lines 46-49. Please note that this is commented out for the Challenge (class-based view) 
#(5 points) As a developer, I want to create a GET by id endpoint that does the following things:
#Accepts a value from the request’s URL (The product ID) | Returns a 200 status code. | Responds with the product in the database that has the id that was sent through the URL.
    # line 77 and lines 81-83. Please note that this is commented out for the Challenge (class-based view)  
# (5 points) As a developer, I want to create a POST endpoint that does the following things:
# Accepts a body object from the request in the form of a Product model | Adds the new product to the database | Returns a 201 status code | Responds with the newly created product object.
    # line 43 and lines 50-54. Please note that this is commented out for the Challenge (class-based view)  
# (5 points) As a developer, I want to create a PUT endpoint that does the following things:
# Accepts a value from the request’s URL (The product ID) | Accepts a body object from the request in the form of a Product model | 
# Finds the product in the table and updates with the properties that were sent | Returns a 200 status code | Responds with the newly updated product object.
    # line 77 and lines 84-88. Please note that this is commented out for the Challenge (class-based view)  
# (5 points) As a developer, I want to create a DELETE endpoint that does the following things:
# Accepts a value from the request’s URL | Returns a 204 status code (NO CONTENT).
    # line 77 and lines 89-91. Please note that this is commented out for the Challenge (class-based view) 
#Challenge: reformat your project using classed based views
    #starting on line 28 has the class to view the products list and create a product
    #starting on line 56 has the class that retrieves (by id), updates, or deletes a product

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product

class ProductsList(APIView):
#A class-based view that lists all products or creates a new product

    def get (self, request, format=None):
        products = Product.objects.all()
        serializers = ProductSerializer(products, many=True) #this is going to take our product table and convert to json
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializers = ProductSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)  #this validates that API user input is true or accurate to the database
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)

#Below was the function-based view to request all products and update a product
# @api_view(['GET', 'POST'])
# def products_list(request):

#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializers = ProductSerializer(products, many=True) #this is going to take our product table and convert to json
#         return Response(serializers.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializers = ProductSerializer(data=request.data)
#         serializers.is_valid(raise_exception=True)  #this validates that API user input is true or accurate to the database
#         serializers.save()
#         return Response(serializers.data, status=status.HTTP_201_CREATED)

class ProductDetail(APIView):
#A class-based view that retrieves (by id), updates, or deletes a product
    
    def get(self, request, pk, format=None):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)  

    def put(self, request, pk, format=None):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data) #this compares current product data and takes in requested data from user
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def delete(self, request, pk, format=None):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Below was the function-based view to request a product by id, update, and delete
# @api_view(['GET', 'PUT', 'DELETE'])
# def products_detail(request, pk): #this pk allows for input for the product id

#     product = get_object_or_404(Product, pk=pk)  #since I imported django shortcut (above) we can use this function to check for errors. Just have to enter (Model, Value)
#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data, status=status.HTTP_200_OK)  
#     elif request.method == 'PUT':
#         serializer = ProductSerializer(product, data=request.data) #this compares current product data and takes in requested data from user
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
