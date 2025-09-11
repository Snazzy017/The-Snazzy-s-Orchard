from django.urls import path
from .views import (
    home,
    contact,
    about,
    products,
    cart,
    checkout,
)

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('products/', products, name='products'),
    path('about/', about, name='about'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout')


]