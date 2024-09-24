from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_qty = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name


class Material(models.Model):
    material_name = models.CharField(max_length=100)

    def __str__(self):
        return self.material_name


class MaterialProduct(models.Model):
    product_id = models.ManyToManyField(Product)
    material_id = models.ManyToManyField(Material)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.product.product_name}-{self.material.material_name}({self.quantity})'


class Warehouse(models.Model):
    material_id = models.ManyToManyField(Material)
    remainder = models.ManyToManyField(Material)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.material.material_name}-{self.remainder} units @ ${self.price}'
