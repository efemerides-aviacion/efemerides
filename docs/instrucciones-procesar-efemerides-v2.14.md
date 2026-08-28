# Documento de Instrucciones Editoriales para Procesar Efemérides de Aviación
> Última actualización: 2026-08-28  
> Versión: v2.14

---

## PRINCIPIO FUNDAMENTAL DE INTEGRIDAD
**Regla de oro:** solo incluir información verificada en fuentes confiables. La ausencia de datos es preferible a la invención o deducción.

---

## COMPORTAMIENTO OPERATIVO DEL ASISTENTE

### 1) Respetar el grado de intervención pedido por el usuario
Si el usuario:
- pide una efeméride nueva → generar el post completo;
- pide solo una corrección puntual → entregar el snippet exacto;
- pide solo un `<figure>` → devolver únicamente el `<figure>`;
- pide solo el commit → no reabrir el post completo;
- dice explícitamente **“no regeneres el post”** → no regenerar el post.

### 2) Respetar la edición manual del usuario
Si el usuario ya ajustó manualmente en su repositorio:
- título;
- categoría;
- divisor;
- enlaces;
- imagen;

no debe “corregírsele de vuelta” salvo instrucción expresa. La prioridad es **acompañar** el flujo editorial real, no forzarlo.

### 3) No discutir cambios de repo ya asumidos
Si el usuario ya cambió el nombre de archivo, el título público o la categoría en el repositorio, debe asumirse como la referencia editorial vigente, salvo que el propio usuario pida reevaluarlo.

---

## FORMATO DE LA SOLICITUD DEL USUARIO

Estructura mínima esperada:

```markdown
# Efeméride
## Fecha
AAAA-MM-DD
## Tema
[Descripción breve]
## Categoría
[nacimiento / evento / fundacion / accidente / seguridad / supervivencia / espacial / conmemoracion]
## Archivo del post
AAAA-MM-DD-nombre-del-archivo.md
```

**Campo `fecha_publicacion`.** El borrador que aporta el editor incluye en su
cabecera YAML el campo `fecha_publicacion`, con el día previsto de salida. Las
efemérides se publican **el mismo día y el mismo mes del hito**, de modo que ese
campo determina el año que debe emplearse para calcular los años transcurridos
(véase «Cómputo de años transcurridos»). Si el campo no consta, se toma el año en
curso.

Campos opcionales frecuentes:
- `Título del post`
- `Imagen`
- `Pie de foto`
- `Referencias`
- `Información relevante`
- `Información previa`
- `Resumen ejecutivo (borrador)`
- `Nota importante`

---

## CRITERIO DE SUSPENSIÓN

Si no se encuentran al menos dos fuentes primarias o institucionales capaces de sostener el núcleo del hecho, debe detenerse la generación y reportarse:

> “Información insuficiente para generar efeméride verificable. Datos faltantes: [especificar]. Se requiere investigación adicional.”

### Mínimo de referencias del post publicado

Sostener el núcleo del hecho y documentar el post son exigencias distintas.
**Todo post lleva al menos cuatro referencias verificadas**, de las cuales dos
como mínimo han de ser primarias o institucionales. Regla vigente desde el 16
de agosto de 2026, motivada por tres efemérides consecutivas entregadas con
solo dos referencias.

El borrador preliminar aportado por el editor **no computa** a estos efectos y
no se cita en el post.

---

## FASE DE INVESTIGACIÓN PREVIA

1. Buscar fuentes primarias, institucionales o documentales sólidas.
2. Contrastar los datos críticos con múltiples fuentes independientes.
3. Resolver discrepancias de fecha, lugar, nombres, cifras o clasificación.
4. Determinar si la imagen propuesta por el usuario puede usarse realmente.
5. Si una imagen concreta no puede descargarse por bloqueo técnico, **decirlo expresamente al editor, en el chat**.
6. Verificar que cada referencia corresponda de verdad al tema del post, **leyendo
   su contenido y no solo comprobando que responde**. Un código 200 no acredita
   nada sobre el sujeto de la página. Si una URL aportada en el borrador no
   responde, **buscar primero la ruta vigente o un equivalente de solvencia
   comparable**; solo si la búsqueda resulta infructuosa se informa al editor por
   chat, para que pueda facilitar una fuente accesible.
