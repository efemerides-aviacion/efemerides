# Instrucciones de formato de salida para efemérides
> Última actualización: 2026-08-21  
> Versión: v2.13

---

## POLÍTICA DE IDIOMAS

### Uso de términos, frases y referencias en otros idiomas

1. **Idioma principal del post:** el post final debe redactarse íntegramente en **español neutro**.

2. **Excepciones permitidas para mantener idioma original:**
   - nombres propios de personas;
   - nombres oficiales de aeronaves;
   - matrículas y códigos técnicos;
   - nombres de unidades militares o agencias cuando su forma original sea editorialmente preferible;
   - topónimos oficiales de uso ampliamente reconocido;
   - siglas universalmente conocidas.

3. **Obligación de traducir:**
   - títulos, subtítulos y descripciones narrativas;
   - citas completas, que deben traducirse al español;
   - términos técnicos cuando exista equivalente claro en español.

4. **Idiomas permitidos en `## Referencias Verificadas`:** español e inglés.  
   Excepción: una fuente en otro idioma solo podrá usarse si el dato es indispensable y no existe alternativa razonable, y deberá quedar matizada en nota aclaratoria.

---

## FORMATO GENERAL DE ENTREGA

1. El producto final debe entregarse dentro de un bloque Markdown cuando se solicite en chat como texto final.
2. No incluir marcadores automáticos del tipo `[citation:X]`, `[1]`, `[2]`, etc.
3. No incluir la etiqueta `[VERIFICADO]` en el texto visible.
4. Solo se admite `[NO CONFIRMADO]` cuando la línea editorial decida mantener un dato de alto valor contextual pese a no estar plenamente cerrado.

---

## ENLACES: NORMA EDITORIAL VIGENTE

### 1) Enlaces dentro del cuerpo del texto
Todo enlace insertado en párrafos narrativos debe usar HTML inline con este estilo:

```html
<a href="https://ejemplo.com" style="color: #315fea; text-decoration: none;">texto del enlace</a>
```

### 2) Prohibiciones
- No usar `href="[URL](URL)"`.
- No dejar enlaces subrayados por defecto en el cuerpo, salvo causa excepcional.
- No inventar URLs de publicación futura.
- No usar nombres de archivo `.md` como si fueran URLs públicas.
- No usar `post_url` ni estructuras inferidas si el contenido aún no está publicado.

### 3) Enlaces cruzados entre efemérides
- evitar repetir la misma URL;
- pueden utilizarse varios enlaces cruzados distintos si son pertinentes;
- preferir su ubicación en `## Desarrollo Cronológico`;
- usar exclusivamente la URL pública real del post ya publicado;
- nunca enlazar una efeméride consigo misma.

### 4) Forma canónica de los enlaces internos

La URL de toda efeméride publicada sigue el patrón canónico de Jekyll:

```
https://efemerides-aviacion.github.io/efemerides/:categoria/:año/:mes/:día/:slug.html
```

La fecha va **en barras** (`/1897/01/06/`), nunca unida por guiones
(`/1897-01-06/`): esa ruta no existe y devuelve 404. El slug es el nombre del
archivo sin el prefijo de fecha; si el nombre termina en guion, el slug
publicado lo pierde (Jekyll elimina guiones terminales) y el enlace se escribe
sin él. Antes de entregar el post, cada enlace interno se comprueba contra este
patrón, no contra el nombre del archivo.

Motivo: en agosto de 2026 se entregaron varios posts con fechas en guiones y el
editor sustituyó los enlaces a mano copiándolos del navegador.

---

## FORMATO DE CIFRAS NUMÉRICAS

- miles con **punto**;
- decimales con **coma**.

**Correcto ✅**
- `2.408 millas`
- `18,15 horas`
- `4.000 km`

**Incorrecto ❌**
- `2,408 millas`
- `18.15 horas`
- `4,000 km`

### Años transcurridos desde el hito

Las efemérides se publican **el mismo día y el mismo mes del hecho**, de modo que
la distancia temporal con el presente es un entero exacto:

```
años transcurridos = año de publicación − año del hito
```

El año de publicación se toma del campo `fecha_publicacion` del borrador aportado
por el editor; si no consta, se emplea el año en curso.

**Correcto ✅**
- hito de 1945, publicación en 2026 → `ochenta y un años después`

**Incorrecto ❌**
- hito de 1945, publicación en 2026 → `ochenta años después`

