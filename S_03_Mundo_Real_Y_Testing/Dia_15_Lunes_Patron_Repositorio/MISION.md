✍️ Misión de Hoy: Montar el Entorno Profesional
Hoy no escribiremos lógica de negocio, sino que haremos el trabajo de infraestructura para montar un proyecto profesional desde cero.

---

Paso 1: Crear el Espacio de Trabajo
En tu computadora, crea una nueva carpeta para todo el proyecto, llámala django_tienda. Abre tu terminal dentro de esa carpeta, la carpeta estara al nivel de la semana 3 ya que vamos a trabajar sobre ella toda la semana.

Paso 2: Crear un Entorno Virtual
Un entorno real siempre empieza con un entorno virtual para aislar las dependencias del proyecto.

```bash
# 1. Crea el entorno virtual (la carpeta se llamará 'venv')
python -m venv venv
# 2. Activalo
.\venv\Scripts\activate
```
Verás (venv) al principio de la línea de tu terminal. Esto significa que estás dentro del entorno.

Paso 3: Instalar las Dependencias
Ahora, instalemos Django y Django REST Framework.

```bash
pip install django djangorestframework
```

Paso 4: Iniciar el Proyecto y la App de Django
Vamos a crear la estructura de Django.

```bash
# 1. Crea el proyecto. 'config' es para los ajustes, '.' lo crea en la carpeta actual.
django-admin startproject config .

# 2. Crea la app que contendrá nuestros adaptadores de API.
python manage.py startapp api
```

Paso 5: Integrar Nuestro Núcleo Hexagonal
Este es el paso clave. Ve a la carpeta de tu proyecto tienda_hexagonal que ya construimos, y copia la carpeta src/tienda completa y pégala dentro de la raíz de tu nuevo proyecto django_tienda.

¡Listo! Tu Estructura Profesional
Al final de estos pasos, tu proyecto django_tienda tendrá esta estructura:

![estructura de carpetas](django_tienda_structure.png)

---

Tu Tarea de Hoy
Sigue los 5 pasos anteriores para crear y configurar tu proyecto django_tienda.

Abre config/settings.py y añade 'api' y 'rest_framework' a tu lista de INSTALLED_APPS.

Ejecuta python manage.py runserver en tu terminal para confirmar que el proyecto de Django se inicia sin errores.

Una vez que tengas el servidor de desarrollo de Django corriendo, habrás completado la configuración inicial. Mañana, empezaremos a escribir código y crearemos nuestro primer adaptador real: el DjangoOrdenRepository, que conectará nuestro dominio con el ORM de Django.

---

Todo lo anterior es el proceso para preparar nuestro entorno de trabajo en caso de no saber como hacerlo, pero el dia de hoy corresponde a implementar el patron de repositorio para la persistencia de datos.

## 🧠 Misión de Hoy: Construir el DjangoOrdenRepository

Hoy vamos a construir la pieza más importante que conecta nuestro núcleo de negocio con Django: el adaptador de persistencia. Crearemos un `DjangoOrdenRepository` que utilizará el ORM (Mapeo Objeto-Relacional) de Django para guardar y leer nuestras órdenes en una base de datos real (por ahora, una base de datos SQLite que Django crea por defecto).

### Paso 1: Definir el Modelo de Django

Primero, necesitamos decirle a Django cómo se verá la tabla de "órdenes" en la base de datos. Esto se hace en el archivo de modelos de nuestra app a`api`.

#### Acción:
Abre el archivo `api/models.py` y pega el siguiente código. Lee los comentarios para entender por qué este modelo es diferente a nuestro modelo de dominio.	

```python
# api/models.py
from django.db import models

class OrdenModel(models.Model):
    """
    Este es el modelo que representa nuestra tabla en la base de datos.
    Es un "detalle de implementación" de bajo nivel.
    No es nuestro modelo de dominio 'Orden'.
    """
    # Usamos un campo JSON para guardar los items de la orden.
    # Es una forma sencilla de almacenar datos estructurados sin crear otra tabla.
    items = models.JSONField()

    # Podríamos añadir más campos que solo le importan a la base de datos,
    # como la fecha de creación.
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Orden #{self.id}"
```

