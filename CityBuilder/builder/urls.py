from django.urls import path, include
from . import views

urlpatterns = [
path('', views.HomeView.as_view(), name='home'),
path('dwarf/city', views.DwarfCity.as_view(), name='dwarfcity'),
path('dwarf/size', views.DwarfSizeSelect.as_view(), name='dwarfsize'),
]