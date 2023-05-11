from django.db import models

# Create your models here.
class ThankPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateField()
    author = models.CharField(max_length=100)
