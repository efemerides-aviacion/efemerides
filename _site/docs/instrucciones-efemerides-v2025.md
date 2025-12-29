# Documento de Instrucciones Editoriales para Efemérides de Aviación
> Última actualización: 2025-12-29

---

## PRINCIPIO FUNDAMENTAL DE INTEGRIDAD
**Regla de oro:** Solo incluir información verificada en fuentes confiables. La ausencia de datos es preferible a la invención o deducción.

---

## CRITERIO DE SUSPENSIÓN
Si no se encuentran al menos 2 fuentes primarias verificables que confirmen fecha, lugar, protagonistas y aeronave, se detiene la generación y se reporta:

> "Información insuficiente para generar efeméride verificable. Datos faltantes: [especificar]. Se requiere investigación adicional."

---

## FASE DE INVESTIGACIÓN PREVIA
1. Buscar fuentes primarias recientes.  
2. Verificar datos críticos contra al menos 3 fuentes independientes.  
3. Resolver discrepancias en fechas, nombres y cifras.  
4. Documentar actualizaciones relevantes.  
5. Insertar URL directo y funcional en la sección de referencias.  
6. Validar imágenes contra repositorios históricos.  
7. Documentar explícitamente los datos no verificados.  

---

## ESTRUCTURA OBLIGATORIA DEL DOCUMENTO

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

2. **Bloque de imagen**  
   ```html
   <figure>
     <img class="post-image" src="{{ site.baseurl }}/assets/img/[imagen].jpg" alt="[Tema]">
     <figcaption class="post-caption">[Descripción de la imagen]</figcaption>
   </figure>
   ```

3. **Resumen ejecutivo**  
   - 3–4 líneas máximo, solo datos verificados.  

4. **Datos técnicos e históricos**  
   - Lista fluida con indicadores de certeza: [VERIFICADO], [FUENTE ÚNICA], [NO CONFIRMADO].  

5. **Cuerpo principal – Secciones temáticas**  
   - Contexto histórico  
   - Desarrollo cronológico de los hechos  
   - Consecuencias e impacto  
   - Estado actual / legado  

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
