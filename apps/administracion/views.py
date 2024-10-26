from django.shortcuts import render
from django.contrib.auth.decorators import login_required
@login_required 
# Create your views here.

def departamentos(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administracion/departamentos.html', context=context)
@login_required 
def vistadepartamento(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administracion/Vista-Departamento.html', context=context)
@login_required 
def productos(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administracion/productos.html', context=context)
@login_required 
def gestionproductos(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administracion/gestionproductos.html', context=context)
@login_required 
def contratos(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administracion/contratos.html', context=context)
@login_required 
def contrato(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administracion/contrato.html', context=context)
@login_required 
def certificaciones(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administracion/certificaciones.html', context=context)
@login_required 
def proveedores(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administracion/proveedores.html', context=context)
@login_required 
def licitaciones(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administracion/licitaciones.html', context=context)
@login_required 
def proyectos(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administracion/proyectos.html', context=context)
@login_required 
def kpi(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Administración"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

    
    return render(request, 'pages/Administracion/kpi.html', context=context)