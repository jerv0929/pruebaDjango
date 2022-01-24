from django.shortcuts import render
from django.http import HttpResponse
from inventario.models import producto, imagene

# Create your views here.

def login(request):
    
    if request.method=="POST":
        var_user=request.POST['user']
        var_pass=request.POST['pass']

        return render(request, 'validacion.html', {"user": var_user, "pass": var_pass})
    else:
        return render(request, 'ingreso.html')

def inicio(request):

    return render(request, 'index.html')

def todos(request):

    return render(request, 'todos.html')

def acero(request):

    return render(request, 'acero.html')

def cover(request):

    return render(request, 'covergold.html')

def laminado(request):

    return render(request, 'laminado.html')

def plata(request):

    return render(request, 'plata.html')

def registro(request):
    
    return render(request, 'registro.html')

def nuevoproducto(request):

    if request.method=="POST":
        var_ref=request.POST['ref']
        var_cat=request.POST['cat']
        var_des=request.POST['des']
        var_pre=request.POST['pre']
        var_can=request.POST['can']

        nuevo=producto.objects.create(referencia=var_ref, categoria=var_cat, descripcion=var_des, precio=var_pre, cantidad=var_can)
        

        return render(request, 'producto-agregado.html')
    else:
        
        return render(request, 'nuevo-producto.html')