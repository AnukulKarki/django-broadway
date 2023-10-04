from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Classroom

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