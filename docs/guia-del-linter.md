# Guía del validador estructural de efemérides
> Última actualización: 2026-10-25 (nueva auditoría **14**: marcado de `## Referencias Verificadas` — envoltorio obligatorio `<div class="references"><ul><li>…</li></ul></div>`, aviso ante cualquier clase ajena a la hoja de estilos del sitio —`references-box` u otra— y aviso ante lista Markdown sin `<li>`; en modo `[AVISO]`, no retroactiva y sin cambios de código de salida. Censo sobre `672` posts en el HEAD `fbc8d8024f46`: **665** con el envoltorio normativo, **7** sin él y **11** avisos nuevos; `0` cambios de veredicto).
> Última actualización anterior: 2026-10-22 (calibración integral de la auditoría [AVISO] 12 en `awk` POSIX compatible con `bash 3.2` de macOS: audita todas las ocurrencias de `YAML` (`title`/`excerpt`), cuerpo y `Nota aclaratoria`, incluidos apócopes `un`/`veintiún`, `A X años de…`, aproximaciones `casi`/`más de`/`durante X años`, edad viva `cumple X años` y `Un siglo después` sin ancla; censo verificado sobre `663` posts: **117 posts** y **132 ocurrencias**; `0` cambios de código de salida). Actualización previa del mismo día: 2026-10-22 (nueva auditoría [AVISO] 13: títulos de realeza, nobleza y dignidades en minúscula ante nombre propio — Manual de Estilo v1.22, § 4.3, decisión D1-c; Plantilla Maestra v2.25, regla maestra 5; Instrucciones de Formato v2.24 —; no computa como fallo y no es retroactiva). Actualización anterior: 2026-10-21 (nueva auditoría [AVISO] 12: recuento de años anclado al presente, tras la derogación de la regla de cómputo — Manual de Estilo v1.20, § 5.9 —; no computa como fallo y no es retroactiva). > Última actualización: 2026-10-19 (la auditoría de imagen deja de bifurcar por categoría: el tamaño de casa es **1.200 × 675 para todas**, incluida `nacimiento`, conforme a la Plantilla Maestra v2.22 y su regla maestra 12; el código y el número de comprobaciones no cambian). Actualización anterior: 2026-10-06 (a partir de hoy el validador audita además las bandas por sección; se documenta esa auditoría y se corrige el localizador del bloque `Resumen Ejecutivo`). Actualización anterior: 2026-10-06 (reconciliación de los recuentos de extensión del corpus en dos fotografías verificadas; sin cambios de reglas ni de código ejecutable). Actualización anterior: 2026-10-02 (alineación de referencias con Plantilla Maestra v2.21, Instrucciones de Formato v2.20 e Instrucciones de Procesar v2.15; sin cambios de código ni auditorías nuevas).

## Finalidad

`tools/efemerides-linter.sh` valida automáticamente la estructura editorial de un post antes de entregarlo. No sustituye la investigación, la lectura completa ni la revisión humana de fuentes, licencias, redacción y contexto.

## Archivos

- `tools/efemerides-linter.sh`: programa de validación.
- `tools/efemerides-rangos-excepciones.txt`: cuatro excepciones D1-a/D2-a legibles por máquina.
- `docs/excepciones-rangos-y-tratamientos.md`: explicación humana y normativa de esas excepciones.

El archivo de excepciones debe permanecer junto al script para que el validador pueda localizarlo después de clonar el repositorio.

## Uso

```bash
tools/efemerides-linter.sh /ruta/al/post.md /ruta/al/directorio/de/imagenes
```

Auditoría limitada a grados, tratamientos y cargos civiles:

```bash
tools/efemerides-linter.sh /ruta/al/post.md --solo-rangos
```

## Resultado

- Código `0` y `VEREDICTO: APROBADO`: las comprobaciones automáticas pasaron.
- Código `1` y `VEREDICTO: FALLECE`: debe corregirse al menos una infracción.
- Código `2`: invocación incorrecta o archivo inexistente.

Los avisos no equivalen por sí solos a una aprobación editorial. La imagen debe localizarse para que sus dimensiones sean comprobadas efectivamente.

Desde el 2026-10-19 la comprobación de la imagen aplica un único tamaño de casa, **1200x675**, a todas las categorías: el mensaje de aprobación reza `Imagen <dims> — tamaño de casa para [<categoría>] (1200x675)` y el de rechazo `Imagen <dims> — el tamaño de casa es 1200x675 para todas las categorías, incluida nacimiento (regla maestra 12)`. Antes de esta fecha la auditoría exigía 800x1000 a `nacimiento`; el cambio **no es retroactivo** y no reabre los cierres comunicados, de modo que las 103 imágenes de nacimiento publicadas a 800x1000 siguen aprobadas tal como quedaron registradas y solo fallarían si se re-auditaran. Su migración, si el editor la ordena, es una tanda aparte con recorte manual.

