# codigo_ejemplo/pagos_malo.py

def procesar_pago(monto: float, metodo: str):
    """
    Procesa un pago. Este código viola el OCP porque
    necesita ser modificado para cada nuevo método de pago.
    """
    if metodo == "tarjeta":
        print(f"Procesando ${monto} con tarjeta de crédito...")
        # Lógica específica para la pasarela de tarjetas
        print("Pago con tarjeta exitoso.")
    elif metodo == "paypal":
        print(f"Procesando ${monto} con PayPal...")
        # Lógica específica para la API de PayPal
        print("Pago con PayPal exitoso.")
    else:
        # Si añadimos "cripto", tenemos que añadir otro "elif" aquí.
        raise ValueError("Método de pago no soportado.")

# Uso
procesar_pago(100, "tarjeta")
procesar_pago(50, "paypal")