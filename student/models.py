from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length = 50, blank = True, null = True)
    last_name = models.CharField(max_length = 50, blank = True, null = True)
    gender = models.CharField(max_length = 10, blank = True, null = True)
    age = models.DecimalField(max_digits = 7, decimal_places = 0, blank=True, null=True)
    major = models.CharField(max_length = 50, blank = True, null = True)