from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CollegeStudent(models.Model):
    moodleID = models.IntegerField(primary_key = True)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    class Meta:
        db_table = "college_students" 

class StudentMetaInfo(models.Model):
    moodleID = models.ForeignKey(User, on_delete = models.CASCADE)
    phonenumber = models.IntegerField()
    class Meta:
        db_table = "user_information" 