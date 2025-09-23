from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
#Home View
def home(request):
    return render(request, 'home/home.html')

#About View
def about(request):
    return render(request, 'home/about.html')

#shop View
def shop(request):
    products = Product.objects.filter(is_available=True).order_by("-created_at")
    return render(request, "home/shop.html", {"products": products})


#contact View
def contact(request):
    return render(request, 'home/contact.html')

#shop detail View
# views.py
from django.shortcuts import render, get_object_or_404
from .models import Product

def shop_detail(request, pk):  # must be 'pk' to match the URL
    product = get_object_or_404(Product, id=pk)

    # For tags if you add them later
    tags = product.tags.split(',') if hasattr(product, 'tags') and product.tags else []

    # If you use multiple images with a related model
    product_images = product.images.all() if hasattr(product, 'images') else []

    # Related products
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:5]

    context = {
        'product': product,
        'tags': tags,
        'product_images': product_images,
        'related_products': related_products,
    }
    return render(request, 'home/shop_detail.html', context)





#cart View
def cart(request):
    return render(request, 'home/cart.html')

#checkout View
def checkout(request):
    return render(request, 'home/checkout.html')

def b2(request):
    return render(request, 'home/b2.html')

def login(request):
    return render(request, 'home/login.html')

def signup(request):
    return render(request, 'home/signup.html')

def forgotpassword(request):
    return render(request, 'home/forgotpassword.html')