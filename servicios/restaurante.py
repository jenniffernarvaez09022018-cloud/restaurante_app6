from modelos.producto import Producto

class Restaurante:
    def __init__(self):
        self.productos: list[Producto] = []

    def establecer_productos(self, productos: list[Producto]):
        self.productos = productos

    def obtener_productos(self) -> list[Producto]:
        return self.productos

    def registrar_producto(self, producto: Producto) -> bool:
        if any(p.id_producto == producto.id_producto for p in self.productos):
            raise ValueError(f"El ID {producto.id_producto} ya pertenece a otro producto.")
        self.productos.append(producto)
        return True

    def buscar_producto(self, id_producto: int) -> Producto | None:
        for p in self.productos:
            if p.id_producto == id_producto:
                return p
        return None

    def actualizar_producto(self, id_producto: int, nombre: str, precio: float, categoria: str) -> bool:
        prod = self.buscar_producto(id_producto)
        if not prod:
            return False
        prod.nombre = nombre
        prod.precio = precio
        prod.categoria = categoria
        return True

    def eliminar_producto(self, id_producto: int) -> bool:
        prod = self.buscar_producto(id_producto)
        if prod:
            self.productos.remove(prod)
            return True
        return False