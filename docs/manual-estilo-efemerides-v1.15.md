# Manual de Estilo de Efemérides
> Edición consolidada: 2026-09-03  
> Versión: v1.15

---

## 1. Propósito

Este manual resume las lecciones aprendidas en la producción reciente de efemérides y convierte esas decisiones editoriales en normas reutilizables.

Su objetivo es alinear:
- rigor histórico;
- claridad narrativa;
- consistencia visual;
- transparencia metodológica **ante el editor**, no ante el lector (véase § 9.1);
- compatibilidad con el flujo real de trabajo del editor.

---

## 2. Filosofía editorial

### 2.1 Verdad antes que exhaustividad
Es mejor omitir un dato dudoso que rellenarlo por intuición.

### 2.2 Contexto antes que acumulación
Una buena efeméride no es una lista de datos: es una pieza breve, sólida y bien organizada.

### 2.3 Respeto al repositorio vivo
Si el editor ya corrigió manualmente un título, categoría, imagen o divisor, ese estado tiene prioridad práctica.

### 2.4 Transparencia cuando algo falla
Si una fuente visual no puede usarse por restricciones técnicas, debe decirse. Nunca debe ocultarse la sustitución.

---

## 3. Estructura ideal de una efeméride

1. YAML inicial
2. Figura
3. Resumen Ejecutivo
4. Datos verificados del evento
5. Contexto Histórico
6. Desarrollo Cronológico
7. Consecuencias e Impacto
8. Legado
9. Referencias Verificadas
10. Nota aclaratoria (si aplica)
11. Metadatos de Control

### Regla de estructura
Las cabeceras normativas deben mantenerse exactamente en su forma oficial.

---

## 4. Estilo de redacción

### 4.1 Tono
- sobrio;
- profesional;
- historiográfico sin rigidez innecesaria;
- empático en accidentes y tragedias;
- sin sensacionalismo.

### 4.2 Lenguaje
- español neutro;
- precisión técnica sin jerga excesiva;
- evitar calcos torpes del inglés;
- traducir citas o expresiones completas si se incluyen.

### 4.3 Grados militares, jerarquías de aviación y tratamientos

Los grados militares, de cualquier arma, país y época, se escriben con mayúscula
inicial cuando preceden inmediatamente a un nombre propio. La lista es
**enunciativa, no cerrada**: Teniente, Subteniente, Capitán, Mayor, Teniente
Coronel, Coronel, Alférez, General de Brigada, Teniente de Navío, Comodoro,
Sargento…, y rige para grados ajenos y antiguos del mismo modo. La
capitalización rige también seguidos del nombre: *Capitán Gastón
Lafannechère*, *Teniente Vicente Landaeta Gil*, *Teniente de Navío Roberto
Guérin*, *Coronel David López Henríquez*, *General Emilio Fernández*. Sin
nombre propio van en minúscula (*el coronel retirado firmó el informe*).

El **plural que encabeza una lista de nombres propios conserva la
mayúscula**: *los Tenientes Gómez y Ramírez*, *los Mayores Squier y Wallace*.
Precisión del editor (2026-09-03): era el vacío que dejaba sin criterio la
correcta escritura de nóminas de oficiales en los ensayos de Fort Myer.

Las jerarquías de la aviación se tratan como los grados militares: *Capitán* y
*Primer Oficial* (y equivalentes) van con mayúscula inicial cuando acompañan al
nombre propio (*Capitán Omar Ospina*, *Primer Oficial David Muñoz*) y en
minúscula sin él (*el capitán desconecta el autopiloto*, *el primer oficial
avisa*). Precisión del investigador del 12 de agosto de 2026: son denominaciones
jerárquicas tan significativas como el grado castrense.

Los **tratamientos honoríficos y académicos** —Doctor, Licenciado, Señor,
Señora, Señorita y sus femeninos— siguen la regla de los grados: mayúscula
inicial cuando preceden inmediatamente al nombre propio (*Doctor Juan Pablo
Rojas Paúl*, *Licenciada Gregoria*), minúscula en cualquier otro uso. Decisión
D2-a del editor (2026-09-03), alineada con el protocolo venezolano y el uso
periodístico recogidos en el anexo *Comparación de tratamientos y rangos*
(`docs/anexo-comparacion-tratamientos-y-rangos.md`).

