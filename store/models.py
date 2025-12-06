from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')  # requires Pillow
    stock = models.IntegerField(default=10)

    def __str__(self):
        return self.name


class OrderRequest(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=15)
    customer_address = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        default='Pending'  # Pending, Contacted, Delivered
    )
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.product.name}"
