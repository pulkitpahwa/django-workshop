from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField()
    student_class = models.CharField(max_length=5)
    branch = models.CharField(max_length = 20)
    contact_number = models.CharField(max_length=10)
    email = models.EmailField()
    batch = models.CharField(max_length=9)


    def __str__(self):
        return self.name 
