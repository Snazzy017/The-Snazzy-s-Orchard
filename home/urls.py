from django.urls import path
from .views import (
    home,
    contact,
    about,
    products,
)

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('products/', products, name='products'),
    path('about/', about, name='about'),
]