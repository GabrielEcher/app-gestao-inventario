from django.contrib import admin
from django.urls import path, include
from inv_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inv_manager.urls')),
]