La cifra se escribe con letra cuando encabeza la frase. La regla alcanza a todas
las formulaciones equivalentes: «X décadas más tarde», «un siglo después», «X años
antes de hoy» y cualquier mención de aniversario.

---

## RANGOS, NOMBRES Y ESTILO HISTÓRICO

### Grados militares
En temas militares, los grados deben ir con mayúscula inicial:
- `Teniente`
- `Capitán`
- `Mayor`
- `Teniente Coronel`
- `Coronel`
- `General de Brigada`

### Precisión nominal
Si una fuente usa variantes de nombre, apellido, matrícula o designación:
- elegir la forma mejor respaldada;
- explicar la discrepancia en nota aclaratoria cuando sea relevante;
- **coherencia entre posts relacionados:** una misma persona conserva la misma
  forma nominal en todos los posts que la mencionan (caso «Susan Koerner»,
  14 de agosto de 2026); si se cambia, se armonizan en el mismo commit de
  corrección todos los posts afectados.

---

## FIGURAS, PIE DE FOTO E IMÁGENES

### 1) Pie de foto
Debe indicar claramente:
- qué muestra la imagen;
- si corresponde o no al hecho exacto;
- fecha o periodo, si se conoce;
- fuente.

### 2) Cuando el usuario pide una imagen concreta
Si la imagen señalada por el usuario no puede descargarse por 403, anti-bot, Cloudflare o restricción similar:
- debe informarse de forma explícita **al editor, en el chat**;
- no debe reemplazarse silenciosamente por otra;
- **no debe consignarse en el post**: el pie de foto solo indica qué muestra la
  imagen finalmente empleada y si corresponde o no al hecho exacto.

### 3) Si el usuario pide solo un snippet de figura
Entregar **solo** el bloque `<figure>...</figure>` corregido, sin regenerar el resto del post, salvo que pida algo más.

### 4) Tamaño de casa; se permite ampliar
Las imágenes se entregan a **800 × 1.000** en `nacimiento` y a **1.200 × 675**
en el resto. Si la toma es menor, se amplía con remuestreo de calidad (Lanczos) y unsharp
ligero. Si es mayor, se reduce. WebP (quality 90-92, method 6). El **nombre de archivo de la imagen es el del post** (sin `.md`). La resolución
**no se menciona en el post**: es nota de trabajo y se comunica al editor por chat.
Queda derogada la fórmula «no se amplían / resolución nativa». El 678 era errata.

---

## REFERENCIAS VERIFICADAS

### Número mínimo de referencias

**Todo post lleva al menos cuatro referencias verificadas**, y al menos dos de
ellas han de ser primarias o institucionales. Regla vigente desde el 16 de
agosto de 2026.

**Cómo contar:** entradas `<li>`, viñetas `-` y numeración `1.` en la sección de referencias. Contar solo `<li>` da falsos positivos.

Motivo: tres efemérides consecutivas se publicaron con solo dos referencias, un
aparato documental insuficiente para sostener el núcleo del hecho y para que el
lector pueda contrastarlo.

Si tras agotar la investigación no se alcanzan cuatro referencias pertinentes y
verificadas por contenido, se aplica el criterio de suspensión de las
Instrucciones de Procesamiento y se informa al editor por chat.

### Revisión obligatoria de URLs
Antes de incluir una URL:
1. abrir la página y **leer su contenido**, no limitarse a comprobar que responde;
2. confirmar que el título y el cuerpo corresponden al tema real de la efeméride;
3. descartar enlaces genéricos, páginas rotas o temas no aeronáuticos.

**Un código 200 no valida una fuente.** Acredita que el servidor devuelve algo, no
que ese algo trate del sujeto de la efeméride. La validación es de contenido.

### Fichas de archivo, museo y biblioteca
Los repositorios documentales identifican sus fondos con códigos correlativos, de
modo que un dígito equivocado devuelve una ficha válida y ajena al asunto. Antes de
emplear una de estas fichas —como referencia, como `href` del `<figure>` o como
origen de una imagen— deben confirmarse:

1. el **título o leyenda de la ficha misma**, no el del resultado de búsqueda que
   llevó hasta ella;
2. el **identificador digital** y la signatura, que han de coincidir con los del
   archivo de imagen descargado;
3. la **fecha** de la toma o del documento, contrastada con la cronología del hecho;
4. la **imagen**, examinada visualmente cuando la ficha la ofrezca;
5. el **estado de derechos**, si la imagen va a reproducirse.

