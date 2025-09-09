### Tu Misión
- **Ejecuta el Código:** Primero, guarda y corre el script para entender qué hace. Verás que funciona, pero su diseño es muy frágil.

- Analiza y Encuentra las Violaciones: Antes de escribir una sola línea de código, tómate tu tiempo para leer la clase Orden y las clases de Producto. Hazte estas preguntas:

- **SRP:** ¿Qué clase tiene demasiadas responsabilidades? ¿Cuántas razones diferentes hay para cambiar la clase Orden?

- **OCP:** ¿Qué parte del código tendrías que modificar si el jefe te pide añadir "pago con criptomonedas"?

- **LSP:** ¿Qué pasa si una función necesita calcular el volumen de envío (ancho x alto x largo)? Un ProductoDigital no tiene dimensiones. ¿Es realmente un Producto en todos los contextos? ¿La herencia es la correcta?

- **ISP:** ¿Hay alguna "interfaz gorda" implícita? ¿Estamos forzando a alguna clase a tener atributos o métodos que no necesita (como el peso_kg en ProductoDigital)?

- **DIP:** ¿La clase Orden depende de detalles concretos en lugar de abstracciones? ¿Qué pasaría si quisieras cambiar el sistema de envío de emails por uno que use SMS?

- **Refactoriza:** En tu carpeta mi_proyecto_refactorizado/, crea un nuevo archivo tienda_limpia.py. Reescribe el sistema desde una perspectiva SOLID. Piensa en crear clases más pequeñas y enfocadas:

- **Quizás una clase para el Carrito.**

- **Clases separadas para cada MetodoDePago.**

- **Un ServicioDeNotificacion que no dependa de smtplib.**

- **Una mejor jerarquía para los Productos.**

- **¡Este es un gran desafío que pondrá a prueba todo lo que has aprendido! No hay una única solución correcta. El objetivo es que termines con un código que sea flexible, mantenible y fácil de entender.**

- **¡Tómate tu tiempo y disfruta el proceso de convertir el caos en orden! 💪**
