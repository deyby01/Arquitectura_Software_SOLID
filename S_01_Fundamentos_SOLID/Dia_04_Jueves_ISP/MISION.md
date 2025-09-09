# ✍️ Misión del Día 4: Refactorizar aplicando ISP

Tu misión hoy es tomar el diseño de un sistema para una máquina multifuncional y refactorizarlo para que no viole el Principio de Segregación de Interfaces.

### 1. Código Inicial

Ve a la carpeta `Dia_04_Jueves_ISP/`. Crea un archivo llamado `maquinas_malo.py` dentro de la carpeta `codigo_ejemplo/` y pega el siguiente código:

```python
# codigo_ejemplo/maquinas_malo.py
from abc import ABC, abstractmethod

class IMaquina(ABC):
    @abstractmethod
    def imprimir(self, documento):
        pass

    @abstractmethod
    def escanear(self, documento):
        pass

    @abstractmethod
    def enviar_fax(self, documento):
        pass


class MaquinaMultifuncional(IMaquina):
    def imprimir(self, documento):
        print(f"Imprimiendo {documento}")

    def escanear(self, documento):
        print(f"Escaneando {documento}")

    def enviar_fax(self, documento):
        print(f"Enviando por fax {documento}")


class ImpresoraAntigua(IMaquina):
    def imprimir(self, documento):
        print(f"Imprimiendo {documento} en la impresora antigua.")

    def escanear(self, documento):
        # ¡Problema! Esta impresora no puede escanear.
        raise NotImplementedError("Esta impresora no soporta escaneo.")

    def enviar_fax(self, documento):
        # ¡Problema! Esta impresora no puede enviar faxes.
        raise NotImplementedError("Esta impresora no soporta envío de fax.")


# Uso
multifuncional = MaquinaMultifuncional()
multifuncional.imprimir("un reporte")
multifuncional.escanear("una foto")

impresora_vieja = ImpresoraAntigua()
impresora_vieja.imprimir("un currículum")
# La siguiente línea rompería el programa:
# impresora_vieja.escanear("una factura")
```

----

### **Tu Tarea**
- **1.** Analiza el código y explica por qué la clase ImpresoraAntigua viola el ISP.

- **2.** Crea un nuevo archivo en tu carpeta mi_solucion/ llamado maquinas_bueno.py.

- **3.** Refactoriza el código siguiendo el patrón que aprendiste en la teoría:

- **4.** Crea interfaces (ABCs) pequeñas y específicas para cada funcionalidad: IImprimible, IEscaneable, IFaxable.

- **5.** Haz que la clase MaquinaMultifuncional herede de las tres interfaces.

- **6.** Haz que la clase ImpresoraAntigua herede solamente de la interfaz que realmente puede implementar.

- **7.** Demuestra que tu nuevo diseño es mejor. Muestra cómo puedes crear una nueva clase, por ejemplo EscanerModerno, que solo escanea, sin tener que implementar métodos de impresión o fax.

**¡Adelante!** Este principio te ayudará a crear componentes de software mucho más cohesivos y reutilizables.
