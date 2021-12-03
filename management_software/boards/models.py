from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    initials = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    company = models.CharField(max_length=30)

class Board(models.Model):
    name = models.CharField(max_length=30)


