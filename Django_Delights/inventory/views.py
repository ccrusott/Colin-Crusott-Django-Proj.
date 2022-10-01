from django.shortcuts import render
from django.http import HttpResponse
from .models import MenuItem, Ingredient, RecipeRequirements, Purchase
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import Http404
# Create your views here.
def index(request):
    return HttpResponse("Welcome to the Inventory")

class MenuItemList(ListView):
    model = MenuItem
    template = "inventory/menu_list.html"

class MenuItemCreate(CreateView):
    model = MenuItem
    template = "inventory/menu_item_create.html"
    fields = ['menu_item_name', 'item_price']
class MenuItemDelete(DeleteView):
    model = MenuItem
    template = "inventory/menu_item_delete.html"
    success_url = "inventory/menu/list"
class MenuItemUpdate(UpdateView):
    model = MenuItem
    template = "inventory/menu_item_update.html"
    forms = ['menu_item_name', 'item_price']
    success_url = "inventory/menu/list"
class IngredientList(ListView):
    model = Ingredient
    template = "inventory/ingredient_list.html"
class IngredientCreate(CreateView):
    model = Ingredient
    template = "inventory/ingredient_create.html"
    fields = ['name', 'quantity', 'price_per_unit', 'unit']
class IngredientDelete(DeleteView):
    model = Ingredient
    template = "inventory/ingredient_delete.html"
    success_url = "inventory/ingredient/list"
class IngredientUpdate(UpdateView):
    model = Ingredient
    template = "inventory/ingredient_update.html"
    forms = ['name', 'quantity', 'price_per_unit', 'unit']
    success_url = "inventory/ingredient/list"
