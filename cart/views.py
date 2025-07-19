from django.shortcuts import render

# Create your views here.
def add_to_cart(request):
    return render(request, "add_to_cart.html")