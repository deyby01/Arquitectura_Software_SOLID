from abc import ABC, abstractmethod

class IMensajero(ABC):
    @abstractmethod
    def enviar(self, destinatario: str, mensaje: str) -> None:
        pass

class EmailSender(IMensajero):
    def enviar(self, destinatario: str, mensaje: str) -> None:
        print(f"Enviando email a {destinatario}: {mensaje}")

class SMSSender(IMensajero):
    def enviar(self, destinatario: str, mensaje: str) -> None:
        print(f"Enviando SMS a {destinatario}: {mensaje}")

# Implementando nueva clase
class SlackSender(IMensajero):
    def enviar(self, destinatario: str, mensaje: str) -> None:
        print(f"Enviando Slack a {destinatario}: {mensaje}")

class Notificador:
    def __init__(self, mensajero: IMensajero):
        self.mensajero = mensajero

    def enviar_notificacion(self, destinatario: str, mensaje: str) -> None:
        envio = self.mensajero.enviar(destinatario, mensaje)


# Area de pruebas
if __name__ == "__main__":
    email_sender = EmailSender()
    notificador_email = Notificador(email_sender)
    notificador_email.enviar_notificacion("test@example.com", "Hola Mundo desde Email")

    sms_sender = SMSSender()
    notificador_sms = Notificador(sms_sender)
    notificador_sms.enviar_notificacion("123456789", "Hola Mundo desde SMS")

    # Usando nueva clase, sin modificar Notificador()
    slack_sender = SlackSender()
    notificador_slack = Notificador(slack_sender)
    notificador_slack.enviar_notificacion("slack-channel@example.com", "Hola Mundo desde SLACK")