7. Documentar en nota aclaratoria los puntos no totalmente cerrados **que interesen
   al lector**; las incidencias del proceso se reservan para el chat.
8. Si el usuario dejó el título en blanco, generarlo con el patrón:
   - `“[día] de [mes] de [año] | [descripción precisa del hecho]”`

---

## POLÍTICA DE IMÁGENES

### 1) Prioridad de la selección del usuario
La imagen propuesta por el usuario tiene prioridad editorial cuando sea usable y verificable.

### 2) Si el origen bloquea la descarga
Debe explicarse sin ambigüedad **al editor, en el chat**:
- que la imagen se consideró;
- que el entorno no pudo descargarla o utilizarla;
- cuál fue el motivo técnico observable (403, anti-bot, Cloudflare, etc.).

Esta explicación **no se traslada nunca al post**.

### 3) Sustitución de imagen
Solo sustituir por otra imagen:
- si el usuario lo permite;
- o si la imagen original es inaccesible y se informa de forma transparente al editor.

### 4) Verificación de la ficha de origen
Antes de descargar una imagen o de enlazar su ficha en el `<figure>`, debe leerse
la ficha y confirmarse que el sujeto retratado es el de la efeméride. La
comprobación abarca el título de la propia ficha, el identificador digital, la
fecha, la imagen y el estado de derechos.

La cautela es máxima en los repositorios de identificadores correlativos
—`loc.gov`, `iwm.org.uk`, `archives.gov`, `nationalmuseum.af.mil`,
`images.nasa.gov`, archivos fotográficos nacionales—, donde una cifra equivocada
devuelve una ficha válida y ajena al asunto.

Si se descubre que una ficha empleada no corresponde al sujeto, se sustituye por la
correcta y se informa al editor por chat. La incidencia **no se consigna en el
post**.

### 5) Pie de foto
Nunca atribuir a una imagen representativa una fecha, lugar o identidad que no tenga realmente.

### 6) Tamaño de casa
Las imágenes se entregan a **800 × 1.000** en `nacimiento` y a **1.200 × 675**
en el resto, con ampliación de calidad (Lanczos + unsharp) si la toma es menor (Plantilla v2.16,
regla maestra 12). WebP quality 90-92, method 6. El nombre de archivo coincide con el del post. La resolución no se menciona en el post.

### 7) Fecha de hechos pluridiarios
Se conmemora la **culminación** (aterrizaje, llegada, término), no el inicio. Excepción: Apolo 11 (20 de julio).


---

## ENLACES CRUZADOS ENTRE EFEMÉRIDES

### Regla editorial consolidada
- evitar repetir la misma URL dentro del post;
- pueden utilizarse varios enlaces cruzados distintos si son pertinentes;
- debe colocarse preferentemente en `## Desarrollo Cronológico`;
- solo usar la URL pública real del post ya publicado;
- nunca enlazar una efeméride consigo misma;
- no usar rutas `.md`, `post_url`, URLs inventadas o estructuras futuras inferidas.

---

## ESTRUCTURA OBLIGATORIA DEL POST FINAL

1. YAML inicial
2. `<figure>`
3. Resumen Ejecutivo
4. `## Datos verificados del evento`
5. `## Contexto Histórico`
6. `## Desarrollo Cronológico`
7. `## Consecuencias e Impacto`
8. `## Legado`
9. `## Referencias Verificadas`
10. `Nota aclaratoria` (si aplica)
11. `## Metadatos de Control`

### Cabeceras rígidas
Las cabeceras normativas no deben alterarse.

### Introducciones obligatorias
Todo título de nivel 2 o 3 debe ir seguido de un párrafo introductorio, salvo:
- `## Datos verificados del evento`
- `## Referencias Verificadas`

---

## METADATOS DE CONTROL

Debe usarse la versión actualizada:

```markdown
## Metadatos de Control
- **Timestamp de verificación:** ...
- **Fuentes primarias/institucionales consultadas:** ...
- **Fuentes secundarias de contraste:** ... *(nunca el borrador preliminar del editor)*
- **Discrepancias resueltas:** ... *(solo divergencias entre fuentes publicadas; se omite el campo si no las hubo)*
- **Nivel de confianza:** Alto / Medio / Bajo
- **Cláusula final:** “Cuando una afirmación relevante no pudo ser confirmada, se omitió o se marcó como [NO CONFIRMADO]”.
```

