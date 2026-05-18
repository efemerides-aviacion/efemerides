# Instrucciones de formato de salida para efemérides v-1.4 2026-05-17

## POLÍTICA DE IDIOMAS (NUEVO)
### Uso de términos y frases en inglés u otros idiomas diferentes al español

1. **Idioma principal del post:** El post final debe redactarse íntegramente en **español neutro**, accesible para una audiencia hispanohablante global.

2. **Excepciones permitidas para mantener inglés:**
   - **Nombres propios de personas** (ej. *John F. Kennedy*, *Charles Lindbergh*).
   - **Nombres oficiales de aeronaves** en su idioma original (ej. *Westland Sea King HC.4*, *Lockheed C-130 Hercules*).
   - **Matrículas y códigos técnicos** (ej. *ZA294*, *N12345*).
   - **Nombres de unidades militares o agencias** (ej. *Royal Navy*, *846 Naval Air Squadron*, *Special Air Service - SAS*).
   - **Topónimos oficiales** en su forma local más reconocida (ej. *Puerto Argentino / Stanley*, *Falklands* cuando se menciona junto a Malvinas).
   - **Siglas universalmente conocidas** (ej. *SAS*, *RAF*, *NASA*, *FAA*).

3. **Obligación de traducir:**
   - **Títulos, subtítulos y descripciones narrativas**: Deben redactarse en español.
   - **Frases completas o citas en inglés**: Deben traducirse al español. Se puede incluir el texto original entre paréntesis o nota a pie de página, con atribución clara.
   - **Nombres de instituciones traducibles**: Si existe una traducción establecida en español (ej. *Armada Real Británica* en lugar de *Royal Navy*), se usará la versión en español, seguida de la original solo si es relevante.
   - **Términos técnicos con equivalente en español**: Priorizar el español (ej. *despachador de vuelo* en lugar de *flight dispatcher*).

4. **Referencias y URLs:** Las fuentes pueden estar en cualquier idioma, pero el contenido del post debe explicar la información sin asumir que el lector entiende otros idiomas.

5. **Caso particular del inglés en el título del post:**
   - El título debe ser en español.
   - Si incluye un nombre propio o una matrícula en inglés, se mantiene tal cual.

### Ejemplo práctico:

| Incorrecto ❌ | Correcto ✅ |
|---------------|-------------|
| "The Westland Sea King HC.4 ZA294 crashed during a night flight." | "El Westland Sea King HC.4, matrícula ZA294, se estrelló durante un vuelo nocturno." |
| "The 846 Naval Air Squadron was operating from HMS Hermes." | "El Escuadrón Aéreo Naval 846 (846 Naval Air Squadron) operaba desde el HMS Hermes." |

---

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