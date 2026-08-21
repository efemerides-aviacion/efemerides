# Documento Maestro de Plantillas de Efemérides de Aviación
> Última actualización: 2026-08-21  
> Versión: v2.16

---

## Nota sobre esta versión

**Novedad de la v2.16.** Segunda pasada de **coherencia interna** sobre los
ejemplos, en la línea de la v2.13 y por el mismo motivo: los ejemplos son el
modelo del que se copian los posts, y venían incumpliendo las reglas que este
documento impone. Ninguna regla cambia de fondo. (a) **Veinticinco cabeceras**
de los ejemplos se ajustan a la regla maestra 1: `Desarrollo Cronológico`,
`Consecuencias e Impacto` y `Legado` figuraban en **nivel 3** en siete de las
nueve plantillas, y `espacial` y `seguridad` las escribían además en minúscula
(`Desarrollo cronológico`, `Consecuencias e impacto`, `Contexto histórico`).
(b) El ejemplo de `seguridad`, el más dañado, tenía la cabecera `## Referencias`
en lugar de `## Referencias Verificadas`, `## Metadatos de control` en
minúscula, `Nivel de confianza: alto` en minúscula y un `</div` **sin cerrar**
que podía romper el render. (c) Cuatro ejemplos incumplían la **regla maestra
14**: `fundacion` y `supervivencia` traían tres referencias, y los placeholders
de `[espacial, accidente]` y `conmemoracion` una sola; ahora exhiben el mínimo
de cuatro. (d) Los metadatos de los siete ejemplos heredados usaban la etiqueta
`Fuentes primarias consultadas`, que pasa a la forma normativa **`Fuentes
primarias/institucionales consultadas`**. (e) El ejemplo de `supervivencia`
encabezaba sus datos con `## Datos biográficos y eventos`, una de las variantes
que la regla maestra 1 proscribe expresamente; pasa a `## Datos verificados del
evento`.

Tras esta pasada, los nueve ejemplos exhiben las siete cabeceras canónicas en
nivel 2 y el mínimo de cuatro referencias.

**Novedad de la v2.15.** Tres precisiones de la sesión del 20 de agosto de 2026: (a) el **nombre de archivo de la imagen coincide con el del post** (sin `.md`, extensión `.webp` o, si el editor entrega otro formato, esa extensión); (b) las referencias se **cuentan** por `<li>`, viñeta `-` y numeración `1.` —contar solo `<li>` da falsos positivos—; (c) los hechos de **más de un día** se conmemoran en la **culminación** (salvo Apolo 11). La regla maestra 12 (tamaño de casa y ampliación) no cambia.

**Novedad de la v2.14.** Se reescribe la **regla maestra 12**: las imágenes se entregan al tamaño de casa (**800 × 1.000** en `nacimiento`; **1.200 × 675** en el resto). Se permite y se espera ampliar con remuestreo de calidad. Queda derogado «no se amplían / resolución nativa». Se corrige la errata **678 → 675**. La resolución sigue sin mencionarse en el post (regla 8).

**Novedad de la v2.13.** Corrección de las **contradicciones internas de este
documento** en materia de separadores, detectadas al auditar la v2.12: sus
ejemplos incumplían sus propias reglas y venían propagando el defecto a los posts
que los tomaban como modelo. (a) Los **siete `<hr>` desnudos** que precedían al
`note-box` en los ejemplos de Fonck, Tenerife, A380, CASA, Mercury, EgyptAir y
Vesna Vulović adoptan el degradado de su categoría; (b) los **diez `<hr ... />`
autocerrados** de los ejemplos de `fundacion`, `espacial` y `[espacial,
accidente]` pasan a la forma normativa `<hr ...>`; (c) se añade a la tabla de
degradados la precisión de que **el separador previo a la nota aclaratoria cuenta
como divisor de sección** y lleva degradado, ambigüedad que originó las omisiones;
(d) se normaliza el doble espacio tras `to right,` en diez divisores. Ninguna
regla cambia de fondo: la v2.13 hace que los ejemplos obedezcan a las reglas que
el propio documento ya imponía desde la v2.1.

**Novedad de la v2.12.** Dos reglas de la sesión del 16 de agosto de 2026:
(a) el **borrador preliminar aportado por el editor deja de citarse** en el
post, también en los metadatos, por tratarse de un insumo opcional procedente
de modelos generativos que introdujeron datos erróneos (regla maestra 6,
reescrita); (b) **mínimo de cuatro referencias verificadas** por post, dos de
ellas primarias o institucionales (regla maestra 14).

**Novedad de la v2.10.** Se incorporan las normas de la sesión del 12 de agosto
de 2026: (a) la **regla maestra 13**, de separadores entre bloques: exactamente
una línea divisoria con el degradado de la categoría en cada frontera entre
bloques de primer nivel, ni más ni menos, y con la precisión de que `fundacion`
usa el mismo verde que `nacimiento`; (b) la extensión de la regla de grados a
las jerarquías de la aviación civil (*Capitán*, *Primer Oficial*) cuando
acompañan nombre propio (regla maestra 5 y Manual § 4.6).

**Novedad de la v2.9.** Se incorporan tres reglas de trabajo acordadas en las
sesiones del 8 y 9 de agosto de 2026: (a) la **URL canónica de los enlaces
internos** (regla maestra 11), con la fecha en barras y la pérdida del guion
terminal en los slugs; (b) las **imágenes al tamaño de casa** (reescrito en v2.14: se permite ampliar)
(regla maestra 12); (c) la extensión del principio de documento limpio: las
notas sobre resolución de imagen y las líneas de estado del documento no van en
el post, y la fórmula «borrador preliminar del investigador» se emplea únicamente
como fuente de contraste en los metadatos, nunca como línea de estado.
*(Derogado en la v2.12: el borrador ya no se cita en absoluto. Véase la regla
maestra 6.)*

**Novedad de la v2.8.** Se incorpora la **regla de verificación de contenido de las
fuentes** (regla maestra 10). Que una URL responda con código 200 no acredita nada
sobre lo que esa URL contiene. Antes de emplear una ficha de archivo, museo o
biblioteca —sea como referencia, como enlace del `<figure>` o como origen de una
imagen— debe leerse su contenido y confirmarse que el sujeto representado es el de
la efeméride. La comprobación es especialmente exigente en los repositorios cuyos
identificadores son correlativos y cuyas fichas contiguas corresponden a materias
sin relación entre sí.

**Novedad de la v2.7.** Se incorpora la **regla de cómputo de años transcurridos**
(regla maestra 9). Las efemérides se publican el mismo día y mes del hito, de modo
que el número de años que separa el hecho de la publicación es siempre exacto y
debe calcularse restando el año del hito al año de publicación. Toda mención del
tipo «ochenta años después» debe verificarse contra esa resta.

**Novedad de la v2.6.** Se precisa el alcance del campo «Discrepancias
resueltas»: las comprobaciones rutinarias del flujo de trabajo —entre ellas la
verificación de coherencia entre fecha, título, nombre de archivo y YAML— son
control de calidad interno y **no deben consignarse en el post**. Solo se
registran divergencias reales entre fuentes publicadas.

**Novedad de la v2.5.** Se incorpora el **principio de documento limpio**: el post
publicado es un producto historiográfico dirigido al lector, no un informe del
proceso de elaboración. En consecuencia, queda prohibido mencionar en el post
—en cualquier sección, incluidas la nota aclaratoria y los metadatos— el borrador
preliminar del investigador, sus errores, las URLs que no pudieron consultarse y
las incidencias técnicas del entorno de trabajo. Todo ello se comunica al editor
por chat. Véase la regla maestra 8.

Esta versión reconstruye el documento maestro a partir de la **v1.8 (2026-07-02)**,
recuperando las siete plantillas de ejemplo completas que se habían perdido en las
versiones v2.x, e incorporando las reglas editoriales consolidadas en la v2.1 y la
v2.2.

El motivo de la reconstrucción es que las versiones intermedias describían los
divisores de sección únicamente por el nombre del color (*«evento → azul»*), sin
los códigos hexadecimales. Esa laguna dio lugar a divisores erróneos en varias
efemérides. Las plantillas de ejemplo son la referencia operativa de la que se
extraen esos códigos, y su ausencia hacía el documento incompleto.

Se añaden además dos plantillas que no existían en ninguna versión anterior,
correspondientes a las categorías `[espacial, accidente]` y `conmemoracion`,
elaboradas a partir de efemérides reales ya publicadas en el repositorio. El
documento cubre así las nueve categorías reconocidas.

---

## Propósito del documento

Este documento reemplaza la lógica de ejemplos dispersos por una **plantilla maestra unificada** para todas las efemérides. Su objetivo es asegurar consistencia estructural, precisión editorial y compatibilidad con el estilo ya consolidado del proyecto.

Esta versión incorpora reglas nuevas surgidas del trabajo editorial reciente, entre ellas:
- uso obligatorio de enlaces HTML sin subrayado;
- explicación expresa cuando una imagen propuesta por el usuario no puede descargarse por bloqueo técnico;
- capitalización de grados militares en contextos históricos o castrenses;
- prohibición de citar el borrador preliminar del editor entre las fuentes (regla maestra 6);
- mínimo de cuatro referencias verificadas por post (regla maestra 14);
- prohibición de repetir la misma URL en enlaces cruzados; se permiten varios enlaces distintos y pertinentes, preferiblemente en `## Desarrollo Cronológico`;
- prohibición de usar URLs inferidas o futuras para posts no publicados;
- **principio de documento limpio**: el post no relata el proceso de investigación
  ni las incidencias del entorno de trabajo (regla maestra 8);
- **verificación de contenido de las fuentes**: ninguna URL se emplea por el solo
  hecho de responder; su contenido debe corresponder al sujeto (regla maestra 10).

---

## Reglas maestras aplicables a todas las categorías

### 1) Cabeceras obligatorias
Las cabeceras normativas del post deben mantenerse **exactamente** así:
- `## Datos verificados del evento`
- `## Contexto Histórico`
- `## Desarrollo Cronológico`
- `## Consecuencias e Impacto`
- `## Legado`
- `## Referencias Verificadas`
- `## Metadatos de Control`

No deben sustituirse por variantes como “Referencias”, “Contexto histórico”, “Estado actual”, “Conclusiones” o equivalentes, salvo autorización expresa del editor.

### 2) Enlaces HTML obligatorios
Dentro del cuerpo del post, las referencias internas o externas integradas en párrafos deben escribirse con este formato:

```html
<a href="https://ejemplo.com" style="color: #315fea; text-decoration: none;">texto del enlace</a>
```

#### Norma específica:
- No usar enlaces Markdown en mitad del texto si rompen la armonía visual.
- No usar subrayado por defecto.
- Verificar siempre la sintaxis correcta de `href`.

**Correcto ✅**
```html
<a href="https://ejemplo.com" style="color: #315fea; text-decoration: none;">enlace</a>
```

**Incorrecto ❌**
```html
<a href="[https://ejemplo.com](https://ejemplo.com)">enlace</a>
```

### 3) Enlaces cruzados entre efemérides
Cuando sea útil enlazar otra efeméride del proyecto:
- evitar repetir la misma URL dentro del post;
- permitir varios enlaces cruzados distintos cuando sean pertinentes;
- colocarlos de preferencia en `## Desarrollo Cronológico`;
- nunca enlazar el post consigo mismo;
- usar únicamente la **URL pública real** de una efeméride ya publicada;
- no usar `post_url`, nombres de archivo `.md` ni URLs futuras inferidas.

### 4) Imágenes seleccionadas por el usuario
Si el usuario indica una imagen concreta:
- debe intentarse priorizar esa imagen;
- si el origen bloquea la descarga por 403, anti-bot, Cloudflare u otra restricción técnica, se debe **decir expresamente al editor, en el chat**;
- no se debe sustituir silenciosamente por otra imagen sin explicarlo.

Fórmula recomendada en la comunicación con el usuario:
> “Se consideró la imagen propuesta, pero no pudo descargarse/emplearse desde este entorno por restricciones técnicas del sitio de origen.”

**Importante:** esta explicación pertenece siempre al chat, **nunca al post**. En el
documento publicado solo se consigna, si procede, que la imagen empleada no
corresponde al instante exacto del hecho (véase la sección de pies de foto y la
regla maestra 8).

### 5) Grados militares
En temas militares o biográficos castrenses, los grados deben escribirse con mayúscula inicial:
- `Teniente`
- `Capitán`
- `Mayor`
- `Teniente Coronel`
- `Coronel`
- `General de Brigada`

Las jerarquías de la aviación (*Capitán*, *Primer Oficial* y equivalentes) siguen
la misma regla cuando acompañan al nombre propio (*Capitán Omar Ospina*, *Primer
Oficial David Muñoz*); sin nombre propio van en minúscula (*el capitán desconecta
el autopiloto*).

### 6) Metadatos: el borrador no se cita

En `## Metadatos de Control` **no se menciona el archivo base aportado por el
editor**. Quedan derogadas las fórmulas `borrador preliminar del investigador` y
`borrador preliminar del usuario`, que hasta la v2.11 debían emplearse como
fuente de contraste.

**Motivo.** El borrador es un insumo **opcional, no preferible**: procede de
modelos generativos que introdujeron fechas equivocadas, cifras inexactas y
atribuciones inventadas. Figurar entre las fuentes de contraste le confería una
solvencia que no tiene.

**Tratamiento correcto.** El borrador es punto de partida de la investigación;
cada dato que aporte se verifica en fuente publicada y se cita **esa** fuente.
Las discrepancias detectadas se comunican al editor por chat (regla maestra 8).

Sigue prohibida cualquier línea independiente de estado del documento en el post
(«borrador preliminar», «pendiente de revisión del editor» y equivalentes).

### 7) Transferencia de referencias
No trasladar referencias, notas o conexiones de una efeméride a otra por simple similitud temática. Solo deben reutilizarse si son **directamente pertinentes** al nuevo caso.

