from django.shortcuts import render, redirect
from crud.models import *
from .forms import ClassroomForm, ClassroomModelForm
from django.http import HttpRequest

# Create your views here.
def classroom (request:HttpRequest):
    if request.method == "POST":
        # name = request.POST.get('name')
        form = ClassroomForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            
            Classroom.objects.create(name = name)
        return redirect("cb_classroom")
    
    form = ClassroomForm()
    classrooms = Classroom.objects.all()
    return render(request,"classBased/classroom.html", {"title":"classroom","classrooms":classrooms, "form":form})

def model_classroom(request:HttpRequest):
    if request.method == "POST":
        # name = request.POST.get('name')
        form = ClassroomModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("cb_classroom")
    
    form = ClassroomModelForm()
    classrooms = Classroom.objects.all()
    return render(request,"classBased/classroom.html", {"title":"classroom","classrooms":classrooms, "form":form})