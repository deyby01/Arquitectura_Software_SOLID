# ✍️ Misión del Día 2: Refactorizar aplicando OCP

Tu misión hoy es tomar un sistema de procesamiento de pagos que viola el Principio de Abierto/Cerrado y refactorizarlo para que sea extensible sin necesidad de modificarlo.

### 1. Código Inicial

Ve a la carpeta `Dia_02_Martes_OCP/`. Crea un archivo llamado `pagos_malo.py` dentro de la carpeta `codigo_ejemplo/` y pega el siguiente código:

```python
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
```

**Tu Tarea**

Analiza el código y explica por qué la función procesar_pago viola el OCP.

Crea un nuevo archivo en tu carpeta mi_solucion/ llamado pagos_bueno.py.

Refactoriza el código siguiendo el patrón que aprendiste en la teoría:

Crea una Clase Base Abstracta (ABC) llamada MetodoDePago con un método abstracto procesar(monto).

Crea clases concretas como PagoConTarjeta y PagoConPaypal que hereden de MetodoDePago e implementen el método procesar.

La nueva función realizar_cobro(monto, metodo) debe aceptar un objeto de tipo MetodoDePago y llamar a su método procesar sin usar condicionales if/elif para determinar el tipo de pago.

Demuestra que tu sistema está "abierto a la extensión" creando una nueva clase PagoConCripto y usándola con tu función realizar_cobro sin modificar nada del código que ya habías escrito.