from django.contrib import admin

from .models import *

class coordinateAdmin(admin.ModelAdmin) :
    list_display = []
    for columnName in coordinates._meta.fields :
        list_display.append(columnName.get_attname_column()[0])

admin.site.register(coordinates,coordinateAdmin)
