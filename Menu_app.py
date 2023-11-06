import locale

# Función para agregar una compra
def agregar_compra(lista_compras, monto):
    lista_compras.append(monto)
    print(f"Compra de ${monto:.2f} agregada correctamente.")
    return monto

# Función para mostrar las compras
def mostrar_compras(lista_compras):
    if not lista_compras:
        print("No hay compras registradas.")
    else:
        print("Listado de compras:")
        for i, compra in enumerate(lista_compras, 1):
            print(f"Compra {i}: ${compra:.2f}")

# Función para mostrar el total gastado
def mostrar_total(lista_compras):
    if not lista_compras:
        print("No hay compras registradas.")
    else:
        total = sum(lista_compras)
        total_formateado = locale.currency(total, grouping=True)
        print(f"Total gastado: {total_formateado}")

# Inicialización de la lista de compras
compras = []

# Funcion para formato Peso Chileno
locale.setlocale(locale.LC_ALL, 'es_CL.UTF-8')

while True:
    print("\nMenú:")
    print("1. Agregar compra")
    print("2. Mostrar compras")
    print("3. Mostrar total gastado")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        monto = float(input("Ingrese el monto de la compra: "))
        agregar_compra(compras, monto)
    elif opcion == "2":
        mostrar_compras(compras)
    elif opcion == "3":
        mostrar_total(compras)
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