Los **cargos y oficios civiles van en minúscula incluso ante nombre propio**:
*el comandante del vuelo*, *el ingeniero civil Gustavo Heny*, *el presidente de
la aerolínea*, *el presidente Juan Pablo Rojas Paúl*. Decisión D1-a del editor
(2026-09-03): se mantiene la regla vigente y se armonizan hacia ella las
correlaciones capitalizadas heredadas.

**Fundamento de la desviación respecto a la Ortografía de la RAE** —que
prescribe minúscula uniforme para grados, jerarquías y tratamientos—: es una
elección deliberada de la casa, no una licencia tipográfica. El proyecto
conmemora la aviación con abundante material de entorno venezolano, donde la
mayúscula protocolaria es la forma esperada; la comparación completa de pautas
se custodia como anexo normativo, y la regla es auditada por el linter
(`efemerides-linter.sh`, regla maestra 5 de la Plantilla).

Motivos y precedentes: en la efeméride del 14 de julio de 1938 se entregó
«teniente» dos veces en minúscula y el editor debió corregirlo a mano antes del
commit (2026-08-08); el Subteniente Manuel Ríos convivía con su grafía
minúscula dentro del mismo post (1921-04-15, auditoría del 03-09-2026); los
seis grados del alta de Orville Wright en Fort Myer se capitalizaron antes de
su publicación (03-09-2026).

### 4.4 Siglas y acrónimos
En su primera aparición en el documento, toda sigla o acrónimo se escribe con
el nombre completo en el idioma original, seguido de la sigla entre paréntesis y
de la traducción al español entre paréntesis: *United States Army Air Corps
(USAAC) (Cuerpo Aéreo del Ejército de los Estados Unidos)*. En las apariciones
siguientes se emplea solo la sigla.

### 4.5 Alusiones al investigador y al editor
Cuando un post o documento deba aludir a quien aporta una fuente, una imagen o
una traducción, se emplea *el investigador* para la labor de investigación y
*el editor* únicamente para la figura editorial firmante. No se atribuyen al
editor tareas de investigación ni al investigador tareas editoriales.

### 4.6 Títulos: honra con hazaña o cualidad
El título de una efeméride biográfica honra al personaje: tras el nombre debe
ir la hazaña, el hito o la cualidad que lo caracteriza («Nacimiento de Bessie
Coleman, primera mujer afroamericana con licencia internacional de piloto»).
Quedan proscritos los títulos escuetos de solo nombre. La caracterización se
toma del contenido verificado del propio post (excerpt o cuerpo), nunca se
inventa; y el enriquecimiento del título **no altera** el slug, el nombre de
archivo ni la URL pública. Las auditorías de categoría se registran en el anexo
de sesión (precedente: los nueve títulos de `nacimiento` del 12 de agosto de
2026).

### 4.7 Ejes y movimientos de la aeronave
Los tres movimientos se nombran con su eje exacto: el **alabeo** es rotación en
torno al eje **longitudinal**; el **cabeceo** (balanceo), en torno al
**transversal o lateral** —el que sube y baja el morro—; y la **guiñada**, en
torno al **vertical**. Toda frase que asigne un movimiento a un eje se contrasta
con la definición, no con la intuición. Caso sensible: la glosa en prosa de los
sistemas amortiguadores (*pitch damper*, *yaw damper*), donde cabe describir el
cabeceo «en el eje vertical» por confusión con la guiñada. Precedente: en el
post del récord Sageburner (28-08-1961) el amortiguador de cabeceo aparecía
descrito como suavizante de «los movimientos del morro en el eje vertical»; ni el
lazo de verificación del asistente ni la revisión del editor lo detectaron, y lo
señalaron tres lectores el día de la conmemoración. El editor lo corrigió en la
rama el 28-08-2026 («eje transversal o lateral»).

---

## 5. Reglas de repetición

### 5.1 Excerpt
Debe ser breve y útil para SEO/listado.

### 5.2 Resumen Ejecutivo
Debe condensar el hecho y ampliarlo ligeramente.

### 5.3 Datos verificados
Debe aportar lo factual sin copiar el Resumen Ejecutivo.

### 5.4 Desarrollo Cronológico
Es el espacio preferente para hitos fechados y para un posible enlace cruzado interno.

