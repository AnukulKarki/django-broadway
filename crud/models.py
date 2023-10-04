from django.db import models

# Create your models here.
class Classroom(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="classroomStudent")

    def __str__(self):
        return self.name

class StudentProfile(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    picture = models.FileField(null=True, blank=True, upload_to="profilePicture")
    address = models.CharField(max_length=25)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return f"Profile of {self.student.name}"