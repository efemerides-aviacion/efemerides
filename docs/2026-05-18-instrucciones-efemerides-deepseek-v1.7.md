# Instrucciones de formato de salida para efemérides v-1.7 2026-05-18

## POLÍTICA DE IDIOMAS
### Uso de términos, frases y referencias en otros idiomas

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

4. **Idiomas permitidos en las Referencias verificadas:**
   - La sección `## Referencias verificadas` solo podrá incluir enlaces a fuentes redactadas en **español** o en **inglés**.
   - No se aceptarán referencias en ruso, chino, japonés, árabe, francés, alemán, portugués, italiano ni ningún otro idioma diferente al español o inglés.
   - **Excepción:** Si una fuente en otro idioma es la única que contiene un dato crítico y absolutamente indispensable, se podrá incluir siempre que:
     - Se advierta con la etiqueta `[NO CONFIRMADO]` (si el dato no está verificado) o
     - Se acompañe de una nota aclaratoria que explique su contenido en español.
   - Esta excepción debe usarse con extrema moderación y solo cuando no exista alternativa en español o inglés.

5. **Caso particular del inglés en el título del post:**
   - El título debe ser en español.
   - Si incluye un nombre propio o una matrícula en inglés, se mantiene tal cual.

6. **Restricción adicional de coherencia:** Si durante la investigación previa se localizan fuentes en otros idiomas (ej. ruso, chino, francés), estas podrán usarse internamente para verificar datos, pero **no deberán incluirse** en la lista de referencias del post final. En su lugar, se buscará una fuente equivalente en español o inglés que respalde el mismo dato.

### Ejemplo práctico:

| Incorrecto ❌ | Correcto ✅ |
|---------------|-------------|
| "The Westland Sea King HC.4 ZA294 crashed during a night flight." | "El Westland Sea King HC.4, matrícula ZA294, se estrelló durante un vuelo nocturno." |
| "The 846 Naval Air Squadron was operating from HMS Hermes." | "El Escuadrón Aéreo Naval 846 (846 Naval Air Squadron) operaba desde el HMS Hermes." |
| Referencia: `letopis.by` (en ruso) | Referencia: `Russia Beyond` (en inglés) |
| Referencia: `Wikipedia ZH` (en chino) | (eliminada, buscar alternativa en inglés/español) |

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

9. **Verificación obligatoria de URLs en referencias:**
   - Antes de incluir cualquier URL en la sección `## Referencias verificadas`, el asistente debe **verificar explícitamente** que el contenido de esa página corresponde al tema de la efeméride.
   - **Procedimiento obligatorio:**
     - Leer el título del artículo en la URL.
     - Confirmar que el título contiene el nombre del protagonista, la aeronave o el evento relevante.
     - Si el título no coincide, **descartar la URL inmediatamente**.
   - **Casos de rechazo automático:**
     - URLs cuyo contenido sea sobre política, guerra actual, vehículos terrestres, o temas no relacionados con la aviación o la efeméride específica.
     - URLs que redirijan a páginas de error, contenido genérico o portales sin artículo específico.
   - **Consecuencia de no verificar:** Incluir una URL no relacionada invalida automáticamente el producto final, al igual que los marcadores `[citation:X]`.

   **Ejemplos de URLs que deben ser rechazadas:**
   - `pravdareport.com/russia/120344-maresyev` → (artículo sobre Obama, Siria y Rusia, no sobre Marésiev)
   - `topwar.ru/214090-aleksej-maresev-chelovek-i-letchik-legenda-otechestvennoj-aviacii.html` → (artículo sobre Ucrania y blindados Rosomak, no sobre Marésiev)

10. **Notas aclaratorias (NUEVO):**
    - **Cuándo deben incluirse:**
      - Cuando existan **discrepancias entre fuentes** (cifras, fechas, nombres, lugares).
      - Cuando un **dato relevante no pudo ser verificado** y se incluye con `[NO CONFIRMADO]`.
      - Cuando sea necesario **matizar una clasificación** (ej. seguridad vs. accidente).
      - Cuando haya **contexto adicional imprescindible** para entender el evento.
    - **Formato obligatorio:**
      ```html
      <div class="note-box">
        <p><strong>Nota aclaratoria:</strong> [Texto de la aclaración].</p>
      </div>

      Ubicación: Inmediatamente después de ## Referencias verificadas y antes de ## Metadatos de Control.

    - Ejemplos extraídos de la plantilla maestra:

        - aviacion-fundacion (Airbus): "Algunas fuentes secundarias mencionan el acuerdo ministerial de 1969 como 'fundación', pero la constitución legal del GIE ocurrió el 18 de diciembre de 1970. La hora exacta de la firma no pudo ser verificada."  
        - aviacion-espacial (John Glenn): "La alarma sobre el escudo térmico resultó ser falsa; Glenn mantuvo la calma y completó la reentrada con éxito."  
        - aviacion-seguridad (EgyptAir): "Aunque este hecho terminó con un accidente y fatalidades, su naturaleza corresponde a un incidente de seguridad en la aviación (secuestro/terrorismo), no a un accidente aeronáutico."  