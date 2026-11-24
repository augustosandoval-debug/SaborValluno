from abc import ABC, abstractmethod
from enum import Enum

class EstadoPedido(Enum):
    REGISTRADO = 1
    EN_PREPARACION = 2
    LISTO = 3
    ENTREGADO = 4
    CANCELADO = 5

class ProductoPedido:
    def __init__(self, producto, cantidad: int):
        if cantidad < 1 or cantidad > 20:
            raise ValueError("La cantidad debe estar entre 1 y 20.")
        self._producto = producto
        self._cantidad = cantidad

    @property
    def producto(self): return self._producto
    @property
    def cantidad(self): return self._cantidad

class Pedido(ABC):
    def __init__(self, id_pedido: str, cliente, metodo_pago=None):
        self._id_pedido = id_pedido
        self._cliente = cliente
        self._items = []
        self._estado = EstadoPedido.REGISTRADO
        self._metodo_pago = metodo_pago

    @property
    def estado(self): return self._estado
    
    def agregar_item(self, producto, cantidad: int):
        if self._estado != EstadoPedido.REGISTRADO:
            raise Exception("Solo se pueden agregar productos en estado REGISTRADO.")
        self._items.append(ProductoPedido(producto, cantidad))

    def quitar_item(self, id_producto: str):
        if self._estado != EstadoPedido.REGISTRADO:
            raise Exception("Solo se pueden quitar productos en estado REGISTRADO.")
        self._items = [i for i in self._items if i.producto._id_prod != id_producto]

    def cambiar_estado(self, nuevo_estado: EstadoPedido):
        transiciones = {
            EstadoPedido.REGISTRADO: [EstadoPedido.EN_PREPARACION, EstadoPedido.CANCELADO],
            EstadoPedido.EN_PREPARACION: [EstadoPedido.LISTO],
            EstadoPedido.LISTO: [EstadoPedido.ENTREGADO]
        }
        if nuevo_estado not in transiciones.get(self._estado, []):
            raise Exception(f"Transición inválida de {self._estado.name} a {nuevo_estado.name}")
        self._estado = nuevo_estado

    def calcular_subtotal(self) -> float:
        return round(sum(item.producto.calcular_precio() * item.cantidad for item in self._items), 2)

    @abstractmethod
    def calcular_cargos(self) -> float:
        pass

    def calcular_total(self) -> float:
        return round(self.calcular_subtotal() + self.calcular_cargos(), 2)

class PedidoLocal(Pedido):
    def __init__(self, id_pedido: str, cliente, numero_mesa: int, metodo_pago=None):
        super().__init__(id_pedido, cliente, metodo_pago)
        if numero_mesa < 1 or numero_mesa > 15:
            raise ValueError("La mesa debe estar entre 1 y 15.")
        self._numero_mesa = numero_mesa

    def calcular_cargos(self) -> float:
        return 0.0

class PedidoLlevar(Pedido):
    def calcular_cargos(self) -> float:
        platos_totales = sum(item.producto.contar_platos() * item.cantidad for item in self._items)
        return platos_totales * 2.0

class PedidoDelivery(Pedido):
    def __init__(self, id_pedido: str, cliente, zona: str, metodo_pago=None):
        super().__init__(id_pedido, cliente, metodo_pago)
        self._zona = zona
        self._tarifas = {"Cercado": 8.0, "Quillacollo": 15.0, "Sacaba": 15.0, "Vinto": 20.0}
        if zona not in self._tarifas:
            raise ValueError("Zona no válida.")

    def calcular_cargos(self) -> float:
        subtotal = self.calcular_subtotal()
        if subtotal < 40.0:
            raise ValueError("El pedido mínimo para delivery es de Bs 40.")
        
        cargo = self._tarifas[self._zona]
        if self._zona == "Cercado" and subtotal >= 150.0:
            cargo = 0.0
        return cargo

    def set_metodo_pago(self, metodo_pago):
        if metodo_pago.__class__.__name__ not in ["Efectivo", "PagoQR"]:
            raise ValueError("Delivery solo acepta pago en Efectivo o QR.")
        self._metodo_pago = metodo_pago