---

## CÓMPUTO DE AÑOS TRANSCURRIDOS

Las efemérides se publican el mismo día y el mismo mes del hecho. La distancia
temporal entre el hito y su publicación es por tanto un número entero exacto de
años:

```
años transcurridos = año de publicación − año del hito
```

El año de publicación procede del campo `fecha_publicacion` del borrador.

**Ejemplo.** Hito del 9 de agosto de 1945 publicado el 9 de agosto de 2026:
2026 − 1945 = **81 años**. Corresponde escribir «ochenta y un años después», no
«ochenta años después».

**Alcance.** La regla se aplica a cualquier mención de la distancia con el
presente, en cualquier sección, aunque su lugar habitual es `## Legado`. Quedan
sujetas a verificación las fórmulas «X años después», «X décadas más tarde», «un
siglo después», «X años antes de hoy» y toda referencia a un aniversario.

**Criterio.** Se emplea siempre la cifra exacta. Solo cabe una expresión
aproximada cuando la comparación no es con la fecha de publicación sino con un
tercer hecho histórico de datación imprecisa.

**Comprobación.** Forma parte de la lista de control interna que se ejecuta al
cerrar el documento y, como el resto de comprobaciones rutinarias, no se menciona
en el post.

---

## POLÍTICA DE REDACCIÓN Y TONO

- tono respetuoso, sobrio y profesional;
- evitar sensacionalismo;
- distinguir hechos confirmados de hipótesis;
- no mezclar referencias ajenas a la efeméride en curso;
- no sobrecargar con enlaces internos innecesarios;
- capitalizar grados militares cuando aplique.

---

## VERIFICACIÓN EN PRODUCCIÓN Y ENTORNO TÉCNICO

### 1) El navegador del editor es el único verificador de producción
Las sondas de red del entorno del investigador devuelven 404 envejecidos contra
`efemerides-aviacion.github.io` y **no son medio de verificación**. La
comprobación en producción la realiza el editor en su navegador (captura o
confirmación) tras cada push. El investigador verifica en local con el
verificador del repositorio y mediante lectura de fuentes.

### 2) Consulta del catálogo: clon disperso con rama, o API
Para consultar el corpus se usa clon disperso apuntando a la rama de
publicación:

```
git clone -b restauracion-efemerides-3 --depth 1 --filter=blob:none --sparse <repo>
git sparse-checkout set _posts
```

o la API/raw de GitHub para archivos puntuales. Prohibido el clon íntegro:
satura el espacio de trabajo compartido. Sin el modificador de rama, el clon
trae contenido ajeno y el catálogo miente (precedente: omisión de un enlace a
Los Rodeos en la efeméride de Aviaco, 2026-08-09).

### 3) Reconstrucción de texto desde PDF
Al reconstruir párrafos desde extracciones de PDF: (a) no aplicar la unión de
guion de corte de línea a renglones que terminan dentro de una URL (los slugs
con guiones quedan mutilados y producen 404); (b) en las traducciones
entregables, todas las referencias llevan hiperenlace activo con las mismas URL
del post en español, no solo las que aparezcan visibles en el texto fuente.

### 4) Editores y visores no son entorno de verificación
La vista previa de Markdown de Visual Studio Code no navega enlaces `<a>`
inline: un enlace que allí parece muerto puede estar sano en producción, y
viceversa. Toda discrepancia observada en el editor se contrasta en el
navegador antes de tocar el post.

---

## LECTURA OBLIGATORIA DEL ARCHIVO FINAL

Antes de entregar o presentar cualquier post en chat, debe hacerse una lectura completa del archivo final mediante `read_file` para detectar:
- mezcla de datos de otros posts;
- errores de plantilla;
- restos de autocrítica o notas internas;
- enlaces mal copiados;
- duplicidades no deseadas.

---

## FLUJO DE COMMIT

### Regla vigente
El commit debe proponerse **después** de que el usuario revise el contenido o después de incorporar sus observaciones finales.

### Interpretación editorial
Ese commit debe funcionar como la **incorporación formal** del post al repositorio, no como un parche provisional de corrección.

