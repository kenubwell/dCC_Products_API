from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_list),
    path('<pk>/', views.products_detail),
]