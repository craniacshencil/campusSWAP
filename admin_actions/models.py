from django.db import models

# Create your models here.
class AdminApprovalFeedback(models.Model):
    product_id = models.IntegerField(primary_key = True)
    feedback = models.TextField()
    class Meta:
        db_table = "admin_approval_feedback"

class AdminApprovalFeedbackResource(models.Model):
    resource_id = models.IntegerField(primary_key = True)
    feedback = models.TextField()
    class Meta:
        db_table = "admin_approval_feedback_resources"
