from django.urls import path
from .views import (
    home,
    contact,
    about,
    shop,
    shop_detail, 
    cart,
    checkout,
    b2,
    login,
    signup,
    forgotpassword
)

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('shop/', shop, name='shop'),
    path('about/', about, name='about'),
    path('shop_detail/<int:pk>/', shop_detail, name='shop_detail'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('b2/', b2, name='b2'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('forgotpassword/', forgotpassword, name='forgotpassword')
]
