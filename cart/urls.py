from django.urls import path

from cart.views import add_to_cart, get_cart, remove_from_cart

urlpatterns = [
    path('get/', get_cart),
    path('add/', add_to_cart),
    path('remove/', remove_from_cart)
]
