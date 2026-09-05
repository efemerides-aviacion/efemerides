# Guía del validador estructural de efemérides

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

## Normas de mantenimiento

1. Todo cambio del script debe contrastarse con los seis rectores vigentes.
2. Si cambian nombres de cabeceras, categorías, gradientes, dimensiones, enlaces o reglas D1-a/D2-a, debe actualizarse el script en el mismo flujo autorizado por el editor.
3. El encabezado debe indicar las versiones rectoras contra las que fue auditado.
4. Las excepciones nuevas deben documentarse simultáneamente en el registro humano y en el archivo legible por máquina.
5. El linter debe ejecutarse después de la última edición. Si el post cambia luego, se renueva el timestamp y se vuelve a ejecutar.
6. `APROBADO` acredita conformidad estructural automatizada, no veracidad histórica ni suficiencia de licencias.
