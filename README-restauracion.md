# Restauración de Efemérides

## Contexto
Durante la revisión del repositorio se detectó que los enlaces a los posts de efemérides arrojaban error 404 en GitHub Pages. El problema se originó tras una modificación en el archivo `_layouts/post.html`, que afectó la forma en que Jekyll generaba las páginas individuales.

## Commit estable
- **Hash:** `91f5ae0`  
- **Estado:** Último commit en el que los posts se renderizan correctamente.  
- **Acción:** Se usó como base para crear la rama `restauracion-efemerides-3`.

## Commit problemático
- **Hash:** `6499fa1`  
- **Mensaje:** *Se modificó el footer del post.html*  
- **Archivo afectado:** `_layouts/post.html`  
- **Cambio realizado:** Se eliminó la línea `{{ page.author }}` del pie de página.  
- **Efecto:** Rompió la compilación y generó errores 404 en todos los posts.

## Solución aplicada
- Se creó la rama `restauracion-efemerides-3` a partir del commit estable (`91f5ae0`).  
- Se configuró GitHub Pages para compilar desde esta rama.  
- Los posts volvieron a renderizarse correctamente.

## Próximos pasos
- Evitar reintroducir cambios en `_layouts/post.html` sin revisión técnica.  
- Documentar cualquier modificación futura en layouts para asegurar que no afecte la compilación.  
- Mantener esta rama como referencia editorial y técnica para restauraciones futuras.
