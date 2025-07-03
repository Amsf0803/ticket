import random

Espera = random.randint(0,450)

Cliente = input("Con quien tengo el gusto: ")

Donde = int(input("Va a ser para comer aqui? \n\t1 Si \n\t2 No \n\tElegir: "))

def Ubicacion():
    global Donde
    if Donde == 1:
        return "Aqui"
    elif Donde == 2:
        return "Llevar"
    else:
        return "Decida"

def mostrar_menu():
    print("Menú:")
    print("1. Hamburguesa - $80")
    print("2. Hotdog - $30")
    print("3. Refresco - $25")

def obtener_pedido():
    pedido = {}
    while True:
        mostrar_menu()
        opcion = input("¿Qué deseas ordenar? (1: Hamburguesa, 2: Hotdog, 3: Refresco): ")
        
        if opcion == '1':
            item = "Hamburguesa"
        elif opcion == '2':
            item = "Hotdog"
        elif opcion == '3':
            item = "Refresco"
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")
            continue
        
        cantidad = int(input(f"¿Cuántas {item}s deseas ordenar?: "))
        if item in pedido:
            pedido[item] += cantidad
        else:
            pedido[item] = cantidad
        
        mas = input("¿Deseas ordenar algo más? (si/no): ").strip().lower()
        if mas != 'si':
            break
    
    return pedido

def imprimir_ticket(pedido):
    total = 0
    print("------------------------------------")
    print(f"#{Espera}----------------------{Ubicacion()}")
    print(Cliente)
    print("------------------------------------")
    print("\n--- Ticket de Compras ---")
    for item, cantidad in pedido.items():
        if item == "Hamburguesa":
            precio = 80
        elif item == "Hotdog":
            precio = 30
        elif item == "Refresco":
            precio = 25
        
        costo = cantidad * precio
        total += costo
        print(f"{cantidad} {item}{' ' * (20 - len(item))}${costo}")
    print("------------------------------------")
    print(f"{'Total':<20}${total}")


def main():
    pedido = obtener_pedido()
    imprimir_ticket(pedido)


if __name__ == "__main__":
    main()





