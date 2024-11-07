from django.db import models

# Create your models here.

class course(models.Model):
    id = models.TextField(primary_key=True, max_length=5)
    name = models.TextField(max_length=20)

    def __str__(self):
        return f'{self.name}'

class student(models.Model):
    name = models.TextField(max_length=20)
    age = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to='crud_images/')
    course = models.ForeignKey(course,max_length=20,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
    
