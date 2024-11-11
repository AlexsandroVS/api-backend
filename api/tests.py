from django.test import TestCase, Client  # type: ignore
from django.urls import reverse  # type: ignore
from api.models import Producto, Venta, Proveedor, Categoria, Factura, Cliente, Persona  # Asegúrate de importar los modelos necesarios
from decimal import Decimal

class ReporteVentasTest(TestCase):
    def setUp(self):
        # Configura el cliente para realizar solicitudes
        self.client = Client()

        # Crea los objetos necesarios para las pruebas
        self.proveedor = Proveedor.objects.create(nombre="Proveedor A", direccion="Direccion A", telefono="123456789", email="proveedor@example.com")
        self.categoria = Categoria.objects.create(nombre="Categoria A")
        self.producto = Producto.objects.create(nombre="Producto A", descripcion="Descripcion A", presentacion="Presentacion A", fecha_vencimiento="2024-12-31", proveedor=self.proveedor, categoria=self.categoria)
        self.producto_b = Producto.objects.create(nombre="Producto B", descripcion="Descripcion B", presentacion="Presentacion B", fecha_vencimiento="2024-12-31", proveedor=self.proveedor, categoria=self.categoria)

        # Crea un cliente
        self.cliente = Cliente.objects.create(persona=Persona.objects.create(nombre="Cliente A", apellidos="Apellido A", direccion="Direccion Cliente A", correo="cliente@example.com", telefono="987654321", identificacion="12345678"))

        # Crea una factura asociando al cliente
        self.factura = Factura.objects.create(cantidad=5, empleado=None, cliente=self.cliente, fecha="2024-10-17")

        # Crea algunas ventas asociadas a la factura
        Venta.objects.create(factura=self.factura, producto=self.producto, cantidad=5, precio_unitario=Decimal('10.00'), total=Decimal('50.00'))
        Venta.objects.create(factura=self.factura, producto=self.producto_b, cantidad=3, precio_unitario=Decimal('20.00'), total=Decimal('60.00'))

    def test_reporte_ventas(self):
        response = self.client.get(reverse('reporte-ventas'))  # Asegúrate de que este nombre coincida con el de tus urls

        # Verifica que la respuesta sea un PDF
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')

        # Verifica que el contenido del PDF sea el esperado
        self.assertIn(b'Reporte de Ventas', response.content)  # Verifica que el encabezado esté presente
        self.assertIn(b'Venta #1: Producto A - 5 unidades', response.content)  # Verifica que la venta A esté presente
        self.assertIn(b'Venta #2: Producto B - 3 unidades', response.content)  # Verifica que la venta B esté presente
