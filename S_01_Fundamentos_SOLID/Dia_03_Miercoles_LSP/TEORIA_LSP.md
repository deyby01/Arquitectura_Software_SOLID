# 🧠 Día 3: El Principio de Sustitución de Liskov (LSP)

Si el Principio de Abierto/Cerrado (OCP) nos dice que debemos poder **extender** nuestro sistema, el Principio de Sustitución de Liskov (LSP) nos da la regla para asegurarnos de que esas extensiones sean seguras y no rompan el código existente.

> **Los objetos de una superclase deben poder ser reemplazados por objetos de sus subclases sin afectar la corrección del programa.**

En palabras sencillas: si tienes una clase `Padre` y una clase `Hijo` que hereda de `Padre`, deberías poder usar un objeto `Hijo` en cualquier lugar donde se espere un objeto `Padre` **y que todo siga funcionando como se espera**.

El LSP nos dice que las subclases no solo deben implementar los mismos métodos que la clase padre, sino que deben hacerlo de una manera que **mantenga el contrato del padre**. Esto incluye el tipo de datos que reciben, el tipo de datos que devuelven, las excepciones que lanzan, y el comportamiento general del método.



### Ejemplo Clásico: Violando el LSP

El ejemplo más famoso es el de `Rectángulo` y `Cuadrado`. Un cuadrado *es* un rectángulo (si lo miras desde un punto de vista matemático), pero si lo modelas con herencia, rompes el LSP.

```python
# Mal Ejemplo: La subclase rompe el contrato del padre
class Rectangulo:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    def set_ancho(self, valor):
        self._ancho = valor

    def set_alto(self, valor):
        self._alto = valor

    def area(self):
        return self._ancho * self._alto

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        # Un cuadrado es un rectángulo donde alto y ancho son iguales
        super().__init__(lado, lado)

    # Esto viola el LSP porque cambia el comportamiento del padre
    # para mantener el invariante de un cuadrado (lados iguales).
    def set_ancho(self, valor):
        self._ancho = valor
        self._alto = valor # ¡Aquí está el problema!

    def set_alto(self, valor):
        self._ancho = valor
        self._alto = valor # ¡Aquí está el problema!

# Código cliente que espera un Rectangulo
def aumentar_ancho_y_calcular_area(rectangulo: Rectangulo):
    ancho_original = rectangulo._ancho
    rectangulo.set_alto(10)
    rectangulo.set_ancho(5)
    print(f"Área esperada: {ancho_original * 10}")
    print(f"Área real: {rectangulo.area()}")

# Uso
rect = Rectangulo(5, 4)
aumentar_ancho_y_calcular_area(rect) # Esto funciona como se espera.

print("---")

cuad = Cuadrado(5)
aumentar_ancho_y_calcular_area(cuad) # ¡Esto rompe el programa!