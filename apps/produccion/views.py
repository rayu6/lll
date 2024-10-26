from django.shortcuts import render
from django.contrib.auth.decorators import login_required
@login_required 
# Create your views here.
def inventario(request):
    context = {
        'mainModuleName': 'Producción',
        'modulos': [
            {'parentModuleName': 'Inventario'},
            #{'childModuleName': 'HIJO'}  
        ],
        #'defaultUrl': 'menucapacitaciones',
        #'defaultChildUrl': 'rhGestionarCapacitaciones',
    }

    # Add context data here
    # context['test'] = 'OK'

    # Page from the theme
    return render(request, 'pages/Produccion/inventario/inventario.html', context=context)

@login_required 
def Editarproducto(request):
    context = {
        'mainModuleName': 'Producción',
        'modulos': [
            {'parentModuleName': 'Inventario'},
            {'childModuleName': 'Editar Producto'}  
        ],
        #'defaultUrl': 'menucapacitaciones',
        #'defaultChildUrl': 'rhGestionarCapacitaciones',
    }

    # Add context data here
    # context['test'] = 'OK'

    # Page from the theme
    return render(request, 'pages/Produccion/inventario/Editarproducto.html', context=context)
@login_required 
def ingenieria(request):
    context = {
        'mainModuleName': 'Producción',
        'modulos': [
            {'parentModuleName': 'Ingeniería'},
            #{'childModuleName': 'Editar Producto'}  
        ],
        #'defaultUrl': 'menucapacitaciones',
        #'defaultChildUrl': 'rhGestionarCapacitaciones',
    }

    # Add context data here
    # context['test'] = 'OK'

    # Page from the theme
    return render(request, 'pages/Produccion/ingenieria/ingenieria.html', context=context)
@login_required 
def EditarFormula(request):
    context = {
        'mainModuleName': 'Producción',
        'modulos': [
            {'parentModuleName': 'Ingeniería'},
            {'childModuleName': 'Editar Fórmula'}  
        ],
        #'defaultUrl': 'menucapacitaciones',
        #'defaultChildUrl': 'rhGestionarCapacitaciones',
    }

    # Add context data here
    # context['test'] = 'OK'

    # Page from the theme
    return render(request, 'pages/Produccion/ingenieria/Editarformula.html', context=context)
@login_required 
def procesos(request):
    context = {
        'mainModuleName': 'Producción',
        'modulos': [
            {'parentModuleName': 'Procesos'},
            #{'childModuleName': 'Editar Producto'}  
        ],
        #'defaultUrl': 'menucapacitaciones',
        #'defaultChildUrl': 'rhGestionarCapacitaciones',
    }

    # Add context data here
    # context['test'] = 'OK'

    # Page from the theme
    return render(request, 'pages/Produccion/procesos/procesos.html', context=context)
@login_required 
def EditarProceso(request):
    context = {
        'mainModuleName': 'Producción',
        'modulos': [
            {'parentModuleName': 'Procesos'},
            {'childModuleName': 'Editar Proceso'}  
        ],
        #'defaultUrl': 'menucapacitaciones',
        #'defaultChildUrl': 'rhGestionarCapacitaciones',
    }

    # Add context data here
    # context['test'] = 'OK'

    # Page from the theme
    return render(request, 'pages/Produccion/procesos/EditarProceso.html', context=context)
@login_required 
def detalleprocesos(request):
    context = {
        'mainModuleName': 'Producción',
        'modulos': [
            {'parentModuleName': 'Procesos'},
            {'childModuleName': 'Detalle del Proceso'}  
        ],
        #'defaultUrl': 'menucapacitaciones',
        #'defaultChildUrl': 'rhGestionarCapacitaciones',
    }

    # Add context data here
    # context['test'] = 'OK'

    # Page from the theme
    return render(request, 'pages/Produccion/procesos/detalleprocesos.html', context=context)
@login_required 
def produccion(request):
    context = {
        'mainModuleName': 'Producción',
        'modulos': [
            {'parentModuleName': 'Modulo Producción'},
            #{'childModuleName': 'Editar Proceso'}  
        ],
        #'defaultUrl': 'menucapacitaciones',
        #'defaultChildUrl': 'rhGestionarCapacitaciones',
    }

    # Add context data here
    # context['test'] = 'OK'

    # Page from the theme
    return render(request, 'pages/Produccion/produccion.html', context=context)
@login_required 
def logistica(request):
    context = {
        'mainModuleName': 'Producción',
        'modulos': [
            {'parentModuleName': 'Logística'},
            #{'childModuleName': 'Editar Proceso'}  
        ],
        #'defaultUrl': 'menucapacitaciones',
        #'defaultChildUrl': 'rhGestionarCapacitaciones',
    }

    # Add context data here
    # context['test'] = 'OK'

    # Page from the theme
    return render(request, 'pages/Produccion/logistica.html', context=context)
@login_required 
def mantenimiento(request):
    context = {
        'mainModuleName': 'Producción',
        'modulos': [
            {'parentModuleName': 'Mantenimiento'},
            #{'childModuleName': 'Editar Proceso'}  
        ],
        #'defaultUrl': 'menucapacitaciones',
        #'defaultChildUrl': 'rhGestionarCapacitaciones',
    }

    # Add context data here
    # context['test'] = 'OK'

    # Page from the theme
    return render(request, 'pages/Produccion/mantenimiento.html', context=context)
@login_required 
def seguridad(request):
    context = {
        'mainModuleName': 'Producción',
        'modulos': [
            {'parentModuleName': 'Seguridad'},
            #{'childModuleName': 'Editar Proceso'}  
        ],
        #'defaultUrl': 'menucapacitaciones',
        #'defaultChildUrl': 'rhGestionarCapacitaciones',
    }

    # Add context data here
    # context['test'] = 'OK'

    # Page from the theme
    return render(request, 'pages/Produccion/seguridad.html', context=context)