### 5.5 Consecuencias e Impacto
Expone efectos inmediatos o cercanos.

### 5.6 Legado
Expone la proyección a largo plazo.

### 5.7 Distancia temporal con el presente
Las efemérides se publican **el mismo día y el mismo mes del hito**. Cuando el
texto menciona los años transcurridos —habitualmente en `## Legado`—, la cifra
es un entero exacto:

```
años transcurridos = año de publicación − año del hito
```

El año de publicación se toma del campo `fecha_publicacion` del borrador. Se
emplea la cifra exacta, no la redondeada: para un hito de 1945 publicado en 2026,
«ochenta y un años después», nunca «ochenta años después».

---

## 6. Política de enlaces

### 6.1 Enlaces dentro del texto
Usar HTML inline:

```html
<a href="https://ejemplo.com" style="color: #315fea; text-decoration: none;">texto</a>
```

### 6.2 Prohibiciones
- no enlaces subrayados por defecto en el cuerpo;
- no `href` mal formados;
- no URLs públicas inventadas;
- no archivos `.md` como enlaces públicos.

### 6.3 Enlaces cruzados internos
- evitar repetir la misma URL;
- pueden utilizarse varios enlaces cruzados distintos y pertinentes;
- mejor en `## Desarrollo Cronológico`;
- nunca enlazar una efeméride consigo misma;
- solo si la otra efeméride ya está realmente publicada;
- cuando el texto aluda a una serie, ranking o contraste entre hechos (primer
  accidente, récord superado, tragedia más reciente), es pertinente enlazar los
  hitos de esa serie con criterio editorial coherente; cada enlace debe portar
  su propio dato (fecha y magnitud), no formar una lista desnuda;
- **reciprocidad:** cuando una efeméride recién publicada vuelve posible o
  necesario un enlace desde posts ya publicados (y viceversa), se añade el
  enlace recíproco mediante commit de corrección (caso de los tres hermanos
  Wright, 14 de agosto de 2026).

---

## 7. Política de imágenes

### 7.1 Principio de prioridad
La imagen sugerida por el editor/usuario es prioritaria si puede verificarse y descargarse.

### 7.2 Transparencia técnica
Si el origen bloquea la descarga:
- explicarlo;
- no ocultarlo;
- no sustituir silenciosamente.

### 7.3 Identidad del sujeto retratado
Antes de descargar o enlazar una imagen debe confirmarse que el sujeto que aparece
en ella es el de la efeméride, contrastando la ficha de origen y, cuando sea
posible, la propia imagen. La verificación del enlace no sustituye a la del
contenido (§ 8.6).

### 7.4 Exactitud del pie de foto
El pie debe indicar si la imagen es:
- exacta del hecho;
- posterior;
- anterior;
- representativa de un aparato similar.

### 7.5 Cuando se pide solo una figura
Responder únicamente con el `<figure>` exacto.

### 7.6 Tamaño de casa; se permite ampliar
Las imágenes se entregan a **800 × 1.000** en `nacimiento` y a **1.200 × 675**
en el resto. Se permite ampliar con remuestreo de calidad (Lanczos) y unsharp ligero. WebP
(quality 90-92, method 6) a esas cotas. El nombre de archivo de la imagen es el del post. **No se menciona la resolución en el post**: es nota de trabajo y
pertenece al chat (§ 9.1). Queda derogado «no se amplían / resolución nativa». El 678 era errata.

### 7.7 Fuentes limpias con licencia, preferentes
Cuando la misma imagen existe en una copia realojada con marca de agua y en un
repositorio con licencia libre verificada (p. ej. Wikimedia Commons con permiso
VRT), se prefiere el archivo limpio y se acredita al autor en el pie («Foto:
Andrés Dallimonti, Airliners.net, vía Wikimedia Commons»). La licencia y la
fecha de la toma se toman de la ficha del repositorio, no de copias de terceros
(precedente: el HK-4374X del vuelo 708, 12 de agosto de 2026).

---

## 8. Política de fuentes

### 8.1 Jerarquía
1. institucionales / primarias;
2. museos / archivos / organismos;
3. medios serios y especializados;
4. fuentes secundarias de contraste.

El **borrador preliminar aportado por el editor queda fuera de la jerarquía**
desde el 16 de agosto de 2026: es un insumo de trabajo opcional, no preferible,
y no se cita en el post. Véase § 8.3.

