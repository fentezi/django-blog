from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

from django.views.decorators.http import require_POST
from furnitures import models
from . import forms
from .cart import Cart


# Create your views here.
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(models.FurnituresModel, id=product_id)
    form = forms.CartForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(models.FurnituresModel, id=product_id)
    cart.remove(product)
    return JsonResponse({'success': True})


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = forms.CartForm(
            initial={
                'quantity': item['quantity'],
                'update': True,
            }
        )
    return render(request, 'cart/detail_cart.html', {'cart': cart, })
