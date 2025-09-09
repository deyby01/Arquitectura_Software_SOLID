# codigo_ejemplo/tienda_sucia.py
import smtplib
from email.mime.text import MIMEText

# --- Clases que representan los productos ---

class Producto:
    def __init__(self, nombre: str, precio: float, peso_kg: float):
        self.nombre = nombre
        self.precio = precio
        self.peso_kg = peso_kg

# Un producto digital no tiene peso, pero nos vemos forzados a ponerle uno.
class ProductoDigital(Producto):
    def __init__(self, nombre: str, precio: float):
        super().__init__(nombre, precio, 0) # Peso es 0

# --- La clase principal que hace de todo ---

class Orden:
    def __init__(self):
        self.items = []
        self.estado = "abierta"
        self.total = 0
        self.peso_total_kg = 0

    def agregar_item(self, producto: Producto, cantidad: int):
        item = {"producto": producto, "cantidad": cantidad}
        self.items.append(item)
        print(f"Añadido: {cantidad} x {producto.nombre}")

    def calcular_totales(self):
        self.total = 0
        self.peso_total_kg = 0
        for item in self.items:
            producto = item["producto"]
            cantidad = item["cantidad"]
            self.total += producto.precio * cantidad
            self.peso_total_kg += producto.peso_kg * cantidad
        
        # Añadir coste de envío basado en el peso
        if self.peso_total_kg > 0:
            self.total += self.peso_total_kg * 1.5 # $1.5 por kg
        
        print(f"Total a pagar: ${self.total:.2f}")
        print(f"Peso total del envío: {self.peso_total_kg:.2f} kg")

    def procesar_pago(self, tipo_pago: str, tarjeta_info: str = None):
        print(f"Procesando pago con '{tipo_pago}'...")
        
        # Violación de OCP: si queremos añadir un nuevo método de pago, hay que modificar esta clase.
        if tipo_pago == "tarjeta":
            if not tarjeta_info:
                raise ValueError("Se requiere información de la tarjeta.")
            print(f"Cobrando a la tarjeta {tarjeta_info}...")
            # Lógica de la pasarela de pago...
        elif tipo_pago == "paypal":
            print(f"Redirigiendo a PayPal...")
            # Lógica de la API de PayPal...
        else:
            raise ValueError("Método de pago no soportado.")
        
        self.estado = "pagada"
        print("¡Pago completado con éxito!")
    
    def enviar_confirmacion_email(self, destinatario: str):
        if self.estado != "pagada":
            print("No se puede enviar la confirmación. La orden no ha sido pagada.")
            return

        # Violación de SRP y DIP: La clase Orden no debería saber cómo enviar emails.
        # Está acoplada a la implementación concreta de smtplib.
        print(f"Enviando confirmación a {destinatario}...")
        
        remitente = "no-reply@tienda.com"
        asunto = f"Confirmación de tu orden"
        cuerpo = f"Gracias por tu compra. Tu orden por un total de ${self.total:.2f} ha sido procesada."
        
        # Simulación del envío de email (esto requeriría un servidor SMTP real)
        # msg = MIMEText(cuerpo)
        # msg['Subject'] = asunto
        # msg['From'] = remitente
        # msg['To'] = destinatario
        # with smtplib.SMTP('smtp.example.com') as server:
        #     server.send_message(msg)
            
        print("Email de confirmación enviado.")

# --- Flujo de ejecución ---

if __name__ == "__main__":
    # Crear productos
    libro = Producto(nombre="El Principito", precio=15.99, peso_kg=0.5)
    curso_online = ProductoDigital(nombre="Curso de Python", precio=49.99)

    # Crear una orden
    mi_orden = Orden()
    
    # Agregar items
    mi_orden.agregar_item(libro, 2)
    mi_orden.agregar_item(curso_online, 1)

    # Procesar la orden
    mi_orden.calcular_totales()
    
    try:
        mi_orden.procesar_pago("tarjeta", "1234-5678-9012-3456")
        mi_orden.enviar_confirmacion_email("cliente@email.com")
    except ValueError as e:
        print(f"Error: {e}")