### 8.2 Pertinencia
No arrastrar fuentes de una efeméride a otra salvo relevancia directa.

### 8.3 El borrador preliminar no es fuente

El borrador que aporta el editor procede de modelos generativos que han
introducido fechas equivocadas, cifras inexactas y atribuciones inventadas. Es
un **punto de partida opcional**, nunca un respaldo.

- No se cita en los metadatos ni en ninguna sección del post.
- Cada dato que aporte se verifica en fuente publicada, y se cita **esa** fuente.
- Las discrepancias entre el borrador y la investigación se comunican al editor
  por chat (§ 9.1).

Queda derogada la fórmula «borrador preliminar del investigador» como fuente de
contraste en «Metadatos de Control».

### 8.4 Mínimo de cuatro referencias

Todo post lleva **al menos cuatro referencias verificadas**, y al menos dos de
ellas primarias o institucionales. El borrador no computa.

Motivo: tres efemérides consecutivas se publicaron con solo dos referencias, un
aparato documental demasiado estrecho para el rigor que el proyecto exige y para
que el lector pueda contrastar lo que lee.

### 8.5 Verificación mínima
Toda URL debe corresponder verdaderamente al tema del post.

### 8.6 Verificación de contenido, no de disponibilidad
Que un enlace responda no significa que diga lo que se le atribuye. La
comprobación válida es la del **contenido**: hay que leer la página y confirmar
que su título, su leyenda y sus datos catalográficos corresponden al sujeto de la
efeméride.

La cautela se extrema en las fichas de archivo, museo o biblioteca identificadas
por códigos correlativos —Library of Congress, Imperial War Museums, National
Archives, museos de fuerzas aéreas, hemerotecas digitalizadas—, donde un dígito
equivocado devuelve una ficha impecable y ajena al asunto. Deben confirmarse el
título de la propia ficha, el identificador digital, la fecha y, cuando la haya, la
imagen misma.

Vale para cualquier destino: referencia, enlace del cuerpo, `href` del `<figure>` y
origen de una imagen descargada. Un enlace mal verificado en el `<figure>` es el
más grave de todos, porque presenta al lector una imagen bajo una identidad que no
le pertenece.

---

## 9. Nota aclaratoria

Debe usarse cuando haga falta proteger la precisión editorial:
- discrepancias de fechas;
- cifras conflictivas;
- identidad incompleta de aparato o persona;
- imagen representativa;
- diferencia entre previsión y ejecución real;
- fundación vs inauguración vs activación;
- reclamaciones de combate vs derribos confirmados.

Formato:

```html
<div class="note-box">
  <p><strong>Nota aclaratoria:</strong> [Texto].</p>
</div>
```

### 9.1 Principio de documento limpio

El post se dirige al lector y contiene el **resultado** de la investigación. El relato
del proceso pertenece al chat con el editor.

**Fuera del post, siempre:**
- las comprobaciones rutinarias del flujo de trabajo, como la verificación de
  coherencia entre fecha, título, nombre de archivo y YAML;
- los errores del borrador preliminar del investigador;
- los enlaces que devolvieron 403, 404 o bloqueo anti-bot;
- las sustituciones de fuentes o imágenes por problemas de acceso;
- cualquier referencia al entorno técnico de trabajo.

**Dentro del post, cuando aporte valor al lector:**
- la divergencia entre fuentes publicadas y solventes (cifras, fechas, husos);
- la advertencia de que una imagen es representativa y no exacta.

**Al editor, por chat:** las discrepancias detectadas respecto al borrador y los
enlaces inaccesibles, estos últimos **solo después de haber buscado sin éxito un
reemplazo equivalente**, para que pueda facilitar una fuente alternativa.

Regla práctica: *si interesa a quien lee, va al post; si solo interesa a quien
produce, va al chat.*

---

## 10. Metadatos de Control

### Fórmula derogada
**No** debe emplearse ya, en ninguna forma:
- ~~`borrador preliminar del investigador`~~

El borrador del editor no se cita entre las fuentes (§ 8.3).

### Campo «Discrepancias resueltas»
Recoge **únicamente** divergencias entre fuentes publicadas: cifras que no coinciden
entre instituciones, fechas alternativas, husos horarios, denominaciones. Nunca
errores del borrador, enlaces caídos ni incidencias del entorno (§ 9.1).

