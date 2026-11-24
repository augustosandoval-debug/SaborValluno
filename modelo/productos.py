from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, id_prod: str, nombre: str, precio_base: float):
        if precio_base < 0:
            raise ValueError("El precio debe ser mayor a cero.")
        self._id_prod = id_prod
        self._nombre = nombre
        self._precio_base = precio_base

    @abstractmethod
    def calcular_precio(self) -> float:
        pass

    @abstractmethod
    def esta_disponible(self, dia: str) -> bool:
        pass

    @abstractmethod
    def contar_platos(self) -> int:
        pass

class Plato(Producto):
    def __init__(self, id_prod: str, nombre: str, precio_base: float, tipo_plato: str):
        super().__init__(id_prod, nombre, precio_base)
        self._tipo_plato = tipo_plato

    def calcular_precio(self) -> float:
        return self._precio_base

    def esta_disponible(self, dia: str) -> bool:
        if self._nombre.lower() == "chicharrón" and dia.lower() != "domingo":
            return False
        return True

    def contar_platos(self) -> int:
        return 1

class Bebida(Producto):
    def __init__(self, id_prod: str, nombre: str, precio_base: float, tipo_bebida: str, es_jarra: bool = False):
        super().__init__(id_prod, nombre, precio_base)
        self._tipo_bebida = tipo_bebida
        self._es_jarra = es_jarra

    def calcular_precio(self) -> float:
        if self._es_jarra:
            return self._precio_base * 3
        return self._precio_base

    def esta_disponible(self, dia: str) -> bool:
        return True

    def contar_platos(self) -> int:
        return 0

class Combo(Producto):
    def __init__(self, id_prod: str, nombre: str, descuento: float = 0.10):
        super().__init__(id_prod, nombre, 0.0) 
        self._descuento = descuento
        self._productos = []

    def agregar_producto(self, producto: Producto):
        if producto == self:
            raise ValueError("Un combo no puede contenerse a sí mismo.")
        self._productos.append(producto)

    def calcular_precio(self) -> float:
        if len(self._productos) < 2:
            raise ValueError("Un combo debe tener al menos 2 productos.")
        suma = sum(p.calcular_precio() for p in self._productos)
        return round(suma * (1 - self._descuento), 2)

    def esta_disponible(self, dia: str) -> bool:
        return all(p.esta_disponible(dia) for p in self._productos)

    def contar_platos(self) -> int:
        return sum(p.contar_platos() for p in self._productos)