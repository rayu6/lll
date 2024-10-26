from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
@login_required
# Create your views here.
def index(request):

    context = {
        'mainModuleName': 'recursos_humanos',
        'modulos': [
            {'parentModuleName': 'horario'},
            {'childModuleName': 'gestor_horario'}  # default
        ],
        'defaultUrl': 'menuhorario',
        'defaultChildUrl': 'rhGestionarHorario',
    }

    # Add context data here
    # context['test'] = 'OK'

    # Page from the theme
    return render(request, 'pages/rh/horario.html', context=context)

@login_required
def gestionarHorario(request):
    
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
                            {'parentModuleName': 'horario'},
                            {'childModuleName': 'gestor_horario'},  # default
                            {'subChildModuleName': tipoSolicitudContext},
                        ],
                        'defaultUrl': 'menuhorario',
                        'defaultChildUrl': 'rhGestionarHorario',
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
                    {'parentModuleName': 'horario'},
                    {'childModuleName': 'gestionar_horario'}
                ],
                'defaultUrl': 'menuhorario',
                'defaultChildUrl': 'rhGestionarHorario'
            }

            rendered = render_to_string(
                'pages/rh/horario/gestionar-horario.html')

            content = {'HTMLData': rendered,
                       'MetaData': context
                       }

            return JsonResponse(content)
    else:

        context = {
            'mainModuleName': 'recursos_humanos',
            'modulos': [
                {'parentModuleName': 'horario'},
                {'childModuleName': 'gestionar_horario'}
            ],
            'defaultUrl': 'menuhorario',
            'defaultChildUrl': 'rhGestionarHorario'
        }

        content = {'HTMLData': '',
                   'MetaData': context
                   }

        return JsonResponse(content)

    context = {
        'meta': {
            'mainModuleName': 'recursos_humanos',
            'modulos': [
                {'parentModuleName': 'horario'},
                {'childModuleName': 'gestionar_horario'},
            ],
            'defaultUrl': 'menuhorario',
            'defaultChildUrl': 'rhGestionarHorario',
        }
    }

    rendered = render_to_string(
        'pages/rh/horario/gestionar-horario.html')

    content = {
        'HTMLData': rendered,
        'MetaData': context
    }

    return JsonResponse(content)