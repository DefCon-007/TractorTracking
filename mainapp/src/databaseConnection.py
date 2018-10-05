from mainapp.models import coordinates,scriptExceptions

def getAllCoordinates() :

    try :
        data = coordinates.objects.all()
        listToReturn = list()
        for val in data :

            listToReturn.append({
                    "latitude" : val.latitude,
                    "longitude" : val.longitude,
                                })
        return listToReturn
    except Exception as e:
        print(e)
        return None


def cleardata() :
    coordinates.objects.all().delete()

def addNewException(excep,rep) :
    try :
        data = scriptExceptions()
        data.excep = excep
        data.rep = rep
        data.save()
    except Exception as e:
        print(e)
        pass

def getAllExceptions() :
    try :
        data = scriptExceptions.objects.all()
        listToReturn = list()
        for val in data :
            listToReturn.append({
                "date" : val.created_at,
                "excep" : val.excep,
                "rep" : val.rep,
            })
        return listToReturn
    except :
        return []


def addNewCoordinate(lat,long) :
    try :
        data = coordinates()
        data.latitude = lat
        data.longitude = long
        data.save()
        return True
    except Exception as e :
        print(e)
        return False