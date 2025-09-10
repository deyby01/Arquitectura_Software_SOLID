## 🧠 Día 11: Definiendo los Puertos

Hoy continuamos trabajando dentro de nuestro núcleo de negocio, la carpeta domain. Ayer definimos los "sustantivos" de nuestro negocio (los modelos Orden, Libro). Hoy definiremos los "contratos" que nuestro negocio necesita para hablar con el mundo exterior.

En la Arquitectura Hexagonal, los Puertos son las compuertas de comunicación de nuestro núcleo. Como vimos en el diagrama, hoy nos enfocaremos en los Puertos Secundarios: las interfaces que definen lo que nuestro núcleo necesita del mundo exterior.

Recordando: ¿Qué es un Puerto Secundario?
Un puerto secundario es una promesa que el núcleo le pide al mundo exterior que cumpla. Es el núcleo diciendo:

"No sé cómo vas a procesar un pago, pero necesito que me des algo que tenga un método procesar_pago(monto)".

"No sé cómo vas a guardar una orden en una base de datos, pero necesito que me des algo que tenga un método guardar(orden)".

En Python, estas promesas o contratos los definimos con nuestras ya conocidas Clases Base Abstractas (ABCs).

Flash Recordatorio ⚡️: Principio de Inversión de Dependencias (DIP)

Este es el corazón del DIP. Al definir estos puertos, hacemos que nuestro núcleo dependa de estas abstracciones (I...), no de detalles concretos como una base de datos PostgreSQL o un servicio de email específico.