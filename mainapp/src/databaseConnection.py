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