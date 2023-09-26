from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home(request: HttpRequest):
    return HttpResponse("<h1>Hello World !!!</h1>")

def emptypath(request:HttpRequest):
    return HttpResponse("<h1>THis is root page </h1>")

def htmlRoot(request:HttpRequest):
    people = [
        {"First":"Anukul","Last": "Karki" , "Address":"Kadaghari"},
        {"First":"Bhupendra","Last": "Neupane" , "Address":"Baneshwor"},
        {"First":"Srizan","Last": "Shakya" , "Address":"Sankhamul"},
    ]

    name = {"First":"Anukul","Last": "Karki" , "Address":"Kadaghari"}

    return render(request,template_name='myapp/home.html', context={"title":"Root Page",'name':name, 'people':people})