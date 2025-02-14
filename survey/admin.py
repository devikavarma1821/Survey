# admin.py
from django.contrib import admin
from .models import DemographicInformation, Transportation, EnvironmentalAwareness, FoodConsumption, Miscellaneous, Occupation,WasteManagement

admin.site.register(DemographicInformation)
admin.site.register(Transportation)
admin.site.register(EnvironmentalAwareness)
admin.site.register(FoodConsumption)
admin.site.register(Miscellaneous)
admin.site.register(Occupation)
admin.site.register(WasteManagement)