Sitios de riesgo habitual: `loc.gov`, `iwm.org.uk`, `archives.gov`,
`nationalmuseum.af.mil`, `images.nasa.gov`, hemerotecas y archivos fotográficos
nacionales.

El enlace del `<figure>` es el más sensible: un error ahí atribuye al lector una
identidad falsa sobre la imagen que está viendo.

### Regla de pertinencia
No transferir referencias de una efeméride a otra solo porque parezcan parecidas.  
Cada referencia debe ser **realmente pertinente** al post en curso.

---

## NOTAS ACLARATORIAS

### Cuándo deben incluirse
- discrepancias entre **fuentes publicadas y solventes**;
- imágenes representativas en vez de exactas;
- diferencias entre fecha de fundación, activación, inauguración o entrada en servicio;
- cambio entre reclamaciones de época y cifras revisadas;
- cualquier matiz esencial para no inducir a error.

### Cuándo NO deben incluirse
La nota aclaratoria **nunca** menciona:
- errores, fechas equivocadas o enlaces rotos del borrador preliminar del investigador;
- URLs que devolvieron 403, 404 o bloqueo anti-bot;
- sustituciones de fuentes o imágenes motivadas por problemas de acceso;
- el entorno técnico de trabajo o su flujo de verificación.

Todo lo anterior se comunica **al editor por chat**. Véase «Principio de documento
limpio» en la Plantilla Maestra, regla maestra 8.

### Formato obligatorio
```html
<div class="note-box">
  <p><strong>Nota aclaratoria:</strong> [Texto de la aclaración].</p>
</div>
```

### Ubicación
Inmediatamente después de `## Referencias Verificadas` y antes de `## Metadatos de Control`.

---

## METADATOS DE CONTROL

### El borrador aportado por el editor no se cita en el post

**Regla vigente desde el 16 de agosto de 2026.** El borrador preliminar **no se
menciona en ninguna sección del post**, tampoco en los metadatos. Queda
derogada la fórmula `borrador preliminar del investigador` como fuente de
contraste.

**Motivo.** El borrador es un insumo **opcional, no preferible**: procede de
modelos generativos que han introducido datos erróneos y atribuciones
inventadas. Citarlo entre las fuentes le confiere una solvencia que no tiene y
compromete la credibilidad del aparato de referencias.

**Tratamiento correcto.** El borrador se usa como punto de partida y toda
afirmación que aporte se verifica en fuente publicada; en el post se cita
**esa** fuente, nunca el borrador. Las discrepancias detectadas entre el
borrador y la investigación se comunican al editor por chat.

Sigue proscrita, con mayor razón, toda línea independiente de estado del
documento («borrador preliminar», «pendiente de revisión del editor» y
equivalentes).

### Campo «Discrepancias resueltas»
Recoge **exclusivamente** divergencias entre fuentes publicadas: cifras, fechas,
husos horarios, denominaciones. Queda prohibido consignar en él errores del
borrador, enlaces caídos, rutas obsoletas, incidencias del entorno o
comprobaciones rutinarias del flujo de trabajo.

**Fórmula proscrita:** «se verificó la coherencia entre la fecha del hecho, el
título, el nombre del archivo y el YAML». La comprobación es obligatoria; su
mención en el post, no.

Cuando no haya divergencias entre fuentes, el campo se omite.

### Nivel de confianza
Debe ser explícito y justificado por la robustez de las fuentes:
- `Alto`
- `Medio`
- `Bajo`

---

## PAUTAS DE REDACCIÓN PARA EVITAR REPETICIONES

### Jerarquía de la información
- **Excerpt (YAML):** la versión más breve.
- **Resumen Ejecutivo:** síntesis ampliada.
- **Cuerpo:** desarrollo interpretativo y cronológico.

### Reglas por sección
- **Excerpt:** no incluir datos secundarios.
- **Resumen Ejecutivo:** no repetir literalmente el excerpt.
- **Datos verificados del evento:** evitar repetir lo ya dicho en el resumen.
- **Contexto Histórico:** no duplicar la cronología principal.
- **Desarrollo Cronológico:** concentrar hitos y fechas.
- **Consecuencias e Impacto:** efectos inmediatos o de corto plazo.
- **Legado:** efectos de largo plazo, memoria o influencia histórica.

