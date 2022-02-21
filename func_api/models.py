from django.db import models

class Student_data(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    # def __str__(self):
    #     self.name

