### 🧠 Día 17: Inyección de Dependencias en la Práctica

El problema que vamos a resolver es: ¿cómo una vista de Django (`views.py`) obtiene una instancia de `OrdenService` que ya venga configurada con el `DjangoOrdenRepository` que necesita?

No queremos que la vista haga esto:

```python
# ¡MAL! La vista no debería saber qué repositorio usar.
from tienda.adapters.django_orm import DjangoOrdenRepository
from tienda.application.services import OrdenService

def mi_vista(request):
    repositorio = DjangoOrdenRepository()
    servicio = OrdenService(repositorio)
    # ...
```

Esto acopla la vista a una implementación concreta del repositorio y viola el principio de que los detalles de "cableado" deben estar en un solo lugar.

**La Solución:** Usaremos un **Contenedor de Inyección de Dependencias**. Es un componente centralizado cuyo único trabajo es saber cómo construir nuestros servicios y sus dependencias.

#### Flash Recordatorio ⚡️: Principio de Inyección de Dependencias (DIP)

La Inyección de Dependencias (DI) es la técnica que usamos para satisfacer el **principio** del mismo nombre. En lugar de que un servicio cree sus propias dependencias, se las "inyectamos" desde fuera. Un contenedor automatiza este proceso.