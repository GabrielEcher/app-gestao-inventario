from django.urls import path
from . import views

app_name = 'inv_manager'

urlpatterns = [
    path('inventario/', views.Inventory.as_view(), name='inventory')
]

