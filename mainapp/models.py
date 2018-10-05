from django.db import models

class coordinates(models.Model) :
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
# Create your models here.
