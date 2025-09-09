# 🧠 Día 2: El Principio de Abierto/Cerrado (OCP)

Ayer terminamos creando una nueva clase `ExportarReporteCSV` para añadir una funcionalidad sin tocar el código existente. Esa es la esencia del Principio de Abierto/Cerrado.

> **Las entidades de software (clases, módulos, funciones) deben estar abiertas para la extensión, pero cerradas para la modificación.**

En palabras sencillas: tu código debería permitirte **añadir nuevas funcionalidades sin tener que cambiar el código que ya existe, funciona y ha sido probado**.

Imagina el sistema eléctrico de tu casa. Está **cerrado** en el sentido de que no tienes que romper las paredes para cambiar los cables cada vez que compras un nuevo electrodoméstico. Pero está **abierto** a través de los enchufes, que te permiten **extender** su funcionalidad conectando una lámpara, un televisor o un cargador.



En software, las "paredes" son tu código ya escrito y los "enchufes" son las **abstracciones** (como clases base o interfaces).

### Ejemplo Práctico: Violando el OCP

Este es un error muy común. Tenemos una función que hace diferentes cosas basándose en un parámetro de tipo.

```python
# Mal Ejemplo: Modificamos la función cada vez que hay un nuevo formato.
from reporte_bueno import Reporte # Reutilizamos la clase Reporte de ayer

def exportador_general(reporte: Reporte, formato: str):
    # ¡Esto es un gran "if" de la perdición!
    if formato == "json":
        print("Exportando a JSON...")
        # ...lógica para exportar a json
    elif formato == "csv":
        print("Exportando a CSV...")
        # ...lógica para exportar a csv
    # ¿Y si mañana necesitamos XML? ¿O PDF?
    # Tendríamos que añadir más "elif" aquí, modificando la función.
```

Este código no está "cerrado". Cada nuevo formato nos obliga a abrirlo y modificarlo, con el riesgo de romper algo que ya funcionaba.

### Refactorización: Aplicando el OCP con Abstracciones

La solución es crear un "contrato" o "enchufe" común. En Python, usamos **Clases Base Abstractas (ABCs)** para esto.

```python
# Buen Ejemplo: Abierto a nuevos exportadores, cerrado a modificaciones.
from abc import ABC, abstractmethod
from reporte_bueno import Reporte # Reutilizamos la clase de ayer

# 1. Creamos el "contrato" o la abstracción (nuestro enchufe).
class Exportador(ABC):
    @abstractmethod
    def exportar(self, reporte: Reporte):
        """Este método DEBE ser implementado por cualquier subclase."""
        pass

# 2. Creamos implementaciones concretas (nuestros electrodomésticos).
class ExportadorJson(Exportador):
    def exportar(self, reporte: Reporte):
        print("Exportando reporte a JSON...")
        # ...lógica real de exportación a JSON.

class ExportadorCsv(Exportador):
    def exportar(self, reporte: Reporte):
        print("Exportando reporte a CSV...")
        # ...lógica real de exportación a CSV.

# 3. El código cliente ahora depende de la abstracción, no de los detalles.
def procesar_exportacion(reporte: Reporte, exportador: Exportador):
    # Esta función ya no necesita "if's". No sabe qué exportador es,
    # solo sabe que puede llamar al método ".exportar()".
    exportador.exportar(reporte)

# --- USO ---
mi_reporte = Reporte("Título", "Contenido")
exportador_json = ExportadorJson()
exportador_csv = ExportadorCsv()

procesar_exportacion(mi_reporte, exportador_json)
procesar_exportacion(mi_reporte, exportador_csv)

# ¿Y si ahora necesitamos exportar a XML?
# ¡No tocamos NADA del código anterior! Solo añadimos esto:
class ExportadorXml(Exportador):
    def exportar(self, reporte: Reporte):
        print("¡NUEVO! Exportando reporte a XML...")

exportador_xml = ExportadorXml()
procesar_exportacion(mi_reporte, exportador_xml)
```

Hemos creado un sistema robusto. La función `procesar_exportacion` está **cerrada** a cambios, pero el sistema general está **abierto** a ser extendido con tantos nuevos exportadores como queramos.