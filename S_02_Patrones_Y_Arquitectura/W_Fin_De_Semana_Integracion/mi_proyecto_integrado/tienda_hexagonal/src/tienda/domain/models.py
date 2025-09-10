from abc import ABC, abstractmethod

class IProducto(ABC):
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

class IProductoFisico(IProducto):
    def __init__(self, nombre: str, precio: float, peso_kg: float):
        super().__init__(nombre, precio)
        self.peso_kg = peso_kg

class Libro(IProductoFisico):
    pass

class CursoOnline(IProducto):
    pass


class Orden:
    def __init__(self, id: int = None):
        self.id = id
        self.items = []

    def agregar_item(self, producto: IProducto, cantidad: int):
        item = {"producto": producto, "cantidad": cantidad}
        self.items.append(item)

    def calcular_total(self) -> float:
        total = 0
        for item in self.items:
            total += item["producto"].precio * item["cantidad"]
        return total