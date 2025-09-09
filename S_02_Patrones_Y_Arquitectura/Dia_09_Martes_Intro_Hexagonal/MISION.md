# ✍️ Tu Misión de Hoy

Hoy no escribirás código. Tu misión es **conceptual**: diseñar la arquitectura de la tienda que refactorizamos usando el modelo **Hexagonal**.

## 📝 Tu Tarea

Toma una hoja de papel (o una herramienta de diagramas simple) y dibuja la arquitectura de tu `tienda_limpia.py`.

### 1️⃣ Dibuja el Hexágono

> En el centro, escribe las clases que pertenecen al núcleo de negocio.

**Pista**: `Orden`, `UserService`, `ServicioDeNotificacion`, etc.

### 2️⃣ Identifica los Puertos Primarios (Lado Izquierdo)

> ¿Cuáles son las acciones principales que tu sistema ofrece?

* Escríbelas en el borde del hexágono
* **Ejemplos**: `agregar_item_a_orden`, `realizar_pago`, `enviar_confirmacion`

### 3️⃣ Identifica los Puertos Secundarios (Lado Derecho)

> ¿Qué necesita tu núcleo del mundo exterior para funcionar?

* Escribe las interfaces (ABCs) que definiste
* **Ejemplos**: `MetodoPago`, `INotificacion`, y quizás una nueva como `IOrdenRepository` para guardar la orden

### 4️⃣ Dibuja los Adaptadores Primarios (Externos, a la Izquierda)

> ¿Qué cosas podrían iniciar una acción en tu sistema?

* Dibuja cajas para ellas
* **Ejemplos**: "Vista de Django", "App Móvil", "Script de Consola"
* Conecta estas cajas a los puertos primarios

### 5️⃣ Dibuja los Adaptadores Secundarios (Externos, a la Derecha)

> ¿Qué tecnologías concretas implementarán los puertos secundarios?

* Dibuja cajas para ellas
* **Ejemplos**: `PagoConTarjeta`, `MensajeroEmail`, `OrdenRepositoryPostgreSQL`
* Conecta estas cajas a los puertos secundarios