from django.db import models

# Create your models here.
class Orders(models.Model):
    moodleID = models.IntegerField()
    productID = models.IntegerField()
    orderID = models.CharField(max_length = 100)
    class Meta:
        db_table = "orders"

class Payments(models.Model):
    productID = models.IntegerField()
    buyer_moodleID = models.IntegerField()
    seller_moodleID = models.IntegerField()
    orderID = models.CharField(max_length = 100)
    paymentID = models.CharField(max_length = 100)
    transaction_signature = models.CharField(max_length = 100)
    class Meta:
        db_table = "payments"
