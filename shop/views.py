from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from cart.forms import CartAddProductForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {'category': category,
               'categories': categories, 'products': products}
    return render(request, 'shop/product/list.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    cart_product_form = CartAddProductForm()
    context = {'product': product, 'cart_product_form': cart_product_form}
    return render(request, 'shop/product/detail.html', context)


def contact(request):
    return render(request, 'contact.html')

def send_message(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        new_message = Message(name=name, email=email, message=message)
        new_message.save()

        return redirect('shop:contact')
    else:
        return redirect('shop:contact')