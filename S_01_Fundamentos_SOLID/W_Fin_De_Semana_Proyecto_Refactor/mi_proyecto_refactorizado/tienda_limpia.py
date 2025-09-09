from abc import ABC, abstractmethod
import time

class IProducto(ABC):
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

class IProductoFisico(IProducto):
    def __init__(self, nombre: str, precio: float, peso_kg: float):
        super().__init__(nombre, precio)
        self.peso_kg = peso_kg


class Libro(IProductoFisico):
    pass

class CursoOnline(IProducto):
    pass


# Interfaz para los metodos de pago
class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto: float):
        pass

# Tipos de pago comunes
class PagoConTarjeta(MetodoPago):
    def procesar_pago(self, monto: float):
        print(f"Procesando ${monto} con tarjeta de crédito...")
        time.sleep(3)
        print("Pago con tarjeta Exitoso.")

    
class PagoConPayPal(MetodoPago):
    def procesar_pago(self, monto: float):
        print(f"Procesando ${monto} con PayPal...")
        time.sleep(3)
        print("Pago con PayPal Exitoso.")

class PagoConCripto(MetodoPago):
    def procesar_pago(self, monto: float):
        print(f"Iniciando Transferencia de ${monto} en BTC...")
        time.sleep(5) 
        print("Transferencia confirmada en la red. Pago con cripto exitoso.")
    

class INotificacion(ABC):
    @abstractmethod
    def notificar(self, destinatario: str, mensaje: str):
        pass

class MensajeroEmail(INotificacion):
    def notificar(self, destinatario: str, mensaje: str):
        print(f"Enviando mensaje a {destinatario} via Email: {mensaje}")

class MensajeroSMS(INotificacion):
    def notificar(self, destinatario: str, mensaje: str):
        print(f"Enviando mensaje a {destinatario} via SMS: {mensaje}")


class ServicioDeNotificacion:
    def __init__(self, mensajero: INotificacion):
        self.mensajero = mensajero

    def enviar_confirmacion_de_orden(self, destinatario: str, orden: 'Orden'):
        total_orden = orden.calcular_total()
        mensaje = f"Gracias por tu compra. Tu orden por un total de ${total_orden:.2f} ha sido procesada."
        self.mensajero.notificar(destinatario, mensaje)

class Orden:
    def __init__(self):
        self.items = []

    def agregar_item(self, producto: IProducto, cantidad: int):
        item = {"producto": producto, "cantidad": cantidad}
        self.items.append(item)
        print(f"Añadido: {producto.nombre} x {cantidad}")

    def calcular_total(self) -> float:
        total = 0
        for item in self.items:
            producto = item["producto"]
            cantidad = item["cantidad"]
            total += producto.precio * cantidad
        return total

    def calcular_peso_total(self) -> float:
        peso_total = 0
        for item in self.items:
            producto = item["producto"]
            if isinstance(producto, IProductoFisico):
                cantidad = item["cantidad"]
                peso_total += producto.peso_kg * cantidad
        
        return peso_total

    def procesar_pago(self, metodo_pago: MetodoPago):
        total = self.calcular_total()
        metodo_pago.procesar_pago(total)

# --- FLUJO DE EJECUCIÓN ---
if __name__ == "__main__":
    print("--- Iniciando nueva orden ---")
    mi_orden = Orden()
    
    libro = Libro(nombre="El Principito", precio=15.99, peso_kg=0.5)
    curso = CursoOnline(nombre="Curso de SOLID", precio=49.99)

    mi_orden.agregar_item(libro, 2)
    mi_orden.agregar_item(curso, 1)
    
    print("\n--- Calculando totales ---")
    print(f"Total de la orden: ${mi_orden.calcular_total():.2f}")
    print(f"Peso total del envío: {mi_orden.calcular_peso_total():.2f} kg")

    print("\n--- Procesando pago ---")
    pago_tarjeta = PagoConTarjeta()
    mi_orden.procesar_pago(pago_tarjeta)

    print("\n--- Enviando notificación ---")
    mensajero_email = MensajeroEmail()
    servicio_notificacion = ServicioDeNotificacion(mensajero_email)
    servicio_notificacion.enviar_confirmacion_de_orden("cliente@email.com", mi_orden)