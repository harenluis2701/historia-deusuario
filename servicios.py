
def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un nuevo producto al inventario.
    
    Args:
        inventario (list): Lista de diccionarios con el inventario actual.
        nombre (str): Nombre del producto.
        precio (float): Precio unitario.
        cantidad (int): Unidades en stock.
    """
    inventario.append({
        "nombre": nombre.strip().lower(),
        "precio": float(precio),
        "cantidad": int(cantidad)
    })

def mostrar_inventario(inventario):
    """Muestra todos los productos del inventario en formato tabla."""
    if not inventario:
        print("\nEl inventario está vacío.")
        return
    
    print("\n--- INVENTARIO ACTUAL ---")
    print(f"{'NOMBRE':<20} | {'PRECIO':<10} | {'CANTIDAD':<10}")
    print("-" * 45)
    for p in inventario:
        print(f"{p['nombre'].title():<20} | ${p['precio']:<9.2f} | {p['cantidad']:<10}")
    print("-" * 45)

def buscar_producto(inventario, nombre):
    """
    Busca un producto por su nombre.
    
    Retorna:
        dict: El producto si se encuentra, None en caso contrario.
    """
    nombre_buscado = nombre.strip().lower()
    for p in inventario:
        if p["nombre"] == nombre_buscado:
            return p
    return None

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """Actualiza el precio y/o cantidad de un producto existente."""
    producto = buscar_producto(inventario, nombre)
    if producto:
        if nuevo_precio is not None:
            producto["precio"] = float(nuevo_precio)
        if nueva_cantidad is not None:
            producto["cantidad"] = int(nueva_cantidad)
        return True
    return False

def eliminar_producto(inventario, nombre):
    """Elimina un producto del inventario por su nombre."""
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        return True
    return False

def calcular_estadisticas(inventario):
    """
    Calcula y retorna estadísticas clave del inventario.
    
    Retorna:
        dict: Diccionario con unidades totales, valor total, producto más caro y con mayor stock.
    """
    if not inventario:
        return None

    unidades_totales = sum(p["cantidad"] for p in inventario)
    
    # Uso de lambda para calcular el subtotal (precio * cantidad) de cada producto
    subtotal = lambda p: p["precio"] * p["cantidad"]
    valor_total = sum(subtotal(p) for p in inventario)
    
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "mas_caro": producto_mas_caro,
        "mayor_stock": producto_mayor_stock
    }