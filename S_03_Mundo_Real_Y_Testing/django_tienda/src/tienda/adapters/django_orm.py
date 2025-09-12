from src.tienda.domain.models import Orden, Libro, CursoOnline, IProducto
from src.tienda.domain.ports import IOrdenRepository
from src.tienda.domain.exceptions import OrdenNoEncontradaError
from api.models import OrdenModel

class DjangoOrdenRepository(IOrdenRepository):

    def _mapear_a_modelo(self, orden: Orden) -> dict:
        """
        Traduce un objeto Orden del dominio a un diccionario para el modelo de Django.
        """
        items_para_db = []
        for item in orden.items:
            producto = orden.items
            datos_producto = {
                "nombre": producto.nombre,
                "precio": producto.precio,
                "cantidad": item["cantidad"]
            }

            # Verificamos el tipo de producto
            if isinstance(producto, Libro):
                datos_producto["tipo_producto"] = "libro"
                datos_producto["peso_kg"] = producto.peso_kg
            elif isinstance(producto, CursoOnline):
                datos_producto["tipo_producto"] = "curso_online"

            items_para_db.append(datos_producto)

        return {"items": items_para_db}

    def _mapear_a_dominio(self, orden_model: OrdenModel) -> Orden:
        """
        Traduce un objeto OrdenModel de Django a un objeto Orden del dominio.
        """
        orden = Orden(id=orden_model.id)

        for item in orden_model.items:
            if item["tipo_producto"] == "libro":
                producto = Libro(item["nombre"], item["precio"], item["peso_kg"])
            elif item["tipo_producto"] == "curso_online":
                producto = CursoOnline(item["nombre"], item["precio"])
            
            orden.agregar_item(producto, item["cantidad"])
        
        return orden

    def guardar(self, orden: 'Orden'):
        datos_modelo = self._mapear_a_modelo(orden)

        # El ORM de Django crea un registro si el id no existe, o lo actualiza si existe.
        orden_modelo, _ = OrdenModel.objects.update_or_create(
            id=orden.id,
            defaults=datos_modelo
        )
        # Actualizamos el id en nuestro objeto de dominio por si era una nueva orden
        orden.id = orden_modelo.id

    def buscar_por_id(self, orden_id: int) -> 'Orden':
        try:
            orden_modelo = OrdenModel.objects.get(id=orden_id)
            return self._mapear_a_dominio(orden_modelo)
        except OrdenModel.DoesNotExist:
            raise OrdenNoEncontradaError(f"Orden con ID {orden_id} no encontrada.")
        