### 8) Principio de documento limpio

El post publicado se dirige al lector y solo debe contener el **resultado** de la
investigación. El relato del proceso de elaboración pertenece al chat con el editor.

**Nunca deben aparecer en el post**, en ninguna sección:
- menciones a errores, imprecisiones, fechas equivocadas o enlaces rotos
  del borrador preliminar del investigador;
- referencias a URLs que devolvieron 403, 404, bloqueo anti-bot o Cloudflare;
- sustituciones de una fuente por otra motivadas por problemas de acceso;
- rutas obsoletas frente a rutas vigentes de un mismo recurso;
- cualquier alusión al entorno técnico de trabajo, sus limitaciones o su flujo
  de verificación;
- las notas sobre resolución o tratamiento de las imágenes (por ejemplo, «la
  mayor resolución disponible es 1.024 × 580»);
- las líneas de estado del documento («borrador preliminar», «pendiente de
  revisión» y equivalentes);
- las **comprobaciones rutinarias del procedimiento**, que se dan por supuestas
  y no aportan nada al lector. Fórmula expresamente proscrita: «se verificó la
  coherencia entre la fecha del hecho, el título, el nombre del archivo y el
  YAML». Esa verificación es obligatoria, pero pertenece a la lista de control
  interna, nunca al documento publicado.

**Sí deben comunicarse al editor por chat**, con el detalle que resulte útil:
- las discrepancias detectadas entre el borrador y la investigación propia;
- los enlaces del borrador que no funcionan, **una vez agotada la búsqueda de un
  reemplazo equivalente**, para que el editor pueda aportar una fuente accesible;
- las decisiones de sustitución de fuentes o imágenes y su motivo.

**Sí puede permanecer en el post** la divergencia entre **fuentes publicadas y
solventes** cuando su explicitación aporta valor historiográfico al lector: cifras
que no coinciden entre instituciones, husos horarios, denominaciones alternativas.
Esa es la función legítima de la nota aclaratoria y del campo «Discrepancias
resueltas».

**Criterio de discernimiento:** si el dato interesa a quien lee la efeméride, va
al post; si solo interesa a quien la produce, va al chat.

### 9) Cómputo de años transcurridos

Las efemérides se publican **el mismo día y el mismo mes del hito**. La distancia
temporal entre el hecho y su publicación es, por tanto, un número entero exacto de
años, sin fracciones ni redondeos.

**Regla de cálculo:**

```
años transcurridos = año de publicación − año del hito
```

El año de publicación se toma del campo `fecha_publicacion` del borrador aportado
por el editor. Si ese campo no consta, se emplea el año en curso.

**Ejemplo.** Hito del 9 de agosto de 1945, publicado el 9 de agosto de 2026:
2026 − 1945 = **81 años**. Es incorrecto escribir «ochenta años después», aunque
la cifra redonda resulte más cómoda.

**Alcance de la regla.** Afecta a cualquier mención de la distancia temporal en el
cuerpo del post, con independencia de la sección en que aparezca. Son formulaciones
sujetas a verificación:
- «X años después…»;
- «X décadas más tarde…»;
- «un siglo después…»;
- «X años antes de…», cuando el término de comparación es la fecha de publicación;
- toda referencia a un aniversario.

**Criterio de redacción.** Se emplea la **cifra exacta**, escrita con letra cuando
encabeza la frase. Solo cabe una fórmula aproximada («más de ocho décadas») cuando
el texto no compara con la fecha de publicación sino con un tercer hecho histórico
de fecha imprecisa.

**Comprobación obligatoria.** La cifra se verifica al cerrar el documento, junto
con el resto de la lista de control interna. Como toda comprobación rutinaria, no
se menciona en el post.

### 10) Verificación de contenido de las fuentes

Un código de respuesta 200 acredita únicamente que el servidor devuelve una
página. **No acredita que esa página trate del sujeto de la efeméride.** La
comprobación de que un enlace «funciona» es, por tanto, insuficiente: toda URL
debe verificarse por su **contenido**.

**Regla.** Antes de incorporar una URL al post —en `## Referencias Verificadas`,
en un enlace del cuerpo, en el atributo `href` del `<figure>` o como origen de una
imagen descargada— debe leerse la página y confirmarse que el título, el pie
descriptivo y los datos catalográficos corresponden a la persona, la aeronave, el
lugar o el hecho de la efeméride.

**Ámbito de riesgo especial.** La exigencia se extrema en los repositorios
documentales cuyos identificadores son correlativos y cuyas fichas contiguas no
guardan relación temática entre sí: Library of Congress, Imperial War Museums,
National Archives, National Museum of the United States Air Force, NASA Image and
Video Library, archivos fotográficos nacionales y hemerotecas digitalizadas. En
esos sistemas, un identificador equivocado en un dígito devuelve una ficha
perfectamente válida y perfectamente ajena.

**Extremos que deben confirmarse en una ficha de archivo:**
- el **título o leyenda** de la propia ficha, no el del resultado de búsqueda que
  condujo a ella;
- el **identificador digital** y la signatura, que deben coincidir con los del
  recurso de imagen efectivamente descargado;
- la **fecha** de la toma o del documento, contrastada con la cronología del hecho;
- el **estado de derechos**, cuando la imagen vaya a reproducirse.

**Verificación visual.** Cuando la ficha aporte la imagen, esta debe examinarse
antes de darla por buena. Una fotografía de grupo, un retrato o un aparato que no
concuerdan con lo que la efeméride describe invalidan la ficha aunque el
identificador parezca correcto.

**Precedente que motiva la regla.** En la efeméride del nacimiento de Hugo Eckener
se enlazó en el `<figure>` una ficha de la Library of Congress cuya URL respondía
correctamente pero que correspondía a un retrato de Stanley Baldwin y su familia.
El error se detectó en la revisión del editor, no en la del asistente, porque la
comprobación se había limitado al código de respuesta.

**Tratamiento del error.** La sustitución de una ficha equivocada por la correcta
es una incidencia del proceso de elaboración: se comunica al editor por chat y
**no deja rastro en el post**, conforme a la regla maestra 8.

### 11) URL canónica de los enlaces internos

Todo enlace interno a otra efeméride del proyecto se construye con el patrón
canónico de Jekyll:

```
https://efemerides-aviacion.github.io/efemerides/:categoria/:año/:mes/:día/:slug.html
```

Es decir, la fecha del post va **en barras** (`/1897/01/06/`), nunca unida por
guiones (`/1897-01-06/`), que es una ruta inexistente y produce 404. El slug se
toma del nombre de archivo sin el prefijo de fecha. Si el nombre de archivo
termina en guion, el slug publicado **pierde ese guion** (Jekyll elimina los
guiones terminales al slugificar), y el enlace se escribe sin él.

**Comprobación.** Antes de entregar el post, cada enlace interno se verifica
contra este patrón, no contra el nombre del archivo de origen.

**Precedente que motiva la regla.** En agosto de 2026 varios posts se entregaron
con fechas unidas por guiones; el editor hubo de sustituir a mano cada enlace
copiando la URL del navegador.

### 12) Imágenes al tamaño de casa

Las imágenes se entregan al **tamaño de casa**:

| Uso | Dimensiones |
| :--- | :--- |
| `nacimiento` | **800 × 1.000** |
| Resto de categorías | **1.200 × 675** |

**Nombre de archivo.** El de la imagen es el del post, sin `.md`: `AAAA-MM-DD-slug.webp` (o `.jpg` si el editor entrega ese formato). El campo YAML `image:` y el `src` del `<figure>` usan ese mismo nombre.

Si la toma es menor, **se amplía** hasta esas cotas con remuestreo de calidad (Lanczos) y un unsharp ligero, para no entregar una imagen blanda. Ampliar no inventa detalle óptico que no estaba; evita el desenfoque del estirado. Si la toma es mayor, se reduce al estándar. Entrega en WebP (quality 90-92, method 6).

**No se menciona la resolución en el post:** es nota de trabajo y pertenece al chat (regla maestra 8). La advertencia de imagen representativa, cuando proceda, sigue rigiéndose por la sección «Pie de foto: reglas obligatorias».

Queda derogada la fórmula de la v2.9–v2.13 «las imágenes no se amplían / resolución nativa». El 678 que figuraba como alto del encabezado era errata; el alto canónico es **675**.

### 13) Separadores entre bloques

Cada frontera entre bloques de primer nivel del post —`<figure>`,
`highlight-box` del Resumen Ejecutivo, cada sección `##` y toda `note-box`—
lleva **exactamente una** línea divisoria con el degradado de la categoría: ni
ausentes (sección sin separador), ni duplicadas, ni con gradiente ajeno o `<hr>`
plano. La categoría `fundacion` emplea el mismo verde que `nacimiento`
(`#1b5e20, #2e7d32`). Las secciones adicionales legítimas (p. ej. «Principales
figuras») añaden su separador propio. La comprobación es mecanizable: un barrido
por script debe confirmar un separador del color correcto por frontera.

Los barridos de normalización deben detectar **todas las variantes** de la
línea divisoria ajena: orden de colores reverso (`#283593, #1a237e` frente a
`#1a237e, #283593`) y redacción sin espacios (`to right,#1a237e,#283593`); los
patrones de búsqueda se escriben tolerantes a espacios y órdenes. Los posts con
separadores faltantes se completan según sus fronteras de bloque, no solo se
recoloran. Casos del 14 de agosto de 2026: 47 reversos de `evento`, 14 fuera
de categoría y los restos de `1919-02-05` y `1934-12-30`.

Origen: normalización de la categoría `fundacion` del 12 de agosto de 2026, que
corrigió 40 de 41 posts (gradientes índigo, verde claro o azul, `<hr>` planos y
separadores faltantes, hasta posts publicados sin ninguno), completada el 13 de
agosto con el resto del corpus.

### 14) Mínimo de cuatro referencias verificadas

Todo post lleva en `## Referencias Verificadas` **al menos cuatro entradas**, y
al menos **dos** de ellas han de ser primarias o institucionales. El borrador
del editor no computa, porque no se cita (regla maestra 6).

Cada referencia se valida por su **contenido**, conforme a la regla maestra 10:
cuatro enlaces que responden pero no acreditan nada no cumplen esta regla.

Si agotada la investigación no se reúnen cuatro referencias pertinentes, se
aplica el criterio de suspensión de las Instrucciones de Procesamiento y se
informa al editor por chat.

**Cómo contar.** El corpus usa tres formatos de lista en `## Referencias Verificadas`: `<li>`, viñeta `-` y numeración `1.`. Hay que contar los tres. Contar solo `<li>` produce decenas de falsos positivos (detectado el 18 de agosto de 2026 al auditar el § 4.h).

**Origen de la regla.** Los tres posts anteriores al del BAe Hawk se publicaron
con solo dos referencias, un aparato documental insuficiente para sostener el
hecho y para que el lector pueda contrastarlo. Acordada el 16 de agosto de 2026.

### 15) Hechos de más de un día

Cuando el hito se extiende a lo largo de varios días (travesía, récord, misión), la efeméride se fecha y se publica en el día de la **culminación**, no en el del despegue o el inicio. **Excepción:** Apolo 11, que el proyecto conmemora el 20 de julio (alunizaje), no el amerizaje.

**Origen.** Earhart transcontinental: despegue el 24 de agosto de 1932, aterrizaje el 25; la URL y el post son del 25. El 24 responde 404.

---

## Estructura universal del post

```yaml
---
layout: post
title: "[día] de [mes] de [año] | [título preciso de la efeméride]"
date: AAAA-MM-DD
categories: [categoria]
author: Enrique Pomares
pais: [país o combinación pertinente]
operator: [si aplica]
excerpt: "[frase breve, precisa y útil para SEO/listados]"
image: AAAA-MM-DD-nombre-de-imagen.webp
---
```

```html
<figure>
  <img class="post-image" src="{{ site.baseurl }}/assets/img/AAAA-MM-DD-nombre-de-imagen.webp" alt="[descripción breve y precisa de la imagen]">
  <figcaption class="post-caption">[pie de foto con identificación, contexto, fecha y fuente].</figcaption>
</figure>
```

```html
<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, [color1], [color2]);">
```

```html
<!-- ## Resumen Ejecutivo -->
<div class="highlight-box">
<p>[Párrafo 1 del resumen]</p>
<p>[Párrafo 2 del resumen]</p>
</div>
```

Luego, en este orden:
1. `## Datos verificados del evento`
2. `## Contexto Histórico`
   - `### Entorno social`
   - `### Entorno tecnológico`
   - `### Entorno cultural`
3. `## Desarrollo Cronológico`
4. `## Consecuencias e Impacto`
5. `## Legado`
6. `## Referencias Verificadas`
7. `Nota aclaratoria` (solo si procede)
8. `## Metadatos de Control`

---

## Plantilla base por categoría

### A) Nacimiento
Usar cuando el hito principal sea el nacimiento de una figura relevante.

#### Datos verificados sugeridos
- fecha y lugar de nacimiento;
- fallecimiento;
- nacionalidad;
- servicio u organización;
- unidades;
- aeronaves;
- rango;
- logros verificables.

#### Particularidades
- si hay cifras de victorias, condecoraciones o récords controvertidos, explicar la diferencia en nota aclaratoria o sección específica.

---

### B) Evento
Usar cuando el hecho central sea un primer vuelo, récord, misión, presentación, demostración, rescate, etc.

#### Datos verificados sugeridos
- fecha;
- lugar;
- protagonistas;
- aeronave o sistema;
- duración, carga, altitud, velocidad o cifra clave, si aplica;
- resultado inmediato.

#### Particularidades
- si existen precedentes relacionados ya publicados, pueden enlazarse varios, siempre que cada URL aparezca una sola vez.
- si la imagen es solo representativa y no del día exacto, debe decirse en el pie o en la nota.

