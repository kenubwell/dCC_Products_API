#Challenge: reformat your project using classed based views
    # I refactored my paths in lines 8-9 to the class-based views coded in the views.py file

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductsList.as_view()),
    path('<pk>/', views.ProductDetail.as_view()),
]