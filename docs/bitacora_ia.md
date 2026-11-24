# Bitácora de Uso de IA

**Estudiante:** Augusto Sandoval
**Variante:** A
**Proyecto:** Sistema Sabor Valluno

| N.º | Fecha | Herramienta | Tipo de uso | Consulta textual (resumen) | Qué acepté | Qué modifiqué y por qué | Archivo o clase | ¿Lo explico sin ayuda? |
|---|---|---|---|---|---|---|---|---|
| 1 | 18/11 | ChatGPT | Error | "Por qué sale ModuleNotFoundError: No module named 'modelo'" | La explicación de cómo funcionan las carpetas en Python (crear el `__init__.py` y ordenar los archivos). | Moví los archivos para que la estructura coincida con mis importaciones. | Estructura general | Sí |
| 2 | 19/11 | ChatGPT | Concepto | "Cómo evitar que un Combo se agregue a sí mismo en Python" | La validación `if producto == self`. | Adapté el mensaje de error para que sea más claro para el usuario. | `modelo/productos.py` | Sí |
| 3 | 20/11 | ChatGPT | Revisión | "Cómo aplicar polimorfismo en el cálculo de envases sin usar isinstance" | El uso de `sum(p.contar_platos() for p in self._productos)` | Lo integré en la clase PedidoLlevar para que cuente los platos de los combos. | `modelo/pedidos.py` | Sí |
| 4 | 21/11 | ChatGPT | Generación | "Cómo hacer un menú de consola interactivo en Python" | La estructura básica de `while True` con `input()`. | Le agregué las validaciones de las opciones y la lógica de pago. | `main.py` | Sí |

**Declaración:** Declaro que este registro incluye uso de IA en el proyecto y que puedo explicar el código que entrego.