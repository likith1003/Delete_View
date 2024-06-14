from django.db import models

# Create your models here.

class School(models.Model):
    sname = models.CharField(max_length=50, primary_key=True)
    spno = models.CharField(max_length=50)
    sprincy = models.CharField(max_length=50)
    sadd = models.CharField(max_length=50)

    def __str__(self):
        return self.sname
    

class Student(models.Model):
    stdname = models.CharField(max_length=50)
    stdpno = models.CharField(max_length=50)
    sname = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.stdname
    
    