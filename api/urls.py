from django.urls import path
from .views import hello_world, MessageView, SimpleStudentView, SimpleStudentListView, ClassroomDetailAPIView, ClassroomAPIView, studentAPIView, StudentProfileAPIView

urlpatterns = [
    path("hello-world/", hello_world),
    path("message/", MessageView.as_view()),
    path("simple-student/<int:id>/", SimpleStudentView.as_view()),
    path("student-list/", SimpleStudentListView.as_view())
]

urls_with_serializers = [
    path("classroom/<int:id>", ClassroomDetailAPIView.as_view()),
    path("classroom/", ClassroomAPIView.as_view()),
    path("student/",studentAPIView.as_view()),
    path("studentProfile/", StudentProfileAPIView.as_view())
]

urlpatterns += urls_with_serializers