from dataclasses import fields
from django.shortcuts import render
from django.http import HttpResponse
from .models import MenuItem, Ingredient, RecipeRequirements, Purchase
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import Http404
# Create your views here.
class HomeView(TemplateView):
    template_name = "inventory/home.html"

class MenuItemList(ListView):
    model = MenuItem
    template = "inventory/menuitem_list.html"

class MenuItemCreate(CreateView):
    model = MenuItem
    template = "inventory/menuitem_form.html"
    fields = ['menu_item_name', 'item_price']
class MenuItemDelete(DeleteView):
    model = MenuItem
    template = "inventory/menuitem_confirm_delete.html"
    success_url = "/menu/list"
class MenuItemUpdate(UpdateView):
    model = MenuItem
    template = "inventory/menuitem_update.html"
    fields = ['menu_item_name', 'item_price']
    success_url = "/menu/list"
class IngredientList(ListView):
    model = Ingredient
    template = "inventory/ingredient_list.html"
class IngredientCreate(CreateView):
    model = Ingredient
    template = "inventory/ingredient_form.html"
    fields = ['name', 'quantity', 'price_per_unit', 'unit']
class IngredientDelete(DeleteView):
    model = Ingredient
    template = "inventory/ingredient_confirm_delete.html"
    success_url = "/ingredient/list"
class IngredientUpdate(UpdateView):
    model = Ingredient
    template = "inventory/ingredient_update.html"
    fields = ['name', 'quantity', 'price_per_unit', 'unit']
    success_url = "/ingredient/list"
class RecipeReqList(ListView):
    model = RecipeRequirements
    template = "inventory/reciperequirements_list.html"
class RecipeCreate(CreateView):
    model = RecipeRequirements
    template = "inventory/reciperequirements_form.html"
    fields = ['ingredient', 'menu_item', 'quantity_needed']
class RecipeUpdate(UpdateView):
    model = RecipeRequirements
    template = "inventory/reciperequirements_update.html"
    fields = ['ingredient', 'menu_item', 'quantity_needed']
    success_url= "/recipe/list"
class RecipeDelete(DeleteView):
    model = RecipeRequirements
    template = "inventory/reciperequirements_confirm_delete.html"
    success_url = "/recipe/list"
class PurchaseList(ListView):
    model = Purchase
    template = "inventory/purchase_list.html"
class PurchaseCreate(CreateView):
    model = Purchase
    template = "inventory/purchase_form.html"
    fields = ['purchased_item', 'timestamp']
class PurchaseUpdate(UpdateView):
    model = Purchase
    template = "inventory/purchase_update.html"
    fields = ['purchased_item', 'timestamp']
    success_url= "/purchase/list"
class PurchaseDelete(DeleteView):
    model = Purchase
    template = "inventory/purchase_confirm_delete.html"
    success_url = "/purchase/list"
