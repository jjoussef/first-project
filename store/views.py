from django.shortcuts import render , get_object_or_404
from cart.forms import ProductAddForm
from .models import Category , Product

def product_list(request , category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    category = None
    # if category_slug
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)
    return render(request , 'home.html' ,{'categories':categories ,'products':products  , 'category':category})


def product_detail(request , id ,slug):
    form = ProductAddForm()
    product = get_object_or_404(Product , id=id , slug=slug  , available=True)
    return render(request , 'product_details.html' ,{'product':product  , 'form':form})