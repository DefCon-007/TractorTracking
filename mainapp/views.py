from django.shortcuts import render
from mainapp.src import databaseConnection as db

def index(request) :
    coordinateList = db.getAllCoordinates()
    print(type(coordinateList))
    print(coordinateList)
    context = {
        "coordinatesList" : coordinateList
    }
    return  render(request, "mainapp/index.html", context=context)
# Create your views here.
