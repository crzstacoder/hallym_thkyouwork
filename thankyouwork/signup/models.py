from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Posting(models.Model) :
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postings')


    def __str__(self):
        return self.title
    