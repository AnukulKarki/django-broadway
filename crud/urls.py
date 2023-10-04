from django.urls import path
from .views import crud, classroomDelete, classroomUpdate

urlpatterns = [
    path("",crud, name="crudClassroom"),
    path("class/delete/<int:id>/",classroomDelete, name="classroomDelete"),
    path("class/update/<int:id>/",classroomUpdate, name="classroomUpdate"),
]
