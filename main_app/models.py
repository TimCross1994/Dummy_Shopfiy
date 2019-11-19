from django.db import models

# Create your models here.
class Search(models.Model):
    search = models.TextField(max_length=100)