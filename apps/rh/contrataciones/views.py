from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.
from django.contrib.auth.decorators import login_required



@login_required 
def index(request):

    context = {
        'mainModuleName': 'recursos_humanos',
        'modulos': [
            {'parentModuleName': 'contrataciones'},
            {'childModuleName': 'gestor_contratos'}  # default
        ],
        'defaultUrl': 'menucontrataciones',
        'defaultChildUrl': 'rhGestionarContratos',
    }

    # Add context data here
    # context['test'] = 'OK'

    # Page from the theme
    return render(request, 'pages/rh/contrataciones.html', context=context)

@login_required 
def gestionarContratos(request):

    if request.method == 'GET':

        if request.GET.get('element_id'):

            tipoSolicitud = (request.GET.get('element_id'))

            if (tipoSolicitud[:3] == 'R02'):

                tipoSolicitud = tipoSolicitud[3:-4]

                tipoSolicitudContext = ''.join(
                    ['_' + char.lower() if char.isupper() else char for char in tipoSolicitud]).lstrip('_')

                context = {
                    'meta': {
                        'mainModuleName': 'recursos_humanos',
                        'modulos': [
                            {'parentModuleName': 'contrataciones'},
                            {'childModuleName': 'gestor_contratos'},  # default
                            {'subChildModuleName': tipoSolicitudContext},
                        ],
                        'defaultUrl': 'menucontrataciones',
                        'defaultChildUrl': 'rhGestionarContratos',
                        'defaultSubChildUrl': ''
                    }
                }

                if (tipoSolicitud == 'AgregarEmpleado'):

                    context['meta'].update(
                        {'defaultSubChildUrl': 'rhAgregarEmpleado'})

                    rendered = render_to_string(
                        'pages/rh/empleados/crud-empleados/agregar.html')

                    content = {
                        'HTMLData': rendered,
                        'MetaData': context
                    }

                    return JsonResponse(content)

                elif (tipoSolicitud == 'ModificarEmpleado'):

                    context['meta'].update(
                        {'defaultSubChildUrl': 'rhModificarEmpleado'})

                    rendered = render_to_string(
                        'pages/rh/empleados/crud-empleados/modificar.html')

                    content = {
                        'HTMLData': rendered,
                        'MetaData': context
                    }

                    return JsonResponse(content)

                elif (tipoSolicitud == 'EliminarEmpleado'):

                    context['meta'].update(
                        {'defaultSubChildUrl': 'rhEliminarEmpleado'})

                    rendered = render_to_string(
                        'pages/rh/empleados/crud-empleados/eliminar.html')

                    content = {
                        'HTMLData': rendered,
                        'MetaData': context
                    }

                    return JsonResponse(content)

            context = {
                'mainModuleName': 'recursos_humanos',
                'modulos': [
                    {'parentModuleName': 'contrataciones'},
                    {'childModuleName': 'gestionar_contratos'}
                ],
                'defaultUrl': 'menucontrataciones',
                'defaultChildUrl': 'rhGestionarContratos'
            }

            rendered = render_to_string(
                'pages/rh/contrataciones/gestionar-contratos.html')

            content = {'HTMLData': rendered,
                       'MetaData': context
                       }

            return JsonResponse(content)
    else:

        context = {
            'mainModuleName': 'recursos_humanos',
            'modulos': [
                {'parentModuleName': 'empleados'},
                {'childModuleName': 'gestionar_empleados'}
            ],
            'defaultUrl': 'menuempleado',
            'defaultChildUrl': 'rhGestionarEmpleados'
        }

        content = {'HTMLData': 'hola',
                   'MetaData': context
                   }

        return JsonResponse(content)

    context = {
        'meta': {
            'mainModuleName': 'recursos_humanos',
            'modulos': [
                {'parentModuleName': 'remuneraciones'},
                {'childModuleName': ''},
            ],
            'defaultUrl': 'menuremuneraciones',
            'defaultChildUrl': '',
        }
    }

    rendered = render_to_string(
        'pages/rh/contrataciones/gestionar-contratos.html')

    content = {
        'HTMLData': rendered,
        'MetaData': context
    }

    return JsonResponse(content)

