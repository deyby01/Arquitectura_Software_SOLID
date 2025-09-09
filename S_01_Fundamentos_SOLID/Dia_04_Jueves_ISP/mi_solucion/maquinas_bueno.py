"""
1. La clase antigua viola el principio del ISP por que tiene una clase generica
en la cual hay muchos metodos, y algunos de los mismos no los van a utilizar los objetos
creados a partir de esta clase, ya que alguno solo necesitarian implementar los que necesiten
pero dado que ya habia una clase abstracta que tenia todos los metodos, los objetos debian
implementar estos metodos asi no los utilizaran, lo que hace confuso el codigo y su funcionamiento
y es mas propenso a errores en tiempo de ejecucion.
"""

from abc import ABC, abstractmethod
import time

class IImprimible(ABC):
    """
    Clase que solo se encarga de que se implemente el metodo imprimir()
    """
    @abstractmethod
    def imprimir(self):
        pass

class IEscaneable(ABC):
    """
    Clase que solo se encarga de que se implemente el metodo escanear()
    """
    @abstractmethod
    def escanear(self):
        pass

class IFaxable(ABC):
    """
    Clase que solo se encarga de que se implemente el metodo enviar_fax()
    """
    @abstractmethod
    def enviar_fax(self):
        pass

# Implemento todas mis clases
class MaquinaMultifuncional(IImprimible, IEscaneable, IFaxable):
    def imprimir(self, documento):
        print(f"Imprimiendo {documento}...")
        time.sleep(2)
    
    def escanear(self, documento):
        print(f"Escaneando {documento}...")
        time.sleep(3)
    
    def enviar_fax(self, documento):
        print(f"Enviando por fax {documento}...")
        time.sleep(2)


# Ahora no necesitamos implementar todos los metodos sino solo el que necesitamos
class ImpresoraAntigua(IImprimible):
    """
    Clase que solo implementa el metodo imprimir()
    """
    def imprimir(self, documento):
        print(f"Imprimiendo {documento} en la impresora antigua.")
        time.sleep(3)


# Implementamos la nueva clase demostrando que no necesitamos implementar los metodos de impresion
class EscanerModerno(IEscaneable):
    """
    Clase que solo implementa el metodo escanear()
    """
    def escanear(self, documento):
        print(f"Escaneando {documento}....")
        time.sleep(1)


# Area de pruebas
if __name__ == "__main__":
    # Prueba con la máquina multifuncional
    multifuncional = MaquinaMultifuncional()
    multifuncional.imprimir("un reporte")
    multifuncional.escanear("una foto")
    multifuncional.enviar_fax("un mensaje")

    # Prueba con la impresora antigua
    impresora_vieja = ImpresoraAntigua()
    impresora_vieja.imprimir("un currículum")

    # Probamos solo el escaner
    escaner = EscanerModerno()
    escaner.escanear("un documento")