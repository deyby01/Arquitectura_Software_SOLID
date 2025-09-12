Bienvenido al nuevo Día 15 de la Semana 3. Nuestro objetivo será construir una API para nuestra tienda usando Django y DRF, pero aplicando rigurosamente la Arquitectura Hexagonal que hemos diseñado.

El Panorama General: Django como un Conjunto de Adaptadores
Antes de escribir una línea de código, el concepto más importante que debemos establecer es este: en nuestra nueva arquitectura, el proyecto Django completo no es la aplicación; es solo un conjunto de adaptadores que se conectan a nuestro núcleo de negocio.

Tu núcleo (tienda/): Sigue siendo el rey. Es puro, independiente y no sabe que Django existe.

La app de Django (api/): Será la capa de "adaptadores".

api/models.py: Contendrá los modelos de Django. Actuará como parte de nuestro adaptador de persistencia.

api/views.py y api/serializers.py: Serán nuestros adaptadores primarios, traduciendo las peticiones HTTP a llamadas a nuestros servicios de aplicación.

### Resumen repositorio

Hoy vamos a construir la pieza más importante que conecta nuestro núcleo de negocio con Django: el adaptador de persistencia. Crearemos un DjangoOrdenRepository que utilizará el ORM (Mapeo Objeto-Relacional) de Django para guardar y leer nuestras órdenes en una base de datos real (por ahora, una base de datos SQLite que Django crea por defecto).