Desde el 2026-09-17 el validador emite además un `[AVISO]` léxico cuando el cuerpo del post contiene cualquier forma del verbo «adolecer» (adolece, adolecía, adolecer, adolezca…; Manual de Estilo v1.16, § 4.2): el verbo es correcto aplicado a personas, por lo que el aviso exige lectura humana y no computa como fallo.

Desde el 2026-09-17 las auditorías del principio de documento limpio (Metadatos y cuerpo) marcan `[FALLECE]` ante **cualquier aparición de la palabra «borrador»**, no solo ante la fórmula derogada «borrador preliminar»: las nueve menciones corregidas en el lote BORR-01 (commit `a62cfa0`) usaban variantes («borrador de la investigación preliminar», «borrador del investigador») que el radio anterior no detectaba. Rectores: Plantilla Maestra v2.18, reglas maestras 6 y 8; Manual de Estilo v1.16, § 8.3. El mensaje de fallo indica línea y fragmento.

Desde el 2026-09-23 el validador emite un `[AVISO]` cuando un cargo civil en minúscula (presidente, ministro, director, secretario, gobernador, superintendente, intendente y sus formas) encabeza una denominación en mayúsculas tras «de/del» (Manual de Estilo v1.17, § 4.3, decisión D1-b: el cargo debe capitalizarse cuando la denominación es institucional). El aviso incluye la clasificación heurística de la denominación (museo/archivo, militar, gobierno/estatal, empresa, organización o «revisar») y exige lectura humana, pues los topónimos, los países y los nombres propios quedan fuera de D1-b (regido por D1-a). En el corpus previo al 23-sep estos avisos documentan desviaciones congeladas (no-retroactividad de 2026-09-23); no computan como fallo.

Desde el 2026-09-23 el validador emite un `[AVISO]` ante cualquier enlace externo (http/https) en el cuerpo del post fuera de «## Referencias Verificadas» y de `<figcaption>` (Manual de Estilo v1.17, § 6.4; Instrucciones de Formato v2.17, ap. 5): los enlaces institucionales y documentales solo se colocan en referencias y en las leyendas de las figuras, con la única excepción del externo que sea objeto del relato (juicio humano). Los enlaces canónicos del propio sitio (https://efemerides-aviacion.github.io/efemerides/…) no son externos (regla 18). No computa como fallo.

Desde el 2026-09-29 el validador informa de la **extensión narrativa** del post (Manual de Estilo v1.18, § 5.10; Plantilla Maestra v2.21, regla maestra 16): imprime `[OK]` hasta 1.500 palabras —banda óptima—, un `[AVISO]` entre 1.501 y 1.550 —por encima del óptimo, dentro del tope— y otro `[AVISO]` por encima de 1.550, indicando que procede condensar. La medición abarca del comentario del `Resumen Ejecutivo` al encabezado `## Referencias Verificadas`, descontadas las etiquetas HTML. El límite inferior de la banda (1.150 palabras) es orientativo y **no** se audita. En la fotografía del commit `3778d3c3b440` (2026-09-29; 608 posts), 228 posts quedaban por debajo de 1.150 y 167 superaban el tope recomendado de 1.550. En el HEAD `cbc4443e29e3` (2026-10-06; 624 posts), el mismo conteo arroja 272 por debajo de 1.150 y 70 por encima de 1.550. La banda rige para las nuevas altas desde el 29-09-2026 y es **no retroactiva**; estas cifras describen dos fotografías del corpus y no exigen sanear retroactivamente publicaciones anteriores.

En la misma fecha el validador emite un `[AVISO]` de **repeticiones entre secciones** (Manual de Estilo v1.18, § 5, «un dato, una sección»; Plantilla Maestra v2.21, regla maestra 16): compara los 7-gramas idénticos de cada par de secciones del propio post —mismo radio que el detector de ecos `tools/eco7.py`— excluyendo `Resumen Ejecutivo` (única sección que puede anticipar el contenido), `## Referencias Verificadas` y `## Metadatos de Control`. Informa del número de 7-gramas compartidos y muestra hasta cinco ejemplos con sus secciones. Los topónimos, las denominaciones institucionales y las citas de época repetidos pueden ser legítimos, de modo que el aviso exige lectura humana y no computa como fallo; los posts previos al 29-09-2026 quedan congelados (p. ej., 1914-10-05 registra 11 coincidencias de nombres geográficos entre `Datos verificados` y `Desarrollo Cronológico`).

