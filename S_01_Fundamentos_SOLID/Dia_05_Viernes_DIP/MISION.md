# ✍️ Misión del Día 5: Refactorizar aplicando DIP

Tu misión hoy es tomar un sistema de notificaciones que está fuertemente acoplado y refactorizarlo para que siga el Principio de Inversión de Dependencias.

### 1. Código Inicial

Ve a la carpeta `Dia_05_Viernes_DIP/`. Crea un archivo llamado `notificador_malo.py` dentro de la carpeta `codigo_ejemplo/` y pega el siguiente código:

```python
# codigo_ejemplo/notificador_malo.py

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
```

----

### Tu Tarea
- **1** - Analiza el código y explica por qué la clase Notificador viola el DIP. ¿De qué detalles de bajo nivel depende?

- **2** - Crea un nuevo archivo en tu carpeta mi_solucion/ llamado notificador_bueno.py.

- **3** - Refactoriza el código siguiendo el patrón que aprendiste en la teoría:

- **4** - Crea una abstracción (una ABC) llamada IMensajero con un único método enviar(destinatario, mensaje).

- **5** - Haz que las clases de bajo nivel (EmailSender y SMSSender) implementen esta nueva interfaz. Tendrás que adaptar sus métodos para que coincidan con el de la interfaz.

- **6** - Modifica la clase de alto nivel Notificador. En lugar de crear instancias de los senders, debe recibirlas en su constructor (Inyección de Dependencias).

- **7** - El método enviar_notificacion del Notificador ya no debería tener un if/elif. Debería simplemente usar el mensajero que se le inyectó.

- **8** - Demuestra que tu sistema es flexible. Crea una nueva clase SlackSender que implemente IMensajero y úsala con tu Notificador sin modificar la clase Notificador.