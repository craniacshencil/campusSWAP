from django.db import models

# Create your models here.
class Student(models.Model):
    email = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    moodleid = models.IntegerField()
