# 🧠 La Capa de Aplicación - El Cerebro Orquestador

Esta capa es el "quién" de nuestra arquitectura: el director de orquesta que usa el dominio para ejecutar tareas específicas. Es la pieza que une el mundo exterior con nuestro núcleo de negocio.

**El trabajo de un Servicio de Aplicación es:**
1.  Recibir una petición simple desde un adaptador primario (ej: "crea una nueva orden").
2.  Utilizar los **Modelos de Dominio** para realizar la tarea (ej: `orden.agregar_item()`).
3.  Utilizar los **Puertos Secundarios** para comunicarse con el exterior (ej: guardar la orden a través del `IOrdenRepository`).

Es el único lugar que coordina el flujo de trabajo de un caso de uso completo.

> **Flash Recordatorio ⚡️: Principio de Inversión de Dependencias (DIP)**
>
> Aquí es donde la **Inyección de Dependencias** brilla. Nuestro servicio no sabrá si está usando un `InMemoryOrdenRepository` o un `PostgreSQLRepository`. Solo sabrá que necesita "algo" que cumpla con el contrato `IOrdenRepository`. Le "inyectaremos" el adaptador que necesitemos desde fuera.