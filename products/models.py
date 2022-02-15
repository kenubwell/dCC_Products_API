#(2.5 points) As a developer, I want to create a Product model. Property names must be in snake_case and match the following exactly!
# title - CharField | description - CharField | price - DecimalField | inventory_quantity - IntegerField
    # lines 10 - 14 satisfy this user story
# BONUS: (5 points) As a developer, I want to add the ability to add an image link to each product. (Link to picture on the internet)
    # line 15 for the image link

from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory_quantity = models.IntegerField()
    image_link = models.URLField(max_length=2500) #this variable is for the bonus user story
    
     
