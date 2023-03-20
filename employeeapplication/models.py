from django.db import models

# Create your models here.

class Employee(models.Model):
    eid = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    department = models.CharField(max_length=50)
    salary = models.IntegerField()