Tampoco recoge las **comprobaciones rutinarias del procedimiento**. La fórmula
«se verificó la coherencia entre la fecha del hecho, el título, el nombre del
archivo y el YAML» queda proscrita del post: esa verificación es obligatoria,
pero forma parte de la lista de control interna y el lector la da por supuesta.

Si no se detectó ninguna divergencia entre fuentes, el campo se omite en lugar
de rellenarse con trámites del flujo de trabajo.

### Nivel de confianza
- **Alto:** núcleo del hecho fuertemente respaldado.
- **Medio:** hecho principal sólido, pero con matices abiertos.
- **Bajo:** insuficiencia documental o alta inestabilidad de fuentes.

La línea se escribe desnuda («Alto») cuando existen fuentes primarias o
institucionales consultadas. **Única y exclusivamente** cuando no se pudieron
consultar fuentes primarias y aun así se asigna Alto, se explicita el
fundamento: «núcleo del hecho respaldado por convergencia de fuentes
secundarias independientes; sin fuentes primarias accesibles». Precisión del
investigador (14 de agosto de 2026).

---

## 11. Flujo de trabajo recomendado

1. Leer la solicitud y detectar si pide post, snippet, figura o commit.
2. Investigar el núcleo factual.
3. Verificar imagen y enlaces.
4. Redactar el post o el snippet exacto solicitado.
5. Hacer lectura completa del archivo final.
6. Presentar el resultado.
7. Esperar revisión del editor.
8. Solo después, proponer el commit final.

---

## 12. Compromisos editoriales recientes ya consolidados

- explicar al editor, por chat, cuando una imagen concreta no pudo utilizarse;
- mantener el post limpio de incidencias del proceso de investigación (§ 9.1);
- respetar ediciones manuales del editor en el repo;
- usar enlaces HTML sin subrayado;
- no repetir la misma URL en los enlaces cruzados, admitiendo varios distintos si son pertinentes;
- evitar URLs públicas inferidas de posts no publicados;
- capitalizar grados militares;
- no citar el borrador preliminar entre las fuentes del post (§ 8.3);
- entregar cada post con cuatro referencias verificadas como mínimo (§ 8.4);
- no regenerar un post entero cuando el editor solo pidió snippet o commit.

---

## 13. Errores que deben evitarse

- mezclar datos de efemérides distintas;
- copiar referencias ajenas al tema;
- presentar imágenes representativas como si fueran exactas;
- pelear con la edición manual del editor;
- dar commits prematuros antes de la revisión;
- introducir enlaces internos innecesarios;
- atribuir el cabeceo al eje vertical (es rotación en torno al transversal o lateral; el vertical es el de la guiñada) (§ 4.7);
- llenar el texto de cifras sin jerarquía narrativa;
- relatar en el post los errores del borrador, los enlaces caídos o las
  sustituciones de fuentes motivadas por problemas de acceso (§ 9.1);
- citar el borrador preliminar entre las fuentes de contraste (§ 8.3);
- cerrar un post con menos de cuatro referencias verificadas (§ 8.4);
- tratar la descripción libre de una ficha de repositorio colaborativo como si
  fuera una fuente publicada en discrepancia (§ 8.6);
- redondear a la baja los años transcurridos desde el hito, o calcularlos
  sobre un año de publicación distinto del real (§ 5.7).
- dar por buena una URL porque responde, sin comprobar que su contenido
  corresponde al sujeto de la efeméride (§ 8.6);
- enlazar en el `<figure>` una ficha de archivo que retrata a otra persona,
  aeronave o lugar.
- construir enlaces internos con la fecha unida por guiones
  (`/nacimiento/1897-01-06/…`) en lugar de la URL canónica con barras
  (§ 6.3);
- incluir en el post líneas de estado del documento o notas sobre resolución de
  imágenes (§ 9.1).
- escribir en minúscula un grado, una jerarquía de aviación o un tratamiento honorífico que precede inmediatamente a un nombre propio (§ 4.3);
- capitalizar cargos u oficios civiles ante nombre propio, o escribir en minúscula el plural de grado que encabeza una lista de nombres (§ 4.3, decisiones D1-a y D2-a de 2026-09-03);

