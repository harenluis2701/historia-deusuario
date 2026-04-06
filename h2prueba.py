# app.py
import servicios
import archivos

def solicitar_flotante(mensaje):
    """Asegura que el usuario ingrese un número flotante válido y positivo."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("El valor no puede ser negativo. Intenta de nuevo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor ingresa un número.")

def solicitar_entero(mensaje):
    """Asegura que el usuario ingrese un número entero válido y positivo."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("El valor no puede ser negativo. Intenta de nuevo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor ingresa un número entero.")

def main():
    inventario = []

    while True:
        print("\n" + "="*30)
        print("SISTEMA DE INVENTARIO")
        print("="*30)
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Estadísticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir")
        print("="*30)

        opcion = input("Elige una opción (1-9): ").strip()

        if opcion == '1':
            nombre = input("Nombre del producto: ")
            precio = solicitar_flotante("Precio del producto: ")
            cantidad = solicitar_entero("Cantidad en stock: ")
            
            if servicios.buscar_producto(inventario, nombre):
                print("\nEse producto ya existe. Usa la opción 4 para actualizarlo.")
            else:
                servicios.agregar_producto(inventario, nombre, precio, cantidad)
                print(f"\nProducto '{nombre}' agregado con éxito.")

        elif opcion == '2':
            servicios.mostrar_inventario(inventario)

        elif opcion == '3':
            nombre = input("Ingresa el nombre a buscar: ")
            prod = servicios.buscar_producto(inventario, nombre)
            if prod:
                print(f"\nEncontrado: {prod['nombre'].title()} | Precio: ${prod['precio']:.2f} | Stock: {prod['cantidad']}")
            else:
                print(f"\nProducto '{nombre}' no encontrado.")

        elif opcion == '4':
            nombre = input("Nombre del producto a actualizar: ")
            if servicios.buscar_producto(inventario, nombre):
                print("Deja en blanco si no deseas cambiar el valor.")
                n_precio = input("Nuevo precio: ")
                n_cantidad = input("Nueva cantidad: ")
                
                # Validar inputs vacíos antes de enviar
                n_precio = float(n_precio) if n_precio.strip() else None
                n_cantidad = int(n_cantidad) if n_cantidad.strip() else None
                
                servicios.actualizar_producto(inventario, nombre, n_precio, n_cantidad)
                print(f"\nProducto '{nombre}' actualizado.")
            else:
                print(f"\nProducto '{nombre}' no encontrado.")

        elif opcion == '5':
            nombre = input("Nombre del producto a eliminar: ")
            if servicios.eliminar_producto(inventario, nombre):
                print(f"\nProducto '{nombre}' eliminado.")
            else:
                print(f"\nProducto '{nombre}' no encontrado.")

        elif opcion == '6':
            stats = servicios.calcular_estadisticas(inventario)
            if stats:
                print("\nESTADÍSTICAS DEL INVENTARIO")
                print(f"Unidades totales en stock : {stats['unidades_totales']}")
                print(f"Valor total del inventario: ${stats['valor_total']:.2f}")
                print(f"Producto más caro         : {stats['mas_caro']['nombre'].title()} (${stats['mas_caro']['precio']:.2f})")
                print(f"Producto con mayor stock  : {stats['mayor_stock']['nombre'].title()} ({stats['mayor_stock']['cantidad']} uds)")
            else:
                print("\nNo hay datos para calcular estadísticas.")

        elif opcion == '7':
            ruta = input("Ingresa el nombre del archivo para guardar (ej. datos.csv): ")
            if not ruta.endswith('.csv'): ruta += '.csv'
            archivos.guardar_csv(inventario, ruta)

        elif opcion == '8':
            ruta = input("Ingresa la ruta del archivo a cargar (ej. datos.csv): ")
            if not ruta.endswith('.csv'): ruta += '.csv'
            
            nuevos_productos, errores = archivos.extraer_datos_csv(ruta)
            
            if nuevos_productos is not None:
                print(f"\nSe encontraron {len(nuevos_productos)} productos válidos.")
                if errores > 0:
                    print(f"{errores} filas inválidas fueron omitidas.")
                
                decision = input("¿Sobrescribir el inventario actual? (S/N): ").strip().upper()
                
                if decision == 'S':
                    inventario.clear()
                    inventario.extend(nuevos_productos)
                    print("\nInventario sobrescrito con éxito.")
                else:
                    # Lógica de fusión: Si existe suma cantidad y actualiza precio al más reciente
                    for np in nuevos_productos:
                        existente = servicios.buscar_producto(inventario, np["nombre"])
                        if existente:
                            nueva_cant = existente["cantidad"] + np["cantidad"]
                            servicios.actualizar_producto(inventario, np["nombre"], nuevo_precio=np["precio"], nueva_cantidad=nueva_cant)
                        else:
                            inventario.append(np)
                    print("\nInventario fusionado con éxito (cantidades sumadas, precios actualizados).")

        elif opcion == '9':
            print("\nSaliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("\nOpción no válida. Por favor, selecciona un número del 1 al 9.")

if __name__ == "__main__":
    main()