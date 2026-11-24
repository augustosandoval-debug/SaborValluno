class Cliente:
    def __init__(self, id_cliente: str, nombre: str, telefono: str):
        self._id_cliente = id_cliente
        self._nombre = nombre
        self._telefono = self.validar_telefono(telefono)

    @property
    def telefono(self) -> str:
        return self._telefono

    @telefono.setter
    def telefono(self, valor: str):
        self._telefono = self.validar_telefono(valor)

    def validar_telefono(self, telefono: str) -> str:
        if len(telefono) != 8 or not telefono.isdigit():
            raise ValueError("El teléfono debe tener exactamente 8 dígitos.")
        if telefono[0] not in ['6', '7']:
            raise ValueError("El teléfono debe empezar con 6 o 7.")
        return telefono