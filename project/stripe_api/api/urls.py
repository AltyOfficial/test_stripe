from django.urls import path
from .views import checkout, item_detail

urlpatterns = [
    path('item/<int:pk>/', item_detail, name='item_detail'),
    path('buy/<int:pk>/', checkout, name='checkout'),
]
