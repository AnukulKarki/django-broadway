
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='vies'),
    path('', views.emptypath, name='path'),
    path('page/',views.htmlRoot)
]