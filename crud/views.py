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
        classroomName = request.POST.get("classroomId")
        pp = request.FILES.get('pp')

        StudentObject = Student.objects.create(name=name, email=email, age=age, classroom_id = classroomName)
        StudentProfileObject = StudentProfile.objects.create(contact=contact, address= address, student = StudentObject)
        if pp:
            StudentProfileObject.picture = pp
            StudentProfileObject.save()

        return redirect("crudStudents")

    return render(request, "crud/addStudent.html", {"title":"Add Student", "class": Classroom.objects.all() })

def studentDetail(request:HttpRequest, id):
    StudentObject = Student.objects.get(id=id)
    return render(request, "crud/studentDetail.html", {"title":"Student Details", "student":StudentObject})

def studentUpdate(request:HttpRequest, id):
    StudentObject = Student.objects.get(id=id)
    classes = Classroom.objects.all()

    if request.method == "POST":
        updatedName = request.POST.get('name')
        updatedEmail = request.POST.get('email')
        updatedAge = request.POST.get('age')
        updatedContact = request.POST.get('contact')
        updatedAddress = request.POST.get('address')
        updatedPhoto = request.FILES.get('pp')

        Student.objects.filter(id=id).update(name=updatedName, email = updatedEmail, age = updatedAge)

        sp, b = StudentProfile.objects.update_or_create(student = StudentObject, defaults={"address":updatedAddress, "contact":updatedContact}) #Return Tuple (object StudentProfile Object, boolean (True for Create, False for update))

        if updatedPhoto:
            sp.picture = updatedPhoto
            sp.save()
        return redirect("studentDetail", StudentObject.id)
    return render(request, "crud/studentUpdate.html", {"title":"Student Update", "student":StudentObject, "class":classes})

def studentDelete(request:HttpRequest, id):
    studentObject = Student.objects.get(id=id)
    if request.method == "POST":
        studentObject.delete()
        return redirect("crudStudents")
    return render(request, "crud/studentDelete.html",{"student":studentObject})

