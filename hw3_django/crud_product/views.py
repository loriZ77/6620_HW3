from django.shortcuts import render
from django.http import HttpResponse

products = [
    {'name': 'product1',
     'description': 'This is product1.',
     'price': '$11'
     },
    {'name': 'product2',
     'description': 'This is product2.',
     'price': '$22'
     },
    {'name': 'product3',
     'description': 'This is product3.',
     'price': '$33'
     },
]

shoppingList = [
    {

    }
]

def home(request):
    context = {
        'products': products
    }
    return render(request, 'project/home.html', context)


def shopping_cart(request):
    return render(request, 'project/shopping_cart.html')
