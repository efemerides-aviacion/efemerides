---
layout: default
title: "Índice de países"
---

<style>
  .indice-paises { max-width: 940px; margin: 0 auto; padding: 24px 16px 48px; }
  .indice-paises h1 { color: #0f2740; }
  .indice-paises h2 { border-bottom: 2px solid #1565c0; padding-bottom: 4px; margin-top: 2.2rem; color: #0f2740; }
  .indice-paises ul { list-style: none; padding-left: 0; }
  .indice-paises li { padding: 4px 0; border-bottom: 1px dotted #ddd; }
  .indice-paises a { color: #315fea; text-decoration: none; }
  .indice-paises a:hover { text-decoration: underline; }
  .indice-paises .volver { display: inline-block; margin-bottom: 1rem; font-weight: 600; }
</style>

<div class="indice-paises">
<a class="volver" href="{{ '/' | relative_url }}">&larr; Volver al archivo</a>
<h1>Índice de países</h1>
<p>Cada efeméride figura bajo <strong>todos</strong> los países de su campo <code>pais</code>: las entradas de más de un país aparecen en cada una de sus secciones. Las secciones se generan al publicar a partir de los propios valores de <code>pais</code>, de modo que toda efeméride futura aparece automáticamente bajo su país.</p>

{%- comment -%} 1) Tokens de país: separar, limpiar y normalizar {%- endcomment -%}
{%- assign crudo = "" -%}
{%- for post in site.posts -%}
  {%- assign crudo = crudo | append: post.pais | append: "||" | downcase -%}
{%- endfor -%}
{%- comment -%} Frases compuestas con «y» que son un solo país: se protegen antes de separar {%- endcomment -%}
{%- assign crudo = crudo | replace: "antigua y barbuda", "antigua·barbuda" | replace: "bosnia y herzegovina", "bosnia·herzegovina" | replace: "trinidad y tobago", "trinidad·tobago" | replace: "san cristóbal y nieves", "san cristóbal·nieves" | replace: "san vicente y las granadinas", "san vicente·las granadinas" -%}
{%- assign piezas = crudo | replace: ";", "||" | replace: "/", "||" | replace: ",", "||" | replace: "-", "||" | replace: " y ", "||" | split: "||" -%}
{%- assign limpio = "" -%}
{%- for pieza in piezas -%}
  {%- assign t = pieza | split: "(" | first | remove: "[" | remove: "]" | remove: '"' | remove: "'" | replace: "·", " y " | strip -%}
  {%- if t != "" -%}{%- assign limpio = limpio | append: t | append: "||" -%}{%- endif -%}
{%- endfor -%}
{%- assign tokens = limpio | split: "||" | uniq | sort -%}

{%- comment -%} 2) Alias: variantes que se agrupan bajo un mismo país {%- endcomment -%}
{%- assign grupos = "" -%}
{%- for t in tokens -%}
  {%- assign g = t -%}
  {%- case t -%}
    {%- when "inglaterra" %}{% assign g = "reino unido" %}
    {%- when "república federal de alemania" %}{% assign g = "alemania occidental" %}
  {%- endcase -%}
  {%- assign grupos = grupos | append: g | append: "||" -%}
{%- endfor -%}
{%- assign grupos = grupos | split: "||" | uniq | sort -%}

{%- comment -%} 3) Secciones: recuento y listado por grupo {%- endcomment -%}
{%- for g in grupos -%}
  {%- case g -%}
    {%- when "reino unido" %}{% assign alternas = "reino unido||inglaterra" %}
    {%- when "alemania occidental" %}{% assign alternas = "alemania occidental||república federal de alemania" %}
    {%- else %}{% assign alternas = g %}
  {%- endcase -%}
  {%- assign alts = alternas | split: "||" -%}
  {%- capture etiqueta -%}
    {%- case g -%}
      {%- when "estados unidos" %}Estados Unidos
      {%- when "reino unido" %}Reino Unido
      {%- when "unión soviética" %}Unión Soviética
      {%- when "países bajos" %}Países Bajos
      {%- when "nueva zelanda" %}Nueva Zelanda
      {%- when "emiratos árabes unidos" %}Emiratos Árabes Unidos
      {%- when "corea del norte" %}Corea del Norte
      {%- when "imperio ruso" %}Imperio Ruso
      {%- when "imperio alemán" %}Imperio Alemán
      {%- when "alemania occidental" %}Alemania Occidental
      {%- when "francia libre" %}Francia Libre
      {%- when "vietnam del sur" %}Vietnam del Sur
      {%- else %}{{ g | capitalize }}
    {%- endcase -%}
  {%- endcapture -%}
  {%- capture lista_html -%}
    {%- for post in site.posts -%}
      {%- assign pl = post.pais | default: "" | downcase -%}
      {%- assign ok = false -%}
      {%- for alt in alts -%}
        {%- if pl contains alt %}{% assign ok = true %}{% endif -%}
      {%- endfor -%}
      {%- if ok %}
  <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
      {%- endif %}
    {%- endfor -%}
  {%- endcapture -%}
  {%- assign n = lista_html | split: "<li>" | size | minus: 1 -%}
  {%- if n > 0 %}
  <h2>{{ etiqueta | strip }} ({{ n }})</h2>
  <ul>
  {{ lista_html }}
  </ul>
  {%- endif %}
{%- endfor -%}
</div>
