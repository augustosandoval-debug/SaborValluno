from modelo.productos import Plato, Bebida, Combo
from modelo.pedidos import PedidoDelivery, PedidoLlevar
from modelo.clientes import Cliente

def test_caso_referencia():
    cliente = Cliente("1", "Test", "70000000")
    silpancho = Plato("P1", "Silpancho", 35.0, "Fuerte")
    mocochinchi = Bebida("B1", "Mocochinchi", 6.0, "Natural")
    
    combo = Combo("C1", "Combo Test")
    combo.agregar_producto(silpancho)
    combo.agregar_producto(mocochinchi)
    
    assert combo.calcular_precio() == 36.90, "El combo debe costar 36.90"
    
    pedido = PedidoDelivery("PED1", cliente, "Quillacollo")
    pedido.agregar_item(combo, 2)
    
    assert pedido.calcular_subtotal() == 73.80, "El subtotal debe ser 73.80"
    assert pedido.calcular_cargos() == 15.0, "El envío a Quillacollo es 15"
    assert pedido.calcular_total() == 88.80, "El total debe ser 88.80"

def test_combo_anidado():
    plato = Plato("P1", "Pique", 40.0, "Fuerte")
    bebida = Bebida("B1", "Refresco", 5.0, "Gaseosa")
    combo_interno = Combo("C1", "Combo Interno")
    combo_interno.agregar_producto(plato)
    combo_interno.agregar_producto(bebida) 
    
    otro_plato = Plato("P2", "Sopa", 15.0, "Entrada")
    combo_externo = Combo("C2", "Combo Externo")
    combo_externo.agregar_producto(combo_interno)
    combo_externo.agregar_producto(otro_plato)
    assert combo_externo.calcular_precio() == 49.95

def test_validaciones():
    try:
        Plato("P3", "Error", -5.0, "Fuerte")
        assert False, "Debería lanzar error por precio negativo"
    except ValueError:
        pass
        
    try:
        Cliente("1", "Error", "12345678")
        assert False, "Debería lanzar error por no empezar con 6 o 7"
    except ValueError:
        pass

print("Ejecutando pruebas...")
test_caso_referencia()
test_combo_anidado()
test_validaciones()
print("Todas las pruebas pasaron correctamente.")