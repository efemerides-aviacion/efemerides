# Protocolo de continuidad entre sesiones

> Propuesta operativa preparada el 5 de septiembre de 2026. No modifica por sí sola los seis rectores ni levanta su moratoria. Su finalidad es que cada `AAAA-MM-DD-ESTADO-Y-PENDIENTES.md` permita reconstruir una sesión nueva sin memoria implícita ni archivos locales heredados.

## Principio

El estado diario es un **puente autosuficiente de reconstrucción**, no solo un resumen narrativo. Debe distinguir con claridad la fuente de verdad remota, las reglas vigentes, lo cerrado, lo pendiente y los elementos locales que podrían no sobrevivir al cambio de chat.

## Estructura obligatoria del estado diario

### 0. Resumen ejecutivo

Debe indicar, de forma breve:

- fecha y condición del cierre;
- rama y HEAD al cierre;
- publicaciones o correcciones realizadas;
- número de posts verificado;
- pendientes reales y tareas con fecha;
- incidencias que impidan abrir normalmente la sesión siguiente.

No debe afirmar «sin pendientes» si otro apartado contiene tareas futuras.

### 1. Fuente de verdad: repositorio, rama y HEAD

Debe incluir literalmente:

- sitio: `https://efemerides-aviacion.github.io/efemerides/`;
- repositorio: `https://github.com/efemerides-aviacion/efemerides`;
- rama: `restauracion-efemerides-3`;
- HEAD completo y abreviado;
- fecha y hora de la consulta a la API;
- número de posts y cualquier otro recuento realmente verificado.

La sesión siguiente debe contrastar el HEAD registrado con:

```text
https://api.github.com/repos/efemerides-aviacion/efemerides/branches/restauracion-efemerides-3
```

### 2. Rectores y herramientas vigentes

Debe enumerar nominalmente los seis rectores y sus versiones:

1. `docs/plantilla-maestra-efemerides-v2.18.md`
2. `docs/instrucciones-formato-efemerides-v2.15.md`
3. `docs/instrucciones-procesar-efemerides-v2.14.md`
4. `docs/manual-estilo-efemerides-v1.15.md`
5. `docs/anexo-comparacion-tratamientos-y-rangos.md`
6. `docs/excepciones-rangos-y-tratamientos.md`

Debe registrar también:

- si sigue vigente la moratoria de versiones;
- ruta y versión del linter;
- ruta del archivo de excepciones legible por máquina;
- hash SHA-256 de las herramientas que no estén versionadas;
- forma de recuperarlas si faltan en el workspace.

Una herramienta obligatoria no puede depender únicamente de `/home/user`. Mientras no esté versionada, debe adjuntarse al abrir la sesión o conservarse junto al documento de estado.

### 3. Trabajo cerrado y publicado en la jornada

Por cada alta, corrección o actualización:

- identificación del trabajo;
- commit;
- estado de publicación;
- resultado del cotejo del post;
- resultado del cotejo visual y dimensional de la imagen;
- enlaces verificados por el editor;
- incidencias relevantes y su resolución.

No se repite aquí toda la investigación del post.

### 4. Pendientes y frentes suspendidos

Debe separar:

- tareas activas;
- tareas con fecha;
- frentes suspendidos por falta de fuentes;
- entregables pendientes de revisión o publicación;
- enlaces recíprocos pendientes;
- acciones que corresponden al editor.

Todo elemento resuelto debe salir de este apartado en el siguiente cierre.

### 5. Criterios editoriales consolidados

Solo se registran decisiones que afecten sesiones futuras. Cada una se marca como:

- **RECTOR:** ya incorporada a documentación normativa;
- **PROVISIONAL:** acordada, pero todavía no incorporada;
- **TÉCNICA:** lección del entorno que no altera el estilo público.

No se arrastran indefinidamente reglas ya localizables y claras en los rectores; basta la remisión correspondiente.

### 6. Observaciones sin acción y asuntos reservados al editor

Incluye candidatos futuros y hechos conocidos que no constituyen una tarea inmediata. Debe explicar expresamente quién decide su activación.

No debe mezclar elementos «resueltos y publicados» con pendientes. Los cerrados pasan al historial de la jornada y salen en el siguiente estado.

### 7. Espacio de trabajo y conservación

Configuración reconstruible recomendada:

```text
/home/user/
  efemerides/                         clon disperso de consulta
  efemerides-linter.sh                solo mientras no esté versionado
  en-proceso/
    post/                              entregables de texto pendientes
    img/                               imágenes pendientes
  AAAA-MM-DD-ESTADO-Y-PENDIENTES.md   puente vigente
```

Clonado de apertura:

```bash
git clone --filter=blob:none --no-checkout \
  --branch restauracion-efemerides-3 \
  https://github.com/efemerides-aviacion/efemerides.git efemerides

git -C efemerides sparse-checkout init --cone
git -C efemerides sparse-checkout set docs _posts
git -C efemerides checkout restauracion-efemerides-3
```

Reglas:

- nunca materializar `assets/img`;
- no asumir que el `.git` o los archivos locales sobreviven a un chat nuevo;
- `en-proceso/` se purga solo después de confirmar publicación y cotejo;
- las carpetas de resguardo solo se eliminan por orden del editor;
- el agente no hace commit ni push;
- el editor publica mediante GitHub Desktop.

El estado debe inventariar cualquier archivo local único y explicar si debe adjuntarse en la próxima apertura.

### 8. Calendario vivo

Debe limitarse a:

- fechas próximas con trabajo activo;
- efemérides recientemente publicadas que afecten enlaces nuevos;
- huecos, duplicidades o compromisos expresos;
- frentes suspendidos con posible fecha de reanudación.

No debe convertirse en un historial acumulativo de todo el proyecto.

### 9. Protocolos obligatorios de apertura y cierre

#### Apertura

1. Leer íntegramente el estado adjunto.
2. Consultar la API y comparar el HEAD remoto con el registrado.
3. Reconstruir el clon disperso con la rama explícita.
4. Confirmar que `assets/img` no se materializó.
5. Leer íntegramente los seis rectores antes de aceptar una efeméride.
6. Restaurar y comprobar el linter y su archivo de excepciones.
7. Verificar recuento de `_posts`, calendario y pendientes.
8. Informar cualquier ausencia o divergencia antes de producir contenido.

Si no es posible acceder al repositorio, los rectores o una herramienta obligatoria, debe indicarse expresamente y suspenderse cualquier entrega que dependa de ellos.

#### Cierre

1. Confirmar con la API el HEAD publicado final.
2. Cotejar los posts byte a byte contra la rama, aceptando las ediciones del editor como estado vigente.
3. Cotejar imágenes por contenido, encuadre y dimensiones; no objetar la recomprensión del editor.
4. Registrar commits, publicaciones, incidencias y pendientes reales.
5. Depurar del estado los asuntos ya resueltos.
6. Inventariar archivos locales únicos y mecanismos de recuperación.
7. Generar el estado con esta estructura.
8. Sellarlo con `TZ=America/Mexico_City date` después de la última edición.
9. Si el estado cambia después del sello, volver a sellarlo.

## Control mínimo de coherencia del estado

Antes de entregarlo debe comprobarse:

- el número de commits mencionado coincide con la lista;
- «sin pendientes» no contradice apartados posteriores;
- todo pendiente tiene estado y responsable;
- los nombres y versiones de rectores coinciden con la rama;
- el HEAD coincide con la API;
- las rutas de recuperación son completas;
- ninguna herramienta obligatoria queda referida solo por una ruta local efímera;
- el documento sustituido queda identificado claramente.
