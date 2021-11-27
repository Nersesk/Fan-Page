from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .models import OrderItem
from shop.models import Attributes
from .cart import Cart
from .forms import CartAddProductForm, OrderCreateForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Attributes, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Attributes, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    menu = [{'name': 'News', 'name_url': 'Home'},
            {'name': 'Shop', 'name_url': 'shop'},
            {'name': 'About us', 'name_url': 'about'},
            ]
    for item in cart:
        item['update_q'] = CartAddProductForm(initial={'quantity': item['quantity'],'update': True})

    return render(request,'carts/detail.html',{'menu': menu,})


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order=form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],price=item['price'],quantity=item['quantity'])
            cart.clear()
            return render(request, 'shop/thank_s.html',
                          )
    else:
        form = OrderCreateForm
    return render(request, 'carts/create.html',
                  {'form': form})