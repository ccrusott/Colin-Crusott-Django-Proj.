from django.db import models
from django.utils import timezone
# Create your models here.
class MenuItem(models.Model):
    menu_item_name = models.CharField(unique=True, max_length=30)
    item_price = models.FloatField(max_length=5)
    def get_absolute_url(self):
        return '/menu/list'
    
    def __str__(self):
        return self.menu_item_name + ":" + str(self.item_price)
class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField(default=0)
    price_per_unit = models.FloatField(default=0.0)
    unit = models.CharField(max_length=30, default="Units")
    def get_absolute_url(self):
        return '/ingredient/list'
    def __str__(self):
        return "There are " + str(self.quantity) + " " + self.unit + "s of " +self.name + " available. They cost " + str(self.price_per_unit) + " per " + self.unit
class RecipeRequirements(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, blank=True, null=True)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity_needed = models.FloatField(default=0.0)
    def get_absolute_url(self):
        return '/recipe/list'
    def __str__(self):
        return "You need " + str(self.quantity_needed) + " of " + self.ingredients + " to make " + self.menu_item
class Purchase(models.Model):
    purchased_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now, blank=True)
    def get_absolute_url(self):
        return '/purchase/list'
    def __str__(self):
        return self.purchased_item + " was purchased on " + str(self.timestamp)