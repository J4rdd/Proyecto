print("Bienvenido al nuestro proyecto")
print("Segundo avance")
# Sistema básico para la Tienda de Decoraciones - Aporte

# Diccionarios simulando tablas de la base de datos
trabajadores = [
    {"id": 1, "nombre": "Juan Pérez", "rol": "Decorador", "hora_entrada": "09:00", "hora_salida": "18:00"},
    {"id": 2, "nombre": "Ana López", "rol": "Vendedora", "hora_entrada": "10:00", "hora_salida": "19:00"}
]

productos = [
    {"id": 1, "nombre": "Globo metálico", "stock": 50, "precio": 2.5},
    {"id": 2, "nombre": "Guirnalda", "stock": 20, "precio": 5.0}
]

pedidos = []


# Funciones principales
def registrar_pedido(id_cliente, productos_pedido):
    total = 0
    for item in productos_pedido:
        for prod in productos:
            if prod["id"] == item["id_producto"]:
                if prod["stock"] >= item["cantidad"]:
                    prod["stock"] -= item["cantidad"]
                    subtotal = item["cantidad"] * prod["precio"]
                    total += subtotal
                else:
                    print(f"No hay suficiente stock de {prod['nombre']}")
    pedido = {"id_cliente": id_cliente, "productos": productos_pedido, "total": total}
    pedidos.append(pedido)
    print("✅ Pedido registrado:", pedido)


def mostrar_inventario():
    print("\n📦 Inventario actual:")
    for p in productos:
        print(f"- {p['nombre']}: {p['stock']} unidades disponibles")


# Ejemplo de ejecución
print("=== Sistema de Tienda de Decoraciones (Aporte) ===")
mostrar_inventario()

registrar_pedido(101, [{"id_producto": 1, "cantidad": 3}, {"id_producto": 2, "cantidad": 1}])

mostrar_inventario()
