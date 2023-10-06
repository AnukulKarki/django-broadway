from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Classroom, Student, StudentProfile

# Create your views here.
def crud(request:HttpRequest):
    if request.method == "POST":
        name = request.POST.get("name")
        Classroom.objects.create(name=name)
        return redirect("crudClassroom")
    classroom = Classroom.objects.all()
    return render(request, "crud/classroom.html", {"title":"Classroom", "classrooms":classroom})

def classroomDelete(request:HttpRequest, id):
    classroom = Classroom.objects.get(id=id)
    if request.method == "POST":
        classroom.delete()
        return redirect("crudClassroom")
    return render(request,"crud/classroomDelete.html", {"title":"Classroom Delete", "classroom":classroom})

def classroomUpdate(request:HttpRequest, id):
    classroom = Classroom.objects.get(id=id)
    if request.method == "POST":
        updatedName = request.POST.get("updatedName")
        Classroom.objects.filter(id=id).update(name=updatedName)
        return redirect("crudClassroom")

    return render(request, "crud/classroomUpdate.html", {"title":"Classroom Update", "classroom":classroom})


def student(request:HttpRequest):
    students = Student.objects.all()
    return render(request, "crud/student.html", {"students":students, "title":"Student"})

def addStudent(request:HttpRequest):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        address = request.POST.get("address")
        contact = request.POST.get("contact")
        pp = request.FILES.get('pp')

        StudentObject = Student.objects.create(name=name, email=email, age=age, classroom_id = 1)
        StudentProfileObject = StudentProfile.objects.create(contact=contact, address= address, student = StudentObject)
        if pp:
            StudentProfileObject.picture = pp
            StudentProfileObject.save()

        return redirect("crudStudents")

    return render(request, "crud/addStudent.html", {"title":"Add Student"})


