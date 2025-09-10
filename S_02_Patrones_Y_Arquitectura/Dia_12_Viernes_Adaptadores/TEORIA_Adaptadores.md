🧠 Día 12: Implementando Nuestro Primer Adaptador

Ayer definimos los "enchufes" (puertos) en la pared de nuestro hexágono. Hoy vamos a construir nuestro primer "electrodoméstico" y lo conectaremos: un Adaptador.

Los adaptadores son el código que vive fuera de nuestro dominio y que sirve de puente entre nuestra lógica de negocio pura y la tecnología concreta del mundo exterior.

¿Qué es un Adaptador Secundario?
Es una clase que implementa una de las interfaces (puertos) que nuestro dominio necesita. Su trabajo es traducir las instrucciones simples del puerto a los comandos específicos de una tecnología.

El Puerto (IOrdenRepository) dice: "Necesito un método guardar(orden)".

El Adaptador (OrdenRepositoryPostgreSQL) responde: "Entendido. Para 'guardar', ejecutaré el comando INSERT INTO orders... usando la librería psycopg2".

Hoy, para empezar, crearemos un adaptador de repositorio muy simple que guardará los datos en la memoria del programa, sin necesidad de una base de datos real.

Flash Recordatorio ⚡️: LSP y DIP

Un Adaptador es la materialización de nuestros principios. Debe ser una implementación perfecta de su Puerto (Liskov Substitution Principle). Y al crearlo, completamos el Dependency Inversion Principle: el "detalle" (nuestro adaptador) ahora depende de la "abstracción" (nuestro puerto).