---

## 14. Checklist breve del Editor Senior

- [ ] ¿El hecho principal está cerrado?
- [ ] ¿La imagen está bien atribuida?
- [ ] ¿Los enlaces del cuerpo respetan el estilo visual?
- [ ] ¿Cada enlace cruzado aparece una sola vez y ninguno apunta al propio post?
- [ ] ¿La nota aclaratoria protege contra malentendidos?
- [ ] ¿El post está limpio de menciones al borrador, a enlaces caídos y al entorno técnico?
- [ ] ¿Los años transcurridos desde el hito coinciden con la resta entre el año de publicación y el del hecho?
- [ ] ¿Se leyó el contenido de cada ficha de archivo enlazada y corresponde al sujeto?
- [ ] ¿Todos los enlaces internos usan la URL canónica con barras, sin guion terminal en el slug?
- [ ] ¿Queda fuera del post toda línea de estado del documento y toda nota de resolución de imagen?
- [ ] ¿El post tiene al menos cuatro referencias verificadas, dos de ellas primarias o institucionales?
- [ ] ¿Los metadatos evitan citar el borrador preliminar como fuente de contraste?
- [ ] ¿Los metadatos reflejan honestamente el nivel de certeza?
- [ ] ¿Se respetó exactamente lo que el editor pidió en esta ronda?

---

## 15. Cierre

Este manual debe leerse como documento de síntesis: no sustituye a la plantilla maestra ni a las instrucciones operativas, pero sí fija el criterio editorial para resolver dudas y mantener coherencia en la producción futura de efemérides.

---

## 16. Actualizaciones editoriales v1.1 — 2026-07-28

- Todo post debe conservar divisores `<hr>` antes de cada sección principal.
- Las categorías incluyen `conmemoracion` y `[espacial, accidente]`, con degradados definidos en la plantilla maestra.
- La regla de enlaces cruzados prohíbe repetir la misma URL o enlazar el post consigo mismo, pero permite enlaces distintos y pertinentes.
- El timestamp debe ser dinámico, local y no reutilizado.
- La fecha del hecho, el título, el archivo, el YAML y la URL pública deben ser coherentes.
- Las imágenes representativas deben identificarse con precisión; nunca deben presentarse como exactas.
- Las notas y metadatos no deben narrar cambios internos del flujo de trabajo.
- El commit inicial se entrega únicamente tras solicitud expresa y no menciona imágenes.
- Las cifras usan punto para miles, coma para decimales y conversiones métricas cuando corresponda.
---

## 17. Actualizaciones editoriales v1.2 — 2026-07-29

### Corrección de coherencia sobre enlaces cruzados
Se detectaron en este manual dos formulaciones heredadas de la versión
anterior que contradecían la regla vigente desde la v2.1 del resto de
documentos rectores. Han sido corregidas:

- En el punto 12, «limitar a un solo enlace cruzado cuando sea suficiente»
  se sustituye por la prohibición de repetir la misma URL.
- En el punto 14, la comprobación «¿Hay una sola conexión interna…?» se
  sustituye por la verificación de que cada enlace aparezca una sola vez y
  ninguno apunte al propio post.

### Criterio unificado vigente
- Una misma URL, una sola vez por post.
- Pueden emplearse varios enlaces cruzados distintos si son pertinentes.
- Nunca debe enlazarse una efeméride consigo misma.
- Solo se enlazan efemérides realmente publicadas, con su URL pública real.
- Ubicación preferente en `## Desarrollo Cronológico`.
---

## 18. Actualizaciones editoriales v1.5 — 2026-08-04

### Cómputo de años transcurridos

Se incorpora el apartado 5.7. Las efemérides se publican el mismo día y mes del
hito, de modo que la distancia temporal es un número entero exacto de años que se
obtiene restando el año del hecho al año de publicación, tomado del campo
`fecha_publicacion` del borrador.

Motivo: en la efeméride de Nagasaki del 9 de agosto de 1945, prevista para
publicación el 9 de agosto de 2026, el borrador de salida decía «ochenta años
después» cuando la cifra correcta era **ochenta y uno**. El redondeo a la cifra
redonda es un error recurrente que debe verificarse al cierre.

Se añaden en consecuencia una entrada en el punto 13 (errores que deben evitarse)
y una comprobación en el punto 14 (checklist del Editor Senior).
---

