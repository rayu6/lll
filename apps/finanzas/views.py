from django.shortcuts import render

from django.views.generic import ListView, TemplateView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


#ListView
@method_decorator(login_required, name='dispatch')
class Departamentos(TemplateView):
    # model = MODEL_NAME
    template_name = "pages/finanzas/departamentos/departamentos.html"

    # def get_queryset(self):
    #     queryset = super(model, self).get_queryset()
    #     queryset = queryset.
    #     return queryset


#------------------------ Vista de Centro de Costos con CRUD ------------------------------
@method_decorator(login_required, name='dispatch')
#ListView
class CentroDeCostos(TemplateView):
    template_name = "pages/finanzas/centro-de-costos/centroDeCostos.html"


#CreateView
@method_decorator(login_required, name='dispatch')
class CrearCentroDeCostos(TemplateView):
    template_name = "pages/finanzas/centro-de-costos/crearCentroDeCostos.html"
@method_decorator(login_required, name='dispatch')
#UpdateView
class EditarCentroDeCostos(TemplateView):
    template_name = "pages/finanzas/centro-de-costos/editarCentroDeCostos.html"



#------------------------------------------------------------------------------------------
    

#------------------------------- Vista de Proyectos con CRUD ------------------------------
@method_decorator(login_required, name='dispatch')
#ListView
class Proyectos(TemplateView):
    template_name = "pages/finanzas/proyectos/proyectos.html"

@method_decorator(login_required, name='dispatch')
#CreateView
class CrearProyectos(TemplateView):
    template_name = "pages/finanzas/proyectos/crearProyectos.html"
@method_decorator(login_required, name='dispatch')
#UpdateView
class EditarProyectos(TemplateView):
    template_name = "pages/finanzas/proyectos/editarProyectos.html"



#------------------------------------------------------------------------------------------
    
#---------------------------- Vista de Presupuestos de Centro de Costos con CRUD ------------------------------
@method_decorator(login_required, name='dispatch')   
#ListView
class PresupuestosCDC(TemplateView):
    template_name = "pages/finanzas/presupuestos/centro-de-costos/presupuestos.html"

@method_decorator(login_required, name='dispatch')
#CreateView
class CrearPresupuestosCDC(TemplateView):
    template_name = "pages/finanzas/presupuestos/centro-de-costos/crearPresupuestos.html"
@method_decorator(login_required, name='dispatch')
#UpdateView
class EditarPresupuestosCDC(TemplateView):
    template_name = "pages/finanzas/presupuestos/centro-de-costos/editarPresupuestos.html"

#------------------------------------------------------------------------------------------

#---------------------------- Vista de Presupuestos de Proyectos con CRUD ------------------------------
@method_decorator(login_required, name='dispatch')  
#ListView
class PresupuestosP(TemplateView):
    template_name = "pages/finanzas/presupuestos/proyectos/presupuestos.html"

@method_decorator(login_required, name='dispatch')
#CreateView
class CrearPresupuestosP(TemplateView):
    template_name = "pages/finanzas/presupuestos/proyectos/crearPresupuestos.html"
@method_decorator(login_required, name='dispatch')
#UpdateView
class EditarPresupuestosP(TemplateView):
    template_name = "pages/finanzas/presupuestos/proyectos/editarPresupuestos.html"



#------------------------------------------------------------------------------------------
    

#---------------------------- Vista de Compras con CRUD ------------------------------
@method_decorator(login_required, name='dispatch')    
#ListView
class Compra(TemplateView):
    template_name = "pages/finanzas/compra/compra.html"

@method_decorator(login_required, name='dispatch')
#CreateView
class CrearCompra(TemplateView):
    template_name = "pages/finanzas/compra/crearCompra.html"
@method_decorator(login_required, name='dispatch')
#UpdateView
class EditarCompra(TemplateView):
    template_name = "pages/finanzas/compra/editarCompra.html"

