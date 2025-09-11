from django.shortcuts import render

# Create your views here.
#home view
def home(request):
    return render(request, "home/home.html")

#about view
def about(request):
    return render(request, "home/about.html")

#products view
def products(request):
    return render(request, "home/products.html")

#contact view
def contact(request):
    return render(request, "home/contact.html")

#cart view
def cart(request):
    return render(request, "home/cart.html")

#checkout view
def checkout(request):
    return render(request, "home/checkout.html")
