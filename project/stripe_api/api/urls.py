from django.urls import path

from .views import checkout, checkout_order, item_detail

urlpatterns = [
    path('item/<int:pk>/', item_detail, name='item_detail'),
    path('buy/<int:pk>/', checkout, name='checkout'),
    path('buy-order/<int:pk>/', checkout_order, name='order_checkout'),
]
