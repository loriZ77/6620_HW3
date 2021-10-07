from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True)
    detail = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name

    def add_prod_to_cart(self):
        self.quantity+1