## 19. Actualizaciones editoriales v1.6 — 2026-08-05

### Verificación de contenido de las fuentes

Se incorpora el apartado 8.4 y un nuevo 7.3 sobre la identidad del sujeto
retratado. Un código de respuesta 200 acredita que la página existe, no que trate
del asunto de la efeméride: la verificación debe recaer sobre el contenido —título
de la ficha, identificador digital, fecha e imagen—, con exigencia extrema en los
repositorios de identificadores correlativos.

Motivo: en la efeméride del nacimiento de Hugo Eckener se enlazó en el `<figure>`
una ficha de la Library of Congress que respondía correctamente pero correspondía a
un retrato de Stanley Baldwin y su familia. El error llegó hasta la revisión del
editor porque la comprobación se había limitado a la disponibilidad del enlace.

Se añaden en consecuencia dos entradas en el punto 13 (errores que deben evitarse)
y una comprobación en el punto 14 (checklist del Editor Senior). La numeración del
antiguo 7.3 pasa a 7.4 y la del antiguo 7.4 a 7.5.
---

## 20. Actualizaciones editoriales v1.7 — 2026-08-09

- § 4.3 se refuerza con ejemplos de grados seguidos del nombre y con la regla de
  minúscula para cargos civiles (motivo: el error de los «tenientes» en la
  efeméride del 14 de julio de 1938).
- § 4.4 nuevo: alusiones al investigador y al editor. *(Hoy § 4.5, tras la inserción de § 4.4 «Siglas y acrónimos».)*
- § 7.6 nuevo: las imágenes no se amplían; se entregan a resolución nativa sin
  nota de resolución en el post. *(Derogado en la v1.11: se entregan al tamaño
  de casa y se permite ampliar con remuestreo de calidad. Véase § 7.6 vigente.)*
- § 13 y § 14: se añaden los errores y comprobaciones de enlaces internos con
  fecha en guiones y de líneas de estado o resolución en el post.

Motivo general: reglas acordadas entre el investigador y el editor en las
sesiones del 8 y 9 de agosto de 2026.
---

## 21. Actualizaciones editoriales v1.8 — 2026-08-12

### Grados de la aviación junto al nombre propio
Se extiende la regla de mayúsculas de grados militares a las jerarquías de la
aviación civil: *Capitán* y *Primer Oficial* con mayúscula inicial cuando
acompañan al nombre propio; en minúscula sin él. Precisión del investigador en
la ronda del vuelo 708.

### Títulos con hazaña, hito o cualidad
Nueva sección § 4.6. Los títulos biográficos escuetos quedan proscritos: el
título honra al personaje con su hazaña o cualidad, tomada del contenido
verificado del propio post y sin tocar slug ni URL. Precedente: auditoría de la
categoría `nacimiento` (69 títulos ya enriquecidos, 9 corregidos).

### Series en enlaces cruzados
Se admite en § 6.3 el enlace de series o rankings entre efemérides (primer
accidente, récord superado, tragedia más reciente) siempre que cada enlace
aporte su propio dato. Precedente: la serie venezolana del vuelo 708 (1940,
1944, 1969, 2008).

### Fuentes limpias con licencia
Nueva sección § 7.7: preferencia por el archivo limpio de repositorio con
licencia verificada frente a copias con marca de agua; crédito del autor en el
pie.
---

## 22. Actualizaciones editoriales v1.10 — 2026-08-16

### El borrador preliminar sale de la jerarquía de fuentes
§ 8.1 pierde su quinto escalón y se incorpora § 8.3 (entonces § 8.5): el borrador que aporta el
editor es un insumo opcional, no preferible, procedente de modelos generativos
que introdujeron datos erróneos. No se cita en el post; cada dato que aporte se
verifica y se cita la fuente publicada que lo sostiene. Queda derogada la
fórmula «borrador preliminar del investigador» de § 10.

### Mínimo de cuatro referencias
Nueva § 8.4 (entonces § 8.6): cuatro referencias verificadas como suelo de cada post, dos de
ellas primarias o institucionales. Motivo: los tres posts anteriores al del BAe
Hawk se entregaron con solo dos.

