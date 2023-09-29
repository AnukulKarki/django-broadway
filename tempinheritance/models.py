from django.db import models


class Classroom(models.Model):
    name = models.CharField( max_length=50)

    def __str__(self):
        return self.name


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    age = models.IntegerField()
    Classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="classroom_students", null=True, blank=True)

    def __str__(self):
        return self.name 
    

class StudentProfile(models.Model):
    Student = models.OneToOneField(Student, on_delete=models.CASCADE)  #can provide related name
    contact = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    rollNo = models.IntegerField()

    

    