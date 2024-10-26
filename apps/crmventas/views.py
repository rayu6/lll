from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView, CreateView
# Create your views here.
@login_required 
def zona(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Clientes Ventas"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}
   
    return render(request, 'pages/CLIENTES-VENTAS/zona.html', context=context)
@login_required 
def campana(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Clientes Ventas"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

  
    return render(request, 'pages/CLIENTES-VENTAS/campana.html', context=context)

@login_required 
def calendariocampaña(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Clientes Ventas"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

  
    return render(request, 'pages/CLIENTES-VENTAS/Campanaitems/calendarioact.html', context=context)
@login_required 
def clientes_leads(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Clientes Ventas"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

  
    return render(request, 'pages/CLIENTES-VENTAS/leads-clientes.html', context=context)
@login_required 
def cotizaciones(request):
    context = {
        'mainModuleName': 'Clientes Ventas',
        'modulos': [
            {'parentModuleName': 'Cotizaciones'},
            #{'childModuleName': 'Editar Proceso'}  
        ],
        #'defaultUrl': 'menucapacitaciones',
        #'defaultChildUrl': 'rhGestionarCapacitaciones',
    }

    # Add context data here
    # context['test'] = 'OK'

    # Page from the theme
    return render(request, 'pages/CLIENTES-VENTAS/cotizaciones.html', context=context)
@login_required 
def cotizacionCrear(request):
    context = {
        'mainModuleName': 'Clientes Ventas',
        'modulos': [
            {'parentModuleName': 'Cotizaciones'},
            {'childModuleName': 'Crear Cotización'}  
        ],
        #'defaultUrl': 'menucapacitaciones',
        #'defaultChildUrl': 'rhGestionarCapacitaciones',
    }

    # Add context data here
    # context['test'] = 'OK'

    # Page from the theme
    return render(request, 'pages/CLIENTES-VENTAS/cotizacionesCrear.html', context=context)

@login_required 
def ventas(request):
    context = {
        'mainModuleName': 'Clientes Ventas',
        'modulos': [
            {'parentModuleName': 'Ventas'},
            #{'childModuleName': 'Editar Proceso'}  
        ],
        #'defaultUrl': 'menucapacitaciones',
        #'defaultChildUrl': 'rhGestionarCapacitaciones',
    }

    # Add context data here
    # context['test'] = 'OK'

    # Page from the theme
    return render(request, 'pages/CLIENTES-VENTAS/ventas.html', context=context)
@login_required 
def contratoscv(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Clientes Ventas"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

  
    return render(request, 'pages/CLIENTES-VENTAS/contratoscv.html', context=context)
@login_required 
def postventa(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Clientes Ventas"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

  
    return render(request, 'pages/CLIENTES-VENTAS/postventa.html', context=context)
@login_required 
def reembolso(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Clientes Ventas"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

  
    return render(request, 'pages/CLIENTES-VENTAS/postventa/reembolso.html', context=context)
@login_required 
def soporte(request):
    #AGREGAR EN CADA VIEW PARA NAVIGATION
    modulo = "Clientes Ventas"
    nombre_vista = request.resolver_match.url_name
    context = {'modulo': modulo, 'nombre_vista': nombre_vista}

  
    return render(request, 'pages/CLIENTES-VENTAS/postventa/soporte.html', context=context)