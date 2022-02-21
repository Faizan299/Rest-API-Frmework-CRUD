from django.db import models

# Create your models here.
class studentData(models.Model):
	name = models.CharField(max_length=64)
	email = models.EmailField()