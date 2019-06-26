from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=100)
    telephone=models.CharField(max_length=11)
    email = models.EmailField(null=True)