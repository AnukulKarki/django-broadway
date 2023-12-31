from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Student, StudentProfile, Classroom

# Create your views here.

def student(request: HttpRequest):
    student = [
        {"name":"Anukul","Age":20,"Address":"Kadaghari"},
        {"name":"Bhupey","Age":120,"Address":"Budhha Nagar"},
        {"name":"Srizan","Age":25,"Address":"Sankhamul"}
    ]

    return render(request, template_name='tempinheritance/student.html', context={'student':student})

def model_Student(request:HttpRequest):
    student = Student.objects.all()  #QuerySet 
    return render(request, template_name="tempinheritance/model_Student.html", context={"student":student})

def profileDetials(request:HttpRequest):
    studentProfile = StudentProfile.objects.all()    
    return render(request, template_name="tempinheritance/profileDetail.html", context={"data":studentProfile})

def classroomView(request:HttpRequest):
    classroomData = Classroom.objects.all()
    return render(request, "tempinheritance/classroom.html", {"classroomData": classroomData})


