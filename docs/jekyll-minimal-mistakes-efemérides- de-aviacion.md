markdown
# 🛩️ PROYECTO COMPLETO - Jekyll "Minimal Mistakes" para Efemérides de Aviación

## 📁 INSTRUCCIONES DE USO

1. **Copia TODO este contenido** a un archivo `.md` en tu laptop
2. **Separa cada sección** en los archivos correspondientes según la estructura indicada
3. **Sigue el paso a paso** al final del documento

---

## 🔧 ARCHIVO 1: `_config.yml`

```yaml
# CONFIGURACIÓN PRINCIPAL
title: "Efemérides de Aviación"
subtitle: "Archivo histórico de eventos importantes en aviación mundial"
description: "Blog de efemérides de aviación con más de 100 años de historia"
baseurl: "/efemerides"
url: "https://efemerides-aviacion.github.io"
repository: "efemerides-aviacion/efemerides"

# TEMA
remote_theme: mmistakes/minimal-mistakes
minimal_mistakes_skin: "air"
search: true

# BLOG
permalink: /:categories/:title/
paginate: 12
paginate_path: "/page:num/"
timezone: "America/Mexico"

# AUTOR
author:
  name: "Archivo de Efemérides de Aviación"
  avatar: "/assets/images/avatar.jpg"
  bio: "Recopilación histórica de eventos importantes en aviación"
  links:
    - label: "GitHub"
      icon: "fab fa-github"
      url: "https://github.com/efemerides-aviacion"

# PLUGINS
plugins:
  - jekyll-paginate
  - jekyll-sitemap
  - jekyll-feed
  - jekyll-include-cache

# DEFAULTS
defaults:
  - scope:
      path: ""
      type: posts
    values:
      layout: single
      author_profile: false
      share: true
      related: true
      show_date: true
      read_time: true
      toc: true

# ARCHIVES
category_archive:
  type: liquid
  path: /categorias/

# IMAGES
header:
  image: "/assets/images/banner-aviation.jpg"
  overlay_filter: 0.3

# EXCLUDE
exclude:
  - "*.gem"
  - ".git"
  - "Gemfile"
  - "Gemfile.lock"
🏠 ARCHIVO 2: index.html (en raíz)
html
---
layout: splash
title: "Efemérides de Aviación"
excerpt: "Archivo histórico de eventos importantes en la aviación mundial"
header:
  overlay_image: /assets/images/banner-aviation.jpg
  overlay_filter: 0.5
  overlay_color: "#0056b3"
  actions:
    - label: "Explorar Efemérides"
      url: "/categorias/"
      btn_class: "btn--primary"
  caption: 'Foto: [**NASA**](https://www.nasa.gov)'
---

{% assign featured_post = site.posts | first %}

{% if featured_post %}
<section class="featured-section">
  <h2 class="archive__subtitle">Efeméride Destacada</h2>
  <div class="featured-post">
    <article class="archive__item">
      <div class="archive__item-teaser">
        <img src="{% if featured_post.header.image %}{{ featured_post.header.image }}{% else %}/assets/images/default-aviation.jpg{% endif %}" 
             alt="{{ featured_post.title }}">
        <div class="archive__item-date">
          <span class="archive__item-day">{{ featured_post.date | date: "%d" }}</span>
          <span class="archive__item-month">{{ featured_post.date | date: "%b" }}</span>
        </div>
      </div>
      <div class="archive__item-body">
        <div class="archive__item-category">
          {% for category in featured_post.categories %}
            <span class="badge badge--{{ category | slugify }}">{{ category }}</span>
          {% endfor %}
        </div>
        <h3 class="archive__item-title">
          <a href="{{ featured_post.url }}">{{ featured_post.title }}</a>
        </h3>
        <div class="archive__item-excerpt">
          {{ featured_post.excerpt | markdownify | strip_html | truncate: 200 }}
        </div>
        <a href="{{ featured_post.url }}" class="btn btn--primary">Leer completa →</a>
      </div>
    </article>
  </div>
</section>
{% endif %}

<section class="recent-posts">
  <h2 class="archive__subtitle">Efemérides Recientes</h2>
  <div class="grid__wrapper">
    {% for post in paginator.posts limit:12 %}
      {% include archive-single.html type="grid" %}
    {% endfor %}
  </div>
  
  {% if paginator.total_pages > 1 %}
    <div class="pagination">
      {% if paginator.previous_page %}
        <a href="{{ paginator.previous_page_path }}" class="pagination--pager">
          ← Anteriores
        </a>
      {% endif %}
      
      <span class="pagination__info">
        Página {{ paginator.page }} de {{ paginator.total_pages }}
      </span>
      
      {% if paginator.next_page %}
        <a href="{{ paginator.next_page_path }}" class="pagination--pager">
          Siguientes →
        </a>
      {% endif %}
    </div>
  {% endif %}
</section>
📄 ARCHIVO 3: about.md
markdown
---
layout: single
title: "Acerca de"
permalink: /about/
header:
  overlay_image: /assets/images/about-banner.jpg
  overlay_filter: 0.5
  excerpt: "Conoce la historia y propósito de este archivo"
---

## 📖 Sobre este Proyecto

**Efemérides de Aviación** es un archivo digital dedicado a preservar y compartir los eventos históricos más importantes de la aviación mundial.

### 🎯 Nuestra Misión
1. **Preservar** el legado histórico de la aviación
2. **Educar** sobre hitos y lecciones aprendidas
3. **Honrar** a quienes contribuyeron al desarrollo aeronáutico

## 📊 Datos del Archivo
- **Total de efemérides:** {{ site.posts | size }}
- **Rango temporal:** 1783 - Actualidad
- **Actualización:** Diaria

## 📞 Contacto
- **Email:** efemerides.aviacion@gmail.com
- **GitHub:** [efemerides-aviacion](https://github.com/efemerides-aviacion)

---

*"La aviación prueba que tenemos la capacidad para lograr lo imposible."*  
— Eddie Rickenbacker
📦 ARCHIVO 4: Gemfile
ruby
source "https://rubygems.org"

gem "github-pages", group: :jekyll_plugins
gem "minimal-mistakes-jekyll"
gem "jekyll-include-cache"
gem "jekyll-sitemap"
gem "jekyll-feed"

group :development do
  gem "webrick"
end
🎨 ARCHIVO 5: _sass/custom.scss
scss
// COLORES AERONÁUTICOS
$aviation-blue: #0056b3;
$aviation-red: #e63946;
$aviation-yellow: #ffd700;

// POST DESTACADO
.featured-post {
  margin-bottom: 3em;
  border: 2px solid $aviation-blue;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 86, 179, 0.2);
  
  .archive__item-teaser {
    height: 300px;
    overflow: hidden;
    
    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
  }
  
  .archive__item-date {
    position: absolute;
    top: 20px;
    right: 20px;
    background: $aviation-red;
    color: white;
    padding: 10px;
    border-radius: 5px;
    text-align: center;
    min-width: 70px;
  }
  
  .archive__item-body {
    padding: 2em;
  }
}

// GRID DE EFEMÉRIDES
.grid__wrapper {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2em;
  margin: 2em 0;
}

.archive__item {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  overflow: hidden;
  transition: all 0.3s ease;
  
  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
    border-color: $aviation-blue;
  }
  
  .archive__item-teaser {
    height: 180px;
    
    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
  }
  
  .archive__item-body {
    padding: 1.5em;
  }
}

// BADGES
.badge {
  display: inline-block;
  padding: 0.25em 0.75em;
  border-radius: 20px;
  font-size: 0.75em;
  font-weight: bold;
  margin-right: 0.5em;
  
  &--accidentes-aereos {
    background-color: lighten($aviation-red, 40%);
    color: darken($aviation-red, 20%);
  }
  
  &--aviacion-evento {
    background-color: lighten($aviation-blue, 40%);
    color: darken($aviation-blue, 20%);
  }
}

// PAGINACIÓN
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 3em 0;
  gap: 2em;
  
  &--pager {
    padding: 0.75em 1.5em;
    border: 2px solid $aviation-blue;
    border-radius: 25px;
    color: $aviation-blue;
    text-decoration: none;
    
    &:hover {
      background: $aviation-blue;
      color: white;
    }
  }
}
📋 ARCHIVO 6: _data/navigation.yml
yaml
main:
  - title: "Inicio"
    url: /
  - title: "Categorías"
    url: /categorias/
  - title: "Acerca de"
    url: /about/
📝 ARCHIVO 7: Plantilla de Efeméride (_posts/2024-01-16-ejemplo.md)
markdown
---
layout: single
title: "16 de enero de 2017 | Accidente del Vuelo 6491 de Turkish Airlines Cargo"
date: 2017-01-16
categories: 
  - accidentes-aereos
  - cargo
tags:
  - Turkish Airlines
  - Boeing 747
  - Kirguistán
excerpt: "Un Boeing 747-400F de Turkish Airlines Cargo se estrelló cerca del aeropuerto de Manas..."
header:
  image: /assets/images/turkish-airlines-6491.jpg
  caption: "Boeing 747-400F de Turkish Airlines Cargo"
sidebar:
  - title: "Fecha"
    text: "16 de enero de 2017"
  - title: "Lugar"
    text: "Aeropuerto de Manas, Kirguistán"
  - title: "Aeronave"
    text: "Boeing 747-400F"
  - title: "Operador"
    text: "Turkish Airlines Cargo"
---

## Contexto del Vuelo

El **Vuelo 6491 de Turkish Airlines Cargo** era un vuelo de carga regular...

## Cronología

- **00:25 UTC:** Despegue de Hong Kong
- **04:40 UTC:** Contacto con control de Biskek
- **04:44 UTC:** Impacto en zona residencial

## Lecciones Aprendidas

1. Revisión de procedimientos para vuelos nocturnos
2. Implementación de EGPWS actualizado
3. Consideración de fatiga de tripulación

---

*Última actualización: {{ page.date | date: "%d/%m/%Y" }}*
⚙️ ARCHIVO 8: .github/workflows/jekyll.yml
yaml
name: "Build Jekyll site"

on:
  push:
    branches: ["main"]
  schedule:
    - cron: '0 8 * * *'

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout
      uses: actions/checkout@v4
    
    - name: Setup Ruby
      uses: ruby/setup-ruby@v1
    
    - name: Build with Jekyll
      uses: actions/jekyll-build-pages@v1
    
    - name: Upload artifact
      uses: actions/upload-pages-artifact@v2
🚀 ARCHIVO 9: 404.md
markdown
---
layout: single
title: "404 - Página no encontrada"
permalink: /404.html
header:
  overlay_image: /assets/images/404-banner.jpg
  overlay_filter: 0.5
excerpt: "La efeméride que buscas no está disponible."
---

## ✈️ ¡Ups! Te has perdido en las nubes...

La página que buscas no existe o ha sido movida.

### 📍 ¿Qué puedes hacer?
1. **Usa el buscador** en la parte superior
2. **Explora por categorías**
3. **Vuelve al [inicio](/)** 

---

*✈️ [Volver al inicio](/)*
📁 ESTRUCTURA FINAL DE CARPETAS
text
tu-repositorio/
├── _config.yml                    # 1. Configuración principal
├── index.html                     # 2. Página de inicio
├── about.md                       # 3. Página Acerca de
├── 404.md                         # 9. Página 404
├── Gemfile                        # 4. Dependencias
├── _sass/
│   └── custom.scss                # 5. Estilos personalizados
├── _data/
│   └── navigation.yml             # 6. Navegación
├── _posts/
│   ├── 2024-01-16-ejemplo.md      # 7. Plantilla de efeméride
│   └── (tus efemérides aquí)
├── .github/workflows/
│   └── jekyll.yml                 # 8. Despliegue automático
└── assets/images/
    ├── banner-aviation.jpg
    ├── default-aviation.jpg
    └── (tus imágenes aquí)
🚀 PASO A PASO PARA IMPLEMENTAR
Paso 1: Crear estructura en tu laptop
bash
# Crea estas carpetas en un directorio nuevo
mkdir -p efemerides-aviation
cd efemerides-aviation
mkdir -p _sass _data _posts assets/images .github/workflows
Paso 2: Copiar cada archivo desde este documento
Abre un editor de texto (VS Code, Notepad++, etc.)

Busca cada sección que dice "ARCHIVO X:"

Copia el contenido entre los yaml,html, etc.

Pega en el archivo correspondiente

Paso 3: Orden de creación de archivos
Crea estos archivos en este orden:

_config.yml - Configuración principal

index.html - Página de inicio

about.md - Página Acerca de

Gemfile - Dependencias

_sass/custom.scss - Estilos

_data/navigation.yml - Navegación

_posts/ejemplo.md - Plantilla

.github/workflows/jekyll.yml - Despliegue

404.md - Página 404

Paso 4: Preparar imágenes
Descarga 2-3 imágenes de aviación

Ponlas en assets/images/

Nómbralas: banner-aviation.jpg, default-aviation.jpg

Paso 5: Configurar GitHub
bash
# Inicializar repositorio git
git init
git add .
git commit -m "Inicializando blog de efemérides de aviación"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/efemerides.git
git push -u origin main
Paso 6: Activar GitHub Pages
Ve a tu repositorio en GitHub

Settings → Pages

Source: GitHub Actions

Espera 1-2 minutos para el primer despliegue

Paso 7: Añadir tus efemérides
Copia todos tus archivos .md a la carpeta _posts/

Asegúrate que siguen el formato: YYYY-MM-DD-titulo.md

Cada efeméride debe tener el "front matter" como en la plantilla

⚡ COMANDOS RÁPIDOS PARA TERMINAL
bash
# Para probar localmente (si tienes Ruby instalado)
gem install bundler jekyll
bundle install
bundle exec jekyll serve

# Tu sitio estará en: http://localhost:4000
🔧 SOLUCIÓN DE PROBLEMAS COMUNES
❌ Error: "Theme mmistakes/minimal-mistakes not found"
yaml
# Cambia en _config.yml:
remote_theme: mmistakes/minimal-mistakes@4.24.0
❌ Error: "Could not locate Gemfile"
bash
# Ejecuta desde la carpeta correcta
cd efemerides-aviation
bundle install
❌ Error: Las imágenes no se muestran
Verifica las rutas en los posts

Usa rutas relativas: /assets/images/nombre.jpg

Sube las imágenes a GitHub

❌ Error: GitHub Pages no se despliega
Revisa Actions en tu repositorio GitHub

Mira los logs del workflow

Verifica que _config.yml no tiene errores de sintaxis

📱 RESULTADO FINAL
Tu blog tendrá:

✅ Post destacado grande arriba con imagen

✅ Grid de tarjetas con imágenes para efemérides anteriores

✅ Diseño responsive que funciona en móvil y desktop

✅ Categorías organizadas por tipo de evento

✅ Despliegue automático cada vez que subas contenido

✅ Búsqueda integrada para encontrar efemérides

🆘 SOPORTE RÁPIDO
Si tienes problemas:

Copia y pega el error que ves

Verifica que todos los archivos están en las carpetas correctas

Asegúrate que las fechas en los posts son YYYY-MM-DD

Las imágenes deben estar en assets/images/

✅ CHECKLIST FINAL
Todos los archivos creados en sus carpetas

_config.yml configurado con tus datos

Imágenes en assets/images/

Posts en _posts/ con formato correcto

Repositorio subido a GitHub

GitHub Pages activado

Primer despliegue exitoso

🎉 ¡Listo! Tu blog de efemérides de aviación está listo para volar.

Cada vez que añadas una nueva efeméride en _posts/, GitHub Actions la publicará automáticamente en 1-2 minutos.

¿Necesitas ayuda con algún paso específico?

text

---

## 📥 **CÓMO USAR ESTE ARCHIVO ÚNICO**

1. **Copia TODO** el contenido de arriba (desde `# 🛩️ PROYECTO COMPLETO` hasta el final)
2. **Pégalo** en un archivo nuevo llamado `PROYECTO-COMPLETO.md` en tu laptop
3. **Ve sección por sección** creando cada archivo
4. **Sigue el paso a paso** final

¡Así tienes todo en un solo lugar para referencia rápida!
