from django.shortcuts import render ,redirect ,get_object_or_404
from store.models import Product
from .forms import ProductAddForm
from .cart import Cart
from django.views.decorators.http import require_POST

#  لاضافه منتج او تحديثه
@require_POST
def cart_add(request ,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product ,id=product_id)
    
    form = ProductAddForm(request.POST)
    
    if form.is_valid():
        cd=form.cleaned_data
        cart.add(product=product , quantity=cd['quantity'] , override_quantity=cd['override'])
        
    return redirect('cart_detail')

    



# لحذف منتج من الكارت
@require_POST
def cart_remove(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product , id=product_id)
    cart.remove(product)

    return redirect('cart_detail')


#لعرض المنتاجات فى الكارت

def cart_detail(request):
    cart = Cart(request)
    return render (request , 'cart_details.html' , {'cart':cart})
