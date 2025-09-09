from abc import ABC, abstractmethod
import time

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto: float):
        pass


class PagoConTarjeta(MetodoPago):
    def procesar_pago(self, monto: float):
        print(f"Procesando ${monto} con tarjeta de crédito...")
        time.sleep(3)
        print("Pago con tarjeta Exitoso.")

    
class PagoConPayPal(MetodoPago):
    def procesar_pago(self, monto: float):
        print(f"Procesando ${monto} con PayPal...")
        time.sleep(3)
        print("Pago con PayPal Exitoso.")

class PagoConCripto(MetodoPago):
    def procesar_pago(self, monto: float):
        print(f"Iniciando Transferencia de ${monto} en BTC...")
        # Logica de conexion con la blockchain
        time.sleep(5)# Las transacciones cripto puedes ser mas lentas 
        print("Transferencia confirmada en la red. Pago con cripto exitoso.")
    
def realizar_cobro(monto: float, metodo_pago: MetodoPago):
    metodo_pago.procesar_pago(monto)
    print("Cobro realizado.")


# Ahora vamos a crear las instancias y probar el flujo
if __name__ == "__main__":
    # Vamos a cobrar con tarjeta
    tarjeta = PagoConTarjeta()
    realizar_cobro(100, tarjeta)
    print("-----------------")
    # Ahora vamos a cobrar con PayPal
    paypal = PagoConPayPal()
    realizar_cobro(200, paypal)
    print("-----------------")
    # Ahora vamos a cobrar con cripto
    cripto = PagoConCripto()
    realizar_cobro(300, cripto)