---

### C) Fundación
Usar cuando la efeméride trate la creación, constitución, activación o inauguración de una entidad, unidad, base o institución.

#### Datos verificados sugeridos
- fecha precisa del acto recordado;
- lugar;
- entidad fundada/inaugurada/activada;
- país o países;
- protagonistas;
- marco institucional;
- función inicial.

#### Particularidades
- si existe tensión entre “fundación”, “activación”, “inauguración” o “constitución legal”, debe explicitarse.
- la categoría puede seguir siendo `fundacion` aunque el título use “inauguración”, si así lo decide la línea editorial.

---

### D) Accidente
Usar cuando el hecho central sea un siniestro aéreo o pérdida operacional.

#### Datos verificados sugeridos
- fecha;
- lugar;
- aeronave;
- operador;
- ruta;
- personas a bordo;
- víctimas;
- causa confirmada o estado de la investigación.

#### Particularidades
- evitar sensacionalismo;
- diferenciar claramente entre causa confirmada, hipótesis e investigación abierta;
- si el avión de la imagen no es el siniestrado sino uno similar, indicarlo en el pie.

---

### E) Seguridad
Usar para secuestros, sabotajes, atentados, intrusiones o incidentes AVSEC.

#### Datos verificados sugeridos
- fecha;
- vuelo o instalación;
- operador;
- responsables conocidos;
- lugar;
- desenlace;
- víctimas si las hubo.

#### Particularidades
- si el caso terminó en accidente, aclarar por qué sigue clasificándose como `seguridad`.

---

### F) Espacial
Usar para lanzamientos, vuelos orbitales, alunizajes, hitos suborbitales o récords aeroespaciales.

#### Datos verificados sugeridos
- fecha;
- misión;
- astronautas o tripulación;
- lanzador;
- lugar de lanzamiento;
- duración;
- altitud, órbitas o perfil de misión;
- recuperación o resultado.

#### Particularidades
- si existe disputa entre distintos umbrales de “espacio”, explicarlo en nota aclaratoria.

---

### G) Supervivencia
Usar cuando la efeméride conmemore un récord o caso histórico de supervivencia aérea.

#### Datos verificados sugeridos
- fecha del hecho o del reconocimiento;
- protagonista;
- accidente original vinculado;
- récord o reconocimiento;
- consecuencias posteriores.

---

## Pie de foto: reglas obligatorias

El pie de foto debe responder, cuando sea posible, a esta lógica:
1. qué muestra la imagen;
2. cuándo fue tomada;
3. qué relación tiene con el hecho;
4. de dónde procede.

### Modelos válidos

**Imagen exacta del hecho**
```html
<figcaption class="post-caption">El [objeto/protagonista] durante [evento], [fecha]. Fuente: <a href="https://ejemplo.com" style="color: #315fea; text-decoration: none;">[medio o archivo]</a>.</figcaption>
```

**Imagen representativa, no exacta**
```html
<figcaption class="post-caption">[Aeronave o escena] similar a la involucrada en el hecho recordado. La fotografía fue tomada en [lugar], [fecha]. Fuente: <a href="https://ejemplo.com" style="color: #315fea; text-decoration: none;">[medio o archivo]</a>.</figcaption>
```

**Imagen anterior al hecho**
```html
<figcaption class="post-caption">Imagen anterior al hecho recordado: [aeronave o escena] en [lugar], [fecha], [periodo] antes de [el suceso]. Fuente: <a href="https://ejemplo.com" style="color: #315fea; text-decoration: none;">[medio o archivo]</a>.</figcaption>
```

### Criterio específico para la categoría `accidente`

En las efemérides de siniestros, la imagen preferente es la de **la aeronave intacta
antes del suceso**, no la de sus restos.

Este criterio deriva de la política de tono del manual de estilo, que exige
tratamiento empático en accidentes y tragedias y prohíbe el sensacionalismo. La
fotografía de restos calcinados, fuselajes destrozados o cuerpos rescatados
contradice esa línea, con independencia de que el siniestro haya causado víctimas
o no.

**Orden de preferencia:**
1. la aeronave siniestrada, intacta, en fecha anterior al suceso;
2. una aeronave del mismo tipo y operador, declarada como representativa;
3. el lugar del hecho, un monumento conmemorativo o un retrato de las víctimas;
4. la imagen del siniestro, solo cuando posea valor documental insustituible y no
   resulte gráfica ni morbosa.

**Obligaciones de transparencia:**
- el pie debe declarar siempre que la imagen es anterior al hecho;
- cuando la elección responda a este criterio, debe consignarse en la nota
  aclaratoria en términos históricos o documentales, sin describir el proceso
  editorial interno;
- nunca debe presentarse una imagen anterior como si fuera del momento del
  siniestro.

**Ejemplo aplicado:** en la efeméride del incendio del Zeppelin LZ 4 en Echterdingen
(5 de agosto de 1908) se descartó la fotografía del armazón calcinado, disponible en
dominio público, y se empleó una del dirigible en maniobra de despegue semanas antes
de su destrucción.

---

## Nota aclaratoria: modelo obligatorio

```html
<div class="note-box">
  <p><strong>Nota aclaratoria:</strong> [Texto de la aclaración].</p>
</div>
```

Usarla cuando haya:
- discrepancias de fecha, cifras, lugares, nombres o matrículas **entre fuentes publicadas**;
- cambio deliberado de enfoque editorial;
- distinción necesaria entre “reclamaciones” y “confirmaciones”;
- imágenes no exactas del hecho;
- diferencia entre planificación y ejecución real;
- cualquier matiz imprescindible para no inducir a error.

**No usarla nunca para** (regla maestra 8):
- señalar errores del borrador preliminar del investigador;
- informar de enlaces caídos, bloqueos 403/404 o sustituciones de fuentes;
- describir el proceso de verificación o las limitaciones del entorno.

La nota aclaratoria explica **al lector** por qué el texto dice lo que dice; no
justifica ante el editor cómo se llegó a redactarlo.

---

## Metadatos de Control: plantilla normativa

```markdown
## Metadatos de Control
- **Timestamp de verificación:** AAAA-MM-DD HH:MM:SS ZONA  
- **Fuentes primarias/institucionales consultadas:** [lista breve]  
- **Fuentes secundarias de contraste:** [lista breve; **nunca** el borrador preliminar del editor]  
- **Discrepancias resueltas:** [resumen breve, **exclusivamente** de divergencias entre fuentes publicadas: cifras, fechas, husos, denominaciones. Nunca errores del borrador, enlaces caídos, incidencias del entorno ni comprobaciones rutinarias del flujo de trabajo. Si no hubo divergencias entre fuentes, se omite el campo]  
- **Nivel de confianza:** Alto / Medio / Bajo  
- **Cláusula final:** “Cuando una afirmación relevante no pudo ser confirmada, se omitió o se marcó como [NO CONFIRMADO]”.
```

---

---

## Reglas visuales recomendadas

### Divisores de sección: tabla normativa

Todo post debe llevar un divisor `<hr>` antes de cada sección principal, desde
`## Datos verificados del evento` hasta `## Metadatos de Control`, con el degradado
que corresponda a su categoría.

**Formato obligatorio:**

```html
<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, COLOR1, COLOR2);">
```

**Tabla de degradados por categoría:**

| Categoría | Degradado | Descripción |
| :--- | :--- | :--- |
| `nacimiento` | `#1b5e20, #2e7d32` | Verde oscuro |
| `fundacion` | `#1b5e20, #2e7d32` | Verde oscuro |
| `evento` | `#1565c0, #42a5f5` | Azul |
| `accidente` | `#b71c1c, #c62828` | Rojo |
| `espacial` | `#0d47a1, #29b6f6` | Azul oscuro y celeste |
| `seguridad` | `#0d47a1, #546e7a` | Azul grisáceo |
| `supervivencia` | `#2e7d32, #ef6c00` | Verde y naranja |
| `conmemoracion` | `#2e7d32, #66bb6a, #fbc02d, #f9a825` | Verde y dorado |
| `[espacial, accidente]` | `#0b2545, #134074, #e74c3c, #c0392b` | Azul oscuro y rojo |

**Notas de aplicación:**
- **El separador previo a la nota aclaratoria cuenta como divisor de sección.**
  La nota aclaratoria vive dentro de un `<div class="note-box">` y no bajo un
  encabezado `##`, pero es un bloque de primer nivel a todos los efectos: la
  frontera que la separa de `## Referencias Verificadas` exige su divisor, con el
  degradado de la categoría como cualquier otro. **Nunca un `<hr>` desnudo.**
- Las categorías `nacimiento` y `fundacion` comparten degradado de forma
  deliberada: ambas conmemoran el origen de algo.
- Las categorías `conmemoracion` y `[espacial, accidente]` emplean degradados de
  cuatro paradas.
- Los códigos de esta tabla son normativos. No deben deducirse a partir del nombre
  del color ni sustituirse por tonos aproximados.

### Consistencia visual
- todos los divisores de un mismo post deben usar idéntico degradado;
- no mezclar estilos de divisores dentro de un mismo post;
- si el editor ya ajustó el divisor o la imagen en el repositorio, no revertirlo sin
  instrucción expresa.

---

## Plantillas de ejemplo por categoría

Las nueve plantillas siguientes cubren todas las categorías reconocidas. Las siete
primeras proceden de la v1.8 y se conservan íntegras. Las dos últimas —`[espacial, accidente]` y `conmemoracion`— se han elaborado en la v2.3 a partir de
efemérides reales ya publicadas en el repositorio. Sirven como referencia operativa
completa: estructura, divisores, formato de secciones y estilo de metadatos.

## 🧑‍✈️ Plantilla: Ejemplo de nacimiento

---
layout: post
title: "27 de marzo de 1894 | Nacimiento de René Paul Fonck, as de ases en la Primera Guerra Mundial"
date: 1894-03-27
categories: [nacimiento]
author: Enrique Pomares
pais: Francia
operator: Aéronautique Militaire (Francia)
excerpt: "El 27 de marzo de 1894 nació René Paul Fonck, el as de ases de la aviación aliada durante la Primera Guerra Mundial, con 75 victorias confirmadas, siendo el piloto de la Entente con más derribos y el segundo en la historia del conflicto solo detrás de Manfred von Richthofen."
image: 1894-03-27-rene-paul-fonck-as-primera-guerra-mundial.webp

---

<figure>
  <img class="post-image" src="{{ site.baseurl }}/assets/img/1894-03-27-rene-paul-fonck-as-primera-guerra-mundial.webp" alt="René Paul Fonck, as francés de la Primera Guerra Mundial">
  <figcaption class="post-caption">René Paul Fonck, as de ases de la aviación francesa con 75 victorias confirmadas, ca. 1918. Retrato autografiado original. Fuente: <a href="https://lesautographesdusiecle.com/aviation/12824-fonck-rene-1894-1953.html">Les Autographes du Siecle</a>.</figcaption>
</figure>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #1b5e20, #2e7d32);">

<!-- ## Resumen Ejecutivo -->
<div class="highlight-box">
<p>El 27 de marzo de 1894 nació René Paul Fonck en Saulcy-sur-Meurthe, Francia. Durante la Primera Guerra Mundial se convirtió en el as aliado con más victorias: 75 confirmadas (72 en solitario), superando a todos los pilotos de la Triple Entente. Solo superado por el alemán Manfred von Richthofen (80), Fonck reclamó hasta 142 derribos, destacando por su precisión y economía de munición en escuadrillas como Les Cigognes. Tras la guerra, fue inspector aéreo y falleció en 1953 sin haber resultado herido en combate.</p>
</div>
<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #1b5e20, #2e7d32);">

## Datos verificados del evento
- **Fecha de nacimiento:** 27 de marzo de 1894
- **Lugar:** Saulcy-sur-Meurthe, Francia
- **Fallecimiento:** 18 de junio de 1953 (59 años), París, Francia
- **Servicio:** Aéronautique Militaire (1914–1918; 1937–1939)
- **Unidades:** Escadrille C.47, Escadrille SPA.103 «Les Cigognes»
- **Aeronaves:** Caudron G.III, SPAD VII, SPAD XII (cañón de 37 mm), SPAD XIII
- **Rango:** Teniente (final de guerra), posteriormente Teniente Coronel (1937)
- **Victorias confirmadas:** 75 (72 en solitario, 3 compartidas)
- **Condecoraciones:** Gran Oficial de la Legión de Honor, Cruz de Guerra 1914-1918 (26 palmas), Medalla Militar, Cruz de Guerra belga, entre otras.

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #1b5e20, #2e7d32);">

## Contexto Histórico

René Fonck nació en una Francia que se preparaba para un nuevo siglo de cambios tecnológicos y tensiones geopolíticas. Su juventud coincidió con la carrera por la conquista del aire, tras los pioneros como los hermanos Wright, Blériot o los hermanos Voisin. Al estallar la Primera Guerra Mundial (1914-1918), la aviación militar aún estaba en su infancia, pero evolucionó rápidamente hacia un arma decisiva.

### Entorno social
Francia a finales del siglo XIX era una república consolidada, pero marcada por el revanchismo tras la derrota en la guerra franco-prusiana (1870-1871). Las generaciones que crecieron antes de 1914 lo hicieron con la idea de que una nueva guerra con Alemania era inevitable. Fonck, hijo de un maestro de obras, pertenecía a una clase media que veía en el ejército y la técnica una vía de ascenso social.

### Entorno tecnológico
La aviación era entonces un campo de experimentación. En 1894, los vuelos controlados todavía eran sueños de visionarios. En apenas dos décadas, se pasó del globo aerostático al avión de caza con ametralladoras sincronizadas. Fonck vivió esta transformación desde la trinchera hasta los mandos de los más avanzados SPAD, capaces de superar los 200 km/h.

