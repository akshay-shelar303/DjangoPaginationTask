from django.db import models

class Student(models.Model):
    fname = models.CharField(max_length=32)
    lname = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    marks = models.FloatField()

    def __str__(self):
        return self.fname
