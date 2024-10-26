from django.urls import path
from django.conf.urls import handler404
from . import views


urlpatterns = [
    path('menu/', views.index, name='menuremuneraciones'),
    path('Remuneraciones_Produccion/', views.Rproduccion, name='r_produccion'),
    path('Remuneraciones_CRM/', views.Rcrm, name='r_crm'),
    path('Remuneraciones_Administracion/', views.Radmin, name='r_admin'),
    path('Remuneraciones_Recursos_Humanos/', views.Rrrhh, name='r_rrhh'),
    path('Remuneraciones_Finanzas/', views.Rfinanzas, name='r_finanzas'),
    path('menu/fichaEmpleados/', views.fichasEmpleados, name='rhFichaEmpleados'),
    path('menu/PersonalView/', views.fichasEmpleados, name='rhFichaPersonalView'),
    path('menu/LaboralView/', views.fichasEmpleados, name='rhFichaLaboralView'),
    path('menu/PagoView/', views.fichasEmpleados, name='rhFichaPagoView'),
    path('menu/PrevisionView/', views.fichasEmpleados, name='rhFichaPrevisionView'),
    path('menu/CompetenciasView/', views.fichasEmpleados, name='rhFichaCompetenciasView'),
    path('menu/CargasView/', views.fichasEmpleados, name='rhFichaCargasView'),
    path('menu/DocumentosView/', views.fichasEmpleados, name='rhDocumentosView'),
    path('menu/HorarioView/', views.fichasEmpleados, name='rhHorarioView'),
    path('menu/modeloCalculo/', views.modeloCalculo, name='rhModeloCalculo'),
]

handler404 = ''