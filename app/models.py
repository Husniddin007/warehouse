from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=100)


class Material(models.Model):
    name = models.CharField(max_length=100)


class MaterialProduct(models.Model):
    product_id = models.ManyToManyField(Product)
    material_id = models.ManyToManyField(Material)
    quantity = models.IntegerField()


class Warehouse(models.Model):
    material_id = models.ManyToManyField(Material)
    remainder = models.ManyToManyField(Material)
    price = models.IntegerField()