### Formato obligatorio
El commit se aplica y empuja con **GitHub Desktop**. La entrega consiste en los
archivos finales listos para copiar al clon y el mensaje en los dos campos de
la interfaz, conforme a «Mensajes de commit para GitHub Desktop» de las
Instrucciones de Formato (v2.8):
- **Resumen (Summary):** frase descriptiva en español que nombra el cambio.
- **Descripción (Description):** viñetas con archivos (ruta en el repo) y notas
  pertinentes (imagen y licencia, enlaces internos, documento base).

Quedan derogados el prefijo `feat(efemerides): ...` y el cierre Categoría/País.
No se entregan parches `git am` ni commits construidos en el clon del entorno.
Los cambios homogéneos de muchos archivos se agrupan en tandas cronológicas con
mensaje propio; cada efeméride nueva viaja en un commit único con su imagen.
Las **altas individuales** se entregan como archivos directos en el espacio de
trabajo del asistente (`en-proceso/post/` y `en-proceso/img/`, presentados en el
visor) más el mensaje de commit en texto; **el ZIP queda reservado a las tandas
de corrección** que alcanzan a varios posts, con la estructura del repo. El
espacio `en-proceso/` se depura tras cada publicación confirmada. Práctica
acordada los días 27 y 28 de agosto de 2026, cuando el ZIP llegó a emplearse
para una alta única y quedó derogado para ese caso.

### Correcciones sobre posts ya publicados
Los cambios a posts ya publicados (enlaces recíprocos, armonización de nombres,
divisores, pies de foto) se entregan como **commits de corrección propios**,
posteriores al commit de la efeméride nueva, con mensaje que lista los archivos
y el cambio; nunca mezclados con el commit de incorporación de una efeméride.
Práctica consolidada el 14 de agosto de 2026 (posts de los hermanos Wright).

### Comprobación del estado publicado
La verificación en producción corresponde al navegador del editor. La del
asistente se hace **contra un clon fresco de la rama**: el `.git` del entorno de
trabajo no persiste entre sesiones, de modo que el clon se rehace siempre y lo
publicado solo se lee —lo ya publicado no se regenera ni se modifica; el clon es
la fuente de verdad—. Cotejos: el post publicado debe ser idéntico byte a byte
al entregado, salvo las correcciones que el editor haya aplicado, las cuales
prevalecen y no se revierten. Las imágenes las reexporta el editor al publicar
(perfil ICC, peso y suma de verificación distintos, mismas cotas y encuadre):
el cotejo es de encuadre y dimensiones, nunca de md5, y la recodificación se
asume como estado vigente. Práctica registrada los días 27 y 28 de agosto de
2026 (jornadas de los altos de KAL 007 y Varig 254).

---

## PROHIBICIONES ABSOLUTAS

- no inventar ni deducir datos faltantes;
- no usar URLs ficticias;
- no incluir marcadores `[citation:X]`;
- no reciclar referencias de otro post sin pertinencia real;
- no usar URLs futuras inferidas de posts no publicados;
- no sustituir silenciosamente una imagen concreta que el usuario pidió;
- no dar por verificada una URL por el solo hecho de que responda;
- no enlazar en el `<figure>` una ficha de archivo sin haber confirmado que su
  contenido corresponde al sujeto de la efeméride;
- no regenerar un post completo cuando el usuario solo pidió un snippet o un commit;
- no revertir sin permiso una edición manual ya asumida en el repositorio.

---

## CHECKLIST FINAL
- [ ] El hecho principal está verificado.
- [ ] La imagen es correcta o se explicó al editor, por chat, por qué no pudo usarse la solicitada.
- [ ] La imagen está al tamaño de casa (800 × 1.000 en nacimiento; 1.200 × 675 en el resto) y su nombre coincide con el del post.
- [ ] El post está limpio: no menciona el borrador preliminar, sus errores, enlaces caídos ni el entorno técnico.
- [ ] Se verificó la coherencia entre fecha, título, nombre de archivo y YAML **sin dejar constancia de ello en el post**.
- [ ] «Discrepancias resueltas» contiene divergencias reales entre fuentes, no trámites del procedimiento.
- [ ] Los años transcurridos desde el hito se calcularon sobre el año de `fecha_publicacion` y no se redondearon.
- [ ] Cada URL se validó por su contenido y no por su código de respuesta.
- [ ] Se leyó la ficha de archivo enlazada en el `<figure>` y su sujeto es el de la efeméride.
- [ ] Las incidencias del proceso se comunicaron al editor en el chat, no en el documento.
- [ ] Los enlaces en el texto usan HTML inline con estilo sin subrayado.
- [ ] Solo hay enlaces cruzados si realmente aportan valor.
- [ ] No hay URLs públicas inferidas para posts inéditos.
- [ ] Los metadatos **no** citan el borrador preliminar como fuente de contraste.
- [ ] El post tiene al menos cuatro referencias verificadas, dos de ellas primarias o institucionales.
- [ ] Los grados militares están capitalizados.
- [ ] Se hizo `read_file` completo antes de presentar.
- [ ] Si el usuario pidió solo un snippet, se respondió solo con el snippet.
- [ ] El commit se propone al final del flujo, no al principio.
- [ ] Los enlaces internos usan la URL canónica con barras y el slug sin guion terminal.
- [ ] La verificación en producción se encargó al navegador del editor, no a las sondas del entorno.

