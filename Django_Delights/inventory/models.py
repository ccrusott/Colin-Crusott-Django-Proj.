from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class MenuItem(models.Model):
    menu_item_name = models.CharField(unique=True, max_length=30)
    item_price = models.FloatField(default=0.00)
    def get_absolute_url(self):
        return '/menu/list'

    def get_recipe_url(self):
        return reverse("recipedetail", kwargs={'pk': self.pk})

    def available(self):
        return all(X.enough() for X in self.reciperequirements_set.all())

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
        return self.name
class RecipeRequirements(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null = True)
    menu_item_id = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity_needed = models.FloatField(default=0.0)
    def get_absolute_url(self):
        return '/recipe/list'
    def enough(self):
        return self.quantity_needed <= self.ingredient.quantity
    def __str__(self):
        return str(self.ingredient) + " for " + str(self.menu_item_id)
class Purchase(models.Model):
    purchased_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now, blank=True)
    def get_absolute_url(self):
        return '/purchase/list'
    def __str__(self):
        return self.purchased_item + " was purchased on " + str(self.timestamp)
   