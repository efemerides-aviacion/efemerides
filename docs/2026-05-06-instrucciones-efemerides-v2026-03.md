# Documento de Instrucciones Editoriales para Efemérides de Aviación
> Última actualización: 2026-05-06 Versión: v2026-03

---

## PRINCIPIO FUNDAMENTAL DE INTEGRIDAD
**Regla de oro:** Solo incluir información verificada en fuentes confiables. La ausencia de datos es preferible a la invención o deducción.

---

## FORMATO DE LA SOLICITUD DEL USUARIO

El usuario proporcionará la información de la efeméride en formato **Markdown**, utilizando la siguiente estructura mínima:

```markdown
# Efeméride

## Fecha
AAAA-MM-DD

## Tema
[Descripción breve del evento/personaje]

## Categoría
[aviacion-nacimiento / aviacion-evento / aviacion-fundacion / aviacion-accidente / aviacion-seguridad / aviacion-supervivencia / aviacion-espacial]

## Archivo del post
AAAA-MM-DD-nombre-del-archivo.md

## Título del post
(Opcional: si se deja en blanco, el asistente lo generará automáticamente)

## Imagen
AAAA-MM-DD-nombre-de-la-imagen.webp

## Pie de foto
[Descripción de la imagen con fuente]

## Referencias
- [NombreFuente - Título](URL)
- [NombreFuente - Título](URL)

## Información relevante
[Datos clave: lugar, aeronaves, protagonistas, cifras importantes]

## Información previa
[Contexto anterior al evento: qué existía antes, qué motivó que sucediera]

## Resumen ejecutivo (borrador)
[Párrafo de 3-5 líneas con lo más importante]

## Información adicional
[Datos complementarios que no encajan en las secciones anteriores]

## Nota importante (opcional)
[Aclaraciones sobre fechas, nombres o discrepancias entre fuentes]
```

### Campos opcionales (si aplica al tema):

```markdown
## Desarrollo cronológico (opcional)
- **AAAA-MM-DD:** Hito 1
- **AAAA-MM-DD:** Hito 2

## Victorias acreditadas (solo para ases de aviación)
- **Victorias confirmadas:** [número]
- **Victorias probables:** [número]
- **Controversias:** [explicación]
```

**Nota:** El asistente investigará y completará todas las secciones faltantes del post final (Contexto Histórico, Desarrollo Cronológico detallado, Consecuencias e Impacto, Legado, etc.) basándose en la información proporcionada y en fuentes adicionales verificadas.

---

## CRITERIO DE SUSPENSIÓN
Si no se encuentran al menos 2 fuentes primarias verificables que confirmen fecha, lugar, protagonistas y aeronave, se detiene la generación y se reporta:

> "Información insuficiente para generar efeméride verificable. Datos faltantes: [especificar]. Se requiere investigación adicional."

---

## FASE DE INVESTIGACIÓN PREVIA
1. Buscar fuentes primarias recientes.  
2. Verificar datos críticos contra al menos 4 fuentes independientes.  
3. Resolver discrepancias en fechas, nombres y cifras.  
4. Documentar actualizaciones relevantes.  
5. Insertar URL directo y funcional en la sección de referencias.  
6. Validar imágenes contra repositorios históricos.  
7. Documentar explícitamente los datos no verificados.  
8. **Si el usuario deja el campo "Título del post" en blanco, generar un título siguiendo el formato estándar: "Efemérides de Aviación | [Fecha] | [Descripción concisa del evento]".**

---

## ESTRUCTURA OBLIGATORIA DEL DOCUMENTO (POST FINAL)

### Bloque 1: Documento principal

1. **YAML inicial**  
   Incluye:  
   - `layout`  
   - `title`  
   - `date`  
   - `categories`  
   - `author`  
   - `pais` (sin tilde)  
   - `operator` (si aplica)  
   - `excerpt` 
   - `image`

2. **Bloque de imagen**  
   ```html
   <figure>
     <img class="post-image" src="{{ site.baseurl }}/assets/img/[imagen].webp" alt="[Tema]">
     <figcaption class="post-caption">[Descripción de la imagen]</figcaption>
   </figure>
   ```

