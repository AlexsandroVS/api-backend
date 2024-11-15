# v1/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PersonaViewSet, EmpleadoViewSet, ClienteViewSet, ProveedorViewSet, 
    CategoriaViewSet, ProductoViewSet, MedicamentoViewSet, RegisterView,
    FacturaViewSet, VentaViewSet, PedidoViewSet, DetallePedidoViewSet, CurrentUserView, 
    landing_page, RegisterClienteView  # Agregamos el RegisterClienteView
)

router = DefaultRouter()
router.register(r'personas', PersonaViewSet)
router.register(r'empleados', EmpleadoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'proveedores', ProveedorViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'medicamentos', MedicamentoViewSet)
router.register(r'facturas', FacturaViewSet)
router.register(r'ventas', VentaViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'detalles-pedido', DetallePedidoViewSet)

urlpatterns = [
    path('', landing_page, name='landing_page'),  # Ruta para la landing page en la raíz de la API
    path('v1/', include(router.urls)),  # Rutas de la API con prefijo v1
    path('v1/register/', RegisterView.as_view(), name='register'),  # Ruta para registrar usuario
    path('v1/current-user/', CurrentUserView.as_view(), name='current_user'),  # Ruta para usuario actual
    path('v1/register_cliente/', RegisterClienteView.as_view(), name='register_cliente'),  # Ruta para registrar cliente
]
