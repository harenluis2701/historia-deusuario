# ==========================================
# SISTEMA DE GESTIÓN DE INVENTARIO
# ==========================================
# Lista principal que almacenará los diccionarios de productos

inventario = []

def agregar_producto(inventario):
    """Solicita los datos del producto y los agrega al inventario."""
    print("\n--- Agregar Nuevo Producto ---")
    nombre = input("Ingresa el nombre del producto: ")
    
    # Validamos que el precio y cantidad sean números válidos
    try:
        precio = float(input("Ingresa el precio del producto: "))
        cantidad = int(input("Ingresa la cantidad del producto: "))
        
        # Se crea el diccionario del producto
        producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        
        # Se agrega a la lista del inventario
        inventario.append(producto)
        print(f"¡Producto '{nombre}' agregado con éxito!")
    except ValueError:
        print("Error: El precio debe ser un número y la cantidad un número entero. Inténtalo de nuevo.")

def mostrar_inventario(inventario):
    """Muestra todos los productos registrados en el inventario."""
    print("\n--- Inventario Actual ---")
    
    # Verificamos si la lista está vacía
    if not inventario:
        print("El inventario está vacío. No hay productos para mostrar.")
    else:
        # Recorremos la lista con un bucle for
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")

def calcular_estadisticas(inventario):
    """Calcula el valor total del inventario y la cantidad de productos."""
    print("\n--- Estadísticas del Inventario ---")
    
    if not inventario:
         print("El inventario está vacío. No hay estadísticas para calcular.")
         return

    total_productos = 0
    valor_total_inventario = 0.0
    
    # Recorremos el inventario para hacer los cálculos
    for producto in inventario:
        total_productos += producto['cantidad']
        valor_total_inventario += (producto['precio'] * producto['cantidad'])
        
    print(f"Cantidad total de productos registrados: {total_productos}")
    print(f"Valor total del inventario: {valor_total_inventario}")

# ==========================================
# FLUJO PRINCIPAL DEL PROGRAMA
# ==========================================



# Bucle while que mantiene el menú activo hasta que el usuario decida salir
while True:
    print("\n" + "="*30)
    print(" MENÚ DE INVENTARIO")
    print("="*30)
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")
    
    opcion = input("Elige una opción (1-4): ")
    
    # Estructuras condicionales para procesar la opción del usuario
    if opcion == '1':
        agregar_producto(inventario)
    elif opcion == '2':
        mostrar_inventario(inventario)
    elif opcion == '3':
        calcular_estadisticas(inventario)
    elif opcion == '4':
        print("\nSaliendo del sistema de inventario... ¡Hasta luego!")
        break # Rompe el bucle y finaliza el programa
    else:
        # Manejo de opciones inválidas
        print("\nError: Opción inválida. Por favor, elige un número del 1 al 4.")

# ==========================================
# OBJETIVO DE LA SEMANA RESUMIDO:
# El objetivo de este ejercicio fue aplicar exitosamente estructuras 
# condicionales (if/elif/else) y bucles (while y for) en Python, 
# utilizando listas de diccionarios para gestionar datos de un inventario,
# modularizando el código en funciones limpias y manejando validaciones básicas.
# ==========================================