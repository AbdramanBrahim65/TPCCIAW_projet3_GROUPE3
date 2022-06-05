from django.urls import path
from . import views
urlpatterns = [
    path('inscription/',views.inscriptionPage,name="inscriptionPage"),
    path('acces/',views.accesPage,name="acces"),
    path('Deconnecter/',views.logoutUser,name="Deconnecter"),
]