### Descripciones de repositorios colaborativos
Se añade a § 13 el error de tratar la descripción libre de una ficha de
Wikimedia Commons o similar como fuente publicada en discrepancia. Precedente:
la efeméride del BAe Hawk, en la que ese error llevó a suprimir del post el
aeródromo del primer vuelo, dato firmemente establecido.

Se actualizan en consecuencia § 12, § 13 y § 14.
---

## 23. Actualizaciones editoriales v1.11 — 2026-08-20

- § 7.6 se reescribe: tamaño de casa 800 × 1.000 (`nacimiento`) y 1.200 × 675 (resto); se permite ampliar. Errata 678 → 675. Alineado con Plantilla v2.14, regla maestra 12.


---

## 24. Actualizaciones editoriales v1.13 — 2026-08-21

Pasada de **coherencia interna**. No cambia el fondo de ninguna regla.

- **§ 8 renumerada.** Las subsecciones iban 8.1, 8.2, **8.5, 8.6**, 8.3, 8.4:
  las dos reglas incorporadas el 16 de agosto (borrador y mínimo de
  referencias) se insertaron en medio conservando su número alto, y dejaron
  «Verificación mínima» y «Verificación de contenido» descolocadas. Ahora el
  orden es correlativo: **8.3** borrador, **8.4** mínimo de cuatro
  referencias, **8.5** verificación mínima, **8.6** verificación de contenido.
  Se actualizan todas las remisiones internas del manual.
- **Bloques de actualizaciones reordenados.** Estaban en desorden físico
  (v1.7 antes que v1.1) y **dos llevaban el número 23**. Se ordenan
  cronológicamente y se renumeran de forma correlativa.
- **§ 7.6 en el registro de la v1.7.** Aquella entrada seguía enunciando «las
  imágenes no se amplían; resolución nativa», derogado por la v1.11. Se marca
  como superado sin borrar el registro histórico, igual que se hizo en la v1.2
  con los enlaces cruzados.
- **§ 4.4 en el registro de la v1.7.** Se aclara que la regla de alusiones al
  investigador y al editor es hoy § 4.5, tras insertarse § 4.4 «Siglas y
  acrónimos».

Motivo: auditoría de coherencia de los cuatro rectores del 21 de agosto de
2026, paralela a la de la Plantilla Maestra v2.16.

## 25. Actualizaciones editoriales v1.14 — 2026-08-28

Novedad de fondo puntual, acordada por el editor al levantar la moratoria del
21-08-2026 **solo para los rectores afectados** por los hechos del 27 y 28 de
agosto:

- **§ 4.7 nueva, «Ejes y movimientos de la aeronave».** Definiciones
  canónicas alabeo-longitudinal, cabeceo-transversal (lateral),
  guiñada-vertical, y exigencia de contrastar toda asignación
  movimiento↔eje con la definición. Precedente documentado: la corrección
  pospublicación del post del Sageburner (1961-08-28), error detectado por
  tres lectores y no por los lazos internos; commit de corrección del editor
  en la rama.
- **§ 13, nueva viñeta de errores** remitiendo a § 4.7.

Alineadas en la misma fecha: Plantilla Maestra v2.17, Instrucciones de Formato
v2.14 e Instrucciones de Procesar v2.14.

---

## 26. Actualizaciones editoriales v1.15 — 2026-09-03

- **§ 4.3 reescrita** (decisiones D1-a y D2-a del editor, 2026-09-03): la lista de grados militares pasa a ser enunciativa y no cerrada (Subteniente, Alférez, Teniente de Navío, Comodoro…); se codifica el plural de grado ante lista de nombres propios; se regulan por primera vez los tratamientos honoríficos y académicos (mayúscula al preceder inmediatamente al nombre propio) y se confirma la minúscula de los cargos y oficios civiles. Se añade el párrafo de fundamento que documenta la desviación deliberada frente a la pauta RAE.
- **§ 13, dos viñetas nuevas de errores** remitiendo a § 4.3.
- Nuevo anexo normativo citado: `docs/anexo-comparacion-tratamientos-y-rangos.md` (comparación de pautas aportada por el editor el 03-09-2026, reproducida verbatim).

Alineadas en la misma fecha: Plantilla Maestra v2.18 (regla maestra 5) e Instrucciones de Formato v2.15 (apartado de rangos). Instrucciones de Procesar v2.14: sin novedad.
