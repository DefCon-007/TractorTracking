from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view

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

@api_view(["POST"])
def addNewCoordinate(request) :
    data = request.data
    try :
        lat = float(data["latitude"])
        lon = float(data["longitude"])
        if db.addNewCoordinate(lat,lon) :
            return JsonResponse({"status" : "success"}, status=200)
        return JsonResponse({"status": "fail"}, status=501)
    except Exception as e :
        print(e)
        return JsonResponse({"status": "fail"}, status=501)

@api_view(["GET"])
def sendCoordinates(request) :
    coordinateList = db.getAllCoordinates()
    print(type(coordinateList))
    print(coordinateList)
    resp = {
        "data" : coordinateList
    }
    return JsonResponse(resp, status=200)

@api_view(["POST"])
def addException(request) :
    data = request.data
    try :
        addException(data["exception"], data["rep"])
    except :
        pass

def showExceptions(request) :
    return  render(request, "mainapp/excep.html", context={"list": db.getAllExceptions()})

def clear(request) :
    db.cleardata()
    return redirect("index")
