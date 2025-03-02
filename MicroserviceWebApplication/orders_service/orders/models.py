from django.db import models

class Order(models.Model):
    user_id = models.IntegerField()
    product = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
