from django.urls import path,include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.addNewCoordinate),
    path('getcoordinate/', views.sendCoordinates, name="getcoordinate"),
    path('clear', views.clear, name="clear"),
    path('addexcep', views.addException, name = "addexcep"),
    path('showexcep', views.showExceptions, name = "showexcep"),
]