### Regla de oro
> La misma información no debe aparecer redactada de la misma manera en dos secciones diferentes del cuerpo del post.

---

## MENSAJES DE COMMIT PARA GITHUB DESKTOP

El editor aplica y empuja los commits con **GitHub Desktop**; la entrega del
investigador consiste en los archivos finales listos para copiar al clon y el
mensaje separado en los dos campos de la interfaz. No se entregan parches
`git am` ni commits construidos en el clon del entorno.

Formato obligatorio (vigente desde el 12 de agosto de 2026; quedan derogados el
prefijo `feat(efemerides):` y el cierre Categoría/País):
- **Resumen (Summary):** frase descriptiva en español que nombra el cambio
  («Nueva efeméride: …», «Estandarización de títulos de la categoría …»,
  «Corrección de líneas divisorias de la categoría … (tanda X de Y)»).
- **Descripción (Description):** viñetas con los archivos añadidos o
  reemplazados (ruta dentro del repo) y las notas pertinentes: procedencia y
  licencia de la imagen, enlaces internos nuevos y documento base de la
  investigación.

Tandas: cuando un cambio homogéneo alcance muchos archivos (auditorías de
títulos, normalización de separadores), se agrupa en tandas cronológicas de
alrededor de diez archivos, cada una con su propio mensaje; la efeméride nueva
viaja siempre en un commit único con su imagen.

### Regla editorial nueva
El commit debe proponerse **después** de la revisión del usuario o de la incorporación de sus correcciones, de modo que represente la **incorporación inicial limpia** del post al repositorio, no una sucesión de microajustes.

---

## ERRORES FRECUENTES QUE INVALIDAN LA SALIDA

- marcadores `[citation:X]` sin limpiar;
- enlaces HTML mal formados;
- URLs no verificadas o ajenas al tema;
- uso de URLs públicas inferidas para posts aún no publicados;
- referencias recicladas de otro post sin pertinencia real;
- grados militares en minúscula en contextos donde deben ir capitalizados;
- pies de foto que atribuyen al día o al lugar equivocados una imagen representativa;
- mencionar en el post el borrador preliminar, sus errores, los enlaces
  inaccesibles o el entorno técnico de trabajo;
- consignar en «Discrepancias resueltas» comprobaciones rutinarias del
  procedimiento en lugar de divergencias reales entre fuentes;
- redondear los años transcurridos desde el hito a la cifra redonda más próxima
  en lugar de calcularlos sobre el año de publicación;
- validar una URL por su código de respuesta sin leer su contenido;
- enlazar en el `<figure>` una ficha de archivo cuyo sujeto no es el de la
  efeméride.
- enlaces internos con la fecha unida por guiones en lugar de la forma
  canónica con barras, o con el guion terminal del nombre de archivo
  conservado en el slug;
- líneas de estado del documento o notas sobre resolución de imágenes en el
  post;
- citar el borrador preliminar entre las fuentes de contraste de los metadatos;
- entregar un post con menos de cuatro referencias verificadas.

---

## CAMBIOS INCORPORADOS EN ESTA V2
- normalización del estilo de enlaces HTML sin subrayado;
- regla de un solo enlace cruzado y solo con URL pública real; *(Superado en v2.1: la restricción se refiere a no repetir la misma URL.)*
- capitalización obligatoria de grados militares;
- uso de “borrador preliminar del investigador”; *(Derogado en v2.10: el borrador no se cita en el post.)*
- obligación de explicar bloqueos técnicos en imágenes propuestas por el usuario;
- precisión sobre cuándo devolver solo snippets y cuándo regenerar contenido completo;
- formalización del momento adecuado para proponer el commit.


---

## ACTUALIZACIONES DE PROCESAMIENTO V2.1 — 2026-07-28

- Verificar coherencia entre la fecha solicitada, el hecho, el título, el archivo y la fecha pública.
- Mantener divisores `<hr>` antes de cada sección principal.
- Tratar como distintas las URLs cruzadas diferentes; evitar únicamente repetir la misma URL o enlazar el post consigo mismo.
- Generar un timestamp local dinámico y no reutilizado al terminar cada documento.
- Separar con claridad hecho confirmado, reclamación histórica, hipótesis y dato no confirmado.
- Si la imagen no corresponde al instante exacto, declararlo en el pie y, cuando sea necesario, en la nota aclaratoria.
- No mencionar sustituciones de imagen ni detalles internos del flujo en notas o metadatos.
- No proponer commits antes de la solicitud expresa del editor; el commit inicial debe representar incorporación formal, sin mencionar imágenes.
- Aplicar miles con punto, decimales con coma y conversiones métricas pertinentes.

