from django.db import models

class Student(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)