También desde el 2026-09-29 el validador mide la extensión de `## Metadatos de Control` (Manual de Estilo v1.18, § 10; Plantilla Maestra v2.21, regla maestra 17): `[OK]` hasta 150 palabras y `[AVISO]` por encima, con la indicación de enumerar solo nombres breves de fuentes y resumir `Discrepancias resueltas` en una línea, sin duplicar títulos, autores ni signaturas de `## Referencias Verificadas`. La mediana del corpus es de 110 palabras y 141 posts superan el tope (los peores, entre 300 y 411); las altas recientes de investigación extensa (1914-10-05, 1931-10-05, 1967-10-03) se sitúan entre 236 y 308 palabras.

Desde el 2026-10-10 el validador mide la **extensión de cada sección** (Instrucciones de Formato v2.20,
apartado «Pautas de redacción para evitar repeticiones y extensión del post»; Manual de Estilo v1.18,
§ 5.10). Imprime `[OK]` cuando las seis secciones narrativas caen dentro de su banda —`Resumen
Ejecutivo` 100–130, `## Datos verificados del evento` 140–190, `## Contexto Histórico` 380–480,
`## Desarrollo Cronológico` 300–400 con **5–7 hitos fechados**, `## Consecuencias e Impacto` 150–210
y `## Legado` 110–160— y `[AVISO]` enumerando las desviaciones en caso contrario. La medición va de
la cabecera de la sección a la siguiente, sin divisores `<hr>`, sin etiquetas HTML y sin URLs, el mismo
recorte que la extensión narrativa; si el bloque del `Resumen Ejecutivo` no está localizado, esa
comprobación se omite en lugar de contar 0. La norma **no es retroactiva** y el aviso no computa como
fallo: un post del corpus publicado queda congelado. Las exenciones se anotan en
`tools/efemerides-rangos-excepciones.txt` con la forma `<archivo>|banda:<sección>|motivo`, y se
documentan a la vez en `docs/excepciones-rangos-y-tratamientos.md`.

Fotografía del corpus en el HEAD `4ca66a3b5066` (2026-10-10; 632 posts): 603 posts presentan al menos
una sección fuera de banda y 29 son conformes; por sección, fuera de banda: `Resumen Ejecutivo` 438,
`Datos verificados del evento` 465, `Contexto Histórico` 510, `Desarrollo Cronológico` 425 más 398 con recuento de hitos
fuera de 5–7, `Consecuencias e Impacto` 443 y `Legado` 433. La regresión completa del script con la
auditoría nueva dejó 0 diferencias ajenas a ella y ningún cambio de código de salida: los 10 posts con
`FALLECE` del corpus son los mismos de antes.
## Normas de mantenimiento

1. Todo cambio del script debe contrastarse con los seis rectores vigentes.
2. Si cambian nombres de cabeceras, categorías, gradientes, dimensiones, enlaces, reglas D1-a/D2-a o las bandas de extensión y repetición, debe actualizarse el script en el mismo flujo autorizado por el editor. Toda auditoría nueva que afecte a normas no retroactivas nace en modo `[AVISO]` y se documenta aquí con sus cifras de corpus. Las demás normas de mantenimiento se conservan sin cambio.
3. El encabezado debe indicar las versiones rectoras contra las que fue auditado.
4. Las excepciones nuevas deben documentarse simultáneamente en el registro humano y en el archivo legible por máquina.
5. El linter debe ejecutarse después de la última edición. Si el post cambia luego, se renueva el timestamp y se vuelve a ejecutar.
6. `APROBADO` acredita conformidad estructural automatizada, no veracidad histórica ni suficiencia de licencias.

Desde el 2026-10-21 —y calibrada íntegramente el **2026-10-22** en `awk` POSIX
sin dependencias de `bash 4+` para garantizar compatibilidad nativa en macOS y
Linux— el validador emite un `[AVISO]` (auditoría 12) por **cada ocurrencia** en
`title:`/`excerpt:` del YAML, en el cuerpo del post o en la `Nota aclaratoria`
que exprese una **distancia temporal anclada al presente** (Manual de Estilo
v1.22, § 5.9; Plantilla Maestra v2.25, regla maestra 9). El analizador evalúa
todas las oraciones de cada sección (sin detenerse en la primera mención de
`años`), reconoce cifras en guarismos y en letra —incluidos los apócopes
masculinos `un` y `veintiún`, giros como «A X años de…», «casi / más de /
durante X años», edades vivas («cumple X años») y «Un siglo después» sin fecha
histórica—, descarta edades entre paréntesis, fallecimientos o jubilaciones
fechados, duraciones operativas cerradas, «X años antes» y conmemoraciones
pasadas con fecha completa explícita («los días 4 y 5 de enero de 2026»), y
admite exenciones expresas en `tools/efemerides-rangos-excepciones.txt`.
Fotografía verificada sobre el corpus completo en el HEAD `0c8d5eaf4e14`
(2026-10-22; **663 posts**): **117 posts** y **132 ocurrencias** detectadas
(`98` del núcleo base + `8` con apócope `un`/`veintiún` + `4` de edad viva/giro
directo/siglo + `6` aproximaciones por decena + `1` de cincuentenario en `2026`;
`0` falsos positivos en los otros `546` posts y **0 cambios de código de
salida** en los `663` posts). El aviso guía y verifica el saneamiento por
tandas del corpus sin computar como fallo estructural.

