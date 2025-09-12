from django.db import models

class OrdenModel(models.Model):
    """
    Este es el modelo que representa nuestra tabla en la base de datos.
    Es un "detalle de implementación" de bajo nivel.
    No es nuestro modelo de dominio "Orden"
    """
    # Usamos un campo JSON para guardar los items de la orden.
    # Es una forma sencilla de almacenar datos estructurados sin crear otra tabla.
    items = models.JSONField()

    # Podriamos añadir mas campos que solo le importan a la base de datos,
    # como la fecha de creacion.
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Orden #{self.id}"