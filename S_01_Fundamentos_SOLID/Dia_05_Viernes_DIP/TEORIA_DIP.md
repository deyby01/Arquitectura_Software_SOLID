# 🧠 Día 5: El Principio de Inversión de Dependencias (DIP)

Este es el principio que eleva nuestro pensamiento de "objetos" a "arquitectura". Es el pegamento que une los otros cuatro principios.

La definición formal tiene dos partes:
> **A. Los módulos de alto nivel no deben depender de los módulos de bajo nivel. Ambos deben depender de abstracciones.**
> **B. Las abstracciones no deben depender de los detalles. Los detalles deben depender de las abstracciones.**

Esto suena muy complejo, pero la idea es sorprendentemente simple.

* **Módulos de Alto Nivel:** Son las partes de tu código que contienen la lógica de negocio importante, las reglas centrales de tu aplicación (ej: "calcular el total de una compra", "registrar un nuevo usuario").
* **Módulos de Bajo Nivel:** Son los detalles de implementación, las "tuberías" que hacen que las cosas funcionen (ej: "escribir en un archivo CSV", "conectar a una base de datos MySQL", "enviar un email con la API de SendGrid").

Tradicionalmente, el código fluye así: el módulo de alto nivel llama directamente al de bajo nivel. **El DIP nos dice que esto es un error**. Debemos "invertir" esta dependencia.

### La Analogía Definitiva: El Enchufe 🔌💡

Imagina una lámpara (**alto nivel**). Su propósito es dar luz. Para funcionar, necesita electricidad, que viene de una central eléctrica (**bajo nivel**).

* **Mal Diseño (Sin DIP):** Sería como soldar los cables de la lámpara directamente a los cables de la central eléctrica. La lámpara está *acoplada* a esa central específica. Si la central cambia, tienes que cortar los cables y volver a soldar. Tu lámpara no es portable.
* **Buen Diseño (Con DIP):** Entre la lámpara y la central, creamos una **abstracción**: el estándar del enchufe y la toma de corriente.
    * La lámpara (alto nivel) ya no depende de la central, solo depende del enchufe estándar.
    * La central (bajo nivel) ya no se preocupa por la lámpara, solo se preocupa de proveer electricidad al enchufe estándar.
    * Ambos dependen de la misma abstracción. La dependencia se ha **invertido**. Ahora puedes enchufar tu lámpara en cualquier casa, sin importar de dónde venga la electricidad.



En código, nuestra "abstracción" es una Clase Base Abstracta (ABC) o una interfaz. Y la técnica para conectar las piezas se llama **Inyección de Dependencias**.

### Ejemplo Práctico: Violando el DIP

Un servicio de recordatorio de contraseñas que está "soldado" a una base de datos MySQL.

```python
# Mal Ejemplo: El alto nivel (PasswordReminder) depende directamente del bajo nivel (MySQLDatabase)

# Módulo de Bajo Nivel (el detalle)
class MySQLDatabase:
    def buscar_usuario(self, email: str) -> str:
        # Lógica para conectar a MySQL y buscar
        print(f"Buscando a {email} en la base de datos MySQL...")
        return "usuario_encontrado"

# Módulo de Alto Nivel (la lógica de negocio)
class PasswordReminder:
    def __init__(self):
        # ¡¡¡ERROR!!! Acoplamiento directo.
        # El módulo de alto nivel está creando una instancia del bajo nivel.
        self.db_connection = MySQLDatabase()

    def enviar_recordatorio(self, email: str):
        usuario = self.db_connection.buscar_usuario(email)
        print(f"Enviando recordatorio de contraseña a {usuario}...")
```

Si mañana queremos usar PostgreSQL, estamos obligados a modificar la clase ***PasswordReminder***.

----

### Refactorización: Aplicando el DIP
Ahora vamos a crear nuestro "enchufe" (la abstracción) e inyectar la dependencia.

```python
# Buen Ejemplo: Ambos niveles dependen de la abstracción (IDatabase)
from abc import ABC, abstractmethod

# 1. La Abstracción (nuestro "enchufe" estándar)
class IDatabase(ABC):
    @abstractmethod
    def buscar_usuario(self, email: str) -> str:
        pass

# 2. Los Módulos de Bajo Nivel (los detalles que se adaptan al "enchufe")
class MySQLDatabase(IDatabase):
    def buscar_usuario(self, email: str) -> str:
        print(f"Buscando a {email} en la base de datos MySQL...")
        return "usuario_encontrado_en_mysql"

class PostgreSQLDatabase(IDatabase):
    def buscar_usuario(self, email: str) -> str:
        print(f"Buscando a {email} en la base de datos PostgreSQL...")
        return "usuario_encontrado_en_postgres"

# 3. El Módulo de Alto Nivel (depende de la abstracción, no del detalle)
class PasswordReminder:
    def __init__(self, db_connection: IDatabase):
        # ¡Correcto! La dependencia se "inyecta" desde fuera.
        # Esta clase no sabe si es MySQL o PostgreSQL, solo sabe que
        # cumple con el contrato de IDatabase.
        self.db_connection = db_connection

    def enviar_recordatorio(self, email: str):
        usuario = self.db_connection.buscar_usuario(email)
        print(f"Enviando recordatorio de contraseña a {usuario}...")

# --- Uso ---
# El "cableado" se hace fuera de las clases, en el punto más alto de la aplicación.
mysql_db = MySQLDatabase()
reminder_con_mysql = PasswordReminder(mysql_db)
reminder_con_mysql.enviar_recordatorio("test@example.com")

print("--- Cambiando de base de datos ---")

postgres_db = PostgreSQLDatabase()
reminder_con_postgres = PasswordReminder(postgres_db)
reminder_con_postgres.enviar_recordatorio("test@example.com") # ¡Funciona sin cambiar PasswordReminder!
```