from django.db import models

# Create your models here.
class Ingredient(models.model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField(default=0)
    price_per_unit = models.FloatField(default=0.0)

class MenuItem(models.model):
    grilled_cheese = "GC"
    cheeseburger = "CB"
    hotdog = "HD"
    menu_choices = [
        (grilled_cheese, "Grilled Cheese"), 
        (cheeseburger, "Cheeseburger"),
        (hotdog, "HotDog"),
    ]
    menu_item = CharField(max_length=2, choices=menu_choices, blank=True)
class RecipeRequirements(models.model):
    pass

class Purchase(models.model):
    pass
