from tienda.domain.ports import IOrdenRepository
from tienda.domain.models import Orden
from tienda.domain.exceptions import OrdenNoEncontradaError

class InMemoryOrdenRepository(IOrdenRepository):
    def __init__(self):
        # Usamos el diccionario para simular la tabla de la DB
        self._ordenes = {}
        # Un contador para simular los IDs autoincrementales
        self._next_id = 1

    def guardar(self, orden: Orden):
        # Si la orden no tiene ID, es una nueva
        if not orden.id:
            # Asignamos un ID a la orden
            orden.id = self._next_id
            # Guardamos la orden en el diccionario
            self._ordenes[self._next_id] = orden
            # Incrementamos el contador para el próximo ID
            self._next_id += 1
            # Devolvemos la orden guardada
            return orden
        else:
            # Si la orden tiene ID, es una actualización
            # Actualizamos la orden en el diccionario
            self._ordenes[orden.id] = orden
            # Devolvemos la orden actualizada
            return orden

    def buscar_por_id(self, orden_id: int) -> Orden:
        # Buscamos la orden por ID en el diccionario
        orden = self._ordenes.get(orden_id)
        # Si no se encuentra, lanzamos una excepción
        if not orden:
            raise OrdenNoEncontradaError(f"Orden con ID {orden_id} no encontrada")
        # Devolvemos la orden encontrada
        return orden
