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