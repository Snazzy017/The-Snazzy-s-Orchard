from django.shortcuts import render

# Create your views here.
def add_to_cart(request):
    return render(request, 'cart/add_to_cart.html')