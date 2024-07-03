from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=300)
    age=models.IntegerField()
    emp_id=models.IntegerField()
    department=models.CharField(max_length=200)


    def __str__(self):
        return self.name