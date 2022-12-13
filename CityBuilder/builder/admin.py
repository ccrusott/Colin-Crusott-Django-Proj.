from django.contrib import admin
from .models import Race, CityPrefix, CitySuffix, Business, BusinessPrefix, BusinessSuffix, NPCtraits, BusinessInventory, VillagerFirstNames, VillagerLastNames, PointsOfInterest, WildCard
# Register your models here.
admin.site.register(Race)
admin.site.register(CityPrefix)
admin.site.register(Business)
admin.site.register(BusinessPrefix)
admin.site.register(BusinessSuffix)
admin.site.register(NPCtraits)
admin.site.register(BusinessInventory)
admin.site.register(CitySuffix)
admin.site.register(VillagerFirstNames)
admin.site.register(VillagerLastNames)
admin.site.register(WildCard)
admin.site.register(PointsOfInterest)