### Entorno cultural
La figura del «as» —piloto con cinco o más victorias— nació durante la Gran Guerra para convertir en héroes individuales una contienda anónima y mecanizada. Fonck representó el ideal del piloto técnico, metódico, que maximizaba la eficacia con el mínimo riesgo, en contraste con la imagen romántica del caballero del aire como Guynemer.

## Desarrollo Cronológico

- **27 de marzo de 1894:** Nace René Paul Fonck en Saulcy-sur-Meurthe (departamento de Meurthe-et-Moselle).
- **1914:** Al iniciarse la guerra, es movilizado como ingeniero de combate en unidades de zapadores en las trincheras de Lorena.
- **1915:** Solicita su traslado a aviación. Se forma en la escuela de St. Cyr y obtiene el brevet de piloto militar.
- **1915-1916:** Sirve en la Escadrille C.47 con aviones Caudron G.III, realizando misiones de reconocimiento y artillería. Consigue sus dos primeras victorias compartidas en 1916.
- **Abril de 1917:** Tras un breve paso por la Escadrille N.124 (Lafayette), se incorpora a la prestigiosa Escadrille SPA.103 «Les Cigognes» (Las Cigüeñas), equipada con SPAD VII y XIII. Allí inicia una racha de victorias que lo llevará a ser el máximo as aliado.
- **1917:** Acumula 19 victorias en su primer año con Les Cigognes.
- **1918:** Alcanza su pico operativo. El 9 de mayo derriba seis aviones alemanes en un día. El 15 de septiembre suma dos victorias más en un solo combate. Termina la guerra con 75 victorias confirmadas.
- **1919:** Encabeza el desfile aéreo de la Victoria en París a los mandos de un SPAD.
- **1926:** Intenta sin éxito el primer vuelo sin escalas entre Nueva York y París a bordo de un Sikorsky S-35, accidentándose en el despegue.
- **1937-1939:** Es ascendido a teniente coronel y ejerce como inspector de caza en la Armée de l'Air.
- **Segunda Guerra Mundial:** Colabora con el régimen de Vichy, lo que empaña su legado en la posguerra.
- **18 de junio de 1953:** Fallece en París.

### Sistema de acreditación de victorias

Durante la Primera Guerra Mundial, las fuerzas aliadas establecieron un riguroso sistema para homologar derribos. Francia aplicaba el más estricto de todos: para que una victoria fuera «confirmada», debía cumplir al menos tres condiciones:

1. **Testigos oculares:** Otros pilotos o unidades terrestres debían corroborar el derribo.
2. **Restos del aparato enemigo:** La aeronave debía caer en territorio aliado o localizarse sus restos.
3. **Informes oficiales:** Los partes de guerra debían coincidir con la verificación posterior.

Este sistema, implementado para evitar exageraciones, hacía que muchos derribos reales —sobre todo en territorio enemigo— quedaran sin confirmar. Fonck reclamó personalmente **142 victorias**, de las cuales solo 75 fueron homologadas oficialmente. Su elevada cifra de reclamaciones (muchas sin testigos o con restos no recuperados) ha generado controversia histórica, aunque su condición de máximo as aliado es indiscutida.

## Consecuencias e Impacto

- **Legado militar:** Fonck estableció un récord de eficacia que ningún otro piloto aliado superó. Sus tácticas —ataque desde altura, disparos a corta distancia, consumo mínimo de munición— fueron estudiadas como modelo de precisión.
- **Héroe nacional:** Fue celebrado como héroe en Francia, junto a Guynemer, Nungesser y otros ases de Les Cigognes. Portó la bandera francesa en el desfile de la Victoria.
- **Controversia y olvido:** Su personalidad arrogante y sus colaboraciones con el régimen de Vichy durante la Segunda Guerra Mundial hicieron que su figura fuera menos recordada que la de otros héroes franceses, como Georges Guynemer, muerto en combate en 1917.
- **Innovación técnica:** Fonck voló intensivamente el SPAD XII, una variante equipada con cañón de 37 mm que disparaba a través del eje de la hélice, un arma letal pero de difícil manejo que él dominó con maestría.

## Legado

René Fonck sigue siendo el «as de ases» de la aviación aliada en la Primera Guerra Mundial. Sus 75 victorias confirmadas lo sitúan en la segunda posición histórica tras Manfred von Richthofen (80). A pesar de las controversias sobre sus reclamaciones personales y su conducta en la Segunda Guerra Mundial, su récord operativo permanece imbatido entre los pilotos franceses y de la Entente. Su nombre está inscrito en el Arco del Triunfo en París, y su figura representa la transición entre el pionerismo romántico y la caza militar moderna.

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #1b5e20, #2e7d32);">

## Referencias Verificadas
<div class="references">
  <ul>
    <li><a href="https://es.wikipedia.org/wiki/Ren%C3%A9_Fonck">Wikipedia (ES) – René Fonck</a></li>
    <li><a href="https://en.wikipedia.org/wiki/Ren%C3%A9_Fonck">Wikipedia (EN) – René Fonck</a></li>
    <li><a href="https://prensaohf.com/2021/09/14/rene-fonck-1894-1953-el-as-de-ases-de-los-aiados-en-la-grande-guerre/">Prensa OHF – René Fonck (1894-1953) – El "As de Ases" de los Aliados</a></li>
    <li><a href="https://www.fuerzasaereas.es/2012/12/rene-fonck-fue-el-piloto-de-caza-de-la.html">Fuerzas Aéreas – René Fonck, el As olvidado</a></li>
    <li><a href="https://pantheon.world/profile/person/Ren%C3%A9_Fonck">Pantheon – René Fonck Biography</a></li>
    <li><a href="https://www.firstworldwar.com/bio/fonck.htm">FirstWorldWar.com – Who's Who - Rene Fonck</a></li>
    <li><a href="https://www.earlyaviators.com/efonck.htm">EarlyAviators – René Paul Fonck</a></li>
    <li><a href="https://pt.wikipedia.org/wiki/Ren%C3%A9_Paul_Fonck">Wikipedia (PT) – René Paul Fonck</a></li>
  </ul>
</div>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #1b5e20, #2e7d32);">

<div class="note-box">
<p><strong>Nota aclaratoria:</strong> Esta sección se generará únicamente si existe alguna discrepancia, controversia o detalle que requiera explicación adicional en la efeméride. Si no se necesita se omitirá en la versión final.</p>
</div>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #1b5e20, #2e7d32);">

## Metadatos de Control
- **Timestamp de verificación:** 2026-03-25 10:30:00 UTC  
- **Fuentes primarias/institucionales consultadas:** Wikipedia (ES/EN/PT), Prensa OHF, Fuerzas Aéreas, FirstWorldWar.com, EarlyAviators, Pantheon  
- **Discrepancias resueltas:** Se ha aclarado la diferencia entre las 75 victorias confirmadas oficialmente y las 142 reclamadas por Fonck, explicando el riguroso sistema francés de homologación.  
- **Nivel de confianza:** Alto  
- **Cláusula final:** “Cuando una afirmación relevante no pudo ser confirmada, se omitió o se marcó como [NO CONFIRMADO].”

___


## 🛑 Plantilla: Ejemplo de accidente


---
layout: post
title: "27 de marzo de 1977 | Colisión de dos Boeing 747 en el aeropuerto 'Los Rodeos'"
date: 1977-03-27
categories: [accidente]
author: Enrique Pomares
pais: España
operator: KLM / Pan Am
excerpt: "El 27 de marzo de 1977, dos Boeing 747 chocaron en la pista del aeropuerto de Los Rodeos (Tenerife) en medio de una densa niebla. Con 583 víctimas mortales, es el accidente con más fallecidos en la historia de la aviación civil."
image: 1977-03-27-colision-dos-b747-los-rodeos.webp

---

<figure>
  <img class="post-image" src="{{ site.baseurl }}/assets/img/1977-03-27-colision-dos-b747-los-rodeos.webp" alt="Representación 3D de la colisión de los Boeing 747 en Tenerife">
  <figcaption class="post-caption">Representación en 3D de la colisión entre el Boeing 747‑206B de KLM (PH‑BUF, azul) y el Boeing 747‑121 de Pan Am (N736PA, gris) en la pista del Aeropuerto Los Rodeos (Tenerife), 27 de marzo de 1977. Fuente: <a href="https://www.xataka.com/transporte/1977-dos-boeing-747-colisionaron-aeropuerto-espana-fue-peor-accidente-aereo-historia">Xataka</a>.</figcaption>
</figure>
<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #b71c1c, #c62828);">

<!-- ## Resumen Ejecutivo -->
<div class="highlight-box">
<p>El 27 de marzo de 1977, un Boeing 747 de KLM (vuelo 4805) despegó sin autorización en niebla densa en el aeropuerto de Los Rodeos (Tenerife), colisionando con un Boeing 747 de Pan Am (vuelo 1736) que taxiaba en la misma pista. Murieron 583 personas de 644 a bordo; solo 61 sobrevivieron del Pan Am. Factores clave: malentendidos radiales, visibilidad nula y saturación por desvíos de Gran Canaria por una bomba. Cambió protocolos de aviación globales.</p>
</div>
<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #b71c1c, #c62828);">

## Datos verificados del evento
- **Fecha:** 27 de marzo de 1977
- **Lugar:** Aeropuerto de Los Rodeos (hoy Aeropuerto Tenerife Norte), Tenerife, Islas Canarias, España
- **Aeronaves involucradas:** Boeing 747‑206B (KLM, PH‑BUF, vuelo KL4805); Boeing 747‑121 (Pan Am, N736PA, vuelo PA1736)
- **Víctimas:** 583 fallecidos (248 de KLM, 335 de Pan Am); 61 sobrevivientes (todos del Pan Am)
- **Causa principal:** El capitán de KLM inició el despegue sin autorización clara mientras el Pan Am aún rodaba por la misma pista, con visibilidad reducida por niebla espesa.
- **Impacto inmediato:** Mayor desastre aéreo de la historia civil; redefinió la seguridad operacional y las comunicaciones en cabina.

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #b71c1c, #c62828);">

## Contexto Histórico

A finales de la década de 1970, la aviación comercial crecía exponencialmente. El Boeing 747 («Jumbo») era el icono de la era, capaz de transportar más de 350 pasajeros en vuelos transoceánicos. La seguridad había mejorado, pero la comunicación entre cabina y control de tierra seguía basándose en fraseología imprecisa y una jerarquía rígida que podía inhibir las correcciones del copiloto o el ingeniero de vuelo.

### Entorno social
El accidente ocurrió en pleno auge del turismo europeo en Canarias. La saturación del pequeño aeropuerto de Los Rodeos –diseñado para aviones de tamaño medio– era habitual, pero aquel día se agravó por un atentado frustrado.

### Entorno tecnológico
Los Rodeos carecía de radar de superficie y sus calles de rodaje eran insuficientes para dos 747. Los aviones tenían que desplazarse por la única pista (12/30), lo que forzaba maniobras de rodaje inusuales. Además, las comunicaciones se realizaban por radio en frecuencias con estática y acentos distintos (holandés, inglés americano, español).

### Entorno cultural
La cultura de cabina de la época daba al capitán una autoridad casi incuestionable. La tripulación de KLM mostraba una jerarquía vertical; el copiloto y el ingeniero de vuelo expresaron dudas, pero no lograron detener la maniobra.

## Desarrollo Cronológico

- **13:15 (hora local):** Una bomba explota en la terminal del aeropuerto de Gran Canaria (Las Palmas). Se cierran las operaciones y varios vuelos son desviados a Los Rodeos.
- **13:30–15:00:** Los Boeing 747 de KLM y Pan Am aterrizan en Los Rodeos. El aeropuerto se satura: los aviones se aparcan en plataformas y calles de rodaje, bloqueando la única pista.
- **15:00–16:30:** El aeropuerto de Gran Canaria reabre. Los aviones desviados comienzan a repostar para continuar. KLM reposta 35 minutos, añadiendo 45 toneladas de combustible para el vuelo a Ámsterdam, lo que retrasa su salida y hace más violenta la posterior explosión.
- **16:45:** Ambos 747 reciben autorización para rodar por la pista con rumbo opuesto (KLM hacia el oeste, Pan Am hacia el este) y luego salir por calle de rodaje C‑3. Debido a la niebla, la visibilidad cae a menos de 100 metros.
- **17:03:** El controlador autoriza al KLM a tomar posiciones de despegue y le informa de que Pan Am aún no ha abandonado la pista. El capitán de KLM, Jacob Veldhuyzen van Zanten, inicia la carrera de despegue sin esperar la autorización explícita.
- **17:06:12:** El KLM alcanza V1 (velocidad de decisión). Segundos después, el controlador y la tripulación de Pan Am escuchan «OK» y luego «takeoff» (la frase fue malinterpretada). El copiloto de KLM dice «¿despegar?» y el capitán responde afirmativamente. El controlador, que había dicho «OK, está bien, espere para el despegue, yo le llamo», no fue escuchado por la cabina del KLM debido a interferencias.
- **17:06:32:** El 747 de KLM, ya en rotación, impacta a 140 km/h contra el lado derecho del Pan Am, que aún rodaba por la pista. El ala izquierda del KLM arranca la sección superior del Pan Am y el fuselaje del holandés cae 150 metros más allá en llamas.
- **17:06–17:30:** Comienzan los rescates. Sólo sobreviven 61 pasajeros de la sección delantera del Pan Am; todos a bordo del KLM mueren (248 personas).

## Consecuencias e Impacto

- **Reforma de la comunicación aeronáutica:** Se estandariza la fraseología en inglés. Queda prohibido decir *takeoff* en comunicaciones que no sean una autorización expresa de despegue.
- **Crew Resource Management (CRM):** Se impulsa la formación que promueve la comunicación asertiva en cabina y la toma de decisiones compartida, para que subordinados puedan corregir al capitán sin temor.
- **Seguridad en aeropuertos:** Se exige radar de superficie en aeropuertos con operaciones de grandes aeronaves y mejoran las señales de las calles de rodaje.
- **Investigación y responsabilidades:** La comisión española concluyó que la causa inmediata fue el despegue prematuro del capitán de KLM, aunque señaló factores contribuyentes: la congestión, la niebla y las transmisiones simultáneas que generaron confusión.

