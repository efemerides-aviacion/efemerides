# Instrucciones de formato de salida para efemérides v-1.3 2026-05-06

1. El producto final debe entregarse dentro de un bloque Markdown (triple backticks con "markdown").

2. No incluir ningún marcador de cita del tipo "[citation:X]" ESTO ES SUMAMENTE IMPORTANTE QUE SE CUMPLA.

3. No incluir números de cita como "[5]", "[6]" dentro del texto.

4. No incluir la etiqueta "[VERIFICADO]" en ningún lugar del documento. La inclusión de un dato implica que ya fue verificado. Solo se permite "[NO CONFIRMADO]" cuando excepcionalmente un dato relevante no pudo ser verificado pero se incluye con esa advertencia.

5. Al final del documento, incluir un bloque aparte con el mensaje de COMMIT PARA GITHUB DESKTOP.

6. El mensaje de commit debe seguir el formato:
   - Título: "feat(efemerides): [descripción breve]"
   - Cuerpo: viñetas con los hitos principales
   - Línea final: "Categoría: [categoría]" y "País: [país]"

7. **Formato de cifras numéricas:**
   - Para separar los miles: se usará el **punto (.)**
   - Para los decimales: se usará la **coma (,)**
   - Ejemplo correcto: "2.408 millas" (dos mil cuatrocientas ocho)
   - Ejemplo correcto con decimal: "18,15 horas" (dieciocho coma quince)
   - Ejemplo incorrecto: "2,408 millas" o "18.15 horas"

8. **Prohibición de marcadores automáticos:** Al copiar o parafrasear información de fuentes externas, se deben eliminar manualmente todos los marcadores del tipo "[citation:X]", "[1]", "[2]", etc. ANTES de entregar el documento final. La presencia de estos marcadores invalida automáticamente el producto.