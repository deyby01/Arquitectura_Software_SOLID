# codigo_ejemplo/notificacion_mala.py

class Notificacion:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def enviar(self):
        raise NotImplementedError("Este método debe ser sobrescrito por una subclase.")

class NotificacionSMS(Notificacion):
    def enviar(self):
        print(f"Enviando SMS: {self.mensaje}")

class NotificacionEmail(Notificacion):
    def enviar(self):
        # Lógica para enviar email
        print(f"Enviando Email: {self.mensaje}")

class NotificacionPush(Notificacion):
    def enviar(self):
        # Esto viola LSP. No tiene un "mensaje" simple como las otras.
        # ¿Qué pasa si el cliente espera que el método enviar() solo
        # tome el mensaje del constructor?
        raise ValueError("El tipo de notificación Push requiere un token de dispositivo, no solo un mensaje.")

# Función cliente que procesa una lista de notificaciones
def procesar_notificaciones(notificaciones: list[Notificacion]):
    for notificacion in notificaciones:
        try:
            notificacion.enviar()
        except Exception as e:
            print(f"Error al enviar la notificación: {e}")

# Uso
notis = [
    NotificacionSMS("Tu pedido ha sido enviado."),
    NotificacionEmail("Factura de tu compra."),
    NotificacionPush("Un nuevo mensaje en tu chat."), # ¡Esto romperá el código!
]

procesar_notificaciones(notis)