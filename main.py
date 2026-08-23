from modelos.producto import Producto
from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio

def mostrar_menu():
    print("\n--- GESTIÓN DE RESTAURANTE ---")
    print("1. Listar productos")
    print("2. Registrar producto")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    return input("Seleccione una opción: ")

def main():
    restaurante = Restaurante()
    archivo_servicio = ArchivoServicio("datos/productos.json")

    # Carga inicial de productos al arrancar la aplicación
    productos_cargados = archivo_servicio.cargar_productos()
    restaurante.establecer_productos(productos_cargados)

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            prods = restaurante.obtener_productos()
            if not prods:
                print("\nNo existen productos en el sistema.")
            else:
                print("\n--- CATÁLOGO DE PRODUCTOS ---")
                for p in prods:
                    print(f"ID: {p.id_producto} | Nombre: {p.nombre} | Precio: ${p.precio:.2f} | Categoría: {p.categoria}")

        elif opcion == "2":
            try:
                id_p = int(input("ID del producto: "))
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                categoria = input("Categoría: ")

                nuevo_prod = Producto(id_p, nombre, precio, categoria)
                if restaurante.registrar_producto(nuevo_prod):
                    archivo_servicio.guardar_productos(restaurante.obtener_productos())
                    print("\n¡Producto guardado correctamente en el archivo JSON!")
            except ValueError as e:
                print(f"\n[Error de Entrada]: {e}")

        elif opcion == "3":
            try:
                id_p = int(input("Ingrese el ID a buscar: "))
                prod = restaurante.buscar_producto(id_p)
                if prod:
                    print(f"\nEncontrado -> ID: {prod.id_producto} | Nombre: {prod.nombre} | Precio: ${prod.precio:.2f} | Categoría: {prod.categoria}")
                else:
                    print("\nProducto no encontrado.")
            except ValueError:
                print("\n[Error] El ID debe ser un entero.")

        elif opcion == "4":
            try:
                id_p = int(input("ID del producto a actualizar: "))
                if not restaurante.buscar_producto(id_p):
                    print("\nProducto no encontrado.")
                    continue

                nombre = input("Nuevo nombre: ")
                precio = float(input("Nuevo precio: "))
                categoria = input("Nueva categoría: ")

                if restaurante.actualizar_producto(id_p, nombre, precio, categoria):
                    archivo_servicio.guardar_productos(restaurante.obtener_productos())
                    print("\n¡Producto actualizado y guardado en JSON!")
            except ValueError as e:
                print(f"\n[Error de Entrada]: {e}")

        elif opcion == "5":
            try:
                id_p = int(input("ID del producto a eliminar: "))
                if restaurante.eliminar_producto(id_p):
                    archivo_servicio.guardar_productos(restaurante.obtener_productos())
                    print("\n¡Producto eliminado del sistema y actualizado en JSON!")
                else:
                    print("\nProducto no encontrado.")
            except ValueError:
                print("\n[Error] El ID debe ser un entero.")

        elif opcion == "6":
            print("\n¡Saliendo de la aplicación!")
            break
        else:
            print("\nOpción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()