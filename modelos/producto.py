class Producto:
    def __init__(self, id_producto: int, nombre: str, precio: float, categoria: str):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    @property
    def id_producto(self) -> int:
        return self._id_producto

    @id_producto.setter
    def id_producto(self, valor: int):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El ID del producto debe ser un entero positivo.")
        self._id_producto = valor

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("El precio debe ser un número no negativo.")
        self._precio = float(valor)

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La categoría no puede estar vacía.")
        self._categoria = valor.strip()

    def a_diccionario(self) -> dict:
        """Convierte el objeto a un diccionario compatible con JSON."""
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria
        }

    @classmethod
    def desde_diccionario(cls, datos: dict) -> 'Producto':
        """Reconstruye una instancia de Producto desde un diccionario."""
        try:
            return cls(
                id_producto=datos["id_producto"],
                nombre=datos["nombre"],
                precio=datos["precio"],
                categoria=datos["categoria"]
            )
        except KeyError as e:
            raise KeyError(f"Falta el campo obligatorio {e} en el producto.")