## Legado

El desastre de Tenerife se estudia en todas las escuelas de aviación como caso paradigmático de fallo en comunicación, jerarquía y gestión de recursos. Marcó un antes y después en la seguridad operacional. En Los Rodeos (hoy Aeropuerto Tenerife Norte) se instaló radar de superficie y se construyeron nuevas calles de rodaje. Existen memoriales en Tenerife, Ámsterdam y California, y el accidente ha sido documentado en series como *Segundos Catastróficos* (*Seconds from Disaster*). Cada 27 de marzo se recuerda a las 583 víctimas.

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #b71c1c, #c62828);">

## Referencias Verificadas
<div class="references">
  <ul>
    <li><a href="https://www.xataka.com/transporte/1977-dos-boeing-747-colisionaron-aeropuerto-espana-fue-peor-accidente-aereo-historia">Xataka – 1977: dos Boeing 747 colisionaron en el aeropuerto Los Rodeos</a></li>
    <li><a href="https://skybrary.aero/accidents-and-incidents/b742-b741-tenerife-canary-islands-spain-1977">SKYbrary – B742 / B741, Tenerife Canary Islands Spain, 1977</a></li>
    <li><a href="https://www.rtve.es/noticias/20170327/tragedia-rodeos-40-anos-del-mayor-accidente-historia-aviacion-civil/1511407.shtml">RTVE – La tragedia de Los Rodeos: 40 años del mayor accidente</a></li>
    <li><a href="https://simpleflying.com/tenerife-airport-disaster/">Simple Flying – The Story Of The Tenerife Airport Disaster</a></li>
    <li><a href="https://guanches.org/Accidente_de_Los_Rodeos">Guanches.org – Accidente de Los Rodeos</a></li>
    <li><a href="https://es.wikipedia.org/wiki/Accidente_de_avi%C3%B3n_en_Tenerife_de_1977">Wikipedia (ES) – Accidente de avión en Tenerife de 1977</a></li>
    <li><a href="https://es.wikipedia.org/wiki/Desastre_a%C3%A9reo_de_Tenerife">Wikipedia (ES) – Desastre aéreo de Tenerife</a></li>
  </ul>
</div>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #b71c1c, #c62828);">

<div class="note-box">
<p><strong>Nota aclaratoria:</strong> Esta sección se generará únicamente si existe alguna discrepancia, controversia o detalle que requiera explicación adicional en la efeméride. Si no se necesita se omitirá en la versión final.</p>
</div>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #b71c1c, #c62828);">

## Metadatos de Control
- **Timestamp de verificación:** 2026-03-25 15:00:00 UTC  
- **Fuentes primarias/institucionales consultadas:** Xataka, SKYbrary, RTVE, Simple Flying, Guanches.org, Wikipedia  
- **Discrepancias resueltas:** Algunas fuentes mencionan 583 fallecidos y 61 supervivientes (total 644 personas a bordo); otras cifran en 583/61 coincidentes. Se ha utilizado la cifra oficial del informe español.  
- **Nivel de confianza:** Alto  
- **Cláusula final:** “Cuando una afirmación relevante no pudo ser confirmada, se omitió o se marcó como [NO CONFIRMADO].”

___


## ✈️ Plantilla: Ejemplo de evento

---
layout: post
title: "25 de marzo de 2022 | Primer vuelo del Airbus A380 con 100% SAF"
date: 2022-03-25
categories: [evento]
author: Enrique Pomares
pais: Francia
operator: Airbus
excerpt: "El 25 de marzo de 2022, un Airbus A380 de pruebas (MSN1) realizó el primer vuelo con uno de sus motores alimentado al 100% con combustible de aviación sostenible (SAF), un hito clave en la descarbonización de la aviación comercial."
image: 2022-03-25-primer-vuelo-airbus-380-con-saf.webp

---

<figure>
  <img class="post-image" src="{{ site.baseurl }}/assets/img/2022-03-25-primer-vuelo-airbus-380-con-saf.webp" alt="Airbus A380 con combustible SAF">
  <figcaption class="post-caption">Airbus A380 MSN1 durante su primer vuelo con motor Rolls‑Royce Trent 900 alimentado 100% SAF, 25 marzo 2022, Toulouse‑Blagnac. © Airbus / Airbus Communications.</figcaption>
</figure>
<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #1565c0, #42a5f5);">

<!-- ## Resumen Ejecutivo -->
<div class="highlight-box">
<p>El 25 de marzo de 2022, Airbus llevó a cabo el primer vuelo de un A380 con uno de sus motores funcionando exclusivamente con combustible de aviación sostenible (SAF). La aeronave de pruebas MSN1 despegó del aeropuerto de Toulouse‑Blagnac a las 08:43 horas y completó un vuelo de aproximadamente tres horas. Durante el ensayo, el motor Rolls‑Royce Trent 900 utilizó 27 toneladas de biocombustible no mezclado, mientras los otros tres motores operaron con queroseno convencional. Este hito forma parte de la estrategia de Airbus para certificar el uso de hasta 100% SAF en vuelos comerciales hacia 2030.</p>
</div>
<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #1565c0, #42a5f5);">

## Datos verificados del evento
- **Fecha:** 25 de marzo de 2022
- **Lugar:** Aeropuerto de Toulouse‑Blagnac (TLS), Francia
- **Protagonistas:** Airbus; Rolls‑Royce; Neste (proveedor de SAF)
- **Aeronave/empresa involucrada:** Airbus A380 MSN1 (número de serie 001), equipado con cuatro motores Rolls‑Royce Trent 900
- **Resultado inmediato:** Primer vuelo de un A380 con un motor alimentado 100% SAF, demostrando la viabilidad técnica del combustible sostenible no mezclado en el avión comercial más grande del mundo.

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #1565c0, #42a5f5);">

## Contexto Histórico

La aviación comercial es responsable de aproximadamente el 2,5% de las emisiones globales de CO₂. La industria se ha comprometido a alcanzar la neutralidad de carbono para 2050, y el combustible de aviación sostenible (SAF) es considerado la palanca tecnológica más inmediata para reducir la huella ambiental, ya que puede llegar a disminuir las emisiones hasta un 80% en comparación con el queroseno fósil.

### Entorno social
Tras la crisis provocada por la pandemia de COVID-19, la aviación comenzó a recuperarse con una mayor conciencia ambiental. Las aerolíneas, los fabricantes y los reguladores intensificaron los esfuerzos para demostrar que el vuelo sostenible es posible. El A380, a menudo criticado por su alta emisión por asiento, se convirtió en un símbolo de esta transformación.

### Entorno tecnológico
Hasta entonces, todos los aviones comerciales estaban certificados para volar con mezclas de hasta 50% SAF y 50% queroseno convencional. El salto al 100% SAF requería pruebas exhaustivas en tierra y vuelo para verificar la compatibilidad de materiales, sistemas de combustible y comportamiento del motor. Airbus ya había realizado pruebas similares en un A350 (octubre de 2021) y un A319neo (noviembre de 2021), extendiendo ahora la experiencia al A380.

### Entorno cultural
El vuelo del A380 con 100% SAF fue presentado como un hito mediático por Airbus y sus socios, reforzando el compromiso de la industria con los objetivos del Acuerdo de París. El evento contó con amplia cobertura en medios especializados y generalistas, destacando la colaboración entre fabricantes, proveedores de combustible y aerolíneas.

## Desarrollo Cronológico

- **2020:** Airbus anuncia su hoja de ruta para introducir el primer avión de cero emisiones en 2035 y acelera las pruebas con SAF.
- **Octubre de 2021:** Un Airbus A350 realiza el primer vuelo con 100% SAF en un motor.
- **Noviembre de 2021:** Un Airbus A319neo repite la hazaña con el mismo combustible.
- **25 de marzo de 2022, 08:43:** El A380 de pruebas MSN1 despega de Toulouse‑Blagnac. Durante el vuelo de tres horas, el motor número 1 (el más exterior del ala izquierda) funciona exclusivamente con 27 toneladas de SAF suministrado por Neste, mientras los otros tres motores utilizan queroseno Jet A‑1.
- **Durante el vuelo:** Se realizan pruebas de comportamiento del motor en diferentes regímenes, transiciones, respuesta de los sistemas de combustible y mediciones de emisiones.
- **Post‑vuelo:** El ensayo se considera un éxito y abre la puerta a futuras certificaciones para vuelos comerciales con 100% SAF.
- **2023 en adelante:** Airbus continúa las pruebas con el A380 y otros modelos, colaborando con aerolíneas como Emirates para demostraciones similares.

## Consecuencias e Impacto

- **Avance en la certificación:** Los datos recogidos contribuyen directamente al trabajo de la Organización de Aviación Civil Internacional (OACI) y de las autoridades aeronáuticas (EASA, FAA) para permitir el uso de 100% SAF en toda la flota.
- **Demostración de escalabilidad:** Al utilizar el A380, el avión comercial más grande, se demostró que incluso los motores de mayor tamaño pueden operar con biocombustible puro.
- **Impulso a la producción de SAF:** El éxito de estas pruebas anima a los gobiernos y a la industria a aumentar la producción de combustible sostenible, cuya oferta sigue siendo limitada y costosa.
- **Legado para el A380:** Aunque el A380 ya había dejado de producirse (la última unidad se entregó en 2021), este vuelo demostró que los aviones en servicio pueden adaptarse a combustibles más limpios, prolongando su vida operativa con menor impacto ambiental.

## Legado

El vuelo del A380 con 100% SAF se inscribe en una serie de hitos que están transformando la aviación comercial hacia una mayor sostenibilidad. Junto con las pruebas del A350 y A319neo, este evento confirma que la tecnología está madura para operar con combustibles no fósiles. A futuro, se espera que la certificación permita vuelos regulares con 100% SAF en toda la flota mundial, contribuyendo significativamente a la reducción de emisiones del sector.

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #1565c0, #42a5f5);">

## Referencias Verificadas
<div class="references">
  <ul>
    <li><a href="https://www.airbus.com/en/newsroom/press-releases/2022-03-first-a380-powered-by-100-sustainable-aviation-fuel-takes-to-the">Airbus – First A380 powered by 100% Sustainable Aviation Fuel takes to the skies</a></li>
    <li><a href="https://www.aviacionline.com/el-airbus-a380-realizo-su-primer-vuelo-con-100-de-combustible-sostenible">AviaciónLine – El Airbus A380 realizó su primer vuelo con 100% de combustible sostenible</a></li>
    <li><a href="https://www.velatia.com/es/blog/historico-despegue-de-un-airbus-380-con-combustible-saf-100-sostenible/">Velatia (ES) – Histórico despegue de un Airbus A380 con combustible SAF 100% sostenible</a></li>
    <li><a href="https://www.neste.com/news/neste-enables-emirates-to-operate-world-s-first-airbus-a380-demonstration-flight-with-one-engine-powered-with-100-saf/">Neste – Neste enables Emirates to operate world’s first Airbus A380 demonstration flight with one engine powered with 100% SAF</a></li>
    <li><a href="https://www.airnavradar.com/blog/first-airbus-a380-powered-by-100-sustainable-aviation-fuel-takes-off">AirNavRadar – First Airbus A380 powered by 100% Sustainable Aviation Fuel takes off</a></li>
    <li><a href="https://www.thisisaerospace.com/articles/airbus-a380-100-saf-test/">ThisIsAerospace – Airbus A380 100% SAF test overview</a></li>
    <li><a href="https://skiesmag.com/airbus-a380-100-saf-test-flight/">Skies Mag – First A380 powered by 100% SAF takes to the skies</a></li>
  </ul>
</div>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #1565c0, #42a5f5);">

<div class="note-box">
<p><strong>Nota aclaratoria:</strong> Esta sección se generará únicamente si existe alguna discrepancia, controversia o detalle que requiera explicación adicional en la efeméride. Si no se necesita se omitirá en la versión final.</p>
</div>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #1565c0, #42a5f5);">

## Metadatos de Control
- **Timestamp de verificación:** 2026-03-23 17:30:00 UTC  
- **Fuentes primarias/institucionales consultadas:** Airbus, AviaciónLine, Velatia, Neste, ThisIsAerospace, Skies Mag, AirNavRadar  
- **Discrepancias resueltas:** No se identificaron discrepancias; todas las fuentes coinciden en la fecha (25 de marzo de 2022), el avión (MSN1) y las características del vuelo.  
- **Nivel de confianza:** Alto  
- **Cláusula final:** “Cuando una afirmación relevante no pudo ser confirmada, se omitió o se marcó como [NO CONFIRMADO]”.

___


## 🏗️ Plantilla: Ejemplo de fundacion

---
layout: post
title: "18 de diciembre de 1970 | Fundación de Airbus Industrie (GIE)"
date: 1970-12-18
categories: [fundacion]
author: Enrique Pomares
pais: Francia / Alemania / España / Reino Unido
operator: Airbus Industrie
excerpt: "El 18 de diciembre de 1970 se constituyó Airbus Industrie como un consorcio europeo bajo la figura de Groupement d'Intérêt Économique (GIE), iniciando con el proyecto A300 y marcando el comienzo de la cooperación transnacional en la industria aeronáutica."
image: 1970-12-18-airbus-industrie-fundacion.webp

---

<figure>
  <img class="post-image" src="{{ site.baseurl }}/asscaption>
</figure>
<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #1b5e20, #2e7d32);">