### Paso 2: Crear el Archivo del Adaptador

Ahora, crearemos el archivo donde vivirá nuestro nuevo repositorio.

#### Acción:
Dentro de tu núcleo, en la carpeta `tienda/adapters/`, crea un nuevo archivo llamado `django_orm.py`. Este archivo contendrá todos nuestros adaptadores relacionados con el ORM de Django.	

### Paso 3: Implementar el `DjangoOrdenRepository`
Este es el corazón de la misión. Abriremos `django_orm.py` y escribiremos la clase que actúa como traductor entre nuestro dominio y el modelo de Django.

#### Acción:
Pega el siguiente código en tu nuevo archivo `tienda/adapters/django_orm.py`. Tu tarea será rellenar la lógica de los métodos `_mapear_a_modelo` (traducir del dominio a Django) y `_mapear_a_dominio` (traducir de Django al dominio).

```python
# tienda/adapters/django_orm.py

from tienda.domain.models import Orden, Libro, CursoOnline, IProducto
from tienda.domain.ports import IOrdenRepository
from tienda.domain.exceptions import OrdenNoEnconrtadaError
from api.models import OrdenModel

class DjangoOrdenRepository(IOrdenRepository):
    
    def _mapear_a_modelo(self, orden: Orden) -> dict:
        """Traduce un objeto Orden del dominio a un diccionario para el modelo de Django."""
        # TU TAREA 1: Crea una lista de diccionarios a partir de orden.items
        # que se pueda guardar como JSON. Por ejemplo:
        # [{"nombre": "Libro1", "precio": 10, "cantidad": 2}, ...]
        items_para_db = []
        # ... tu lógica aquí ...
        
        return {"items": items_para_db}

    def _mapear_a_dominio(self, orden_model: OrdenModel) -> Orden:
        """Traduce un OrdenModel de Django a un objeto Orden del dominio."""
        # TU TAREA 2: Crea una nueva Orden y llénala con los items
        # que vienen del JSON de la base de datos (orden_model.items).
        # Tendrás que recrear los objetos Libro o CursoOnline.
        orden = Orden(id=orden_model.id)
        # ... tu lógica aquí ...

        return orden

    def guardar(self, orden: Orden):
        datos_modelo = self._mapear_a_modelo(orden)
        
        # El ORM de Django crea un registro si el id no existe, o lo actualiza si existe.
        orden_modelo, _ = OrdenModel.objects.update_or_create(
            id=orden.id,
            defaults=datos_modelo
        )
        # Actualizamos el id en nuestro objeto de dominio por si era una nueva orden
        orden.id = orden_modelo.id

    def buscar_por_id(self, orden_id: int) -> Orden:
        try:
            orden_modelo = OrdenModel.objects.get(id=orden_id)
            return self._mapear_a_dominio(orden_modelo)
        except OrdenModel.DoesNotExist:
            raise OrdenNoEnconrtadaError(f"Orden con ID {orden_id} no encontrada.")
```

Nota: Para `_mapear_a_dominio`, puedes asumir que si no tiene peso, es un `CursoOnline`, y si lo tiene, es un `Libro`.

### Paso 4: Crear la Base de Datos
Finalmente, vamos a decirle a Django que cree la tabla en la base de datos basándose en nuestro `OrdenModel`.

#### Acción:
En tu terminal (con el entorno virtual activado), ejecuta estos dos comandos:

```bash
# 1. Prepara las migraciones (crea el archivo de instrucciones para la DB)
python manage.py makemigrations api

# 2. Aplica las migraciones (ejecuta las instrucciones y crea la tabla)
python manage.py migrate
```

Si todo va bien, verás que se ha creado un archivo `db.sqlite3` en tu proyecto. ¡Esa es tu base de datos!
