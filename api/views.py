from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from crud.models import Student



# Create your views here.
def hello_world(request):
    response = {"message":"Hello World"}
    return JsonResponse(response)

class MessageView(APIView):
    def get(self, *args, **kwargs):
        return Response([
            {"name":"Anukul", "age":21},
            {"name":"Bhupendra", "age":20}
        ])
class SimpleStudentView(APIView):
    def get(self, *args, **kwargs):
        try:
            StudentObject = Student.objects.get(id=kwargs['id'])
        except:
            return Response({
                "detail":"Not Found"
            })
        return Response({
            "name":StudentObject.name,
            "email":StudentObject.email,
            "age":StudentObject.age,
            "classroom":StudentObject.classroom.name
        })

class SimpleStudentListView(APIView):
    def get(self, *args, **kwargs):
        students = Student.objects.all()
        studentData = []

        dataList = [{"name":data.name} for data in students ]

        for data in students:
            studentData.append(
                {"name":data.name,
                 "email":data.email,
                 "age":data.age,
                 "classroom":data.classroom.name
                }
            )
        return Response(studentData)