import sys
import os

# Esto es un truco para que python encuentre nuestros modulos en la carpeta src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Imports de todas nuestras piezas

# Adaptadores
from tienda.adapters.repositories import InMemoryOrdenRepository
# Servicios de aplicacion
from tienda.application.services import OrdenService, ServicioDeNotificacion
# Modelos de dominio (para crear productos)
from tienda.domain.models import Libro, CursoOnline
# Implementaciones de puertos (para pago y notificacion)
from tienda.adapters.gateways import PagoConTarjeta, MensajeroEmail


# Bloque principal de ejecucion
if __name__ == "__main__":

    print("--- 🚀 INICIANDO APLICACIÓN 🚀 ---")

    # "CABLEADO" / Inyeccion de dependencias
    # Creamos las instancias de nuestros adaptadores (la tecnologia concreta)
    orden_repo = InMemoryOrdenRepository()
    notificador_email = MensajeroEmail()
    metodo_pago = PagoConTarjeta()

    # Creamos las instancias de nuestros servicios, inyectando los adaptadores
    orden_service = OrdenService(orden_repo)
    servicio_notificacion = ServicioDeNotificacion(notificador_email)

    print("--- Dependencias inyectadas. Servicios listos. ---\n")

    # --- 4. SIMULACIÓN DE UN CASO DE USO ---
    print("--- 🛒 Flujo de compra de un cliente ---")

    # El cliente llega, creamos una nueva orden
    nueva_orden = orden_service.crear_nueva_orden()
    print(f"Orden #{nueva_orden.id} creada.")

    # El cliente añade productos a su orden
    libro = Libro(nombre="Clean Architecture", precio=25.50, peso_kg=0.8)
    curso = CursoOnline(nombre="Curso de Arquitectura Hexagonal", precio=79.99)

    orden_actualizada = orden_service.agregar_item_a_orden(
        orden_id=nueva_orden.id,
        producto=libro,
        cantidad=1
    )
    orden_actualizada = orden_service.agregar_item_a_orden(
        orden_id=nueva_orden.id,
        producto=curso,
        cantidad=1
    )

    # El cliente procede al pago
    orden_service.procesar_pago_de_orden(
        orden_id=orden_actualizada.id,
        metodo_pago=metodo_pago
    )

    # El sistema envia una confirmacion 
    servicio_notificacion.enviar_confirmacion_de_orden(
        destinatario="cliente@email.com",
        orden=orden_actualizada
    )

    print("\n--- ✅ Flujo de compra completado con éxito. ---")