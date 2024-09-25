from django.db import models



class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_qty = models.IntegerField()

    def __str__(self):
        return self.product_name

class Material(models.Model):
    matrial_name = models.CharField(max_length=100)

    def __str__(self):
        return self.matrial_name
class Product_Material(models.Model):
        product = models.ForeignKey(Product,on_delete=models.CASCADE)
        matrial = models.ForeignKey(Material,on_delete=models.CASCADE)
        quantity = models.IntegerField()

        def __str__(self):
            return f"{self.product.product_nmae} - {self.matrial.material_name} ({self.quantity})"

class Warehouse(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    remaining_quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.material.matrial_name} - {self.remaining_quantity} ({self.price})"