<!-- ## Resumen Ejecutivo -->
<div class="highlight-box">
<p>El 18 de diciembre de 1970 se constituyó Airbus Industrie bajo la figura jurídica de un Groupement d'Intérêt Économique (GIE). Esta alianza franco-alemana, a la que se unirían España y el Reino Unido, nació para desafiar el dominio estadounidense en el mercado de aviones comerciales. Su primer proyecto, el Airbus A300, introdujo el concepto de fuselaje ancho bimotor.</p>
</div>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #1b5e20, #2e7d32);">

## Datos verificados del evento
- **Fecha:** 18 de diciembre de 1970  
- **Lugar:** Blagnac, Toulouse, Francia  
- **Entidad fundada:** Airbus Industrie (GIE)  
- **Países fundadores:** Francia y Alemania Occidental  
- **Empresas iniciales:** Aérospatiale (Francia) y Deutsche Airbus (Alemania)  
- **Primer presidente:** Henri Ziegler; director técnico: Roger Béteille  
- **Primer modelo en desarrollo:** Airbus A300B  
- **Participación de España:** incorporación en 1971 a través de CASA  

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #1b5e20, #2e7d32);">

## Contexto Histórico
A finales de los años 60, el mercado estaba dominado por Boeing, McDonnell Douglas y Lockheed. Europa comprendió que ninguna empresa nacional podía competir sola. Tras el acuerdo ministerial de 1969 entre Francia y Alemania, la constitución legal del GIE en 1970 consolidó la estructura multinacional.

### Entorno social
La fundación de Airbus representó un esfuerzo europeo por recuperar protagonismo en la aviación comercial y equilibrar el dominio estadounidense.

### Entorno tecnológico
El Airbus A300 introdujo la configuración bimotor de fuselaje ancho, más eficiente que los trireactores de la época, y sentó las bases para innovaciones como el sistema fly-by-wire.

### Entorno cultural
Airbus se convirtió en símbolo de cooperación transnacional y en referente de la industria aeroespacial europea.

## Desarrollo Cronológico
- 1969: Acuerdo ministerial entre Francia y Alemania para desarrollar un avión conjunto.  
- 18 de diciembre de 1970: Constitución legal de Airbus Industrie como GIE.  
- 1971: España se incorpora a través de CASA.  
- Década de 1970: Desarrollo y entrada en servicio del Airbus A300.  

## Consecuencias e Impacto
Airbus rompió el monopolio estadounidense y estableció un nuevo modelo de cooperación industrial. Su éxito abrió camino a una cadena de suministro global y a innovaciones tecnológicas que marcaron la aviación moderna.

## Legado
Airbus es hoy uno de los dos grandes fabricantes de aviones comerciales del mundo. Su fundación en 1970 es considerada el inicio de la cooperación aeroespacial europea moderna.

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #1b5e20, #2e7d32);">

## Referencias Verificadas
<div class="references">
  <ul>
    <li><a href="https://www.airbus.com/en/who-we-are/our-history/the-first-half-century">Airbus – 50 Years of Airbus: The Journey of a European Icon</a></li>
    <li><a href="https://www.flightglobal.com/flight-international/from-the-archive-december-1970/141655.article">FlightGlobal Archive – Airbus Industrie GIE Formation</a></li>
    <li><a href="https://www.airbus.com/en/who-we-are/airbus-in-spain">Airbus Spain (CASA) – Historia de la industria aeronáutica española y su integración en Airbus</a></li>
    <li><a href="https://en.wikipedia.org/wiki/Airbus">Wikipedia (EN) – Airbus</a></li>
  </ul>
</div>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #1b5e20, #2e7d32);">

<div class="note-box">
<p><strong>Nota aclaratoria:</strong> Algunas fuentes secundarias mencionan el acuerdo ministerial de 1969 como “fundación”, pero la constitución legal del GIE ocurrió el 18 de diciembre de 1970. La hora exacta de la firma no pudo ser verificada.</p>
</div>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #1b5e20, #2e7d32);">

## Metadatos de Control
- **Timestamp de verificación:** 2025-12-17 09:45 CST  
- **Fuentes primarias/institucionales consultadas:** Airbus, FlightGlobal, Airbus Spain (CASA)  
- **Discrepancias resueltas:** Diferencia entre acuerdo ministerial de 1969 y constitución legal en 1970.  
- **Datos no confirmados:** Hora exacta de la firma en Toulouse.  
- **Nivel de confianza:** Alto  
- **Cláusula final:** “Cuando una afirmación relevante no pudo ser confirmada, se omitió o se marcó como [NO CONFIRMADO]”.

___


## 📡 Plantilla: Ejemplo de espacial

---
layout: post
title: "20 de febrero de 1962 | John Glenn, primer estadounidense en orbitar la Tierra"
date: 1962-02-20
categories: [espacial]
author: [Enrique Pomares]
pais: Estados Unidos
operator: NASA – Proyecto Mercury
excerpt: "El 20 de febrero de 1962, John H. Glenn Jr. se convirtió en el primer estadounidense en orbitar la Tierra a bordo de la cápsula Friendship 7, completando tres órbitas en 4 h 55 min."
image: 1962-02-20-john-glenn-primer-astronauta-en-circundar-la-tierra.webp

---

<figure>
  <img class="post-image" src="{{ site.baseurl }}/assets/img/1962-02-20-john-glenn-primer-astronauta-en-circundar-la-tierra.webp" alt="John Glenn accede a la cápsula Friendship 7 para el lanzamiento orbital Mercury-Atlas 6, 1962">
  <figcaption class="post-caption">El astronauta John H. Glenn Jr. entra en su cápsula Mercury, la «Friendship 7», mientras se prepara para el lanzamiento del cohete Mercury-Atlas. El 20 de febrero de 1962, Glenn despegó hacia el espacio a bordo de su cohete Mercury-Atlas 6 (MA-6) y se convirtió en el primer estadounidense en orbitar la Tierra. Fuente:Foto NASA.
  </figcaption>
</figure>
<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #0d47a1, #29b6f6);">

<!-- ## Resumen Ejecutivo -->
<div class="highlight-box">
<p>El 20 de febrero de 1962, John H. Glenn Jr. se convirtió en el primer estadounidense en orbitar la Tierra a bordo de la cápsula Friendship 7 (Mercury-Atlas 6). Lanzado desde Cabo Cañaveral con un Atlas LV-3B, completó tres órbitas en 4 h 55 min pese a fallos técnicos y una alarma falsa sobre el escudo térmico. Amerrizó en el Atlántico y fue recuperado por el USS Noa, consolidando un triunfo clave para el programa espacial de EE.UU. frente a la URSS.</p>
</div>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #0d47a1, #29b6f6);">

## Datos verificados del evento
- **Fecha:** 20 de febrero de 1962  
- **Misión:** Mercury-Atlas 6 (MA-6) – Friendship 7  
- **Astronauta:** John H. Glenn Jr. (1921–2016)  
- **Vehículo lanzador:** Atlas LV-3B (SN 109-D)  
- **Lugar de lanzamiento:** Launch Complex 14, Cabo Cañaveral, Florida  
- **Duración total:** 4 h 55 min 23 s  
- **Órbitas completadas:** 3  
- **Altitud máxima:** 265 km  
- **Velocidad orbital:** ~28,000 km/h  
- **Incidentes:** fallo de periscopio, control automático defectuoso (usó manual), falsa alarma de escudo térmico en reentrada  
- **Recuperación:** Amerrizaje a 640 km de las Bahamas; recuperado por USS Noa (DD-841)  

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #0d47a1, #29b6f6);">

## Contexto Histórico
La misión MA-6 fue la quinta tripulada del Proyecto Mercury y la primera orbital de EE.UU., en respuesta al éxito soviético con Yuri Gagarin (1961). Glenn se convirtió en héroe nacional y símbolo de la recuperación del prestigio espacial estadounidense.

## Desarrollo Cronológico
- **1958:** Inicio del Proyecto Mercury.  
- **1961:** Vuelo suborbital de Alan Shepard y Gus Grissom.  
- **20 feb 1962:** Glenn orbita la Tierra en Friendship 7.  
- **1998:** Glenn regresa al espacio en STS-95 a bordo del transbordador Discovery.  

## Consecuencias e Impacto
- **Político:** Restableció confianza en el programa espacial de EE.UU.  
- **Tecnológico:** Validó sistemas de control manual y procedimientos de emergencia.  
- **Cultural:** Glenn se convirtió en figura pública, senador y referente histórico.  

## Legado
La cápsula Friendship 7 se exhibe en el Smithsonian National Air and Space Museum. La misión es considerada uno de los hitos más importantes de la carrera espacial.

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #0d47a1, #29b6f6);">

## Referencias Verificadas
<div class="references">
  <ul>
    <li><a href="https://es.wikipedia.org/wiki/Mercury_Atlas_6">Wikipedia (ES) – Mercury Atlas 6</a></li>
    <li><a href="https://en.wikipedia.org/wiki/Mercury-Atlas_6">Wikipedia (EN) – Mercury-Atlas 6</a></li>
    <li><a href="https://www.nasa.gov/mission/mercury-atlas-6-friendship-7/">NASA – Mercury-Atlas 6: Friendship 7</a></li>
    <li><a href="https://www.nasa.gov/history/friendship7/">NASA History – Friendship 7</a></li>
    <li><a href="https://spacecenter.org/john-glenn-friendship-7-launched/">Space Center Houston – Friendship 7 launched</a></li>
    <li><a href="https://airandspace.si.edu/collection-objects/capsule-mercury-ma-6/nasm_A19670176000">Smithsonian Air & Space – Friendship 7 capsule</a></li>
    <li><a href="https://www.spaceline.org/united-states-manned-space-flight/mercury-program-index/mercury-ma-6-fact-sheet/">Spaceline – Mercury MA-6 Fact Sheet</a></li>
  </ul>
</div>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #0d47a1, #29b6f6);">

<div class="note-box">
<p><strong>Nota aclaratoria:</strong> La alarma sobre el escudo térmico resultó ser falsa; Glenn mantuvo la calma y completó la reentrada con éxito. La cápsula Friendship 7 se conserva en el Smithsonian NASM.</p>
</div>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #0d47a1, #29b6f6);">

## Metadatos de Control
- **Timestamp de verificación:** 2026-02-17 14:05 CST  
- **Fuentes primarias/institucionales consultadas:** NASA, Smithsonian NASM, Space Center Houston  
- **Discrepancias resueltas:** Confirmación de duración exacta del vuelo y detalles de incidentes técnicos.  
- **Nivel de confianza:** Alto  
- **Cláusula final:** “Cuando una afirmación relevante no pudo ser confirmada, se omitió o se marcó como [NO CONFIRMADO]”.

___


## 🔐 Plantilla: Ejemplo de seguridad

---
layout: post
title: "23 de noviembre de 1985 | Secuestro del Vuelo 648 de EgyptAir"
date: 1985-11-23
categories: [seguridad]
author: Enrique Pomares
pais: Egipto
operator: EgyptAir
excerpt: "El Boeing 737-200 de EgyptAir, vuelo 648, fue secuestrado por la Organización Abu Nidal en ruta Atenas–El Cairo, desencadenando una crisis internacional."
image: 1985-11-23-egyptair-flight-648.webp

---

<figure>
  <img class="post-image" src="{{ site.baseurl }}/assets/img/1985-11-23-egyptair-flight-648.webp" alt="Boeing 737-200 de EgyptAir involucrado en el secuestro del Vuelo 648">
  <figcaption class="post-caption">Boeing 737-200 de EgyptAir (matrícula SU-AYH), el avión involucrado en el secuestro del Vuelo 648 por la Organización Abu Nidal el 23 de noviembre de 1985 en ruta Atenas–El Cairo.</figcaption>
</figure>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #0d47a1, #546e7a);">

<!-- ## Resumen ejecutivo -->
<div class="highlight-box">
  <p>
    El 23 de noviembre de 1985, el vuelo 648 de EgyptAir fue secuestrado por militantes de la Organización Abu Nidal tras despegar de Atenas rumbo a El Cairo. El Boeing 737-200, matrícula SU-AYH, fue forzado a aterrizar en Malta, donde se desencadenó una operación de rescate que terminó en tragedia, con decenas de víctimas y un fuerte impacto en la seguridad aérea internacional.
  </p>
</div>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #0d47a1, #546e7a);">

## Datos verificados del evento
- **Fecha del secuestro:** 23 de noviembre de 1985  
- **Vuelo:** EgyptAir 648  
- **Aeronave:** Boeing 737-200, matrícula SU-AYH  
- **Ruta prevista:** Atenas – El Cairo  
- **Lugar de aterrizaje forzado:** Aeropuerto Internacional de Malta  
- **Grupo responsable:** Organización Abu Nidal  
- **Víctimas:** más de 50 fallecidos en la operación de rescate

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #0d47a1, #546e7a);">

## Contexto Histórico
Durante la década de 1980, los secuestros aéreos se convirtieron en una amenaza recurrente en el transporte internacional. El caso del vuelo 648 de EgyptAir destacó por la violencia del desenlace y la participación de un grupo extremista palestino, lo que puso de relieve la vulnerabilidad de la aviación comercial frente al terrorismo.


## Desarrollo Cronológico
- **Despegue:** El vuelo partió de Atenas con destino a El Cairo.  
- **Secuestro:** Militantes armados tomaron el control poco después del despegue.  
- **Aterrizaje en Malta:** El avión fue obligado a aterrizar en el Aeropuerto Internacional de Malta.  
- **Operación de rescate:** Fuerzas especiales intentaron liberar a los pasajeros, pero la intervención resultó en un elevado número de víctimas.  


## Consecuencias e Impacto
- **Seguridad aérea:** El incidente impulsó nuevas medidas de seguridad en aeropuertos y protocolos de respuesta a secuestros.  
- **Relaciones internacionales:** El caso generó tensiones diplomáticas entre Egipto, Malta y otros países involucrados.  
- **Memoria histórica:** El vuelo 648 se convirtió en un símbolo de los riesgos del terrorismo aéreo en los años ochenta.  