---

## ACTUALIZACIONES DE PROCESAMIENTO V2.2 — 2026-07-29

### Corrección de coherencia sobre enlaces cruzados
En la sección «CAMBIOS INCORPORADOS EN ESTA V2» se conserva la redacción
original «regla de un solo enlace cruzado» por tratarse de un registro
histórico, acompañada de una nota que advierte de su superación.

La sección «ENLACES: NORMA EDITORIAL VIGENTE» de este mismo documento ya
recogía correctamente el criterio actual y no requirió modificación.

### Criterio unificado vigente
- Una misma URL, una sola vez por post.
- Pueden emplearse varios enlaces cruzados distintos si son pertinentes.
- Nunca debe enlazarse una efeméride consigo misma.
- Solo se enlazan efemérides realmente publicadas, con su URL pública real.
- Ubicación preferente en `## Desarrollo Cronológico`.

---

## ACTUALIZACIONES DE PROCESAMIENTO V2.3 — 2026-08-01

- **Principio de documento limpio.** El post publicado contiene el resultado de la
  investigación, no su crónica. Queda prohibido mencionar en cualquier sección del
  post el borrador preliminar del investigador, sus errores, los enlaces que no
  pudieron consultarse (403, 404, anti-bot) y las incidencias del entorno técnico.
- Esas incidencias se comunican **al editor por chat**. En el caso de los enlaces
  inaccesibles, solo después de haber buscado sin éxito un reemplazo equivalente,
  para que el editor pueda aportar una fuente alternativa.
- El campo «Discrepancias resueltas» y la nota aclaratoria conservan su función
  historiográfica: recogen divergencias entre fuentes publicadas y solventes, y la
  advertencia de imagen representativa.

---

## ACTUALIZACIONES DE PROCESAMIENTO V2.4 — 2026-08-02

- El campo «Discrepancias resueltas» registra **solo divergencias entre fuentes
  publicadas**. Las comprobaciones rutinarias del flujo de trabajo no se
  mencionan en el post, aunque deban ejecutarse siempre.
- Queda proscrita la fórmula «se verificó la coherencia entre la fecha del
  hecho, el título, el nombre del archivo y el YAML» y cualquier variante.
- Si la investigación no arroja divergencias entre fuentes, el campo se omite.

---

## ACTUALIZACIONES DE PROCESAMIENTO V2.5 — 2026-08-04

- Se incorpora a «Formato de cifras numéricas» el apartado **años transcurridos
  desde el hito**. Las efemérides se publican el mismo día y mes del hecho, de
  modo que los años transcurridos se obtienen restando el año del hito al año de
  publicación, tomado del campo `fecha_publicacion` del borrador.
- Se exige la cifra exacta, no la redondeada.
- Se añade a la lista de errores frecuentes el redondeo de esa cifra.

---

## ACTUALIZACIONES DE PROCESAMIENTO V2.6 — 2026-08-05

- Se reescribe «Revisión obligatoria de URLs»: la validación de una fuente es de
  **contenido**, no de disponibilidad. Un código 200 no acredita que la página
  trate del sujeto de la efeméride.
- Se incorpora el apartado **Fichas de archivo, museo y biblioteca**, con los cinco
  extremos que deben confirmarse —título de la ficha, identificador, fecha, imagen
  y derechos— y la advertencia sobre los repositorios de identificadores
  correlativos.
- Se añaden a la lista de errores frecuentes la validación por código de respuesta
  y el enlace de una ficha ajena al sujeto en el `<figure>`.

---

## ACTUALIZACIONES DE PROCESAMIENTO V2.7 — 2026-08-09

- Se incorpora a «Enlaces: norma editorial vigente» el apartado 4, **forma
  canónica de los enlaces internos**: fecha en barras, slug sin guion terminal,
  comprobación contra el patrón y no contra el nombre del archivo.
- Se incorpora a «Figuras, pie de foto e imágenes» el apartado 4, **resolución
  nativa sin ampliaciones**, con la resolución fuera del post.
- Se precisa en «Metadatos de Control» que la fórmula «borrador preliminar del
  investigador» va solo como fuente de contraste y queda proscrita toda línea
  independiente de estado del documento. *(Derogado en la v2.10: el borrador ya
  no se cita como fuente.)*