#------------------------------------------------------------------------------------------
    

#---------------------------- Vista de Cotizaciones de Compra con CRUD ------------------------------
    
@method_decorator(login_required, name='dispatch')
#ListView
class CotizacionesCompra(TemplateView):
    template_name = "pages/finanzas/compra/cotizaciones/cotizaciones.html"

@method_decorator(login_required, name='dispatch')
#CreateView
class CrearCotizacionesCompra(TemplateView):
    template_name = "pages/finanzas/compra/cotizaciones/crearCotizaciones.html"
@method_decorator(login_required, name='dispatch')
#UpdateView
class EditarCotizacionesCompra(TemplateView):
    template_name = "pages/finanzas/compra/cotizaciones/editarCotizaciones.html"
    

#------------------------------------------------------------------------------------------
    

#---------------------------- Vista de Ordenes de Compra con CRUD ------------------------------
@method_decorator(login_required, name='dispatch')   
#ListView
class OrdenesDeCompra(TemplateView):
    template_name = "pages/finanzas/compra/OrdenesDeCompra/ordenesDeCompra.html"

@method_decorator(login_required, name='dispatch')
#CreateView
class CrearOrdenesDeCompra(TemplateView):
    template_name = "pages/finanzas/compra/OrdenesDeCompra/crearOrdenesDeCompra.html"
@method_decorator(login_required, name='dispatch')
#UpdateView
class EditarOrdenesDeCompra(TemplateView):
    template_name = "pages/finanzas/compra/OrdenesDeCompra/editarOrdenesDeCompra.html"

#------------------------------------------------------------------------------------------
    
#---------------------------- Vista de Cotizaciones de Compra con CRUD ------------------------------
    
@method_decorator(login_required, name='dispatch')
#ListView
class FacturasCompra(TemplateView):
    template_name = "pages/finanzas/compra/facturas/facturas.html"
@method_decorator(login_required, name='dispatch')
#CreateView
class CrearFacturasCompra(TemplateView):
    template_name = "pages/finanzas/compra/facturas/crearFactura.html"
@method_decorator(login_required, name='dispatch')
#UpdateView
class EditarFacturasCompra(TemplateView):
    template_name = "pages/finanzas/compra/facturas/editarFactura.html"


#------------------------------------------------------------------------------------------
    
    
#---------------------------- Vista de Ventas con CRUD ------------------------------
@method_decorator(login_required, name='dispatch')   
#ListView
class Venta(TemplateView):
    template_name = "pages/finanzas/venta/venta.html"
@method_decorator(login_required, name='dispatch')
#CreateView
class CrearVenta(TemplateView):
    template_name = "pages/finanzas/venta/crearVenta.html"
@method_decorator(login_required, name='dispatch')
#UpdateView
class EditarVenta(TemplateView):
    template_name = "pages/finanzas/venta/editarVenta.html"

#------------------------------------------------------------------------------------------

#---------------------------- Vista de Cotizaciones de Venta con CRUD ------------------------------
    
@method_decorator(login_required, name='dispatch')
#ListView
class CotizacionesVenta(TemplateView):
    template_name = "pages/finanzas/venta/cotizaciones/cotizaciones.html"

@method_decorator(login_required, name='dispatch')
#CreateView
class CrearCotizacionesVenta(TemplateView):
    template_name = "pages/finanzas/venta/cotizaciones/crearCotizaciones.html"
@method_decorator(login_required, name='dispatch')
#UpdateView
class EditarCotizacionesVenta(TemplateView):
    template_name = "pages/finanzas/venta/cotizaciones/editarCotizaciones.html"


#------------------------------------------------------------------------------------------
    
#---------------------------- Vista de Ordenes de Venta con CRUD ------------------------------
@method_decorator(login_required, name='dispatch')  
#ListView
class OrdenesDeVenta(TemplateView):
    template_name = "pages/finanzas/venta/OrdenesDeVenta/ordenesDeVenta.html"