---

## CONTROL DE CAMBIOS

| Versión | Fecha | Descripción |
| :--- | :--- | :--- |
| v2026-06 | 2026-07-01 | Base operativa heredada del documento anterior. |
| v2.1 | 2026-07-28 | Consolidación de divisores por sección, timestamp dinámico, enlaces cruzados sin repetir URL, nuevas categorías, formato numérico, coherencia de fechas y nombres de archivo, transparencia de imágenes y política de commits. |
| v2.2 | 2026-07-29 | Alineación de versiones entre los cuatro documentos rectores tras la corrección de coherencia sobre enlaces cruzados. |
| v2.3 | 2026-08-01 | Principio de documento limpio: el post no relata el proceso de investigación. Se excluyen del documento publicado los errores del borrador, los enlaces inaccesibles y las incidencias del entorno; se comunican al editor por chat. |
| v2.4 | 2026-08-02 | El principio de documento limpio alcanza a las comprobaciones rutinarias del flujo de trabajo. Se proscribe en el post la fórmula sobre la verificación de coherencia entre fecha, título, archivo y YAML. |
| v2.5 | 2026-08-04 | Regla de cómputo de años transcurridos: al publicarse la efeméride el mismo día y mes del hito, los años se obtienen restando el año del hecho al del campo `fecha_publicacion`. Se exige cifra exacta y se añade la comprobación al checklist final. |
| v2.6 | 2026-08-05 | Regla de verificación de contenido de las fuentes: las URLs se validan leyendo su contenido, no por su código de respuesta. Se incorpora la verificación obligatoria de la ficha de origen de las imágenes —título, identificador, fecha, imagen y derechos— con exigencia máxima en repositorios de identificadores correlativos. Se amplían prohibiciones absolutas y checklist final. |
| v2.7 | 2026-08-09 | Se incorpora la sección «Verificación en producción y entorno técnico»: el navegador del editor es el único verificador de producción; consulta del catálogo por clon disperso con rama o API; reconstrucción de PDF sin mutilar URL y con hiperenlaces completos en traducciones; VS Code no es entorno de verificación. Se añaden comprobaciones al checklist final. |
| v2.8 | 2026-08-12 | Flujo de commit alineado con la práctica real de GitHub Desktop: entrega de archivos finales más mensaje Resumen/Descripción; tandas cronológicas para cambios homogéneos; commit único por efeméride nueva. Derogado el esquema `feat(efemerides):` con cierre Categoría/País. Prohibidos los parches `git am` y los commits en el clon del entorno. |
| v2.11 | 2026-08-20 | Tamaño de casa 800×1000 / 1200×675; se permite ampliar. |
| v2.12 | 2026-08-20 | Nombre de imagen = post; conteo de refs; hechos pluridiarios en la culminación. |
| v2.13 | 2026-08-21 | Alineación con la Plantilla Maestra v2.16 y el Manual de Estilo v1.13 (renumeración de § 8: la verificación de contenido pasa de § 8.4 a § 8.6). Sin cambios de fondo. |


---

## ACTUALIZACIONES EDITORIALES V2.1 — 2026-07-28

### Divisores de sección
Todo post debe conservar un divisor `<hr>` antes de cada sección principal, desde `## Datos verificados del evento` hasta `## Metadatos de Control`, utilizando el degradado correspondiente a la categoría.

### Enlaces cruzados
La regla limita la repetición de la misma URL, no la cantidad absoluta de enlaces pertinentes. Pueden utilizarse varios enlaces cruzados distintos cuando aporten valor. Nunca debe enlazarse una efeméride consigo misma.

