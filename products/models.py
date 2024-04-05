from django.db import models

# Create your models here.
class ProductListing(models.Model):
    moodleID = models.IntegerField()
    title = models.CharField(max_length = 255)
    category = models.CharField(max_length = 255)
    price = models.IntegerField()
    selected_year = models.CharField(max_length = 255)
    selected_branch = models.CharField(max_length = 255)
    selected_item_type = models.TextField()
    selected_condition = models.CharField(max_length = 255)
    product_description = models.TextField()
    image_urls = models.TextField()
    admin_approval = models.CharField(max_length = 5)
    class Meta:
        db_table = "product_listings"

class ResourceListing(models.Model):
    moodleID = models.IntegerField()
    resource = models.TextField()
    admin_approval = models.CharField(max_length = 5)
    stars = models.IntegerField(default=0)
    class Meta:
        db_table = "resource_listings"

class StarredResources(models.Model):
    moodleID = models.IntegerField()
    resourceID = models.IntegerField()
    class Meta:
        db_table = "starred_resources"




