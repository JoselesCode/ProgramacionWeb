from django.shortcuts import render

# Create your views here.
# mi_aplicacion/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def crudusuario(request):
    return render(request, 'crudusuario.html')

def contacto(request):
    return render(request, 'formulario-contacto.html')

def fortnite(request):
    return render(request, 'Fornite.html')

def gta_cash(request):
    return render(request, 'Cash_gta.html')

def indexLogin(request):
    return render(request, 'indexLogin.html')