Desde el 2026-10-22 el validador emite un `[AVISO]` (auditoría 13) cuando el
`title:` o `excerpt:` del YAML o la prosa del post —incluida la `Nota
aclaratoria` y excluido el listado bibliográfico de `## Referencias
Verificadas`— contienen un **título de realeza, nobleza o dignidad
caballeresca/tradicional con mayúscula inicial ante nombre propio o
denominación nobiliaria** (*Rey*, *Reina*, *Emperador*, *Emperatriz*, *Zar*,
*Káiser*, *Príncipe*, *Princesa*, *Infante*, *Duque*, *Marqués*, *Conde*,
*Vizconde*, *Barón*, *Lord*, *Lady*, *Sir*, *Sultán*, *Emir*, *Jeque*…; Manual
de Estilo v1.22, § 4.3, decisión **D1-c**; Plantilla Maestra v2.25, regla
maestra 5; Instrucciones de Formato v2.24). El filtro descarta la mayúscula
posicional de inicio de enunciado, los sobrenombres antonomásticos (*Barón
Rojo*, *Rey del Café*, *Reina de los Cielos*, *Lady Lindy*), los nombres
propios de aeronaves, premios, instituciones o infraestructuras (*Lucky Lady*,
*Emperador Kanishka*, *Copa del Rey*, *Fundación Infante de Orleans*,
*Aeropuerto Reina Sofía*), los topónimos (*Puerto Príncipe*, *Duque de Caxias*,
*río Sir Daria*, *sector El Conde*) y los antropónimos homónimos, y admite
exenciones expresas en `tools/efemerides-rangos-excepciones.txt`. Fotografía
del corpus en el HEAD `ef6d75235e30` (2026-10-22; 661 posts): **14 posts** y
**34 ocurrencias** residuales (`Sir` 18 en 10 posts, `Lord` 8 en 3 posts,
`Lady` 4 en 2 posts y `Conde del Jarama` 4 en 1 post; 0 ocurrencias en
mayúscula de *rey*, *reina*, *emperador*, *zar*, *conde Zeppelin*, *marqués* o
*jeque*). La regresión completa sobre los 661 posts dejó **0 cambios de código
de salida** y **0 diferencias ajenas a la auditoría 13**; el post del
`1943-10-26` (Do 335) pasa con 61 comprobaciones `[OK]`, 0 avisos y 0 fallos.
La norma **no es retroactiva**: los 14 posts previos quedan congelados.

Desde el 2026-10-25 el validador comprueba además el **marcado de la sección de
referencias** (auditoría 14; Plantilla Maestra v2.25, regla maestra 14, y hoja de
estilos del sitio `assets/css/main.css`). Tres comprobaciones, todas en modo
`[AVISO]` y **no retroactivas**:

1. `[OK] Referencias: envoltorio normativo <div class="references">` cuando la
   sección abre con el envoltorio del patrón de la casa; en su defecto, aviso
   `Referencias sin el envoltorio`.
2. Aviso cuando el envoltorio usa una **clase ajena a la hoja de estilos**
   (`references-box` u otra): `main.css` solo define `.references`, de modo que
   la sección se publica sin caja ni borde y con viñetas. El escaneo abarca
   únicamente las clases que aparecen **antes de la primera entrada** de la
   lista, para no confundir el envoltorio con la `note-box` de la nota
   aclaratoria posterior.
3. Aviso cuando las entradas van en **lista Markdown** (viñeta o numeración) en
   lugar de `<li>` dentro de `<ul>`: el patrón de la casa es
   `<div class="references"><ul><li>…</li></ul></div>`.

Fotografía del corpus en el HEAD `fbc8d8024f46` (2026-10-25; **672 posts**):
**665** con el envoltorio normativo, **7** sin él —`1895-01-02`, `1907-10-10`,
`1927-10-15`, `1956-10-10`, `1967-10-18`, `1976-10-06` y `2019-10-18`, de los
que cuatro llevan además lista Markdown—, **0** con clase ajena y **11** avisos
nuevos en total. La regresión completa sobre los 672 posts deja **0 cambios de
código de salida** (662 con código 0 y los mismos 10 con código 1 que antes de
la auditoría) y **0 diferencias ajenas a la auditoría 14**. La corrección del
`1979-10-31` y de las tres altas afines del `24-10`, publicada en los commits
`f9c1e4dc` y `fbc8d80`, se adelantó a la herramienta y por eso ya no figura
entre los avisos. La norma **no es retroactiva**: los 7 posts previos quedan
congelados.
