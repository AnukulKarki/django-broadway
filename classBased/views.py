from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from crud.models import *
from .forms import ClassroomForm, ClassroomModelForm
from django.http import HttpRequest
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView

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


class classroomView(View):

    def get(self, *args, **kwargs):
        classroom = Classroom.objects.all()
        form = ClassroomModelForm()
        return render(self.request,"classbased/classroom.html", {"classrooms":classroom, "form":form})

    def post(self, *args, **kwargs):
        form = ClassroomModelForm(self.request.POST)
        if form.is_valid():
            form.save()  #can only be used in model form
        return redirect("cb_classroom")
    
class classroomTemplateView(TemplateView):
    template_name = "classBased/classroom.html"

    def get_context_data(self, **kwargs ):
        context = {"classrooms":Classroom.objects.all(), "form":ClassroomModelForm()}
        return context
    
class ClassroomCreateView(CreateView):
    form_class = ClassroomModelForm
    queryset = Classroom.objects.all()
    template_name = "classbased/classroom.html"
    success_url = reverse_lazy("cb_classroom")

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["classrooms"] = self.queryset
        return context
    
class StudentListView(ListView):
    queryset = Student.objects.all()
    template_name = "classBased/student.html"
    context_object_name = "students" #change the key of the dictionary which takes the data from query set

    
    # def get_context_data(self,* args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     # print(context)
    #     # context["students"] = self.queryset
    #     return context