from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def staticHome(request):
    return render(request, template_name="staticRender/staticHome.html", context={"title":"Static Test"})

def protfolio(request):
    return render(request, "staticRender/index.html")