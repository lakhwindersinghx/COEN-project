from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    # Add more fields as needed

    def __str__(self):
        return f"Order {self.id} by {self.customer.username}"
