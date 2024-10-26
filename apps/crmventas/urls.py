from django.urls import path

from . import views

app_name = "app_crmventas"

urlpatterns = [
    #Clientes Ventas
    path('zona', views.zona, name='zona'),
    path('campana', views.campana, name='campana'),
    path('calendariocampana', views.calendariocampaña, name='calendariocampaña'),
    path('clientes_leads', views.clientes_leads, name='clientes_leads'),
    path('cotizaciones', views.cotizaciones, name='cotizaciones'),
    path('cotizacionCrear', views.cotizacionCrear, name='cotizacionCrear'),
    path('ventas', views.ventas, name='ventas'),
    path('contratoscv', views.contratoscv, name='contratoscv'),
    path('postventa', views.postventa, name='postventa'),
    path('reembolso', views.reembolso, name='reembolso'),
    path('soporte', views.soporte, name='soporte'),
]