3. **Resumen ejecutivo**  
   - 3–5 líneas máximo, solo datos verificados.  

4. **Datos técnicos e históricos**  
   - Lista con viñetas de los datos clave del evento (fechas, lugares, aeronaves, protagonistas, cifras).
   - **IMPORTANTE:** No incluir etiquetas como `[VERIFICADO]`, `[FUENTE ÚNICA]` o `[NO CONFIRMADO]` en el texto visible del post.
   - La verificación de cada dato es una condición obligatoria del proceso editorial, pero no debe ser visible para el lector.
   - Si un dato relevante no pudo ser confirmado, se omite de la lista o se explica en la Nota Aclaratoria.

5. **Cuerpo principal – Secciones temáticas**  
   - Contexto histórico (con párrafo introductorio y subtítulos: Entorno social, Entorno tecnológico, Entorno cultural)
   - Desarrollo cronológico de los hechos
   - Consecuencias e impacto
   - Estado actual / legado
   - **REGLAS OBLIGATORIAS PARA TÍTULOS Y SUBTÍTULOS:**
     - Ningún título (sea nivel 2 `##` o nivel 3 `###`) puede aparecer sin un párrafo introductorio inmediatamente debajo de él.
     - El párrafo introductorio debe tener al menos 2 líneas de texto y debe servir como enlace temático con el contenido del título.
     - **Excepciones:** Los títulos `## Datos verificados del evento` y `## Referencias verificadas` pueden ir seguidos directamente de su contenido (lista con viñetas o bloque HTML), sin necesidad de párrafo introductorio.

6. **Referencias verificadas**  
   Formato estándar:
   ```html
   <div class="references">
     <ul>
       <li><a href="[URL]">Fuente 1</a></li>
       <li><a href="[URL]">Fuente 2</a></li>
       <li><a href="[URL]">Fuente 3</a></li>
     </ul>
   </div>
   ```

7. **Metadatos de Control**  
   - Timestamp de verificación  
   - Fuentes primarias consultadas  
   - Discrepancias resueltas  
   - Nivel de confianza (Alto/Medio/Bajo)  
   - Cláusula final de transparencia:  
     “Cuando una afirmación relevante no pudo ser confirmada, se omitió o se marcó como [NO CONFIRMADO]”.

---

## JERARQUÍA DE TÍTULOS
- Título 1: Efeméride principal  
- Título 2: Secciones mayores  
- Título 3: Subdivisiones temáticas  

---

## OPTIMIZACIÓN DE LECTURA
- Longitud máxima: ~1,200 palabras.  
- Párrafos de 5–6 líneas máximo.  
- Uso de listas y viñetas para claridad.  
- Tono respetuoso y profesional.
- Las cifras de medidas deben usar el punto (.) como separadores de miles y la coma (,) como separador de decimales  

---

## CONSIDERACIONES ÉTICAS
- Imparcialidad en eventos controvertidos.  
- Diferenciar hechos confirmados de teorías.  
- Evitar sensacionalismo.  
- Respeto en casos con víctimas.  

---

## PROHIBICIONES ABSOLUTAS
- No inventar ni deducir datos faltantes.  
- No usar URLs ficticias o marcadores de posición.  
- No redondear cifras técnicas sin indicarlo.  
- No atribuir citas sin fuente directa.  
- **No incluir marcadores como `[citation:X]`, `[1]`, `[2]` en el texto del post final.** ESTO ES SUMAMENTE IMPORTANTE QUE SE CUMPLA.

---

## CHECKLIST FINAL
- [ ] Todos los datos tienen fuente identificable.  
- [ ] URLs verificadas y funcionales (no se aceptan enlaces rotos).  
- [ ] Datos no verificados están marcados.  
- [ ] No se han hecho deducciones.  
- [ ] Se distingue entre hechos y teorías.  
- [ ] Metadatos completos.  
- [ ] Longitud respetada.  
- [ ] Tono respetuoso y profesional.  
- [ ] **No hay marcadores `[citation:X]` en el texto.**