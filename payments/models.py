from django.db import models

# Create your models here.
class Orders(models.Model):
    moodleID = models.IntegerField()
    productID = models.IntegerField()
    orderID = models.CharField(max_length = 100)
    class Meta:
        db_table = "orders"
