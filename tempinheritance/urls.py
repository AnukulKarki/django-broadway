from django.urls import path
from .views import student, model_Student

urlpatterns = [
    path('data/', model_Student),
    path('', student)
]
