from abc import ABC, abstractmethod

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, total: float) -> str:
        pass

class Efectivo(MetodoPago):
    def __init__(self, monto_recibido: float):
        self._monto_recibido = monto_recibido

    def procesar_pago(self, total: float) -> str:
        if self._monto_recibido < total:
            raise ValueError("El monto recibido no cubre el total.")
        cambio = round(self._monto_recibido - total, 2)
        return f"Pago en efectivo exitoso. Cambio: Bs {cambio}"

class PagoQR(MetodoPago):
    def __init__(self, codigo_transaccion: str):
        if len(codigo_transaccion) != 10 or not codigo_transaccion.isdigit():
            raise ValueError("El código de transacción debe tener 10 dígitos.")
        self._codigo_transaccion = codigo_transaccion

    def procesar_pago(self, total: float) -> str:
        return f"Pago por QR exitoso. Código: {self._codigo_transaccion}"

class Tarjeta(MetodoPago):
    def __init__(self, numero_tarjeta: str):
        self._numero_tarjeta = numero_tarjeta

    def procesar_pago(self, total: float) -> str:
        comision = round(total * 0.03, 2)
        return f"Pago con tarjeta exitoso. Comisión del 3% (Bs {comision}) incluida en el total."