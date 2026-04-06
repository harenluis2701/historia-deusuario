
import csv
import os

def guardar_csv(inventario, ruta, incluir_header=True):
    """Guarda el inventario actual en un archivo CSV."""
    if not inventario:
        print("\nError: El inventario está vacío. No hay nada que guardar.")
        return False

    try:
        with open(ruta, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            if incluir_header:
                escritor.writerow(['nombre', 'precio', 'cantidad'])
            
            for p in inventario:
                escritor.writerow([p['nombre'], p['precio'], p['cantidad']])
        
        print(f"\nInventario guardado exitosamente en: {ruta}")
        return True
    
    except PermissionError:
        print(f"\nError de permisos: No se puede escribir en {ruta}. Archivo abierto o protegido.")
    except Exception as e:
        print(f"\nError inesperado al guardar: {e}")
    
    return False

def extraer_datos_csv(ruta):
    """
    Lee un archivo CSV, valida sus filas y extrae los productos válidos.
    
    Retorna:
        tuple: (lista de productos válidos, número de filas con errores)
    """
    productos_cargados = []
    filas_invalidas = 0

    try:
        with open(ruta, mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            encabezado = next(lector, None) # Saltar encabezado

            for linea in lector:
                if len(linea) != 3:
                    filas_invalidas += 1
                    continue
                
                try:
                    nombre = linea[0].strip()
                    precio = float(linea[1])
                    cantidad = int(linea[2])

                    if precio < 0 or cantidad < 0 or not nombre:
                        raise ValueError("Valores negativos o nombre vacío")

                    productos_cargados.append({
                        "nombre": nombre.lower(),
                        "precio": precio,
                        "cantidad": cantidad
                    })
                except ValueError:
                    filas_invalidas += 1

        return productos_cargados, filas_invalidas

    except FileNotFoundError:
        print(f"\nError: No se encontró el archivo '{ruta}'.")
    except UnicodeDecodeError:
        print(f"\nError: Formato de archivo no soportado (error de codificación en '{ruta}').")
    except Exception as e:
        print(f"\nError inesperado al cargar: {e}")
    
    return None, 0