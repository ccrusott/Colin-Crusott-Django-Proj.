from dataclasses import fields
from django.shortcuts import render
from django.http import HttpResponse
from .forms import MenuItemForm, IngredientForm, PurchaseForm, RecipeRequirementForm
from .models import MenuItem, Ingredient, RecipeRequirements, Purchase
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import Http404
from django.db.models import Sum, F
# Create your views here.
class HomeView(TemplateView):
    template_name = "inventory/home.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["menu"] = MenuItem.objects.all()
        context["ingredient"] = Ingredient.objects.all()
        context["recipe"] = RecipeRequirements.objects.all()
        context["purchases"] = Purchase.objects.all()
        return context

class MenuItemList(ListView):
    model = MenuItem
    template_name = "inventory/menuitem_list.html"

class MenuItemCreate(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = "inventory/menuitem_form.html"
class MenuItemDelete(DeleteView):
    model = MenuItem
    template_name = "inventory/menuitem_confirm_delete.html"
    success_url = "/menu/list"
class MenuItemUpdate(UpdateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = "inventory/menuitem_update.html"
    success_url = "/menu/list"
class IngredientList(ListView):
    model = Ingredient
    template_name = "inventory/ingredient_list.html"
class IngredientCreate(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "inventory/ingredient_form.html"
class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_confirm_delete.html"
    success_url = "/ingredient/list"
class IngredientUpdate(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "inventory/ingredient_update.html"
    success_url = "/ingredient/list"
class RecipeReqList(ListView):
    model = RecipeRequirements
    template_name = "inventory/reciperequirements_list.html"
class RecipeCreate(CreateView):
    model = RecipeRequirements
    form_class = RecipeRequirementForm
    template_name = "inventory/reciperequirements_form.html"
class RecipeUpdate(UpdateView):
    model = RecipeRequirements
    form_class = RecipeRequirementForm
    template_name = "inventory/reciperequirements_update.html"
    success_url= "/recipe/list"
class RecipeDelete(DeleteView):
    model = RecipeRequirements
    template_name = "inventory/reciperequirements_confirm_delete.html"
    success_url = "/recipe/list"
class PurchaseList(ListView):
    model = Purchase
    template_name = "inventory/purchase_list.html"
class PurchaseCreate(CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = "inventory/purchase_form.html"
class PurchaseUpdate(UpdateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = "inventory/purchase_update.html"
    success_url= "/purchase/list"
class PurchaseDelete(DeleteView):
    model = Purchase
    template_name = "inventory/purchase_confirm_delete.html"
    success_url = "/purchase/list"
class ReportView(TemplateView):
    template_name = "inventory/reports.html"
    
    def get_context_data(self):
        purchased_item_price = Purchase.objects.aggregate(Sum('purchased_item__item_price'))
        ingredients_price = Ingredient.objects.aggregate(price_sum = Sum(F('quantity') * F('price_per_unit')))
        costs = ingredients_price['price_sum']
        income = purchased_item_price['purchased_item__item_price__sum']
        profit = income - costs
        context = super().get_context_data()
        context["costs"] = costs
        context["income"] = income
        context["profit"] = profit

        return context