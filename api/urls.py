from django.urls import path
from rest_framework.routers import DefaultRouter 
from .views import hello_world, MessageView, SimpleStudentView, SimpleStudentListView, ClassroomDetailAPIView, ClassroomAPIView, studentAPIView, StudentProfileAPIView, ClassroomListAPIView, ClassroomCreateAPIView, ClassroomRetrieveAPIView, ClassroomUpdateAPIView, ClassroomDestroyAPIView, ClassroomListCreateAPIView, ClassroomObjectAPIView , ClassroomViewSet, ClassroomListUpdateViewSet, ClassroomListCreateRetriveViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register("classroom-viewset", ClassroomViewSet)
router.register("classroom-list-update",ClassroomListUpdateViewSet)
router.register("classroom-list-create-retrive", ClassroomListCreateRetriveViewSet)

urlpatterns = [
    path("hello-world/", hello_world),
    path("message/", MessageView.as_view()),
    path("simple-student/<int:id>/", SimpleStudentView.as_view()),
    path("student-list/", SimpleStudentListView.as_view()),
    path("login/", obtain_auth_token, name="login")
]

urls_with_serializers = [
    path("classroom/<int:id>", ClassroomDetailAPIView.as_view()),
    path("classroom/", ClassroomAPIView.as_view()),
    path("student/",studentAPIView.as_view()),
    path("studentProfile/", StudentProfileAPIView.as_view())
]

generic_urls = [
    path("generic-classroom-list/", ClassroomListAPIView.as_view()),
    path("generic-classroom-create/", ClassroomCreateAPIView.as_view()),
    path("generic-classroom/", ClassroomListCreateAPIView.as_view()),
    path("generic-classroom-detail/<int:pk>/",ClassroomRetrieveAPIView.as_view()),
    path("generic-classroom-update/<int:pk>/",ClassroomUpdateAPIView.as_view()),
    path("generic-classroom-delete/<int:pk>/",ClassroomDestroyAPIView.as_view()),
    path("generic-classroom/<int:pk>/",ClassroomObjectAPIView.as_view()),
]

urlpatterns += urls_with_serializers + generic_urls + router.urls