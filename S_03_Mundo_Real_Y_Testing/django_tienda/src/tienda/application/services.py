from tienda.domain.models import Orden, IProducto
from tienda.domain.ports import IOrdenRepository, INotificacion, MetodoPago
from tienda.domain.exceptions import OrdenNoEncontradaError

class OrdenService:
    def __init__(self, orden_repository: IOrdenRepository):
        # Inyectamos la dependencia del repositorio.
        # el servicio no sabe ni le importa la implementacion concreta
        self.orden_repository = orden_repository

    def crear_nueva_orden(self) -> Orden:
        # Creamos una instancia de la clase orden
        orden = Orden()
        # Usamos el repositorio para guardarla
        self.orden_repository.guardar(orden)
        # Retornamos la orden creada
        return orden

    def agregar_item_a_orden(self, orden_id: int, producto: IProducto, cantidad: int) -> Orden:
        try:
            # Confiamos en que el repositorio encontrara la orden o lanzara la excepcion
            orden = self.orden_repository.buscar_por_id(orden_id)
            # agregamos el o los items
            orden.agregar_item(producto, cantidad)
            # Guardamos la orden actualizada
            self.orden_repository.guardar(orden)
            print(f"Item añadido a la orden {orden_id}. Nuevo total: ${orden.calcular_total():.2f}")
            return orden
        except OrdenNoEncontradaError as e:
            print(f"Error en el servicio: {e}")
            raise e

    def procesar_pago_de_orden(self, orden_id: int, metodo_pago: MetodoPago) -> Orden:
        try:
            # Confiamos en que el repositorio encontrara la orden o lanzara la excepcion
            orden = self.orden_repository.buscar_por_id(orden_id)
            # procesamos el pago
            metodo_pago.procesar_pago(orden.calcular_total())
            # Guardamos la orden actualizada
            self.orden_repository.guardar(orden)
            return orden
        except OrdenNoEncontradaError as e:
            print(f"Error en el servicio: {e}")
            raise e


class ServicioDeNotificacion:
    def __init__(self, mensajero: INotificacion):
        self.mensajero = mensajero

    def enviar_confirmacion_de_orden(self, destinatario: str, orden: 'Orden'):
        total = orden.calcular_total()
        mensaje = f"Gracias por tu compra. Tu orden #{orden.id} por un total de ${total:.2f} ha sido confirmada."
        self.mensajero.notificar(destinatario, mensaje)