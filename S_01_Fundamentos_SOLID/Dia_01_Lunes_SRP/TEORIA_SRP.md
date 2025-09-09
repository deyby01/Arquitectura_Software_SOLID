Es el estándar en la industria del software a nivel mundial, por lo que es fundamental que las conozcas:

**S** - ****Single Responsibility Principle (Principio de Responsabilidad Única)****
**O** - ****Open/Closed Principle (Principio de Abierto/Cerrado)****
**L** - ****Liskov Substitution Principle (Principio de Sustitución de Liskov)****
**I** - ****Interface Segregation Principle (Principio de Segregación de Interfaces)****
**D** - ****Dependency Inversion Principle (Principio de Inversión de Dependencias)****

---

# 🧠 Día 1: El "Porqué" y el Principio de Responsabilidad Única (SRP)

## El "Porqué": Huyendo del Código Espagueti

Imagina que entras a una cocina a preparar un plato. En una cocina bien organizada, los cuchillos están en un cajón, las especias en un estante y las ollas en otro. Puedes encontrar lo que necesitas rápidamente y trabajar de forma eficiente.

[Image of a clean, organized professional kitchen]

Ahora imagina una cocina donde todo está tirado por el medio: cuchillos, verduras, ollas y platos sucios, todo en una misma pila. Encontrar algo es una pesadilla y limpiar después es casi imposible. Eso es el **"código espagueti"**.

[Image of a messy, chaotic kitchen]

Cuando empezamos a programar, es normal crear clases y funciones que hacen muchas cosas a la vez, como esa cocina desordenada. Funciona al principio, pero con el tiempo, ese **desorden (conocido como "deuda técnica")** hace que:
* **Arreglar un error sea difícil:** Un cambio en una parte puede romper otra cosa inesperadamente.
* **Añadir nueva funcionalidad sea lento y arriesgado.**
* **Entender el código sea un dolor de cabeza** para ti en el futuro o para otros desarrolladores.

Los principios **SOLID** son las reglas de organización para nuestra "cocina de código". Nos ayudan a mantener todo limpio, ordenado y en su lugar.

## El Principio de Responsabilidad Única (SRP)

> **Una clase debe tener una, y solo una, razón para cambiar.**

Esta es la regla más fundamental de todas. Significa que cada clase o módulo en tu programa debe tener **una única y bien definida responsabilidad**.

¿Qué es una "razón para cambiar"? Es un motivo funcional por el cual necesitarías modificar el código. Por ejemplo, un cambio en las reglas de negocio, un cambio en cómo se conecta a la base de datos o un cambio en el formato de un reporte.

### Ejemplo Práctico: Violando el SRP

Mira esta clase. Es un desastre esperando a ocurrir porque mezcla tres responsabilidades.

```python
# Mal Ejemplo: La clase "faz-tudo"
class Usuario:
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password = password

    # Responsabilidad 1: Gestionar datos del usuario (validar, etc.)
    def validar_password(self):
        return len(self.password) >= 8

    # Responsabilidad 2: Lógica de persistencia (Base de Datos)
    def guardar_en_db(self):
        print(f"Guardando {self.nombre} en la base de datos...")
        # Lógica para conectar y guardar en PostgreSQL...

    # Responsabilidad 3: Notificaciones
    def enviar_email_bienvenida(self):
        print(f"Enviando email de bienvenida a {self.email}...")
        # Lógica para conectar al servidor de email y enviar...
```


### ¡Tiene tres razones para cambiar!

## **Refactorización: Aplicando el SRP**
Ahora separamos las responsabilidades en clases distintas.

```python
# Buen Ejemplo: Cada clase tiene su propósito

# Responsabilidad 1: Contener los datos del usuario.
class Usuario:
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password = password

    def validar_password(self):
        return len(self.password) >= 8

# Responsabilidad 2: Gestionar la persistencia de usuarios.
class RepositorioUsuarios:
    def guardar(self, usuario: Usuario):
        print(f"Guardando {usuario.nombre} en la base de datos...")
        # Lógica para conectar y guardar en PostgreSQL...

# Responsabilidad 3: Gestionar el envío de notificaciones.
class ServicioNotificaciones:
    def enviar_email_bienvenida(self, usuario: Usuario):
        print(f"Enviando email de bienvenida a {usuario.email}...")
        # Lógica para conectar al servidor de email y enviar...
```

¡Mucho mejor! Ahora, si la base de datos cambia, solo tocas RepositorioUsuarios. Si el sistema de emails cambia, solo tocas ServicioNotificaciones. Cada pieza es independiente, más fácil de entender y, sobre todo, más fácil de testear.