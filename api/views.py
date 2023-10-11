from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from crud.models import Student, Classroom
from rest_framework import status

from .serializers import ClassroomSerializers, ClassroomModelSerializer, StudentModelSerializer



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
            }, status=status.HTTP_404_NOT_FOUND)
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

        # dataList = [{"name":data.name} for data in students ]

        for data in students:
            studentData.append(
                {"name":data.name,
                 "email":data.email,
                 "age":data.age,
                 "classroom":data.classroom.name
                }
            )
        return Response(studentData)
    
    def post(self, *args, **kwargs):
        print(self.request.data)
        name = self.request.data.get("name")
        email = self.request.data.get("email")
        age = self.request.data.get("age")
        classroom = self.request.data.get("classroom")
        Student.objects.create(name=name, email=email, age=age, classroom_id = classroom)
        return Response({
            "detail":"Student Created Successfully!"
        }, status=status.HTTP_201_CREATED)
    
class ClassroomDetailAPIView(APIView):
    def get(self, *args, **kwargs):
        try:
            classroom = Classroom.objects.get(id=kwargs['id'])
        except Classroom.DoesNotExist:
            return Response({
                "detail":"Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ClassroomSerializers(classroom)  #Serializtion   Can send Only Object
        return Response(serializer.data)
    
    

class ClassroomAPIView(APIView):
    def post(self, *args, **kwargs):
        serializer = ClassroomModelSerializer(data=self.request.data)
        if serializer.is_valid():
            # name = serializer.validated_data.get("name")
            # Classroom.objects.create(name=name)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,*args, **kwargs):
        classroom = Classroom.objects.all()
        serializer = ClassroomModelSerializer(classroom, many = True)  #many = True for multiple value
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class studentAPIView(APIView):
    def get(self, *args, **kwargs):
        student = Student.objects.all()
        serializer = StudentModelSerializer(student, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,*args, **kwargs):
        serializer = StudentModelSerializer(data = self.request.data)
        serializer.is_valid( raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)