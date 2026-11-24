from modelo.productos import Plato, Bebida, Combo
from modelo.pedidos import PedidoLocal, PedidoLlevar, PedidoDelivery

class Restaurante:
    def __init__(self):
        self._menu = []
        self._pedidos = []
        self._mesas_abiertas = set() 

    def registrar_producto(self, producto):
        self._menu.append(producto)

    def registrar_pedido(self, pedido):
        if isinstance(pedido, PedidoLocal):
            if pedido._numero_mesa in self._mesas_abiertas:
                raise ValueError("La mesa ya tiene un pedido abierto.")
            self._mesas_abiertas.add(pedido._numero_mesa)
        self._pedidos.append(pedido)

    def mostrar_menu_disponible(self, dia):
        print(f"\n--- MENÚ DISPONIBLE PARA {dia.upper()} ---")
        for p in self._menu:
            if p.esta_disponible(dia):
                print(f"[{p._id_prod}] {p._nombre} - Bs {p.calcular_precio()}")