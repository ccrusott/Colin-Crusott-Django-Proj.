from django.urls import path
from . import views

urlpatterns = [path('', views.HomeView.as_view(), name='home'),
path('menu/list', views.MenuItemList.as_view(), name='menulist'),
path('menu/create', views.MenuItemCreate.as_view(), name='menucreate'),
path('menu/update/<pk>', views.MenuItemUpdate.as_view(), name='menuupdate'),
path('menu/delete/<pk>', views.MenuItemDelete.as_view(), name='menudelete'),
path('ingredient/list', views.IngredientList.as_view(), name='ingredientlist'),
path('ingredient/create', views.IngredientCreate.as_view(), name='ingredientcreate'),
path('ingredient/update/<pk>', views.IngredientUpdate.as_view(), name='ingredientupdate'),
path('ingredient/delete/<pk>', views.IngredientDelete.as_view(), name='ingredientdelete'),
path('recipe/list', views.RecipeReqList.as_view(), name='recipelist'),
path('recipe/create', views.RecipeCreate.as_view(), name='recipecreate'),
path('recipe/update/<pk>', views.RecipeUpdate.as_view(), name='recipeupdate'),
path('recipe/delete/<pk>', views.RecipeDelete.as_view(), name='recipedelete'),
path('purchase/list', views.PurchaseList.as_view(), name='purchaselist'),
path('purchase/create', views.PurchaseCreate.as_view(), name='purchasecreate'),
path('purchase/update/<pk>', views.PurchaseUpdate.as_view(), name='purchaseupdate'),
path('purchase/delete/<pk>', views.PurchaseDelete.as_view(), name='purchasedelete'),
path('inventory/reports', views.ReportView.as_view(), name='reports')
]