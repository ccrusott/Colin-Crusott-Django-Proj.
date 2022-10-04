from dataclasses import fields
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
    template = "inventory/menuitem_list.html"

class MenuItemCreate(CreateView):
    model = MenuItem
    template = "inventory/menuitem_form.html"
    fields = ['menu_item_name', 'item_price']
class MenuItemDelete(DeleteView):
    model = MenuItem
    template = "inventory/menu_item_delete.html"
    success_url = "/inventory/menu/list"
class MenuItemUpdate(UpdateView):
    model = MenuItem
    template = "inventory/menu_item_update.html"
    fields = ['menu_item_name', 'item_price']
    success_url = "/inventory/menu/list"
class IngredientList(ListView):
    model = Ingredient
    template = "inventory/ingredient_list.html"
class IngredientCreate(CreateView):
    model = Ingredient
    template = "inventory/ingredient_create.html"
    fields = ['name', 'quantity', 'price_per_unit', 'unit']
class IngredientDelete(DeleteView):
    model = Ingredient
    template = "inventory/ingredient_confirm_delete.html"
    success_url = "/inventory/ingredient/list"
class IngredientUpdate(UpdateView):
    model = Ingredient
    template = "inventory/ingredient_update.html"
    fields = ['name', 'quantity', 'price_per_unit', 'unit']
    success_url = "inventory/ingredient/list"
class RecipeReqList(ListView):
    model = RecipeRequirements
    template = "inventory/recipe_list.html"
class RecipeCreate(CreateView):
    model = RecipeRequirements
    template = "inventory/recipe_create.html"
    fields = ['ingredient', 'menu_item', 'quantity_needed']
class RecipeUpdate(UpdateView):
    model = RecipeRequirements
    template = "inventory/recipe_update.html"
    fields = ['ingredient', 'menu_item', 'quantity_needed']
    success_url= "inventory/recipe/list"
class RecipeDelete(DeleteView):
    model = RecipeRequirements
    template = "inventory/recipe_delete.html"
    success_url = "inventory/recipe/list"
class PurchaseList(ListView):
    model = Purchase
    template = "inventory/purchase_list.html"
class PurchaseCreate(CreateView):
    model = Purchase
    template = "inventory/purchase_create.html"
    fields = ['purchased_item', 'timestamp']
class PurchaseUpdate(UpdateView):
    model = Purchase
    template = "inventory/purchase_update.html"
    fields = ['purchased_item', 'timestamp']
    success_url= "inventory/purchase/list"
class PurchaseDelete(DeleteView):
    model = Purchase
    template = "inventory/purchase_delete.html"
    success_url = "inventory/purchase/list"
