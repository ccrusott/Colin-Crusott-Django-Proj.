
from enum import unique
from random import choices
from django.db import models

# Create your models here.
race_choices = (
    ("Human", "Human"),
    ("Dwarf", "Dwarf"),
    ("Elf", "Elf"),
    ("Ork", "Ork"),
)
class Race(models.Model):
    race = models.CharField(max_length=20, choices=race_choices)

    def __str__(self):
        return self.race

class CityPrefix(models.Model):
    prefix = models.CharField(max_length=30, unique=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self):
        return self.prefix

class CitySuffix(models.Model):
    suffix = models.CharField(max_length=30, unique=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self):
        return self.suffix
gender = (
    ("Male", "Male"),
    ("Female", "Female"),
)
class VillagerFirstNames(models.Model):
    first_name=models.CharField(max_length=30, unique=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    gender = models.CharField(max_length=30, choices=gender, default="Male")

    def __str__(self):
        return self.first_name
class VillagerLastNames(models.Model):
    last_name = models.CharField(max_length=30, unique=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name

business_choices = (
    ("Tavern", "Tavern"),
    ("Inn", "Inn"),
    ("Blacksmith", "Blacksmith"),
    ("Tailor", "Tailor"),
    ("Jeweler", "Jeweler"),
    ("Musician's Shop", "Musician's Shop"),
    ("Weapon's Vendor", "Weapon's Vendor"),
    ("Armorer", "Armorer"),
    ("Potion Shop", "Potion Shop"),
    ("General Goods", "General Goods"),
    ("Pet Shop", "Pet Shop"),
    ("Map Maker", "Map Maker"),
    ("Bank", "Bank"),
    ("Library", "Library"),

)
class Business(models.Model):
    type = models.CharField(max_length=30, choices=business_choices)

    def __str__(self):
        return self.type

class BusinessPrefix(models.Model):
    prefix = models.CharField(max_length=30, unique=True)
    type = models.ForeignKey(Business, on_delete=models.CASCADE)

    def __str__(self):
        return self.prefix

class BusinessSuffix(models.Model):
    suffix = models.CharField(max_length=30, unique=True)
    type = models.ForeignKey(Business, on_delete=models.CASCADE)

    def __str__(self):
        return self.suffix
trait_types = (
    ("Common", "Common"),
    ("Official", "Official"),
    ("Guard", "Guard"),
    ("Business", "Business"),
    ("Professional", "Professional"),
)
class NPCtraits(models.Model):
    name = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=50, choices=trait_types, default="Common")
    def __str__(self):
        return self.name

class BusinessInventory(models.Model):
    product = models.CharField(max_length=50, unique=True)
    business_type = models.ForeignKey(Business, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.product

class PointsOfInterest(models.Model):
    name = models.CharField(max_length=100, unique=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
class WildCard(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name