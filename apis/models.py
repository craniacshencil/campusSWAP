from django.db import models

# Create your models here.
class collegeStudent(models.Model):
    moodleID = models.IntegerField(primary_key = True)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    class Meta:
        db_table = "college_students" 