- Se añaden a la lista de errores frecuentes los enlaces internos con fecha en
  guiones y las líneas de estado o resolución en el post.

Motivo: reglas acordadas entre el investigador y el editor en las sesiones del
8 y 9 de agosto de 2026.

---

## ACTUALIZACIONES DE PROCESAMIENTO V2.8 — 2026-08-12

### Commit para GitHub Desktop, formato real de trabajo
Se reescribe la sección «Mensajes de commit para GitHub Desktop» conforme a la
práctica consolidada: entrega de archivos finales más mensaje en los campos
Resumen (Summary) y Descripción (Description) de GitHub Desktop. Se deroga el
esquema `feat(efemerides): …` con cierre Categoría/País, que no se usaba en los
commits reales de la rama. Se documenta la política de tandas cronológicas para
cambios homogéneos de muchos archivos y el commit único para cada efeméride
nueva con su imagen.

### Norma de separadores entre bloques
Remisión a la regla maestra 13 de la Plantilla Maestra (v2.10): un separador del
degradado de la categoría por frontera entre bloques; `fundacion` con el verde
de `nacimiento`. Precedente: normalización de 40 de 41 posts de la categoría el
12 de agosto de 2026, en cuatro tandas.


---

## ACTUALIZACIONES DE PROCESAMIENTO V2.10 — 2026-08-16

### El borrador preliminar deja de citarse como fuente
Se deroga la fórmula `borrador preliminar del investigador` en «Metadatos de
Control». El borrador es un insumo opcional, no preferible, procedente de
modelos generativos que introdujeron datos erróneos; citarlo le atribuía una
solvencia de la que carece. Todo dato que aporte debe verificarse en fuente
publicada, y es esa fuente la que se cita. La mención del borrador se añade a
la lista de errores frecuentes.

### Mínimo de cuatro referencias verificadas
Se incorpora a «Referencias Verificadas» el apartado «Número mínimo de
referencias»: cuatro como suelo, de las cuales al menos dos primarias o
institucionales. Motivo: los tres posts anteriores al del BAe Hawk se
entregaron con solo dos referencias.


---

## ACTUALIZACIONES DE PROCESAMIENTO V2.11 — 2026-08-20

- Se reescribe el apartado de imágenes: tamaño de casa **800 × 1.000** (`nacimiento`) y **1.200 × 675** (resto). Se permite ampliar con remuestreo de calidad. Derogado «resolución nativa sin ampliaciones». Errata 678 → 675. La resolución sigue fuera del post.
- Alineado con la Plantilla Maestra v2.14, regla maestra 12.

---

## ACTUALIZACIONES DE PROCESAMIENTO V2.12 — 2026-08-20

- El nombre de archivo de la imagen coincide con el del post (sin `.md`).
- Las referencias se cuentan por `<li>`, viñeta `-` y numeración `1.`.
- Alineado con la Plantilla Maestra v2.15, reglas 12, 14 y 15. *(Vigente hoy: v2.16.)*


---

## ACTUALIZACIONES DE PROCESAMIENTO V2.13 — 2026-08-21

### Alineación con los rectores corregidos
Pasada de coherencia entre los cuatro documentos, sin cambios de fondo.

- **Plantilla Maestra v2.16.** Segunda corrección de coherencia interna de los
  ejemplos: cabeceras al nivel 2 y con la capitalización canónica de la regla
  maestra 1, ejemplo de `seguridad` saneado (`## Referencias` →
  `## Referencias Verificadas`, `Metadatos de control` → `Metadatos de
  Control`, `alto` → `Alto`, `</div` sin cerrar) y cuatro ejemplos elevados al
  mínimo de cuatro referencias de la regla maestra 14.
- **Manual de Estilo v1.13.** § 8 renumerada en orden correlativo: el borrador
  pasa a § 8.3, el mínimo de cuatro referencias a § 8.4, la verificación mínima
  a § 8.5 y la verificación de contenido a § 8.6.
- **Instrucciones de Procesamiento v2.13.** Misma alineación.

Las reglas de este documento no cambian. Se recuerda que la sección
«Fichas de archivo, museo y biblioteca» de estas Instrucciones se corresponde
con la § 8.6 del Manual de Estilo y con la regla maestra 10 de la Plantilla.
