
nombre = input("Ingresa el nombre del producto: ")# pedimos el nombre del producto


p_ok = False
while p_ok == False:
    p_txt = input("Ingresa el precio: ")
    
    # Revisamos si el texto es un numero (escondemos el punto decimal un segundo para revisar)
    if p_txt.replace(".", "", 1).isdigit(): 
        p = float(p_txt) # Si es un numero, lo convertimos a float
        p_ok = True      # Cambiamos a True para salir del bucle
    else:
        print("Error: El precio debe ser numérico. Intenta de nuevo.")

# Bucle para validar la cantidad (Se repite si hay error)
c_ok = False
while c_ok == False:
    c_txt = input("Ingresa la cantidad: ")
    
    # .isdigit() revisa si el texto ingresado tiene solo numeros enteros
    if c_txt.isdigit():
        c = int(c_txt) # Si es entero, lo convertimos a int
        c_ok = True    # Cambiamos a True para salir del bucle
    else:
        print("Error: La cantidad debe ser un número entero. Intenta de nuevo.")

# Calcular el costo total (Operacion matematica)
costo_total = p * c

# Mostrar resultados en consola
print("Producto:", nombre , "| Precio: " , p ," | Cantidad:", c, "| Total:" , costo_total)

# COMENTARIO GENERAL:
# Este programa registra un producto en el inventario pidiendo su nombre, precio y cantidad.
# Utiliza ciclos y condicionales para asegurar que los datos ingresados sean numeros validos.
# Finalmente, calcula el costo total multiplicando precio por cantidad y muestra el resumen.

