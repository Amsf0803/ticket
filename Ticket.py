import random

MENU = {
    "1": ("Hamburguesa", 80),
    "2": ("Hotdog", 30),
    "3": ("Refresco", 25)
}

def get_cliente():
    return input("Con quien tengo el gusto: ")

def get_donde():
    while True:
        try:
            donde = int(input("Va a ser para comer aqui? \n\t1 Si \n\t2 No \n\tElegir: "))
            if donde in (1, 2):
                return donde
        except ValueError:
            pass
        print("Opción no válida. Por favor, ingresa 1 o 2.")

def ubicacion(donde):
    return "Aqui" if donde == 1 else "Llevar"

def mostrar_menu():
    print("Menú:")
    for k, (item, precio) in MENU.items():
        print(f"{k}. {item} - ${precio}")

def obtener_pedido():
    pedido = {}
    while True:
        mostrar_menu()
        opcion = input("¿Qué deseas ordenar? (1: Hamburguesa, 2: Hotdog, 3: Refresco): ")
        if opcion not in MENU:
            print("Opción no válida.")
            continue
        item, precio = MENU[opcion]
        try:
            cantidad = int(input(f"¿Cuántas {item}s deseas ordenar?: "))
        except ValueError:
            print("Cantidad no válida.")
            continue
        pedido[item] = pedido.get(item, 0) + cantidad
        mas = input("¿Deseas ordenar algo más? (si/no): ").strip().lower()
        if mas != 'si':
            break
    return pedido

def imprimir_ticket(espera, ubicacion, cliente, pedido):
    total = 0
    print("------------------------------------")
    print(f"#{espera}----------------------{ubicacion}")
    print(cliente)
    print("------------------------------------")
    print("\n--- Ticket de Compras ---")
    for item, cantidad in pedido.items():
        precio = next(p for i, (i_name, p) in MENU.items() if i_name == item)
        costo = cantidad * precio
        total += costo
        print(f"{cantidad} {item}{' ' * (20 - len(item))}${costo}")
    print("------------------------------------")
    print(f"{'Total':<20}${total}")

def main():
    espera = random.randint(0, 450)
    cliente = get_cliente()
    donde = get_donde()
    pedido = obtener_pedido()
    imprimir_ticket(espera, ubicacion(donde), cliente, pedido)

if __name__ == "__main__":
    main()
