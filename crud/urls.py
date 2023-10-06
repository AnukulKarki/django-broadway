from django.urls import path
from .views import crud, classroomDelete, classroomUpdate, student, addStudent

urlpatterns = [
    path("",crud, name="crudClassroom"),
    path("class/delete/<int:id>/",classroomDelete, name="classroomDelete"),
    path("class/update/<int:id>/",classroomUpdate, name="classroomUpdate"),
    path("student/", student, name="crudStudents"),
    path("addStudent/",addStudent, name="addStudent")
]
