from django.db import models

# Create your models here.

class Student(models.Model):
    sno = models.IntegerField()
    sname = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    image = models.ImageField(upload_to="upload_images")

    def __str__(self):
        return self.sname
    
