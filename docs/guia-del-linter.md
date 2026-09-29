# Guía del validador estructural de efemérides
> Última actualización: 2026-09-29 (alineación con Plantilla Maestra v2.20 · Manual de Estilo v1.18 · Instrucciones de Formato v2.18; tres auditorías [AVISO] nuevas: extensión narrativa, repeticiones de 7-gramas entre secciones y extensión de los Metadatos de Control)

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

Desde el 2026-09-17 el validador emite además un `[AVISO]` léxico cuando el cuerpo del post contiene cualquier forma del verbo «adolecer» (adolece, adolecía, adolecer, adolezca…; Manual de Estilo v1.16, § 4.2): el verbo es correcto aplicado a personas, por lo que el aviso exige lectura humana y no computa como fallo.

Desde el 2026-09-17 las auditorías del principio de documento limpio (Metadatos y cuerpo) marcan `[FALLECE]` ante **cualquier aparición de la palabra «borrador»**, no solo ante la fórmula derogada «borrador preliminar»: las nueve menciones corregidas en el lote BORR-01 (commit `a62cfa0`) usaban variantes («borrador de la investigación preliminar», «borrador del investigador») que el radio anterior no detectaba. Rectores: Plantilla Maestra v2.18, reglas maestras 6 y 8; Manual de Estilo v1.16, § 8.3. El mensaje de fallo indica línea y fragmento.

Desde el 2026-09-23 el validador emite un `[AVISO]` cuando un cargo civil en minúscula (presidente, ministro, director, secretario, gobernador, superintendente, intendente y sus formas) encabeza una denominación en mayúsculas tras «de/del» (Manual de Estilo v1.17, § 4.3, decisión D1-b: el cargo debe capitalizarse cuando la denominación es institucional). El aviso incluye la clasificación heurística de la denominación (museo/archivo, militar, gobierno/estatal, empresa, organización o «revisar») y exige lectura humana, pues los topónimos, los países y los nombres propios quedan fuera de D1-b (regido por D1-a). En el corpus previo al 23-sep estos avisos documentan desviaciones congeladas (no-retroactividad de 2026-09-23); no computan como fallo.

Desde el 2026-09-23 el validador emite un `[AVISO]` ante cualquier enlace externo (http/https) en el cuerpo del post fuera de «## Referencias Verificadas» y de `<figcaption>` (Manual de Estilo v1.17, § 6.4; Instrucciones de Formato v2.17, ap. 5): los enlaces institucionales y documentales solo se colocan en referencias y en las leyendas de las figuras, con la única excepción del externo que sea objeto del relato (juicio humano). Los enlaces canónicos del propio sitio (https://efemerides-aviacion.github.io/efemerides/…) no son externos (regla 18). No computa como fallo.

Desde el 2026-09-29 el validador informa de la **extensión narrativa** del post (Manual de Estilo v1.18, § 5.10; Plantilla Maestra v2.20, regla maestra 16): imprime `[OK]` hasta 1.500 palabras —banda óptima—, un `[AVISO]` entre 1.501 y 1.550 —por encima del óptimo, dentro del tope— y otro `[AVISO]` por encima de 1.550, indicando que procede condensar. La medición abarca del comentario del `Resumen Ejecutivo` al encabezado `## Referencias Verificadas`, descontadas las etiquetas HTML. El límite inferior de la banda (1.150 palabras) es orientativo y **no** se audita: 228 de los 608 posts del corpus quedan por debajo y la norma no los alcanza. La banda rige para las nuevas altas desde el 29-09-2026 y es **no retroactiva**: 167 posts del corpus superan hoy el tope y quedan congelados como desviaciones documentadas.

En la misma fecha el validador emite un `[AVISO]` de **repeticiones entre secciones** (Manual de Estilo v1.18, § 5, «un dato, una sección»; Plantilla Maestra v2.20, regla maestra 16): compara los 7-gramas idénticos de cada par de secciones del propio post —mismo radio que el detector de ecos `tools/eco7.py`— excluyendo `Resumen Ejecutivo` (única sección que puede anticipar el contenido), `## Referencias Verificadas` y `## Metadatos de Control`. Informa del número de 7-gramas compartidos y muestra hasta cinco ejemplos con sus secciones. Los topónimos, las denominaciones institucionales y las citas de época repetidos pueden ser legítimos, de modo que el aviso exige lectura humana y no computa como fallo; los posts previos al 29-09-2026 quedan congelados (p. ej., 1914-10-05 registra 11 coincidencias de nombres geográficos entre `Datos verificados` y `Desarrollo Cronológico`).

También desde el 2026-09-29 el validador mide la extensión de `## Metadatos de Control` (Manual de Estilo v1.18, § 10; Plantilla Maestra v2.20, regla maestra 17): `[OK]` hasta 150 palabras y `[AVISO]` por encima, con la indicación de enumerar solo nombres breves de fuentes y resumir `Discrepancias resueltas` en una línea, sin duplicar títulos, autores ni signaturas de `## Referencias Verificadas`. La mediana del corpus es de 110 palabras y 141 posts superan el tope (los peores, entre 300 y 411); las altas recientes de investigación extensa (1914-10-05, 1931-10-05, 1967-10-03) se sitúan entre 236 y 308 palabras.

## Normas de mantenimiento

1. Todo cambio del script debe contrastarse con los seis rectores vigentes.
2. Si cambian nombres de cabeceras, categorías, gradientes, dimensiones, enlaces, reglas D1-a/D2-a o las bandas de extensión y repetición, debe actualizarse el script en el mismo flujo autorizado por el editor. Toda auditoría nueva que afecte a normas no retroactivas nace en modo `[AVISO]` y se documenta aquí con sus cifras de corpus. Las demás normas de mantenimiento se conservan sin cambio.
3. El encabezado debe indicar las versiones rectoras contra las que fue auditado.
4. Las excepciones nuevas deben documentarse simultáneamente en el registro humano y en el archivo legible por máquina.
5. El linter debe ejecutarse después de la última edición. Si el post cambia luego, se renueva el timestamp y se vuelve a ejecutar.
6. `APROBADO` acredita conformidad estructural automatizada, no veracidad histórica ni suficiencia de licencias.