### Timestamp
El `Timestamp de verificación` debe generarse dinámicamente al concluir el procesamiento, reflejando la fecha y hora local exactas. No se deben reutilizar timestamps.

### Imágenes y notas
Una imagen representativa debe identificarse como tal. Las notas y metadatos deben tratar únicamente aspectos históricos, técnicos o documentales; no deben describir cambios internos del flujo editorial ni sustituciones realizadas durante el trabajo. *(Ampliado en la v2.3: véase «Principio de documento limpio».)*

### Fechas y nombres de archivo
Antes de redactar, verificar que fecha, tema, título, nombre del archivo, `date` del YAML y URL pública sean coherentes. Toda discrepancia debe resolverse o documentarse.

### Commit inicial
No proponer un commit hasta que el editor lo solicite expresamente. El commit inicial representa la incorporación formal limpia del post y no debe mencionar imágenes ni cambios internos del flujo.

### Categorías incorporadas
Se reconocen también `conmemoracion` y la combinación `[espacial, accidente]`, con sus divisores visuales específicos.

### Formato numérico
Usar punto para miles y coma para decimales. Siempre que sea pertinente, acompañar las unidades originales de su conversión al sistema métrico.

---

## ACTUALIZACIONES EDITORIALES V2.2 — 2026-07-29

### Corrección de coherencia sobre enlaces cruzados
Este documento no contenía formulaciones contrarias al criterio vigente: su
sección «ENLACES CRUZADOS ENTRE EFEMÉRIDES» ya expresaba correctamente la
regla. La versión se eleva a v2.2 únicamente para mantener alineados los
cuatro documentos rectores tras la corrección aplicada en el Manual de Estilo
y en la Plantilla Maestra.

### Criterio unificado vigente
- Una misma URL, una sola vez por post.
- Pueden emplearse varios enlaces cruzados distintos si son pertinentes.
- Nunca debe enlazarse una efeméride consigo misma.
- Solo se enlazan efemérides realmente publicadas, con su URL pública real.
- Ubicación preferente en `## Desarrollo Cronológico`.

---

## ACTUALIZACIONES EDITORIALES V2.3 — 2026-08-01

### Principio de documento limpio

El post publicado es un producto historiográfico dirigido al lector. Contiene el
**resultado** de la investigación, no su crónica.

**Nunca se consigna en el post:**
- que el borrador preliminar del investigador contenía errores, fechas equivocadas,
  cifras inexactas o atribuciones incorrectas;
- que una URL del borrador devolvió 403, 404 o bloqueo anti-bot;
- que una fuente se sustituyó por otra debido a un problema de acceso;
- que una ruta quedó obsoleta y se localizó la vigente;
- ninguna alusión al entorno técnico de trabajo ni a su flujo de verificación.

**Se comunica al editor por chat:**
- las discrepancias detectadas entre el borrador y la investigación propia, con el
  detalle que resulte útil para que quede en conocimiento de ellas;
- los enlaces inaccesibles, **una vez agotada la búsqueda de un reemplazo
  equivalente**, para que el editor valore aportar una fuente alternativa;
- las decisiones de sustitución de fuentes o imágenes y su motivo.

**Permanece en el post, por su valor para el lector:**
- la divergencia entre fuentes publicadas y solventes (cifras que no coinciden entre
  instituciones, fechas alternativas, husos horarios, denominaciones);
- la advertencia de que la imagen es representativa y no exacta.

**Criterio de discernimiento:** si el dato interesa a quien lee la efeméride, va al
post; si solo interesa a quien la produce, va al chat.

---

## ACTUALIZACIONES EDITORIALES V2.4 — 2026-08-02

### Las comprobaciones del procedimiento no se publican

La verificación de coherencia entre la fecha del hecho, el título, el nombre del
archivo, el campo `date` del YAML y la URL pública sigue siendo **obligatoria en
cada efeméride**. Lo que cambia es su tratamiento documental: es un paso de la
lista de control interna y **no se menciona en el post**.

**Proscrito en el documento publicado:**
- «se verificó la coherencia entre la fecha del hecho, el título, el nombre del
  archivo y el YAML»;
- cualquier variante que describa un trámite del flujo de trabajo como si fuera
  un hallazgo de la investigación.

