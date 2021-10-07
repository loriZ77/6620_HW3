from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('cart/', views.shopping_cart, name='shopping_cart'),
    path('<str:product_name>/add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('<str:product_name>/remove/', views.delete_product, name='remove'),
    path('<str:product_name>/update/', views.update_product, name='update'),

]