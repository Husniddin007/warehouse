from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_qty = models.IntegerField()

    def __str__(self):
        return self.product_name


class Material(models.Model):
    material_name = models.CharField(max_length=100)

    def __str__(self):
        return self.material_name


class ProductMaterials(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.FloatField()


class Warehouse(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    remaining_quantity = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.material.material_name} - {self.remaining_quantity} "
