from django.db import models

# Create your models here.

class stud_record(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=10)
    collage = models.CharField(max_length=50)
    semester = models.CharField(max_length=10)
    branch = models.CharField(max_length=10)
    class Meta:
        db_table= "stud_record"