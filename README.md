# Restaurante App - Persistencia JSON (Semana 10)

**Estudiante:** Jenniffer Elizabeth Achina Narvaez

## Descripción del Sistema
Evolución del sistema de gestión `restaurante_app` que incorpora la persistencia de productos en formato JSON mediante `ArchivoServicio` y manejo específico de excepciones en operaciones de entrada/salida.

## Estructura del Proyecto
```text
restaurante_app/
│
├── datos/
│   └── productos.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md