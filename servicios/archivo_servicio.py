import json
import os
from modelos.producto import Producto

class ArchivoServicio:
    def __init__(self, ruta_archivo: str = "datos/productos.json"):
        self.ruta_archivo = ruta_archivo

    def guardar_productos(self, productos: list[Producto]) -> bool:
        """Serializa la lista de objetos Producto y la guarda en el archivo JSON."""
        try:
            directorio = os.path.dirname(self.ruta_archivo)
            if directorio and not os.path.exists(directorio):
                os.makedirs(directorio)

            lista_datos = [p.a_diccionario() for p in productos]
            with open(self.ruta_archivo, "w", encoding="utf-8") as f:
                json.dump(lista_datos, f, indent=4, ensure_ascii=False)
            return True
        except PermissionError:
            print(f"\n[Error de Permisos] Sin autorización de escritura en '{self.ruta_archivo}'.")
        except Exception as e:
            print(f"\n[Error de Escritura] No se guardaron los datos: {e}")
        return False

    def cargar_productos(self) -> list[Producto]:
        """Lee el JSON, valida los registros y reconstruye la lista de objetos Producto."""
        productos = []
        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
                if not isinstance(datos, list):
                    print("\n[Error de Formato] El JSON debe contener una lista de registros.")
                    return []

                for i, registro in enumerate(datos):
                    try:
                        if not isinstance(registro, dict):
                            raise ValueError("El elemento no es un diccionario válido.")
                        prod = Producto.desde_diccionario(registro)
                        productos.append(prod)
                    except (KeyError, ValueError) as e:
                        print(f"[Aviso] Registro #{i+1} descartado por datos no válidos: {e}")

        except FileNotFoundError:
            print(f"\n[Aviso] No se encontró '{self.ruta_archivo}'. Se iniciará con una lista vacía.")
        except json.JSONDecodeError:
            print(f"\n[Error] El archivo '{self.ruta_archivo}' contiene un JSON corrupto o no válido.")
        except PermissionError:
            print(f"\n[Error de Permisos] Sin autorización de lectura en '{self.ruta_archivo}'.")
        
        return productos