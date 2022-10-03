from django.urls import path
from . import views

urlpatterns = [path('home/', views.index, name='index'),
path('menu/list', views.MenuItemList.as_view(), name='menulist'),
path('menu/create', views.MenuItemCreate.as_view(), name='menucreate'),
path('menu/update/<pk>', views.MenuItemUpdate.as_view(), name='menuupdate'),
path('menu/delete/<pk>', views.MenuItemDelete.as_view(), name='menudelete')
]