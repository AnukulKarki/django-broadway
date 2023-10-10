from django.urls import path
from .views import hello_world, MessageView, SimpleStudentView, SimpleStudentListView

urlpatterns = [
    path("hello-world/", hello_world),
    path("message/", MessageView.as_view()),
    path("simple-student/<int:id>/", SimpleStudentView.as_view()),
    path("student-list", SimpleStudentListView.as_view())
]
