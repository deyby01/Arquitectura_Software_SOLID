## ✍️ Tu Misión de Hoy
Tu misión es crear un contenedor de dependencias que ensamble nuestro `OrdenService` y luego usarlo en una vista de Django.

### Paso 1: Instalar una Librería de DI
Para hacer esto de manera profesional, usaremos una librería muy popular llamada `dependency-injector`.

Acción: En tu terminal (con el entorno virtual activado), ejecuta:
```bash
pip install dependency-injector
```

### Paso 2: Crear el Contenedor

Crearemos un archivo central para definir todas nuestras dependencias.

**Acción:** En tu app `api`, crea un nuevo archivo llamado `containers.py` y pega el siguiente código:

```python
# api/containers.py
from dependency_injector import containers, providers
from tienda.application.services import OrdenService
from tienda.adapters.django_orm import DjangoOrdenRepository

class Container(containers.DeclarativeContainer):
    
    # El 'wiring' nos permite inyectar dependencias en funciones o vistas de Django
    wiring_config = containers.WiringConfiguration(modules=[".views"])
    
    # --- Adaptadores (Bajo Nivel) ---
    # Definimos cómo construir nuestro repositorio.
    # El provider.Factory significa que se creará una nueva instancia cada vez que se pida.
    orden_repository = providers.Factory(
        DjangoOrdenRepository
    )
    
    # --- Servicios (Alto Nivel) ---
    # Definimos cómo construir nuestro servicio de órdenes.
    # Fíjate cómo le decimos que su 'orden_repository' será el que definimos arriba.
    orden_service = providers.Factory(
        OrdenService,
        orden_repository=orden_repository
    )
```
Este archivo es ahora la "receta" centralizada para construir tus servicios.

### Paso 3: Usar el Contenedor en una Vista

Ahora, le pediremos al contenedor que nos dé un servicio listo para usar dentro de una vista de Django.

**Acción:** Abre el archivo `api/views.py` y reemplaza su contenido con esto:

```python
# api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dependency_injector.wiring import inject, Provide

from .containers import Container
from tienda.application.services import OrdenService

# Usamos DRF para crear una vista basada en clase
class OrdenView(APIView):
    
    # La magia ocurre aquí. El decorador @inject le dice al contenedor
    # que debe inyectar las dependencias que declaremos.
    @inject
    def post(self, 
             request, 
             orden_service: OrdenService = Provide[Container.orden_service]):
        """
        Crea una nueva orden.
        """
        print("VISTA: Petición POST recibida para crear orden.")
        
        # 1. El 'orden_service' que recibimos ya está completamente configurado
        #    con su DjangoOrdenRepository, listo para usar.
        nueva_orden = orden_service.crear_nueva_orden()
        
        print(f"VISTA: Servicio creó la orden con ID #{nueva_orden.id}")
        
        # 2. Devolvemos una respuesta HTTP exitosa.
        return Response(
            {"id": nueva_orden.id, "mensaje": "Orden creada exitosamente."},
            status=status.HTTP_201_CREATED
        )
```

### Paso 4: Conectar la URL

Finalmente, necesitamos una URL para poder llamar a nuestra vista.

**1.** En la carpeta `api`, crea un nuevo archivo `urls.py`.

**2.** Pega esto en `api/urls.py`:

```python
from django.urls import path
from .views import OrdenView

urlpatterns = [
    path('ordenes/', OrdenView.as_view(), name='crear-orden'),
]
```

**3.** Abre `config/urls.py` y haz que incluya las URLs de tu app `api`:

```python
from django.contrib import admin
from django.urls import path, include # <-- Añade 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), # <-- Añade esta línea
]
```

#### ¡Pruébalo!

**1.** Corre el servidor: `python manage.py runserver`

**2.** Abre tu navegador o una herramienta como Postman y haz una petición **POST** a `http://127.0.0.1:8000/api/ordenes/`.

**3.** Revisa la terminal donde corre el servidor. Deberías ver los `print` de la vista, del servicio y del ORM, ¡y una nueva orden se habrá creado en tu base de datos `db.sqlite3`!

Has conectado con éxito una vista de Django a tu núcleo de negocio de una manera limpia, desacoplada y profesional.