@method_decorator(login_required, name='dispatch')
#CreateView
class CrearOrdenesDeVenta(TemplateView):
    template_name = "pages/finanzas/venta/OrdenesDeVenta/crearOrdenesDeVenta.html"
@method_decorator(login_required, name='dispatch')
#UpdateView
class EditarOrdenesDeVenta(TemplateView):
    template_name = "pages/finanzas/venta/OrdenesDeVenta/editarOrdenesDeVenta.html"

#------------------------------------------------------------------------------------------
    
#---------------------------- Vista de Cotizaciones de Venta con CRUD ------------------------------
    
@method_decorator(login_required, name='dispatch')
#ListView
class FacturasVenta(TemplateView):
    template_name = "pages/finanzas/venta/facturas/facturas.html"
@method_decorator(login_required, name='dispatch')
#CreateView
class CrearFacturasVenta(TemplateView):
    template_name = "pages/finanzas/venta/facturas/crearFactura.html"
@method_decorator(login_required, name='dispatch')
#UpdateView
class EditarFacturasVenta(TemplateView):
    template_name = "pages/finanzas/venta/facturas/editarFactura.html"


#------------------------------------------------------------------------------------------
    
#---------------------------- Vista de Proveedores con CRUD ------------------------------
@method_decorator(login_required, name='dispatch')   
class Proveedor(TemplateView):
    template_name = "pages/finanzas/proveedores/proveedores.html"
@method_decorator(login_required, name='dispatch')
#CreateView
class CrearProveedor(TemplateView):
    template_name = "pages/finanzas/proveedores/crearProveedores.html"
@method_decorator(login_required, name='dispatch')
#UpdateView
class EditarProveedor(TemplateView):
    template_name = "pages/finanzas/proveedores/editarProveedores.html"

#------------------------------------------------------------------------------------------
    
#---------------------------- Vista de Impuestos con CRUD ------------------------------
@method_decorator(login_required, name='dispatch')    
class Impuestos(TemplateView):
    template_name = "pages/finanzas/impuestos/impuestos.html"
@method_decorator(login_required, name='dispatch')
#CreateView
class CrearImpuestos(TemplateView):
    template_name = "pages/finanzas/impuestos/crearImpuestos.html"
@method_decorator(login_required, name='dispatch')
#UpdateView
class EditarImpuestos(TemplateView):
    template_name = "pages/finanzas/impuestos/editarImpuestos.html"

#------------------------------------------------------------------------------------------
    
#---------------------------- Vista de Flujo de Caja con CRUD ------------------------------
@method_decorator(login_required, name='dispatch')   
class FlujoDeCaja(TemplateView):
    template_name = "pages/finanzas/flujo-de-caja/flujoDeCaja.html"
@method_decorator(login_required, name='dispatch')
#CreateView
class CrearFlujoDeCaja(TemplateView):
    template_name = "pages/finanzas/flujo-de-caja/crearFlujoDeCaja.html"
@method_decorator(login_required, name='dispatch')
#UpdateView
class EditarFlujoDeCaja(TemplateView):
    template_name = "pages/finanzas/flujo-de-caja/editarFlujoDeCaja.html"


#---------------------------- Vista de Contabilidad ------------------------------
    
@method_decorator(login_required, name='dispatch')
#ListView
class CuentasContables(TemplateView):
    template_name = "pages/finanzas/contabilidad/cuentasContables/cuentasContables.html"
@method_decorator(login_required, name='dispatch')
#CreateView
class CrearCuentasContables(TemplateView):
    template_name = "pages/finanzas/contabilidad/cuentasContables/crearCuentasContables.html"
@method_decorator(login_required, name='dispatch')
#UpdateView
class EditarCuentasContables(TemplateView):
    template_name = "pages/finanzas/contabilidad/cuentasContables/editarCuentasContables.html"