## Legado
El secuestro del vuelo 648 de EgyptAir marcó un punto de inflexión en la percepción global sobre la seguridad aérea. Las lecciones aprendidas influyeron en la creación de estándares internacionales más estrictos para la protección de pasajeros y tripulaciones.

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #0d47a1, #546e7a);">

## Referencias Verificadas
<div class="references">
  <ul>
    <li><a href="https://en.wikipedia.org/wiki/EgyptAir_Flight_648">Wikipedia (EN) – EgyptAir Flight 648</a></li>
    <li><a href="https://aviation-safety.net/wikibase/327099">https://aviation-safety.net/wikibase/327099</a></li>
    <li><a href="https://es.wikipedia.org/wiki/Vuelo_648_de_EgyptAir">https://es.wikipedia.org/wiki/Vuelo_648_de_EgyptAir</a></li>
    <li><a href="https://www.nbcnews.com/news/world/egyptair-hostage-drama-look-back-historic-hijackings-n547126">EgyptAir Hostage Drama: A Look Back at Historic Hijackings</a></li>
    <li><a href="https://www.routeyou.com/es-mt/location/view/50611294">Vuelo 648 de EgyptAir</a></li>
  </ul>
</div>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #0d47a1, #546e7a);">

<div class="note-box">
  <p><strong>Nota aclaratoria:</strong> Aunque este hecho terminó con un accidente y fatalidades, su naturaleza corresponde a un incidente de seguridad en la aviación (secuestro/terrorismo), no a un accidente aeronáutico. Por ello, se clasifica en la categoría de seguridad y no en “accidente”.</p>
</div>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #0d47a1, #546e7a);">

## Metadatos de Control
- **Timestamp de verificación:** 2026-01-04 13:25 CST  
- **Fuentes primarias/institucionales consultadas:** Wikipedia, Aviation Safety Network, BBC News  
- **Discrepancias resueltas:** Número de víctimas varía entre fuentes; se documenta como “más de 50” para consistencia.  
- **Nivel de confianza:** Alto  
- **Cláusula final:** “Cuando una afirmación relevante no pudo ser confirmada, se omitió o se marcó como [NO CONFIRMADO]”.

___


## 🔐 Plantilla: Ejemplo de supervivencia

---
layout: post
title: "3 de enero de 1974 | Récord Guinness de supervivencia aérea"
date: 1974-01-03
categories: [supervivencia]
author: Enrique Pomares
pais: Yugoslavia
excerpt: "Auxiliar de a bordo y única superviviente del vuelo JAT 367 en 1972. Récord Guinness por sobrevivir a la caída libre más alta sin paracaídas."
image: 1974-01-03-record-guinness-supervivencia-aerea.webp

---

<figure>
  <img class="post-image" src="{{ site.baseurl }}/assets/img/1974-01-03-record-guinness-supervivencia-aerea.webp" alt="Vesna Vulović frente a un avión de JAT">
  <figcaption class="post-caption">Vesna Vulović en uniforme de auxiliar de vuelo, junto a un avión DC-9 de Yugoslav Airlines (JAT). Fotografía tomada en aeropuerto europeo durante la década de 1970.</figcaption>
</figure>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #2e7d32, #ef6c00);">

<!-- ## Resumen Ejecutivo -->
<div class="highlight-box">
    <p>
    El 3 de enero de 1974 se reconoció oficialmente la supervivencia de Vesna Vulović en el accidente del vuelo JAT 367 ocurrido en 1972. Con apenas 23 años, sobrevivió a una caída libre desde más de 10.000 metros de altura, convirtiéndose en símbolo mundial de resiliencia y en poseedora de un récord Guinness único.
    </p>
</div>
<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #2e7d32, #ef6c00);">

## Datos verificados del evento
- **Fecha de nacimiento:** 3 de enero de 1950  
- **Lugar de nacimiento:** Belgrado, Yugoslavia  
- **Logros destacados:** Superviviente única del vuelo JAT 367; récord Guinness por la caída libre más alta sin paracaídas (10.160 m / 33.330 pies)  
- **Servicio profesional:** Auxiliar de a bordo en Yugoslav Airlines (JAT)  
- **Fecha de fallecimiento:** 23 de diciembre de 2016, Belgrado  

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #2e7d32, #ef6c00);">

## Contexto Histórico
El accidente del vuelo JAT 367 ocurrió el 26 de enero de 1972, cuando una explosión en pleno vuelo desintegró la aeronave sobre Checoslovaquia. De los 28 ocupantes, solo Vesna Vulović sobrevivió. Su caso fue ampliamente difundido y se convirtió en un referente mundial.

### Entorno social
La década de 1970 estuvo marcada por tensiones políticas en Europa y por incidentes relacionados con terrorismo aéreo. El accidente del JAT 367 se enmarca en ese contexto.

### Entorno tecnológico
La aviación comercial experimentaba un crecimiento acelerado, pero aún carecía de protocolos de seguridad modernos en la inspección de equipajes.

### Entorno cultural
La supervivencia de Vesna fue interpretada como un “milagro” y recibió gran cobertura mediática, convirtiéndose en un símbolo de esperanza.

## Desarrollo Cronológico
- **26/01/1972:** Explosión en vuelo del JAT 367 sobre Checoslovaquia.  
- **26/01/1972:** Vesna es hallada con graves lesiones, pero con vida.  
- **1972–1973:** Recuperación prolongada en hospitales yugoslavos.  
- **3/01/1974:** Reconocimiento oficial y registro en Guinness World Records.  
- **Décadas posteriores:** Figura pública en Serbia, defensora de causas sociales.  

## Consecuencias e Impacto
- Refuerzo de controles de seguridad aérea en Europa.  
- Caso emblemático en estudios médicos sobre supervivencia extrema.  
- Inspiración cultural y mediática en documentales y efemérides.

## Legado
Vesna Vulović es recordada como la mujer que desafió lo imposible en la historia de la aviación. Su nombre permanece en los registros Guinness y en la memoria colectiva como símbolo de resiliencia.

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #2e7d32, #ef6c00);">

## Referencias Verificadas
<div class="references">
  <ul>
    <li><a href="https://es.wikipedia.org/wiki/Vesna_Vulovi%C4%87">Wikipedia – Vesna Vulović</a></li>
    <li><a href="https://www.guinnessworldrecords.com/world-records/highest-fall-survived-without-parachute">Guinness World Records – Highest fall survived without parachute</a></li>
    <li><a href="https://www.infobae.com/america/mundo/2024/12/18/la-increible-historia-de-vesna-vulovic-la-azafata-que-sobrevivio-a-una-caida-libre-desde-10000-metros-de-altura-sin-paracaidas/">Infobae – Historia de Vesna Vulović</a></li>
    <li><a href="https://en.wikipedia.org/wiki/Vesna_Vulovi%C4%87">Wikipedia (EN) – Vesna Vulović</a></li>
  </ul>
</div>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #2e7d32, #ef6c00);">

<div class="note-box">
<p><strong>Nota aclaratoria:</strong> Esta sección se generará únicamente si existe alguna discrepancia, controversia o detalle que requiera explicación adicional en la efeméride. Si no se necesita se omitirá en la versión final.</p>
</div>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #2e7d32, #ef6c00);">

## Metadatos de Control
- **Timestamp de verificación:** 2026-01-02 22:35:00 UTC  
- **Fuentes primarias/institucionales consultadas:** Wikipedia, Guinness World Records, Infobae  
- **Discrepancias resueltas:** Debate sobre la altitud exacta de la caída; Guinness mantiene cifra oficial de 10.160 m  
- **Nivel de confianza:** Alto  
- **Cláusula final:** “Cuando una afirmación relevante no pudo ser confirmada, se omitió o se marcó como [NO CONFIRMADO]”.

---

## 🛰️ Plantilla: Ejemplo de [espacial, accidente]

> Categoría combinada, para siniestros ocurridos en el ámbito espacial.
> Ejemplo real publicado: *1 de febrero de 2003 | Desintegración del transbordador Columbia (STS-107)*.

---
layout: post
title: "1 de febrero de 2003 | Desintegración del transbordador Columbia (STS-107), una tragedia que marcó la exploración espacial"
date: 2003-02-01
categories: [espacial, accidente]
author: Enrique Pomares
pais: Estados Unidos
operator: NASA
excerpt: "El transbordador Columbia se desintegró durante la reentrada atmosférica y provocó la pérdida de sus siete tripulantes."
image: 2003-02-01-accidente-transbordador-columbia-sts107.webp
---

<figure>
  <img class="post-image" src="{{ site.baseurl }}/assets/img/2003-02-01-accidente-transbordador-columbia-sts107.webp" alt="Fotografía oficial de la tripulación de siete astronautas de la misión STS-107">
  <figcaption class="post-caption">Retrato oficial de la tripulación de la misión STS-107, octubre de 2001. Fuente: <a href="https://commons.wikimedia.org/wiki/File:Crew_of_STS-107,_official_photo.jpg" style="color: #315fea; text-decoration: none;">NASA / Wikimedia Commons</a>.</figcaption>
</figure>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #0b2545, #134074, #e74c3c, #c0392b);">

<!-- ## Resumen Ejecutivo -->
<div class="highlight-box">
<p>[Párrafo 1: el hecho central, con hora, lugar y desenlace.]</p>
<p>[Párrafo 2: causa técnica y consecuencia institucional.]</p>
</div>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #0b2545, #134074, #e74c3c, #c0392b);">

## Datos verificados del evento

- **Fecha del desastre:** 1 de febrero de 2003 (08:59 EST / 13:59 UTC).
- **Lugar:** espacio aéreo sobre Texas y Luisiana, Estados Unidos.
- **Misión:** STS-107.
- **Vehículo:** transbordador espacial Columbia (OV-102).
- **Operador:** NASA.
- **Tripulación fallecida:** [relación nominal con grados y funciones].
- **Causa técnica primaria:** [descripción].

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #0b2545, #134074, #e74c3c, #c0392b);">

## Contexto Histórico

[Párrafo introductorio.]

### Entorno social
[Texto.]

### Entorno tecnológico
[Texto.]

### Entorno cultural
[Texto.]

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #0b2545, #134074, #e74c3c, #c0392b);">

## Desarrollo Cronológico

[Párrafo introductorio.]

- **[fecha]:** [hito, con enlace cruzado si procede].
- **[fecha]:** [hito].

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #0b2545, #134074, #e74c3c, #c0392b);">

## Consecuencias e Impacto

[Efectos inmediatos: suspensión de operaciones, investigación, reformas.]

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #0b2545, #134074, #e74c3c, #c0392b);">

## Legado

[Proyección a largo plazo: memoria, cambios doctrinales, monumentos.]

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #0b2545, #134074, #e74c3c, #c0392b);">

## Referencias Verificadas

- <a href="https://ejemplo.com" style="color: #315fea; text-decoration: none;">[Fuente institucional 1]</a>
- <a href="https://ejemplo.com" style="color: #315fea; text-decoration: none;">[Fuente institucional 2]</a>
- <a href="https://ejemplo.com" style="color: #315fea; text-decoration: none;">[Fuente secundaria de contraste 1]</a>
- <a href="https://ejemplo.com" style="color: #315fea; text-decoration: none;">[Fuente secundaria de contraste 2]</a>

<!-- Mínimo cuatro entradas, dos de ellas primarias o institucionales (regla maestra 14). -->

<div class="note-box">
  <p><strong>Nota aclaratoria:</strong> [Matices necesarios.]</p>
</div>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #0b2545, #134074, #e74c3c, #c0392b);">

## Metadatos de Control
- **Timestamp de verificación:** AAAA-MM-DD HH:MM:SS ZONA
- **Fuentes primarias/institucionales consultadas:** [lista]
- **Fuentes secundarias de contraste:** [lista]
- **Discrepancias resueltas:** [resumen]
- **Nivel de confianza:** Alto / Medio / Bajo
- **Cláusula final:** "Cuando una afirmación relevante no pudo ser confirmada, se omitió o se marcó como [NO CONFIRMADO]".

---

## 🎖️ Plantilla: Ejemplo de conmemoracion

> Para fechas conmemorativas recurrentes, no para el hecho puntual que las originó.
> Ejemplo real publicado: *23 de julio de 1941 | Día de la Fuerza Aérea del Perú*.

---
layout: post
title: "23 de julio de 1941 | Conmemoración del Día de la Fuerza Aérea del Perú y el heroísmo de José Abelardo Quiñones"
date: 1941-07-23
categories: [conmemoracion]
author: Enrique Pomares
pais: Perú
operator: Fuerza Aérea del Perú
excerpt: "Cada 23 de julio el Perú honra a su Fuerza Aérea en memoria del sacrificio del Capitán FAP José Abelardo Quiñones."
image: 1941-07-23-conmemoracion-dia-fuerza-aerea-peru.webp
---

<figure>
  <img class="post-image" src="{{ site.baseurl }}/assets/img/1941-07-23-conmemoracion-dia-fuerza-aerea-peru.webp" alt="Retrato oficial del Capitán FAP José Abelardo Quiñones Gonzales en uniforme militar">
  <figcaption class="post-caption">Retrato oficial del Héroe Nacional del Perú, Capitán FAP José Abelardo Quiñones Gonzales (1914-1941). Fuente: <a href="https://commons.wikimedia.org/wiki/File:MINISTRO_DE_DEFENSA_REALIZ%C3%93_VISITA_DE_TRABAJO_A_CHICLAYO_(14153905388).jpg" style="color: #315fea; text-decoration: none;">Ministerio de Defensa del Perú / Wikimedia Commons</a>.</figcaption>
</figure>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #2e7d32, #66bb6a, #fbc02d, #f9a825);">

