from django.shortcuts import render
from .models import *
from .forms import *
from cart.cart import Cart
# Create your views here.


def order_create(request):
    cart = Cart(request)
    # if request.method == 'POST':
    if request.POST:
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
                cart.clear()
                return render(request, 'orders/created.html', {'order': order})
    else:
        form = OrderCreateForm()
        context = {'cart': cart, 'form': form}
        return render(request, 'orders/create.html', context)
