from abc import ABC, abstractmethod

class MetodoPago(ABC):
    abstractmethod
    def procesar_pago(self, monto: float):
        pass

class INotificacion(ABC):
    @abstractmethod
    def notificar(self, destinatario:str, mensaje: str):
        pass

class IOrdenRepository(ABC):    
    @abstractmethod
    def guardar(self, orden: 'Orden'):
        """ Guarda una orden en el sistema de persistencia. """
        pass

    @abstractmethod
    def buscar_por_id(self, orden_id: int) -> 'Orden':
        """Busca una Orden por su identificador Unico. """
        pass