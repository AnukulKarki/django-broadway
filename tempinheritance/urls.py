from django.urls import path
from .views import student, model_Student, profileDetials, classroomView

urlpatterns = [
    path('data/', model_Student, name="data"),
    path('', student, name="student"),
    path('profile/',profileDetials, name="profile"),
    path('classroom/',classroomView , name="classroom")
]
