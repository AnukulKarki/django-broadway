from django.urls import path
from .views import classroom, model_classroom

urlpatterns = [
    path("classroom/", classroom, name="cb_classroom"),
    path("model-classroom/", model_classroom, name="cb_model_classroom"),
]