**Razón:** al lector le interesa saber que dos instituciones discrepan sobre una
cifra; no le aporta nada leer que el redactor comprobó que el nombre del archivo
coincide con la fecha. Lo primero es historiografía; lo segundo, higiene interna.

### Cuándo omitir el campo

Si la investigación no arroja divergencias entre fuentes publicadas, el campo
«Discrepancias resueltas» se suprime de los metadatos en lugar de rellenarse con
comprobaciones rutinarias.

---

## ACTUALIZACIONES EDITORIALES V2.5 — 2026-08-04

### Cómputo de años transcurridos

Se incorpora una sección propia con la regla de cálculo y se documenta en «Formato
de la solicitud del usuario» la función del campo `fecha_publicacion` del borrador,
que hasta ahora no tenía uso normativo asignado.

**Origen de la regla.** En la efeméride de Nagasaki del 9 de agosto de 1945,
prevista para el 9 de agosto de 2026, el texto de salida decía «ochenta años
después» cuando la cifra correcta era ochenta y uno. El error nace de asociar el
hito a una cifra redonda de aniversario en lugar de calcularla.

**Consecuencia operativa.** La verificación se añade al checklist final. Como toda
comprobación del procedimiento, se ejecuta siempre y no se menciona en el post.

---

## ACTUALIZACIONES EDITORIALES V2.6 — 2026-08-05

### Verificación de contenido de las fuentes

El punto 6 de la fase de investigación previa pasa a exigir la lectura del
contenido de cada URL. Un código de respuesta 200 acredita que el servidor
devuelve una página, no que esa página trate del sujeto de la efeméride.

### Verificación de la ficha de origen de las imágenes

Se incorpora un nuevo apartado 4 a la política de imágenes. Antes de descargar una
imagen o de enlazar su ficha en el `<figure>` deben confirmarse el título de la
ficha, el identificador digital, la fecha, la imagen y el estado de derechos. La
exigencia es máxima en los repositorios cuyos identificadores son correlativos,
donde un dígito equivocado devuelve una ficha impecable y ajena.

Motivo: en la efeméride del nacimiento de Hugo Eckener se enlazó en el `<figure>`
una ficha de la Library of Congress que respondía correctamente pero correspondía a
un retrato de Stanley Baldwin y su familia.

La sustitución de una ficha errónea es una incidencia del proceso: se comunica al
editor por chat y no deja rastro en el post.

---

## ACTUALIZACIONES EDITORIALES V2.7 — 2026-08-09

### Verificación en producción y entorno técnico

Se incorpora una sección nueva con cuatro apartados:

1. **El navegador del editor es el único verificador de producción.** Las sondas
   del entorno del investigador devuelven 404 envejecidos contra el dominio del
   blog y quedan descartadas como medio de verificación.
2. **Consulta del catálogo por clon disperso con rama** (`-b
   restauracion-efemerides-3 --depth 1 --filter=blob:none --sparse`) o API/raw;
   prohibido el clon íntegro. Sin el modificador de rama, el catálogo miente.
3. **Reconstrucción de texto desde PDF:** no aplicar la unión de guion de corte
   dentro de URL; las traducciones entregables llevan hiperenlaces activos en
   todas las referencias.
4. **VS Code no es entorno de verificación:** su vista previa no navega enlaces
   `<a>` inline.

Motivo: incidencias reales de las sesiones del 8 y 9 de agosto de 2026
(404 envejecidos de las sondas, clon disperso sin rama que omitió el enlace a
Los Rodeos, guion de corte que mutiló la URL de la efeméride de Jimmie Angel en
la traducción, y enlaces «muertos» en VS Code que estaban sanos en producción).

---

## ACTUALIZACIONES EDITORIALES V2.8 — 2026-08-12

### Flujo de commit conforme a GitHub Desktop
El esquema documental `feat(efemerides): ...` con cierre Categoría/País no se
correspondía con los commits reales de la rama («Nueva efeméride: …»,
«Correcciones al post de …», «Estandarización de títulos …»). Se reescribe el
«Formato obligatorio» del flujo de commit con la práctica consolidada y
validada por el editor: archivos finales más mensaje en los campos Resumen y
Descripción de GitHub Desktop; tandas cronológicas de unos diez archivos para
cambios homogéneos; commit único por efeméride nueva con su imagen. El intento
de entregar un parche `git am` el 11 de agosto motivó la precisión del
investigador: el formato del commit es para GitHub Desktop.

