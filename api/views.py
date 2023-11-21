from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from crud.models import Student, Classroom, StudentProfile
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ClassroomSerializers, ClassroomModelSerializer, StudentModelSerializer, StudentProfileModelSerializer
from .viewsets import ListUpdateViewSet, ListCreateRetriveViewSet
from .permissions import isSuperAdminUser



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
        serializer = StudentModelSerializer(student, many = True, context = {"request":self.request}) #Sending request to serailizer through context
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,*args, **kwargs):
        serializer = StudentModelSerializer(data = self.request.data)
        serializer.is_valid( raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class StudentProfileAPIView(APIView):
    def get(self, *args, **kwargs):
        studentProfile = StudentProfile.objects.all()
        serializer = StudentProfileModelSerializer(studentProfile, many = True, context = {"request":self.request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,*args, **kwargs):
        serializer = StudentProfileModelSerializer(data = self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class ClassroomListAPIView(ListAPIView): #List API View  have get Method
    queryset = Classroom.objects.all() # can only have Query Set[]
    serializer_class = ClassroomModelSerializer #Does not need Open Close bracket.


class ClassroomCreateAPIView(CreateAPIView):#Create API
    serializer_class = ClassroomModelSerializer

class ClassroomRetrieveAPIView(RetrieveAPIView): #POST not available
    queryset = Classroom.objects.all() #check from only query set from the data that was sent
    serializer_class = ClassroomModelSerializer

class ClassroomUpdateAPIView(UpdateAPIView):
    queryset = Classroom.objects.all() 
    serializer_class = ClassroomModelSerializer

class ClassroomDestroyAPIView(DestroyAPIView):
    queryset = Classroom.objects.all() 
    serializer_class = ClassroomModelSerializer

class ClassroomListCreateAPIView(ListCreateAPIView): #Can create and display everything
    queryset = Classroom.objects.all() 
    serializer_class = ClassroomModelSerializer

class ClassroomObjectAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomModelSerializer



class ClassroomViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    # pagination_class = LimitOffsetPagination
    pagination_class = PageNumberPagination
    queryset = Classroom.objects.all()
    #Gives permission only for GET and does not provide information to other methods.
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny(),]
        return [isSuperAdminUser(),]
    
    def get_serializer_class(self):
        if self.action == "student":
            return StudentModelSerializer
        return ClassroomModelSerializer
    
    @action(detail = True)
    def student(self, *args, **kwargs):
        classroom_obj = self.get_object()
        students = Student.objects.filter(classroom = classroom_obj)
        ser = self.get_serializer(students, many = True)
        return Response(ser.data)

    
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        # classroom = self.request.GET.get("classroom")
        classroom = self.request.query_params.get("classroom")
        if classroom:
            return Student.objects.filter(classroom_id = classroom)
        return Student.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["name", "email"] #can be similasr
    filterset_fields = ["age", "name","classroom__name"] #must be same as value
    
class ClassroomListUpdateViewSet(ListUpdateViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomModelSerializer


class ClassroomListCreateRetriveViewSet(ListCreateRetriveViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomModelSerializer