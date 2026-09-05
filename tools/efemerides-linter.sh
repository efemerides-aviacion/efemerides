#!/usr/bin/env bash
# ============================================================================
# efemerides-linter.sh — Validador estructural de posts de efemérides
# Normas auditadas: Plantilla Maestra v2.18 · Manual de Estilo v1.15 ·
# Instrucciones de Procesar v2.14 · Instrucciones de Formato v2.15 ·
# anexo y registro de excepciones de rangos/tratamientos.
# Reconstruido el 2026-09-03; alineado y preparado para versionado el 2026-09-05.
#
# Uso:   efemerides-linter.sh /ruta/al/post.md [ruta/al/directorio/img]
# Salidas: cada auditoría imprime [OK] o [FALLECE]. Exit 0 = aprobado.
# ============================================================================
set -u
export LC_ALL=C.UTF-8   # clases [áéíóú] por carácter, no por byte (corr. 2026-09-03: frag truncados y contaje de líneas)

FILE=""; SOLO=0; IMGARG=""
for a in "$@"; do
  case "$a" in
    --solo-rangos) SOLO=1 ;;
    *) if [ -z "$FILE" ]; then FILE="$a"; elif [ -z "$IMGARG" ]; then IMGARG="$a"; fi ;;
  esac
done
if [ -z "$FILE" ] || [ ! -f "$FILE" ]; then
  echo "USO: $0 /ruta/al/post.md [directorio-de-imagenes] [--solo-rangos]"
  exit 2
fi

BASENAME=$(basename "$FILE" .md)
BODY=$(sed -n '/^---$/,$p' "$FILE" | sed '1d;/^---$/,$d!' 2>/dev/null)
# Extrae el cuerpo (tras el segundo --- del YAML)
BODY=$(awk 'c==2{print} /^---$/{c++}' "$FILE")
YAML=$(awk 'c<2{print} /^---$/{c++}' "$FILE" | sed '1d')

FAILS=0
ok()   { printf '[OK]      %s\n' "$1"; }
RANGO_PAT='Grado o jerarquía en minúscula|Tratamiento en minúscula|Cargo civil capitalizado'
SKIPPED=0
GREP_ERR=""
EXC=''
SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
for EXC_FILE in "$SCRIPT_DIR/efemerides-rangos-excepciones.txt" /home/user/efemerides-rangos-excepciones.txt; do
  if [ -f "$EXC_FILE" ]; then
    EXC=$(grep -vE '^[[:space:]]*(#|$)' "$EXC_FILE")
    break
  fi
done
exc_hit() { # $1=file basename, $2=frag: imprime motivo si hay excepción
  [ -z "$EXC" ] && return 1
  while IFS='|' read -r ef fg mo; do
    [ "$1" = "$ef" ] && case "$2" in *"$fg"*) echo "$mo"; return 0 ;; esac
  done <<< "$EXC"; return 1
}
fail() {
  printf '[FALLECE] %s\n' "$1"
  if [ "$SOLO" = 1 ] && ! grep -qE "$RANGO_PAT" <<<"$1"; then
    SKIPPED=$((SKIPPED+1))
  else
    FAILS=$((FAILS+1))
  fi
}

# ---------------------------------------------------------------- YAML (1)
grep -q "^layout: post$" <<<"$YAML" && ok "YAML: layout: post" || fail "YAML: falta layout: post"
grep -q "^title: " <<<"$YAML" && ok "YAML: title presente" || fail "YAML: falta title"
grep -q "^author: Enrique Pomares$" <<<"$YAML" && ok "YAML: autor Enrique Pomares" || fail "YAML: autor debe ser 'Enrique Pomares'"
grep -q "^pais: " <<<"$YAML" && ok "YAML: pais presente" || fail "YAML: falta pais"
grep -q "^excerpt: " <<<"$YAML" && ok "YAML: excerpt presente" || fail "YAML: falta excerpt"
DATE_LINE=$(grep -m1 "^date: " <<<"$YAML" | sed 's/date: //')
IMG_LINE=$(grep -m1 "^image: " <<<"$YAML" | sed 's/image: //')
CATS=$(grep -m1 "^categories: " <<<"$YAML" | sed -E 's/categories: \[([^]]*)\]/\1/' | tr -d ' ')

# Fecha coherente con el nombre de archivo
[[ "$BASENAME" == "$DATE_LINE"-* ]] && ok "YAML: date ($DATE_LINE) coincide con el nombre de archivo" \
  || fail "YAML: date '$DATE_LINE' no coincide con '$BASENAME'"

# Título con patrón "[día] de [mes] de [año] | ..."
YEAR=$(cut -d- -f1 <<<"$DATE_LINE"); MON=$(cut -d- -f2 <<<"$DATE_LINE"); DAY=$(cut -d- -f3 <<<"$DATE_LINE")
MONTHS=(x enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre)
MONNAME=$(printf '%s' "${MONTHS[$((10#$MON))]}")
DAYN=$((10#$DAY))
grep -q "^title: \"${DAYN} de ${MONNAME} de ${YEAR} | .*\"$" "$FILE" \
  && ok "YAML: título sigue el patrón «D de M de AAAA | …»" \
  || fail "YAML: el título no sigue el patrón «${DAYN} de ${MONNAME} de ${YEAR} | …»"

# Imagen: nombre = nombre del post
SLUG="${BASENAME#"$DATE_LINE"-}"
IMG_OK=0
for ext in webp jpg jpeg; do
  [ "$IMG_LINE" = "${DATE_LINE}-${SLUG}.${ext}" ] && IMG_OK=1
done
[ $IMG_OK -eq 1 ] && ok "YAML: image ('$IMG_LINE') coincide con el nombre del post" \
  || fail "YAML: image '$IMG_LINE' debe ser '${DATE_LINE}-${SLUG}.webp'"

# Categorías conocidas
case "$CATS" in
  nacimiento|evento|fundacion|accidente|seguridad|espacial|supervivencia|conmemoracion|"espacial,accidente")
    ok "YAML: categoría(s) válidas: [$CATS]" ;;
  *) fail "YAML: categoría(s) no reconocidas: [$CATS]" ;;
esac

# ------------------------------------------------------- Cabeceras rígidas (2)
REQ_H2=("## Datos verificados del evento" "## Contexto Histórico" "## Desarrollo Cronológico" "## Consecuencias e Impacto" "## Legado" "## Referencias Verificadas" "## Metadatos de Control")
ACTUAL=$(grep -E "^## " <<<"$BODY")
for h in "${REQ_H2[@]}"; do
  grep -qxF "$h" <<<"$ACTUAL" && ok "Cabecera presente: $h" || fail "Falta cabecera normativa: $h"
done
# Variantes: toda H2 distinta de las siete normativas se enumera (sección
# adicional legítima → AVISO; sustitución de una normativa → FALLECE por recuento/orden)
EXTRA_H2=$(grep -E "^## " <<<"$BODY" | grep -vxF -e "${REQ_H2[0]}" -e "${REQ_H2[1]}" -e "${REQ_H2[2]}" -e "${REQ_H2[3]}" -e "${REQ_H2[4]}" -e "${REQ_H2[5]}" -e "${REQ_H2[6]}" || true)
if [ -n "$EXTRA_H2" ]; then
  printf '[AVISO]   H2 no normativa presente (verificar que sea sección adicional legítima):\n'
  while IFS= read -r x; do printf '          %s\n' "$x"; done <<<"$EXTRA_H2"
else
  ok "Sin variantes ni secciones H2 adicionales"
fi
# Orden exacto
N_H2=$(grep -cE "^## " <<<"$BODY")
if [ "$N_H2" -ne 7 ]; then fail "Recuento de H2: se esperan 7, hay $N_H2"; else
  ORDER_OK=1; LAST=0
  for h in "${REQ_H2[@]}"; do
    POS=$(grep -nxF "$h" <<<"$BODY" | cut -d: -f1)
    [ -n "$POS" ] && [ "$POS" -gt "$LAST" ] || { ORDER_OK=0; break; }
    LAST=$POS
  done
  [ $ORDER_OK -eq 1 ] && ok "Las 7 H2 aparecen en el orden normativo" || fail "El orden de las H2 no es el normativo"
fi

# ------------------------------------------------- Resumen Ejecutivo (3)
if grep -qxF '<!-- ## Resumen Ejecutivo -->' <<<"$BODY"; then
  ok "Tag literal '<!-- ## Resumen Ejecutivo -->' presente"
  NEXT=$(grep -A1 -xF '<!-- ## Resumen Ejecutivo -->' <<<"$BODY" | tail -1)
  [ "$NEXT" = '<div class="highlight-box">' ] && ok "El tag va seguido de <div class=\"highlight-box\">" \
    || fail "Tras el tag debe ir exactamente <div class=\"highlight-box\"> (encontrado: '$NEXT')"
  grep -q '</div>' <<<"$BODY" && ok "highlight-box cerrado" || fail "highlight-box sin cierre </div>"
else
  fail "Falta el tag literal '<!-- ## Resumen Ejecutivo -->'"
fi

# --------------------------------------------- Contexto Histórico desglosado (4)
CTX=$(awk '/^## Contexto Histórico$/{f=1;next} /^## /{f=0} f' <<<"$BODY")
H3S=$(grep -E "^### " <<<"$CTX")
for h3 in "### Entorno social" "### Entorno tecnológico" "### Entorno cultural"; do
  grep -qxF "$h3" <<<"$H3S" && ok "Contexto Histórico: $h3 presente" || fail "Contexto Histórico: falta '$h3' (desglose obligatorio)"
done
N_H3=$(grep -cE "^### " <<<"$CTX")
[ "$N_H3" -eq 3 ] && ok "Contexto Histórico: exactamente 3 subsecciones" || fail "Contexto Histórico: se exigen 3 subsecciones H3 exactas, hay $N_H3"

# --------------------------------------------------- Figura inicial (5)
FIRST_BLOCK=$(grep -nE "^(<figure>|## |<div )" <<<"$BODY" | head -1 | cut -d: -f2-)
[ "$FIRST_BLOCK" = "<figure>" ] && ok "El cuerpo inicia con <figure>" || fail "El cuerpo debe iniciar con <figure> (encontrado: '$FIRST_BLOCK')"
grep -q 'class="post-image"' <<<"$BODY" && ok "<img class=\"post-image\">" || fail "Falta class=\"post-image\" en <img>"
grep -q 'class="post-caption"' <<<"$BODY" && ok "<figcaption class=\"post-caption\">" || fail "Falta class=\"post-caption\" en <figcaption>"
grep -q "assets/img/${IMG_LINE}" <<<"$BODY" && ok "src del <figure> apunta a la imagen del YAML" || fail "src del <figure> no coincide con '$IMG_LINE'"

# ------------------------------------------- Divisores y gradiente (regla 13) (6)
GRAD=""
case "$CATS" in
  nacimiento|fundacion)       GRAD="#1b5e20, #2e7d32" ;;
  evento)                     GRAD="#1565c0, #42a5f5" ;;
  accidente)                  GRAD="#b71c1c, #c62828" ;;
  espacial)                   GRAD="#0d47a1, #29b6f6" ;;
  seguridad)                 GRAD="#0d47a1, #546e7a" ;;
  supervivencia)              GRAD="#2e7d32, #ef6c00" ;;
  conmemoracion)              GRAD="#2e7d32, #66bb6a, #fbc02d, #f9a825" ;;
  "espacial,accidente")       GRAD="#0b2545, #134074, #e74c3c, #c0392b" ;;
esac
CANON_HR="<hr style=\"margin: 2rem 0; border: none; height: 2px; background: linear-gradient(to right, ${GRAD});\">"
TOTAL_HR=$(grep -c "^<hr" <<<"$BODY")
CORRECT_HR=$(grep -cxF "$CANON_HR" <<<"$BODY")
HAS_NOTE=$(grep -c '^<div class="note-box">' <<<"$BODY")
EXPECTED_HR=$(( N_H2 + HAS_NOTE + 1 ))
if [ $N_H2 -gt 0 ]; then
  [ "$TOTAL_HR" -eq "$EXPECTED_HR" ] && ok "Recuento de divisores: $TOTAL_HR (=$EXPECTED_HR esperados)" \
    || fail "Recuento de divisores: hay $TOTAL_HR, se esperan $EXPECTED_HR (figura|resumen + resumen|H2 + entre bloques)"
fi
[ "$TOTAL_HR" -eq "$CORRECT_HR" ] && ok "Todos los divisores usan el gradiente normativo de [$CATS]" \
  || fail "Hay $((TOTAL_HR-CORRECT_HR)) divisor(es) con gradiente ajeno, reversible o <hr> plano (categoría [$CATS] exige '${GRAD}')"

# ------------------------- Párrafo introductorio tras títulos (regla del editor 2026-09-03)
# Ningún título puede quedar seguido de otro título: debe abrir con párrafo introductorio
# (o, si la sección representa una lista cronológica/de viñetas, con el primer elemento de lista).
NO_INTRO=$(awk '
  /^#{2,4} /{
    t=$0
    while ((getline l) > 0) {
      if (l ~ /^[[:space:]]*$/) continue
      if (l ~ /^#{1,6} /) print substr(t,1,60) "  →  " substr(l,1,44)
      break
    }
  }' "$FILE")
if [ -z "$NO_INTRO" ]; then
  ok "Todo título abre con párrafo introductorio o contenido de lista"
else
  while IFS= read -r ln; do
    fail "Título sin párrafo introductorio: «${ln}» (regla del editor 2026-09-03; solo eximen las secciones que abren con lista)"
  done <<< "$NO_INTRO"
fi

# -------------------------------------- Enlaces HTML con estilo (regla 2) (7)
BAD_A=$(grep -oE '<a [^>]*>' <<<"$BODY" | grep -vc 'style="color: #315fea; text-decoration: none;"')
[ "${BAD_A:-0}" -eq 0 ] && ok "Todo <a> del cuerpo usa el estilo sin subrayado" \
  || fail "$BAD_A enlace(s) <a> carecen de style=\"color: #315fea; text-decoration: none;\""
grep -qE 'href="\[https?:[^]]*\]\(' <<<"$BODY" && fail "Enlace mal formado href=\"[URL](URL)\"" || ok "Sin enlaces href=\"[URL](URL)\""
grep -qE '\[[^]]+\]\(https?://' <<<"$BODY" && fail "Hay enlaces Markdown en el cuerpo (deben ser HTML)" || ok "Sin enlaces Markdown en el cuerpo"

# ------------------------------------------------ Referencias (regla 14) (8)
REFS=$(awk '/^## Referencias Verificadas$/{f=1;next} /^## /{f=0} f' <<<"$BODY")
NREFS=$(grep -cE '^\s*(<li>|[-*] |[0-9]+\. )' <<<"$REFS")
[ "$NREFS" -ge 4 ] && ok "Referencias verificadas: $NREFS (mínimo 4, contando <li>/viñeta/numeradas)" \
  || fail "Referencias verificadas: solo $NREFS — se exigen al menos 4"
[ "$NREFS" -eq 0 ] && fail "La sección de referencias está vacía"

# ------------------------------------------------- Metadatos de Control (9)
META=$(awk '/^## Metadatos de Control$/{f=1;next} f' <<<"$BODY")
for f in "Timestamp de verificación" "Fuentes primarias/institucionales consultadas" "Nivel de confianza" "Cláusula final"; do
  grep -q "\*\*$f" <<<"$META" && ok "Metadatos: campo '$f' presente" || fail "Metadatos: falta el campo '$f'"
done
grep -qE '\*\*Nivel de confianza:\*\* (Alto|Medio|Bajo)' <<<"$META" && ok "Metadatos: nivel de confianza válido" || fail "Metadatos: Nivel de confianza debe ser Alto / Medio / Bajo"
grep -qi "años transcurridos" <<<"$META" && fail "Metadatos: contiene 'Años transcurridos' (prohibido — integrate en ## Legado)" || ok "Metadatos: sin campo 'Años transcurridos'"
grep -q "borrador preliminar" <<<"$META" && fail "Metadatos: cita el borrador preliminar (regla maestra 6)" || ok "Metadatos: no cita el borrador preliminar"
# Discrepancias: solo divergencias entre fuentes publicadas — advertencia de revisión
DISC=$(grep '\*\*Discrepancias resueltas:\*\*' <<<"$META")
if [ -n "$DISC" ]; then
  if grep -qiE "borrador|40[34]|acceso|entorno|verific[oó] la coherencia" <<<"$DISC"; then
    fail "«Discrepancias resueltas» documenta incidencias del proceso, no divergencias entre fuentes"
  else
    ok "«Discrepancias resueltas» presente (revisar que refleje solo divergencias entre fuentes publicadas)"
  fi
else
  ok "«Discrepancias resueltas» omitido (correcto si no hubo divergencias entre fuentes)"
fi

# --------------------------------------------- Principio de documento limpio (10)
grep -q "borrador preliminar" <<<"$BODY" && fail "El post menciona el borrador preliminar (regla maestra 8)" || ok "Sin menciones al borrador preliminar"
grep -qE '\[citation:[0-9]+\]|\[VERIFICADO\]' <<<"$BODY" && fail "Marcadores automáticos presentes ([citation:X] / [VERIFICADO])" || ok "Sin marcadores automáticos"
grep -qiE "pendiente de revisi[oó]n|mayor resoluci[oó]n disponible" <<<"$BODY" && fail "Hay líneas de estado del documento o notas de resolución (prohibidas)" || ok "Sin líneas de estado ni notas de resolución"

# ------------------------------------------ Enlaces internos canónicos (11)
INTERNAL=$(grep -oE 'https://efemerides-aviacion\.github\.io/efemerides/[^")]*' <<<"$BODY" | sort -u)
LINK_FAIL=0
if [ -n "$INTERNAL" ]; then
  SELF_PATH="/$(printf '%04d' "$((10#$YEAR))")/$(printf '%02d' "$((10#$MON))")/$(printf '%02d' "$((10#$DAY))")/${SLUG}.html"
  while IFS= read -r u; do
    [[ "$u" =~ /efemerides/[a-z]+(/[a-z]+)?/[0-9]{4}/[0-9]{2}/[0-9]{2}/[^/-][^/]*\.html$ ]] \
      || { fail "Enlace interno fuera del patrón canónico (fecha en barras, slug sin guion terminal): $u"; LINK_FAIL=1; }
    [[ "$u" == *"$SELF_PATH"* ]] && { fail "El post se enlaza a sí mismo: $u"; LINK_FAIL=1; }
    [[ "$u" == *"${DATE_LINE}-"* ]] && { fail "Enlace interno con fecha unida por guiones: $u"; LINK_FAIL=1; }
  done <<<"$INTERNAL"
  [ $LINK_FAIL -eq 0 ] && ok "Enlaces internos conformes al patrón canónico de Jekyll"
else
  ok "Sin enlaces internos (nada que auditar)"
fi

# ------------------------------------------------- Grados militares (regla 5)
RANK_RE='teniente de nav[ií]o|tenient[ea]s?|subtenient[ea]s?|alférez|alfereces?|capitanes?|capitán|capitan|coronel(es)?|mayor(es)?|general(es)?|brigadier(es)?|almirantes?|sargent[oa]s?|cab[oa]s?|comodor[oa]s?|primer oficial|oficial(es)? primero'
BAD_RANK=$(grep -nE "(^|[^A-Za-zÁÉÍÓÚáéíóúÑñ])($RANK_RE) +(\([A-Za-záéíóúñÑÁÉÍÓÚ.]+\) +)?[A-ZÁÉÍÓÚ][a-záéíóú]+" "$FILE" || { [ $? -ge 2 ] && GREP_ERR="$GREP_ERR grep"; true; })
if [ -n "$BAD_RANK" ]; then
  while IFS= read -r l; do
    n="${l%%:*}"; frag=$(sed 's/^[0-9]*://' <<<"$l" | grep -oE "($RANK_RE) +(\([A-Za-záéíóúñÑÁÉÍÓÚ.]+\) +)?[A-ZÁÉÍÓÚ][a-záéíóú]+" | head -1)
        BFILE=$(basename "$FILE")
    if MOT=$(exc_hit "$BFILE" "$frag"); then printf '[AVISO]   Excepción D1-a/D2-a en línea %s: «%s» — %s\n' "$n" "$frag" "$MOT"; continue; fi
fail "Grado o jerarquía en minúscula ante nombre propio (línea $n): «$frag» — debe ir capitalizado (regla maestra 5)"
  done <<<"$BAD_RANK"
else
  ok "Grados militares capitalizados ante nombre propio"
fi

# ------------------------------------- Tratamientos honoríficos (D2-a, 2026-09-03)
TRAT_RE='señorit[ae]s?|doctor(a|es|as)?|licenciad[oa]s?|señor(es)?|señoras?'
BAD_TRAT=$(grep -nE "(^|[^A-Za-zÁÉÍÓÚáéíóúÑñ])($TRAT_RE) +[A-ZÁÉÍÓÚ][a-záéíóú]+" "$FILE" || { [ $? -ge 2 ] && GREP_ERR="$GREP_ERR grep"; true; })
if [ -n "$BAD_TRAT" ]; then
  while IFS= read -r l; do
    n="${l%%:*}"; frag=$(sed 's/^[0-9]*://' <<<"$l" | grep -oE "($TRAT_RE) +[A-ZÁÉÍÓÚ][a-záéíóú]+" | head -1)
        BFILE=$(basename "$FILE")
    if MOT=$(exc_hit "$BFILE" "$frag"); then printf '[AVISO]   Excepción D1-a/D2-a en línea %s: «%s» — %s\n' "$n" "$frag" "$MOT"; continue; fi
fail "Tratamiento en minúscula ante nombre propio (línea $n): «$frag» — mayúscula inicial (Manual v1.15 § 4.3, decisión D2-a)"
  done <<<"$BAD_TRAT"
else
  ok "Tratamientos honoríficos capitalizados ante nombre propio (D2-a)"
fi

# -------------------------------------- Cargos civiles en minúscula (D1-a)
CIVIL_RE='Presidente|Vicepresidente|Ministro|Ministra|Canciller|Gobernador|Gobernadora|Alcalde|Alcaldesa|Secretario|Secretaria|Embajador|Embajadora|Senador|Senadora|Diputado|Diputada|Director|Directora|Gerente'
BAD_CIVIL=$(grep -nE "(^|[ .;:»)\"])(El|La|Los|Las|Un|Una)? ?($CIVIL_RE) +[A-ZÁÉÍÓÚ][a-záéíóú]+" "$FILE" | grep -vE "^[0-9]+:(El|La|Los|Las) $CIVIL_RE" || { [ $? -ge 2 ] && GREP_ERR="$GREP_ERR grep"; true; })
if [ -n "$BAD_CIVIL" ]; then
  while IFS= read -r l; do
    n="${l%%:*}"; frag=$(sed 's/^[0-9]*://' <<<"$l" | grep -oE "($CIVIL_RE) +[A-ZÁÉÍÓÚ][a-záéíóú]+" | head -1)
        BFILE=$(basename "$FILE")
    if MOT=$(exc_hit "$BFILE" "$frag"); then printf '[AVISO]   Excepción D1-a/D2-a en línea %s: «%s» — %s\n' "$n" "$frag" "$MOT"; continue; fi
fail "Cargo civil capitalizado ante nombre propio (línea $n): «$frag» — minúscula (Manual v1.15 § 4.3, decisión D1-a)"
  done <<<"$BAD_CIVIL"
else
  ok "Cargos civiles en minúscula ante nombre propio (D1-a)"
fi

# ------------------------------------------------------ Imagen al tamaño (12)
IMGDIR="${IMGARG:-}"
IMG_FILE=""
for d in "$IMGDIR" "/home/user/en-proceso/img" "$(dirname "$FILE")/../img" "/home/user/efemerides/assets/img"; do
  [ -n "$d" ] && [ -f "${d}/${IMG_LINE}" ] && { IMG_FILE="${d}/${IMG_LINE}"; break; }
done
if [ -n "$IMG_FILE" ] && command -v identify >/dev/null 2>&1; then
  DIMS=$(identify -format "%wx%h" "$IMG_FILE")
  if [ "$CATS" = "nacimiento" ]; then WANT="800x1000"; else WANT="1200x675"; fi
  [ "$DIMS" = "$WANT" ] && ok "Imagen $DIMS — tamaño de casa para [$CATS] ($WANT)" \
    || fail "Imagen $DIMS — [$CATS] exige $WANT (regla maestra 12)"
else
  printf '[AVISO]   Imagen no localizada en el entorno (auditar dims. manualmente: %s)\n' "${IMG_LINE}"
fi

# ------------------------------------------------------------------ Veredicto
if [ -n "$GREP_ERR" ]; then fail "Auditoría(s) de rangos estropeadas (error de grep en: $GREP_ERR) — no se puede certificar ninguna ausencia de violaciones"; fi
echo
if [ "$SOLO" = 1 ]; then
  echo "MODO --solo-rangos: el veredicto pesa solo las auditorías D1-a/D2-a (grados, tratamientos, cargos civiles); $SKIPPED fallo(s) estructural(es) ajeno(s) listado(s) sin computar."
fi
if [ $FAILS -eq 0 ]; then
  if [ "$SOLO" = 1 ]; then
    echo "════ VEREDICTO: APROBADO (solo-rangos) — $FILE sin violaciones de grados/tratamientos/cargos. ════"
  else
    echo "════ VEREDICTO: APROBADO — $FILE pasa todas las auditorías estructurales. ════"
  fi
  exit 0
else
  echo "════ VEREDICTO: FALLECE — $FAILS auditoría(s) con fallo. Corregir antes de presentar al editor. ════"
  exit 1
fi
