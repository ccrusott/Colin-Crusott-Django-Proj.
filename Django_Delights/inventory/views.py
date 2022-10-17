from dataclasses import fields
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .forms import MenuItemForm, IngredientForm, PurchaseForm, RecipeRequirementForm
from .models import MenuItem, Ingredient, RecipeRequirements, Purchase
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.db.models import Sum, F
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def logout_request(request):
    logout(request)
    return redirect("home")
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/home.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["menu"] = MenuItem.objects.all()
        context["ingredient"] = Ingredient.objects.all()
        context["recipe"] = RecipeRequirements.objects.all()
        context["purchases"] = Purchase.objects.all()
        return context

class MenuItemList(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "inventory/menuitem_list.html"

class MenuItemCreate(LoginRequiredMixin, CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = "inventory/menuitem_form.html"
class MenuItemDelete(LoginRequiredMixin, DeleteView):
    model = MenuItem
    template_name = "inventory/menuitem_confirm_delete.html"
    success_url = "/menu/list"
class MenuItemUpdate(LoginRequiredMixin, UpdateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = "inventory/menuitem_update.html"
    success_url = "/menu/list"
class IngredientList(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "inventory/ingredient_list.html"
class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "inventory/ingredient_form.html"
class IngredientDelete(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_confirm_delete.html"
    success_url = "/ingredient/list"
class IngredientUpdate(LoginRequiredMixin, UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "inventory/ingredient_update.html"
    success_url = "/ingredient/list"
class RecipeReqList(LoginRequiredMixin, ListView):
    model = RecipeRequirements
    template_name = "inventory/reciperequirements_list.html"
    context_object_name = 'recipe_item'
class RecipeCreate(LoginRequiredMixin, CreateView):
    model = RecipeRequirements
    form_class = RecipeRequirementForm
    template_name = "inventory/reciperequirements_form.html"
class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = RecipeRequirements
    form_class = RecipeRequirementForm
    template_name = "inventory/reciperequirements_update.html"
    success_url= "/menu/list"
class RecipeDetail(LoginRequiredMixin, DetailView):
    model = MenuItem
    template_name = "inventory/recipedetail.html"
    context_object_name = 'recipe_item'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = RecipeRequirements.objects.filter(menu_item_id=self.object)
        return context
class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = RecipeRequirements
    template_name = "inventory/reciperequirements_confirm_delete.html"
    success_url = "/recipe/list"
class PurchaseList(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "inventory/purchase_list.html"
class PurchaseCreate(LoginRequiredMixin, TemplateView):
    template_name = "inventory/purchase_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu_items"] = [X for X in MenuItem.objects.all() if X.available()]
        return context
    def post(self, request):
        menu_item_id = request.POST["menu_item"]
        menu_item = MenuItem.objects.get(pk=menu_item_id)
        requirements = menu_item.reciperequirements_set
        purchase = Purchase(purchased_item=menu_item)

        for requirement in requirements.all():
            required_ingredient = requirement.ingredient
            required_ingredient.quantity -= requirement.quantity_needed
            required_ingredient.save()
        purchase.save()
        return redirect("/purchase/list")


class PurchaseUpdate(LoginRequiredMixin, UpdateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = "inventory/purchase_update.html"
    success_url= "/purchase/list"
class PurchaseDelete(LoginRequiredMixin, DeleteView):
    model = Purchase
    template_name = "inventory/purchase_confirm_delete.html"
    success_url = "/purchase/list"
   
class ReportView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/reports.html"
    
    def get_context_data(self):
        purchased_item_price = Purchase.objects.aggregate(Sum('purchased_item__item_price'))
        ingredients_price = Ingredient.objects.aggregate(price_sum = Sum(F('quantity') * F('price_per_unit')))
        costs = ingredients_price['price_sum']
        income = purchased_item_price['purchased_item__item_price__sum']
        profit = int(income or 0) - int(costs or 0)
        context = super().get_context_data()
        context["costs"] = costs
        context["income"] = income
        context["profit"] = profit

        return context