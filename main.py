from modelo.clientes import Cliente
from modelo.productos import Plato, Bebida, Combo
from modelo.pedidos import PedidoDelivery
from modelo.pagos import Efectivo, PagoQR
from restaurante import Restaurante

def main():
    rest = Restaurante()
    
    rest.registrar_producto(Plato("P01", "Silpancho", 35.0, "Fuerte"))
    rest.registrar_producto(Plato("P02", "Chicharrón", 30.0, "Fuerte"))
    rest.registrar_producto(Bebida("B01", "Mocochinchi", 6.0, "Natural"))
    
    combo = Combo("C01", "Combo Valluno")
    combo.agregar_producto(Plato("P03", "Silpancho Combo", 35.0, "Fuerte"))
    combo.agregar_producto(Bebida("B02", "Mocochinchi Combo", 6.0, "Natural"))
    rest.registrar_producto(combo)

    cliente_test = Cliente("CL01", "Juan Pérez", "71234567")
    
    while True:
        print("\n=== SISTEMA SABOR VALLUNO ===")
        print("1. Ver menú del día")
        print("2. Crear pedido Delivery")
        print("3. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            dia = input("¿Qué día es hoy? (lunes, martes, domingo, etc.): ")
            rest.mostrar_menu_disponible(dia)
            
        elif opcion == "2":
            print("\n--- NUEVO PEDIDO DELIVERY ---")
            id_ped = input("ID del pedido: ")
            zona = input("Zona (Cercado, Quillacollo, Sacaba, Vinto): ")
            
            pedido = PedidoDelivery(id_ped, cliente_test, zona)
            pedido.agregar_item(combo, 2)
            
            print("\n--- DETALLE DEL PEDIDO ---")
            print(f"Subtotal: Bs {pedido.calcular_subtotal()}")
            print(f"Envío: Bs {pedido.calcular_cargos()}")
            print(f"Total: Bs {pedido.calcular_total()}")
            
            print("\n--- PAGO ---")
            print("1. Efectivo\n2. QR")
            opc_pago = input("Método de pago: ")
            
            if opc_pago == "1":
                monto = float(input("Monto recibido: Bs "))
                pago = Efectivo(monto)
                print(pago.procesar_pago(pedido.calcular_total()))
            elif opc_pago == "2":
                codigo = input("Ingrese código QR de 10 dígitos: ")
                pago = PagoQR(codigo)
                print(pago.procesar_pago(pedido.calcular_total()))
            
            rest.registrar_pedido(pedido)
            print("¡Pedido registrado con éxito!")
            
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()