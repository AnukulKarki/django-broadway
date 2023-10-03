from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from tempinheritance.models import Student

# Create your views here.
def form(request:HttpRequest):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")

        Student.objects.create(name=name, email=email,age = age)
        return redirect("data")
    return render(request, "templateForms/form.html")