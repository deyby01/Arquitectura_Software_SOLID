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
    def __init__(self, mensaje):
        super().__init__(mensaje)
        
    def enviar(self):
        print(f"Enviando Push: {self.mensaje}")


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
    NotificacionPush("Un nuevo mensaje en tu chat."), 
]

procesar_notificaciones(notis)