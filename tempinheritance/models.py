from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.name + " "+ str(self.age)
    

class StudentProfile(models.Model):
    Student = models.OneToOneField(Student, on_delete=models.CASCADE)  #can provide related name
    contact = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    rollNo = models.IntegerField()