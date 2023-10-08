from django.urls import path
from .views import crud, classroomDelete, classroomUpdate, student, addStudent,studentDetail, studentUpdate, studentDelete

urlpatterns = [
    path("",crud, name="crudClassroom"),
    path("class/delete/<int:id>/",classroomDelete, name="classroomDelete"),
    path("class/update/<int:id>/",classroomUpdate, name="classroomUpdate"),
    path("student/", student, name="crudStudents"),
    path("addStudent/",addStudent, name="addStudent"),
    path("student/detail/<int:id>/",studentDetail, name="studentDetail"),
    path("student/update/<int:id>",studentUpdate, name="studentUpdate"),
    path("student/delete/<int:id>", studentDelete, name="studentDelete")
]
