from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Product, Cart


def home(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'project/home.html', context)


def shopping_cart(request):
    context = {
        'products': Product.objects.all(),
        'cart': Cart.objects.all(),
        "data": [1, 2, 3, 4, 5]
    }
    return render(request, 'project/shopping_cart.html', context)


def add_to_cart(request, product_name):
    added_product = get_object_or_404(Product, name=product_name)
    try:
        cart = get_object_or_404(Cart, product=added_product)
    except(404, Cart.DoesNotExist):
        cart = added_product.cart_set.create(product=added_product, quantity=0)
    cart.quantity += 1
    cart.save()
    return HttpResponseRedirect(reverse('shopping_cart'))


def delete_product(request, product_name):
    product_to_delete = get_object_or_404(Product, name=product_name)
    cart = get_object_or_404(Cart, product=product_to_delete)
    cart.quantity = 0
    cart.save()
    return HttpResponseRedirect(reverse('shopping_cart'))


def update_product(request, product_name):
    product_to_update = get_object_or_404(Product, name=product_name)
    selected_quantity = int(request.POST['choice'])
    cart = get_object_or_404(Cart, product=product_to_update)
    cart.quantity += selected_quantity
    cart.save()
    return HttpResponseRedirect(reverse('shopping_cart'))
