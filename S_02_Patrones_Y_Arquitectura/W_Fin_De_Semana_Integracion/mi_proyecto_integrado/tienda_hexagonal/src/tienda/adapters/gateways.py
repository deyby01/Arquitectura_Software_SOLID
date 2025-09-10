import time
from tienda.domain.ports import MetodoPago, INotificacion

class PagoConTarjeta(MetodoPago):
    def procesar_pago(self, monto: float):
        print(f"ADAPTADOR: Procesando ${monto:.2f} con tarjeta de credito...")
        time.sleep(2)
        print("ADAPTADOR: Pago con tarjeta exitoso.")

class PagoConPayPal(MetodoPago):
    def procesar_pago(self, monto: float):
        print(f"ADAPTADOR: Procesando ${monto:.2f} con PayPal...")
        time.sleep(3)
        print("ADAPTADOR: Pago con PayPal exitoso.")

class PagoConCripto(MetodoPago):
    def procesar_pago(self, monto: float):
        print(f"ADAPTADOR: Procesando ${monto:.2f} con criptomoneda...")
        time.sleep(4)
        print("ADAPTADOR: Pago con criptomoneda exitoso.")

class MensajeroEmail(INotificacion):
    def notificar(self, destinatario: str, mensaje: str):
        print(f"ADAPTADOR: Enviando email a {destinatario}: {mensaje}")

class MensajeroSMS(INotificacion):
    def notificar(self, destinatario: str, mensaje: str):
        print(f"ADAPTADOR: Enviando SMS a {destinatario}: {mensaje}")