<!-- ## Resumen Ejecutivo -->
<div class="highlight-box">
<p>[Párrafo 1: qué se conmemora y por qué en esa fecha.]</p>
<p>[Párrafo 2: el hecho histórico que da origen a la conmemoración.]</p>
</div>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #2e7d32, #66bb6a, #fbc02d, #f9a825);">

## Datos verificados del evento

- **Fecha central de conmemoración:** 23 de julio.
- **Lugar de la acción histórica:** Quebrada Seca, frontera peruano-ecuatoriana.
- **Figura homenajeada:** Capitán FAP José Abelardo Quiñones Gonzales.
- **Aeronave:** caza North American NA-50 «Torito».
- **Marco legal vigente:** [leyes que establecen la conmemoración].
- **Distinción institucional:** [diferencia entre fecha fundacional y fecha conmemorativa].

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #2e7d32, #66bb6a, #fbc02d, #f9a825);">

## Contexto Histórico

[Párrafo introductorio.]

### Entorno social
[Texto.]

### Entorno tecnológico
[Texto.]

### Entorno cultural
[Texto.]

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #2e7d32, #66bb6a, #fbc02d, #f9a825);">

## Desarrollo Cronológico

[Párrafo introductorio.]

- **[fecha]:** [hito fundacional o biográfico].
- **[fecha]:** [el hecho conmemorado].
- **[fecha]:** [norma legal que consagra la conmemoración].

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #2e7d32, #66bb6a, #fbc02d, #f9a825);">

## Consecuencias e Impacto

[Efectos inmediatos del hecho conmemorado.]

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #2e7d32, #66bb6a, #fbc02d, #f9a825);">

## Legado

[Vigencia de la conmemoración: monumentos, toponimia, actos anuales.]

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #2e7d32, #66bb6a, #fbc02d, #f9a825);">

## Referencias Verificadas

- <a href="https://ejemplo.com" style="color: #315fea; text-decoration: none;">[Fuente institucional 1]</a>
- <a href="https://ejemplo.com" style="color: #315fea; text-decoration: none;">[Fuente institucional 2]</a>
- <a href="https://ejemplo.com" style="color: #315fea; text-decoration: none;">[Fuente secundaria de contraste 1]</a>
- <a href="https://ejemplo.com" style="color: #315fea; text-decoration: none;">[Fuente secundaria de contraste 2]</a>

<!-- Mínimo cuatro entradas, dos de ellas primarias o institucionales (regla maestra 14). -->

<div class="note-box">
  <p><strong>Nota aclaratoria:</strong> [Distinción entre fecha fundacional y conmemorativa, grados militares, etc.]</p>
</div>

<hr style="margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, #2e7d32, #66bb6a, #fbc02d, #f9a825);">

## Metadatos de Control
- **Timestamp de verificación:** AAAA-MM-DD HH:MM:SS ZONA
- **Fuentes primarias/institucionales consultadas:** [lista]
- **Fuentes secundarias de contraste:** [lista]
- **Discrepancias resueltas:** [resumen]
- **Nivel de confianza:** Alto / Medio / Bajo
- **Cláusula final:** "Cuando una afirmación relevante no pudo ser confirmada, se omitió o se marcó como [NO CONFIRMADO]".

---

## Cambios incorporados en esta V2
- Formalización del estilo de enlaces HTML sin subrayado.
- Capitalización obligatoria de grados militares.
- Inclusión de la fórmula “borrador preliminar del investigador”. *(Derogada en v2.12: el borrador no se cita.)*
- Regla de un solo enlace cruzado, preferiblemente en `## Desarrollo Cronológico`. *(Superado en v2.1: la restricción se refiere a no repetir la misma URL.)*
- Prohibición expresa de URLs públicas inferidas para efemérides aún no publicadas.
- Protocolo de transparencia ante imágenes bloqueadas por el sitio origen.

---

## Estado
Este documento queda propuesto como **nueva plantilla maestra de referencia** para futuras efemérides del proyecto.


---

## Reglas incorporadas en la versión v2.1 — 2026-07-28

### Divisores obligatorios
Debe existir un `<hr>` antes de cada sección principal del post. La plantilla de ejemplo no prevalece sobre esta regla de uniformidad visual.

### Categorías y degradados adicionales
- `conmemoracion` → `linear-gradient(to right, #2e7d32, #66bb6a, #fbc02d, #f9a825)`
- `[espacial, accidente]` → `linear-gradient(to right, #0b2545, #134074, #e74c3c, #c0392b)`

### Enlaces cruzados
La restricción se refiere a no repetir la misma URL. Se permiten varios enlaces cruzados diferentes si son pertinentes, están publicados y aportan valor. Está prohibido enlazar una efeméride consigo misma.

### Consistencia documental
La fecha del YAML, la fecha del archivo, el título, el tema y la URL pública deben corresponder al mismo hecho. Las discrepancias deben resolverse o quedar explicadas.

### Timestamp dinámico
Debe reflejar la fecha y hora local exactas de finalización del documento y no puede repetirse entre posts.

### Imágenes representativas
El pie debe distinguir entre imagen exacta, imagen anterior, imagen posterior e imagen representativa. Si la fuente bloquea la descarga, se debe informar de manera expresa.

### Política de commits
El commit inicial solo se entrega tras solicitud expresa. Debe representar la incorporación formal limpia del post, sin mencionar imágenes ni cambios internos del flujo.

### Cifras
Miles con punto, decimales con coma y conversiones métricas cuando resulten pertinentes.

---

## Reglas incorporadas en la versión v2.2 — 2026-07-29

### Corrección de coherencia sobre enlaces cruzados
En el apartado «B) Evento» se corrigió la formulación «un solo enlace cruzado
basta», heredada de la V2 y contraria a la regla vigente desde la v2.1.

En la sección «Cambios incorporados en esta V2» se conserva la redacción
original por tratarse de un registro histórico, acompañada de una nota que
advierte de su superación.

### Criterio unificado vigente
- Una misma URL, una sola vez por post.
- Pueden emplearse varios enlaces cruzados distintos si son pertinentes.
- Nunca debe enlazarse una efeméride consigo misma.
- Solo se enlazan efemérides realmente publicadas, con su URL pública real.
- Ubicación preferente en `## Desarrollo Cronológico`.

---

## Reglas incorporadas en la versión v2.3 — 2026-07-30

### Recuperación de las plantillas de ejemplo
Se restituyen las siete plantillas de ejemplo de la v1.8 (`nacimiento`, `accidente`,
`evento`, `fundacion`, `espacial`, `seguridad` y `supervivencia`), ausentes en las
versiones v2.x.

### Tabla normativa de divisores
La sección «Colores de divisores por categoría» se sustituye por una tabla con los
códigos hexadecimales exactos de las nueve categorías reconocidas. Los degradados
dejan de describirse por el nombre del color.

### Criterio de imágenes en efemérides de accidente
Se incorpora a la sección «Pie de foto: reglas obligatorias» un criterio específico
para la categoría `accidente`: la imagen preferente es la de la aeronave intacta
antes del suceso, no la de sus restos. Se añade además el modelo de pie para
imágenes anteriores al hecho.

### Nuevas plantillas de categorías combinadas y conmemorativas
Se incorporan dos plantillas inexistentes hasta ahora, basadas en efemérides
publicadas del repositorio:

- `[espacial, accidente]`, a partir de la desintegración del transbordador Columbia
  (STS-107) del 1 de febrero de 2003, con degradado de cuatro paradas
  `#0b2545, #134074, #e74c3c, #c0392b`.
- `conmemoracion`, a partir del Día de la Fuerza Aérea del Perú del 23 de julio de
  1941, con degradado de cuatro paradas `#2e7d32, #66bb6a, #fbc02d, #f9a825`.

Ambos degradados se verificaron directamente sobre los posts publicados, que
emplean ocho divisores homogéneos cada uno.

### Control de cambios

| Versión | Fecha | Descripción |
| :--- | :--- | :--- |
| v1.8 | 2026-07-02 | Documento con las siete plantillas de ejemplo por categoría. |
| v2.1 | 2026-07-28 | Divisores por sección, timestamp dinámico, categorías nuevas, coherencia documental, formato numérico. |
| v2.2 | 2026-07-29 | Corrección de coherencia sobre enlaces cruzados: se prohíbe repetir la misma URL, no limitar el número de enlaces distintos. |
| v2.3 | 2026-07-30 | Recuperación de las siete plantillas de ejemplo de la v1.8, tabla normativa de degradados con códigos hexadecimales y adición de las plantillas de `[espacial, accidente]` y `conmemoracion`. |
| v2.4 | 2026-07-31 | Criterio de imágenes para efemérides de accidente: preferencia por la aeronave intacta antes del suceso y modelo de pie para imágenes anteriores al hecho. |
| v2.5 | 2026-08-01 | Principio de documento limpio (regla maestra 8): el post no relata el proceso de investigación. Se excluyen del documento publicado los errores del borrador, los enlaces inaccesibles y las incidencias del entorno; se comunican al editor por chat. Se acota el campo «Discrepancias resueltas» y el uso de la nota aclaratoria a las divergencias entre fuentes publicadas. |
| v2.6 | 2026-08-02 | Extensión del principio de documento limpio a las comprobaciones rutinarias del flujo de trabajo. Queda proscrita en el post la fórmula «se verificó la coherencia entre la fecha del hecho, el título, el nombre del archivo y el YAML» y cualquier equivalente. El campo «Discrepancias resueltas» se omite cuando no hay divergencias entre fuentes. |
| v2.7 | 2026-08-04 | Regla de cómputo de años transcurridos (regla maestra 9): las efemérides se publican el mismo día y mes del hito, de modo que los años transcurridos se obtienen restando el año del hito al año de publicación, tomado del campo `fecha_publicacion` del borrador. Se exige cifra exacta y verificación al cierre del documento. |
| v2.8 | 2026-08-05 | Regla de verificación de contenido de las fuentes (regla maestra 10): un código de respuesta 200 no acredita que la página corresponda al sujeto de la efeméride. Toda ficha de archivo, museo o biblioteca debe verificarse por su contenido —título, identificador, fecha e imagen— antes de emplearse como referencia, como enlace del `<figure>` o como origen de una imagen. Exigencia extrema en repositorios de identificadores correlativos. |
| v2.9 | 2026-08-09 | Reglas de trabajo de las sesiones del 8 y 9 de agosto: URL canónica de enlaces internos con fecha en barras y guion terminal eliminado del slug (regla maestra 11); imágenes a resolución nativa sin ampliaciones y sin nota de resolución en el post (regla maestra 12); la fórmula «borrador preliminar del investigador» solo como fuente de contraste en metadatos, quedando proscritas las líneas de estado del documento y las notas de resolución de imagen (extensión de la regla maestra 8). |
| v2.10 | 2026-08-12 | Regla maestra 13: un separador del degradado de la categoría por frontera entre bloques, con `fundacion` en el verde de `nacimiento`; extensión de la mayúscula de grados a Capitán y Primer Oficial de la aviación junto al nombre propio. |


---

## Reglas incorporadas en la versión v2.12 — 2026-08-16

### El borrador preliminar deja de citarse (regla maestra 6, reescrita)
El archivo base que aporta el editor no se menciona en el post ni en sus
metadatos. Se derogan las fórmulas «borrador preliminar del investigador» y
«borrador preliminar del usuario» como fuentes de contraste. El borrador es un
insumo opcional, no preferible, procedente de modelos generativos que
introdujeron datos erróneos; cada dato que aporte se verifica en fuente
publicada y es esa fuente la que se cita. Se corrigen en consecuencia la
plantilla normativa de «Metadatos de Control» y los metadatos de las plantillas
de ejemplo.

### Mínimo de cuatro referencias verificadas (regla maestra 14, nueva)
Cada post lleva al menos cuatro referencias, dos de ellas primarias o
institucionales, validadas por contenido. Motivo: los tres posts anteriores al
del BAe Hawk se entregaron con solo dos referencias.

### Control de cambios

| Versión | Fecha | Descripción |
| :--- | :--- | :--- |
| v2.11 | 2026-08-14 | Versión de partida de esta ronda. |
| v2.12 | 2026-08-16 | Regla maestra 6 reescrita: el borrador preliminar del editor no se cita en el post ni en los metadatos, por ser insumo opcional procedente de modelos generativos con datos erróneos. Nueva regla maestra 14: mínimo de cuatro referencias verificadas por post, dos de ellas primarias o institucionales. |
| v2.13 | 2026-08-17 | Coherencia interna de los separadores: siete `<hr>` desnudos ante el `note-box` y diez `<hr ... />` autocerrados en los ejemplos pasan a la forma normativa con degradado; se declara que el separador previo a la nota aclaratoria cuenta como divisor de sección; se normaliza el doble espacio en diez divisores. Sin cambios de fondo en las reglas. |
| v2.14 | 2026-08-20 | Regla maestra 12 reescrita: tamaño de casa 800 × 1.000 (`nacimiento`) y 1.200 × 675 (resto); se permite ampliar con remuestreo de calidad. Errata 678 → 675. Derogado «resolución nativa / no se amplían». La resolución sigue fuera del post. |
| v2.15 | 2026-08-20 | Nombre de imagen = nombre del post; conteo de referencias por `<li>`, `-` y `1.`; hechos de más de un día se conmemoran en la culminación (salvo Apolo 11). |
| v2.16 | 2026-08-21 | Segunda pasada de coherencia interna de los ejemplos: 25 cabeceras al nivel y la capitalización de la regla maestra 1; ejemplo de `seguridad` saneado (`## Referencias` → `## Referencias Verificadas`, `Metadatos de control` → `Metadatos de Control`, `alto` → `Alto`, `</div` sin cerrar); cuatro ejemplos elevados al mínimo de cuatro referencias de la regla maestra 14; etiqueta normativa `Fuentes primarias/institucionales consultadas` en los siete ejemplos heredados; `Datos biográficos y eventos` → `Datos verificados del evento` en `supervivencia`. Sin cambios de fondo en las reglas. |
