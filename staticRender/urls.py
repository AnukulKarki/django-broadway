from django.urls import path
from .views import staticHome, protfolio

urlpatterns = [
    path('protfolio/' ,protfolio),
    path('',staticHome)
]
