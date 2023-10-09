from django.urls import path
from .views import classroom, model_classroom, classroomView, classroomTemplateView, ClassroomCreateView, StudentListView

urlpatterns = [
    path("classroom/", classroom, name="cb_classroom"),
    path("model-classroom/", model_classroom, name="cb_model_classroom"),
    path("simple-classroom/",classroomView.as_view()), #as_view --> call the method according to the method type.
    path("template-classroom/",classroomTemplateView.as_view()),
    path("create-classroom",ClassroomCreateView.as_view()),
    path("student-list/", StudentListView.as_view()),
    
]
