from django.urls import path
from . import views

urlpatterns = [
    path('log/', views.getLogs),
    path('log/add/', views.addLog),
    path('station/', views.getStations),
    path('module/', views.getModules)
]