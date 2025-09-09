---

# ✍️ Misión del Día 1: Refactorizar aplicando SRP

Tu misión, si decides aceptarla, es aplicar el Principio de Responsabilidad Única a un fragmento de código que lo viola claramente.

### 1. Código Inicial

Ve a la carpeta `Dia_01_Lunes_SRP/`. Crea un archivo llamado `reporte_malo.py` dentro de la carpeta `codigo_ejemplo/` y pega el siguiente código:

```python
# codigo_ejemplo/reporte_malo.py
import json

class Reporte:
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido

    def generar_reporte(self):
        # Simula la creación del contenido del reporte
        print("Generando contenido del reporte...")
        return {
            "titulo": self.titulo,
            "contenido": self.contenido
        }

    def exportar_json(self):
        # Exporta el reporte a un archivo JSON
        reporte_data = self.generar_reporte()
        nombre_archivo = f"{self.titulo.replace(' ', '_').lower()}.json"
        print(f"Exportando reporte a {nombre_archivo}...")
        with open(nombre_archivo, 'w') as f:
            json.dump(reporte_data, f)
        print("Exportación completa.")

# Uso
mi_reporte = Reporte("Reporte de Ventas Mensual", "Las ventas han subido un 20%.")
mi_reporte.exportar_json()