### Remisiones cruzadas de la ronda del 12 de agosto
- Separadores entre bloques: regla maestra 13 de la Plantilla Maestra v2.10.
- Títulos con hazaña o cualidad y grados de la aviación: Manual de Estilo v1.8,
  §§ 4.6 y 4.3.
- Series en enlaces cruzados y fuentes limpias con licencia: Manual de Estilo
  v1.8, §§ 6.3 y 7.7.


---

## ACTUALIZACIONES EDITORIALES V2.10 — 2026-08-16

### El borrador preliminar no se cita como fuente
El borrador que aporta el editor es un insumo **opcional, no preferible**:
procede de modelos generativos que introdujeron datos erróneos y atribuciones
inventadas. Queda derogada la fórmula «borrador preliminar del investigador»
como fuente de contraste en «Metadatos de Control». El borrador se usa como
punto de partida; cada dato que aporte se verifica en fuente publicada y es esa
fuente la que se cita. Las discrepancias con el borrador se comunican al editor
por chat, como hasta ahora.

### Mínimo de cuatro referencias verificadas
Se incorpora al criterio de suspensión el suelo documental del post publicado:
cuatro referencias como mínimo, dos de ellas primarias o institucionales, sin
contar el borrador. Motivo: los tres posts anteriores al del BAe Hawk se
entregaron con solo dos referencias. Se añaden las dos comprobaciones
correspondientes al checklist final.

### Precedente de la ronda del 16 de agosto
En la reconstrucción de la efeméride del BAe Hawk (21 de agosto de 1974) se
detectó que la versión previa había tratado la descripción libre de una ficha
de Wikimedia Commons como si fuera una fuente en discrepancia, y sobre esa base
suprimió del post el aeródromo del primer vuelo, dato firmemente establecido
por Dunsfold Park, BAE Systems y la literatura. Se recuerda que las
descripciones de usuario en repositorios colaborativos **no son fuentes
publicadas y solventes** a efectos del campo «Discrepancias resueltas»
(regla maestra 10 de la Plantilla Maestra y § 8.6 del Manual de Estilo).


---

## ACTUALIZACIONES EDITORIALES V2.13 — 2026-08-21

### Alineación con los rectores corregidos
Pasada de coherencia entre los cuatro documentos, sin cambios de fondo.

- La **Plantilla Maestra** pasa a **v2.16**: segunda corrección de coherencia
  interna de sus ejemplos (25 cabeceras al nivel y capitalización de la regla
  maestra 1; ejemplo de `seguridad` saneado; cuatro ejemplos elevados al mínimo
  de cuatro referencias; etiqueta normativa en los metadatos).
- El **Manual de Estilo** pasa a **v1.13**: § 8 renumerada en orden correlativo.
  La verificación de contenido de las fuentes, que este documento citaba como
  § 8.4, es ahora **§ 8.6**. Se actualiza la remisión del apartado sobre
  descripciones de repositorios colaborativos.
- Las **Instrucciones de Formato** pasan a **v2.13** por el mismo motivo.

Ninguna regla operativa cambia: el mínimo de cuatro referencias, el tamaño de
casa, el cómputo de años y el principio de documento limpio permanecen tal como
quedaron el 20 de agosto.

## ACTUALIZACIONES DE PROCESAMIENTO V2.14 — 2026-08-28

### Entrega de altas individuales (sección de commit para GitHub Desktop)
Se fija en el rector el acuerdo del 27-28 de agosto de 2026: archivos directos
en `en-proceso/post/` e `en-proceso/img/` presentados en el visor, con mensaje
de commit en texto; ZIP solo para tandas de corrección multi-post; `en-proceso/`
purgado tras la confirmación de publicación.

### Comprobación del estado publicado (apartado nuevo)
Se consolida la práctica de verificación post-publicación: clon fresco siempre
(el `.git` del entorno no persiste), lo publicado no se toca, cotejo del post
byte a byte contra lo entregado aceptando las correcciones del editor, y
comparación de imágenes por encuadre y cotas sin discutir la recodificación del
pipeline (md5 no).

Alineadas en la misma fecha: Plantilla Maestra v2.17, Instrucciones de Formato
v2.14 y Manual de Estilo v1.14.