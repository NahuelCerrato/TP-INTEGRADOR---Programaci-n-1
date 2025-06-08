# Importamos la lista de productos desde el archivo bd_productos.py
from bd_productos import productos

# -------- FUNCIÓN DE BÚSQUEDA LINEAL --------
# Busca un producto por su código dentro de la lista
def busqueda_lineal(lista, codigo_buscado):
    for producto in lista:  # Recorremos todos los productos
        if producto["CODIGO"] == codigo_buscado:  # Si encontramos coincidencia
            return producto  # Lo devolvemos
    return None  # Si no se encuentra, devolvemos None

# -------- FUNCIÓN DE ORDENAMIENTO (BUBBLE SORT) --------
# Ordena la lista por el atributo que le pasemos (clave)
def bubble_sort(lista, clave):
    lista_ordenada = lista.copy()  # Hacemos una copia para no modificar la original
    n = len(lista_ordenada)  # Cantidad de elementos en la lista

    for i in range(n):  # Realizamos n pasadas
        for j in range(0, n - i - 1):  # Comparamos elementos consecutivos
            a = lista_ordenada[j][clave]  # Valor actual (por la clave indicada)
            b = lista_ordenada[j + 1][clave]  # Valor siguiente

            if a is None:
                continue  # Si el valor actual es None, lo salteamos

            # Si el siguiente es None o el actual es mayor, intercambiamos
            if b is None or a > b:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]

    return lista_ordenada  # Devolvemos la lista ordenada

# -------- FUNCIÓN PARA MOSTRAR LOS PRODUCTOS --------
# Imprime cada producto de la lista en una línea
def mostrar_productos(lista):
    for p in lista:
        print(f"{p['CODIGO']} - {p['NOMBRE']} | ${p['PRECIO']} | STOCK: {p['STOCK']}")

# -------- MENÚ PRINCIPAL --------
# Función principal con menú interactivo en consola
def menu():
    while True:
        # Mostramos opciones disponibles
        print("\nMENÚ DE OPCIONES")
        print("1. Buscar producto por código")
        print("2. Ordenar productos por PRECIO (Bubble Sort)")
        print("3. Ordenar productos por STOCK (Bubble Sort)")
        print("4. Salir")

        # Leemos la opción elegida
        opcion = input("Seleccione una opción: ").strip()

        # -------- OPCIÓN 1: Buscar producto --------
        if opcion == "1":
            codigo = input("\nIngrese el código del producto: ").strip().upper()
            resultado = busqueda_lineal(productos, codigo)
            if resultado:
                print(f"Producto encontrado: {resultado['NOMBRE']}")
                print(f"Precio: ${resultado['PRECIO']}")
                stock = resultado["STOCK"]
                if stock is None:
                    print("Este producto no tiene control de stock.")
                elif stock > 0:
                    print(f"Stock disponible: {stock}")
                else:
                    print("Sin stock disponible.")
            else:
                print("Producto no encontrado.")

        # -------- OPCIÓN 2: Ordenar por PRECIO --------
        elif opcion == "2":
            print("\nLista ordenada por PRECIO (menor a mayor):")
            ordenado = bubble_sort(productos, "PRECIO")
            mostrar_productos(ordenado)

        # -------- OPCIÓN 3: Ordenar por STOCK --------
        elif opcion == "3":
            print("\nLista ordenada por STOCK (menor a mayor):")
            ordenado = bubble_sort(productos, "STOCK")
            mostrar_productos(ordenado)

        # -------- OPCIÓN 4: Salir --------
        elif opcion == "4":
            print("\nGracias por usar el programa. Hasta luego.")
            break  # Sale del bucle while y termina el programa

        # -------- Opción inválida --------
        else:
            print("Opción inválida. Intente nuevamente.")

# -------- EJECUCIÓN DEL MENÚ --------
# Si este archivo es el principal, ejecuta el menú
if __name__ == "__main__":
    menu()
