from django.db import models

# Create your models here.

class TextComplaint(models.Model):
    complaint=models.CharField(max_length=100)
    complaint_time=models.DateTimeField(auto_now_add=True)
    predicted_class = models.CharField(max_length=100, blank=True, null=True)