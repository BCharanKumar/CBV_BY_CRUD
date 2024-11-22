from django.db import models

# Create your models here.


class School(models.Model):
    scname=models.CharField(max_length=100)
    scprincpal=models.CharField(max_length=75)
    scadd=models.TextField()

    def __str__(self):
        return self.scname
class Student(models.Model):
    sname=models.CharField(max_length=125)
    sage=models.IntegerField()
    scname=models.ForeignKey(School,on_delete=models.CASCADE)
    def __str__(self):
        return self.sname
    