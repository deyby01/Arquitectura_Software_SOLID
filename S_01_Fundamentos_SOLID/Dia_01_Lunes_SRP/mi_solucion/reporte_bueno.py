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

class ExportarReporteJson:
    def __init__(self, reporte: Reporte):
        self.reporte = reporte

    def exportar_json(self):
        # Exporta el reporte a un archivo JSON
        reporte_data = self.reporte.generar_reporte()
        nombre_archivo = f"{self.reporte.titulo.replace(' ', '_').lower()}.json"
        print(f"Exportando reporte a {nombre_archivo}...")
        with open(nombre_archivo, 'w') as f:
            json.dump(reporte_data, f)
        print("Exportación completa.")


class ExportarReporteCSV:
    def __init__(self, reporte: Reporte):
        self.reporte = reporte

    def exportar_csv(self):
        # Exporta el reporte a un archivo CSV
        reporte_data = self.reporte.generar_reporte()
        nombre_archivo = f"{self.reporte.titulo.replace(' ', '_').lower()}.csv"
        print(f"Exportando reporte a {nombre_archivo}...")
        with open(nombre_archivo, 'w') as f:
            f.write("titulo,contenido\n")
            f.write(f"{reporte_data['titulo']},{reporte_data['contenido']}\n")
        print("Exportación completa.")



# Uso
mi_reporte = Reporte("Reporte de Ventas Mensual", "Las ventas han subido un 20%.")
exportador = ExportarReporteCSV(mi_reporte)
exportador.exportar_csv()