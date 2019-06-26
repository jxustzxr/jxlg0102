from django.db import models
from datetime import datetime
# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=20,null=False)
    author=models.CharField(max_length=20,null=False)
    pub_name=models.DateTimeField(default=datetime.now)
    prince=models.FloatField(default=0)