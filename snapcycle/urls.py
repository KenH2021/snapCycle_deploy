from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name="accueil"),
    path('propos/', views.propos, name="propos"),
    path('beta/', views.beta, name="beta"),
    path('thanks/', views.thanks, name="thanks"),
    path('contact/', views.contact, name="contact"),
    path('mission/', views.mission, name="mission"),
    path('spool/', views.spool, name="spool"),
    path('carbo/', views.carbo, name="carbo"),
    path('camera/', views.cameraIA, name="camera"),
]