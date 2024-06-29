# mi_aplicacion/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('crudusuario/', views.crudusuario, name='crudusuario'),
    path('contacto/', views.contacto, name='contacto'),
    path('fortnite/', views.fortnite, name='fortnite'),
    path('gta_cash/', views.gta_cash, name='gta_cash'),
]