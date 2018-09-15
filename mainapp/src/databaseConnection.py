from mainapp.models import coordinates

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