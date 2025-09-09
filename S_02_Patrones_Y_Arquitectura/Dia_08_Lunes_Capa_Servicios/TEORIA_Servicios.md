# 🧠 Día 8: La Capa de Servicios - El Chef de tu Aplicación

Hoy damos nuestro primer paso para pasar del diseño de "clases" al diseño de "sistemas". Introduciremos un patrón muy simple pero poderoso: la Capa de Servicios (Service Layer).

## 🤔 **El Problema:** ¿Dónde Vive la Lógica de Negocio?
En frameworks como Django, es muy tentador poner el "cerebro" de la aplicación en dos lugares:

### 🖥️ **En las Vistas (views.py):** La vista recibe una petición, crea un usuario en la base de datos, llama a una API externa, envía un email y luego devuelve una respuesta. Esto hace que las vistas se vuelvan gigantes y difíciles de probar.

### 📊 **En los Modelos (models.py):** Se le añade un método .save() al modelo User que, además de guardar, envía un email. Esto es un poco mejor, pero el modelo termina con responsabilidades que no le corresponden.

Ambos enfoques tienen un problema.

## ⚡️ **Flash Recordatorio:** Principio de Responsabilidad Única (SRP)

Acabamos de ver una violación del SRP. La responsabilidad de una vista es manejar la comunicación HTTP (peticiones y respuestas). La de un modelo es representar la estructura de los datos. Ninguna de las dos debería contener la lógica compleja de un proceso de negocio.

## 💡 **La Solución:** El Servicio como Orquestador
La Capa de Servicios es una nueva capa en nuestra aplicación (por ejemplo, un archivo services.py) que se sitúa entre las vistas y los modelos.

Su única responsabilidad es orquestar la lógica de negocio.

### 🍽️ **Pensemos en la analogía de un restaurante:**

#### 🧑‍🍳 **La Vista (El Mesero):** Toma la orden del cliente (la petición HTTP). No cocina.

#### 🥕 **El Modelo (Los Ingredientes):** Son los datos puros (un usuario, un producto). No saben qué plato se va a cocinar con ellos.

#### 👨‍🍳 **La Capa de Servicios (El Chef):** El chef recibe la orden del mesero (la llamada desde la vista), toma los ingredientes (los modelos) y sigue la receta (la lógica de negocio) para preparar el plato. El chef no habla con el cliente.

Esta separación hace que el código sea:

- ✅ **Más fácil de probar:** Puedes probar la lógica del chef sin necesidad de un mesero (sin peticiones HTTP).

- ♻️ **Más reutilizable:** La misma "receta" del chef puede ser usada por el mesero del restaurante, por la app de delivery o para un evento de catering (una API, un script de fondo, etc.).