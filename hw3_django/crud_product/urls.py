from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('cart/', views.shopping_cart, name='shopping_cart')
]