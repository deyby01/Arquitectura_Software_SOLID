# Módulos de bajo nivel (detalles de implementación)
class EmailSender:
    def enviar_email(self, destinatario, mensaje):
        print(f"Enviando email a {destinatario}: {mensaje}")

class SMSSender:
    def enviar_sms(self, destinatario, mensaje):
        print(f"Enviando SMS a {destinatario}: {mensaje}")


# Módulo de alto nivel (lógica de negocio)
class Notificador:
    def __init__(self):
        # ¡Problema! Fuerte acoplamiento con las clases concretas.
        self.email_sender = EmailSender()
        self.sms_sender = SMSSender()

    def enviar_notificacion(self, destinatario, mensaje, modo):
        if modo == "email":
            self.email_sender.enviar_email(destinatario, mensaje)
        elif modo == "sms":
            self.sms_sender.enviar_sms(destinatario, mensaje)
        else:
            raise ValueError("Modo no soportado")

# Uso
notificador = Notificador()
notificador.enviar_notificacion("test@example.com", "Hola Mundo", "email")
notificador.enviar_notificacion("123456789", "Hola Mundo", "sms")