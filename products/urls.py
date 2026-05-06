from django.urls import path
from .views import ProductListCreate

urlpatterns = [
    path('api/products/', ProductListCreate.as_view(), name='product-list-create'),
    
]