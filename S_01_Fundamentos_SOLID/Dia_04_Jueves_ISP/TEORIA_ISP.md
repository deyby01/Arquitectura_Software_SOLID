# 🧠 Día 4: El Principio de Segregación de Interfaces (ISP)

Si el Principio de Liskov (LSP) nos enseña a crear subclases que se comportan correctamente, el Principio de Segregación de Interfaces (ISP) nos enseña a no forzar a esas subclases a tener comportamientos que no necesitan.

> **Ningún cliente debe ser forzado a depender de métodos que no utiliza.**

En palabras más sencillas: **Es mejor tener muchas interfaces pequeñas y específicas que una sola interfaz grande y genérica.**

Imagina que vas a un restaurante. En lugar de darte un menú de desayuno, uno de almuerzo y uno de cena, te entregan un libro gigante con todos los platos que han servido en la historia del restaurante. Para pedir un café, tienes que ignorar el 99% del menú. Esto es ineficiente y confuso. Eso es una "interfaz gorda". El ISP nos dice que es mejor dar a cada cliente un menú pequeño con solo lo que necesita.



En Python, aunque no tenemos la palabra clave `interface` como en otros lenguajes, este principio se aplica perfectamente a las Clases Base Abstractas (ABCs) y a las clases en general.

### Ejemplo Práctico: Violando el ISP

Imagina que estamos diseñando un sistema para gestionar diferentes tipos de trabajadores en una empresa.

```python
# Mal Ejemplo: Una "interfaz gorda" que obliga a todos a hacer de todo
from abc import ABC, abstractmethod

class ITrabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

    @abstractmethod
    def tomar_descanso(self):
        pass

    @abstractmethod
    def comer(self):
        pass

# Esta clase está bien, un humano hace las tres cosas.
class Humano(ITrabajador):
    def trabajar(self):
        print("El humano está trabajando...")

    def tomar_descanso(self):
        print("El humano está tomando un descanso...")

    def comer(self):
        print("El humano está comiendo...")

# ¡Aquí está el problema! Un robot no come ni toma descansos de la misma manera.
class Robot(ITrabajador):
    def trabajar(self):
        print("El robot está trabajando...")

    def tomar_descanso(self):
        # Este método no tiene sentido para un robot.
        # Lo dejamos vacío o lanzamos un error, pero estamos "forzados" a tenerlo.
        pass

    def comer(self):
        # Este método tampoco tiene sentido.
        print("El robot se está recargando...") # ¿Es esto "comer"? Es confuso.
```

La clase Robot se ve forzada a implementar ***tomar_descanso*** y ***comer***, métodos que no son parte de su naturaleza. Esto es una señal de un mal diseño.

----

### **Refactorización: Aplicando el ISP**

La solución es segregar (dividir) la interfaz "gorda" en roles más pequeños y específicos.

```python
# Buen Ejemplo: Interfaces pequeñas y enfocadas en roles
from abc import ABC, abstractmethod

# Rol 1: Algo que puede trabajar
class ITrabajable(ABC):
    @abstractmethod
    def trabajar(self):
        pass

# Rol 2: Algo que necesita descansos
class IDescansable(ABC):
    @abstractmethod
    def tomar_descanso(self):
        pass

# Rol 3: Algo que necesita alimentarse
class IAlimentable(ABC):
    @abstractmethod
    def comer(self):
        pass

# Ahora, las clases solo implementan los roles que necesitan.
# Un humano implementa los tres roles.
class Humano(ITrabajable, IDescansable, IAlimentable):
    def trabajar(self):
        print("El humano está trabajando...")

    def tomar_descanso(self):
        print("El humano está tomando un descanso...")

    def comer(self):
        print("El humano está comiendo...")

# Un robot solo implementa el rol de ser "trabajable".
class Robot(ITrabajable):
    def trabajar(self):
        print("El robot está trabajando...")

# El código es más limpio, más lógico y no hay métodos forzados.
h = Humano()
h.comer()

r = Robot()
r.trabajar()
# r.comer() # Esto daría un error, ¡lo cual es correcto! Un robot no puede comer.
```
Ahora nuestro sistema es mucho más flexible. Si mañana aparece un **"Androide"** que trabaja y descansa pero no come, podemos crearlo heredando solo de ***ITrabajable*** e ***IDescansable***.