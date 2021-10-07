from django.http import HttpResponseRedirect
from django.shortcuts import render
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
        'cart': Cart.objects.all()
    }
    return render(request, 'project/shopping_cart.html', context)


def add_to_cart(request, product):
    c1 = Cart.objects.get(id=1)
    c2 = Cart.objects.get(id=2)
    c3 = Cart.objects.get(id=3)
    product_id = product.name[-1]
    if product_id == '1':
        c1.quantity+1
        c1.save()
    elif product_id == '2':
        c2.quantity+1
        c2.save()
    else:
        c3.quantity+1
        c3.save()
    return HttpResponseRedirect(reverse('project:home'))







