#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verifica-enlaces.py — auditoría de enlaces internos y buscador de candidatos.

Herramienta independiente, pensada para vivir junto a eco7.py. NO modifica el
linter: añade dos comprobaciones que hasta ahora se hacían a mano.

USO
  # 1. Auditar los enlaces internos de un post (antes de entregar)
  python3 rectores/verifica-enlaces.py validar en-proceso/post/AAAA-MM-DD-slug.md
  python3 rectores/verifica-enlaces.py validar post.md --http

  # 2. Buscar candidatos a enlace, en español y en inglés
  python3 rectores/verifica-enlaces.py buscar "Philippine Sea"
  python3 rectores/verifica-enlaces.py buscar "pista de hielo" "Antártida" --desde post.md

  # 3. Sugerencia automática a partir del texto del propio post
  python3 rectores/verifica-enlaces.py sugerir post.md --max 12

CORPUS
  Por defecto ./_posts; si no existe, ./corpus/_posts. Se fija con --corpus.

QUÉ VALIDA (modo validar)
  1. Patrón canónico: https://www.efemeridesdeaviacion.com/<cat>/AAAA/MM/DD/<slug>.html
  2. Que la categoría del prefijo coincida con la del destino
     (error real del 25-11-2026: /evento/ para un post [fundacion]).
  3. Que la fecha de la URL coincida con la del destino.
  4. Que el destino exista en el corpus (enlace muerto).
  5. Que el post no se enlace a sí mismo ni repita destino.

POR QUÉ EL BUSCADOR ES BILINGÜE
  Los títulos y los nombres de archivo del archivo están en español y las
  fuentes técnicas, en inglés. Buscar «Philippine Sea» no encontraba
  `1944-06-20-batalla-mar-filipinas-...` (caso real del 25-11-2026). El
  buscador descompone las frases, traduce cada pieza con un diccionario de
  pares ES↔EN y puntúa también las frases completas.

SALIDA
  Código 0 si no hay fallos; 1 si los hay; 2 si el uso es incorrecto.
"""

import argparse
import re
import sys
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path

SITIO = "https://www.efemeridesdeaviacion.com"
PATRON = re.compile(
    r"^https://www\.efemeridesdeaviacion\.com/"
    r"(?P<cat>[a-z]+(?:/[a-z]+){0,2})/(?P<y>\d{4})/(?P<m>\d{2})/(?P<d>\d{2})/"
    r"(?P<slug>[A-Za-z0-9\-\'\u2019_ñáéíóúü]+)\.html$"
)
FECHA_ARCHIVO = re.compile(r"^(?P<f>\d{4}-\d{2}-\d{2})-(?P<slug>.+)\.md$")


# ---------------------------------------------------------------- normalización

def sin_acentos(t):
    return "".join(c for c in unicodedata.normalize("NFD", t)
                   if unicodedata.category(c) != "Mn")


def normaliza(t):
    t = sin_acentos(t.lower())
    t = re.sub(r"[^a-z0-9ñ]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def raiz(p):
    """Recorte tosco de plurales: aviones→avion, hellcats→hellcat."""
    if len(p) > 4 and p.endswith("es"):
        return p[:-2]
    if len(p) > 3 and p.endswith("s"):
        return p[:-1]
    return p


# --------------------------------------------------------- diccionario ES ↔ EN
PARES = [
    # aeronaves y partes
    ("avion", "aircraft"), ("aeronave", "aircraft"), ("avion de pasajeros", "airliner"),
    ("reactor", "jet"), ("cuatrimotor", "four engine"), ("bimotor", "twin engine"),
    ("helice", "propeller"), ("ala", "wing"), ("fuselaje", "fuselage"),
    ("cabina", "cockpit"), ("tripulacion", "crew"), ("piloto", "pilot"),
    ("comandante", "captain"), ("motor", "engine"), ("turbina", "turbine"),
    ("chorro", "jet"), ("supersonico", "supersonic"), ("prototipo", "prototype"),
    ("primer vuelo", "first flight"), ("avion cisterna", "tanker"),
    # vuelo y operación
    ("vuelo", "flight"), ("volar", "fly"), ("despegue", "takeoff"),
    ("aterrizaje", "landing"), ("aterrizar", "land"), ("apontaje", "carrier landing"),
    ("pista", "runway"), ("pista de hielo", "ice runway"),
    ("hielo azul", "blue ice"), ("aeropuerto", "airport"),
    ("aerodromo", "airfield"), ("base aerea", "air base"),
    ("torre de control", "control tower"), ("radar", "radar"),
    ("travesia", "crossing"), ("cruce", "crossing"), ("record", "record"),
    ("vuelo charter", "charter flight"), ("vuelo regular", "scheduled service"),
    ("carga", "cargo"), ("pasajero", "passenger"), ("pasaje", "passenger"),
    ("aerolinea", "airline"), ("escala", "stopover"),
    # combate
    ("caza", "fighter"), ("bombardero", "bomber"), ("torpedero", "torpedo bomber"),
    ("reconocimiento", "reconnaissance"), ("escuadron", "squadron"),
    ("escuadrilla", "squadron"), ("armada", "navy"), ("fuerza aerea", "air force"),
    ("ejercito", "army"), ("militar", "military"),
    ("portaaviones", "aircraft carrier"), ("portaviones", "aircraft carrier"),
    ("derribo", "kill"), ("derribar", "shoot down"), ("victoria", "victory"),
    ("as", "ace"), ("combate", "combat"), ("batalla", "battle"),
    ("bombardeo", "bombing"), ("incursion", "raid"), ("torpedo", "torpedo"),
    ("ametralladora", "machine gun"), ("artillero", "gunner"),
    # globos y primeros vuelos
    ("globo", "balloon"), ("aerostato", "balloon"), ("aerostacion", "ballooning"),
    ("dirigible", "airship"), ("zeppelin", "zeppelin"), ("planeador", "glider"),
    ("planeo", "gliding"), ("paracaidas", "parachute"), ("salto", "jump"),
    ("alas delta", "hang glider"),
    # espacio
    ("espacio", "space"), ("cohete", "rocket"), ("satelite", "satellite"),
    ("orbita", "orbit"), ("luna", "moon"), ("marte", "mars"),
    # geografía y países
    ("antartida", "antarctica"), ("antartico", "antarctic"),
    ("polo sur", "south pole"), ("polo norte", "north pole"),
    ("reina maud", "queen maud"), ("tierra de la reina maud", "queen maud land"),
    ("filipinas", "philippines"), ("mar de filipinas", "philippine sea"),
    ("marianas", "marianas"), ("midway", "midway"), ("okinawa", "okinawa"),
    ("pacifico", "pacific"), ("atlantico", "atlantic"), ("mar", "sea"),
    ("japon", "japan"), ("alemania", "germany"), ("inglaterra", "england"),
    ("gran bretana", "britain"), ("reino unido", "united kingdom"),
    ("estados unidos", "united states"), ("canada", "canada"),
    ("noruega", "norway"), ("portugal", "portugal"), ("sudafrica", "south africa"),
    ("ciudad del cabo", "cape town"), ("australia", "australia"),
    ("espana", "spain"), ("mexico", "mexico"), ("argentina", "argentina"),
    ("brasil", "brazil"), ("islandia", "iceland"), ("groenlandia", "greenland"),
    ("francia", "france"), ("italia", "italy"), ("rusia", "russia"),
    # conflicto y entorno
    ("primera guerra mundial", "world war i"),
    ("segunda guerra mundial", "world war ii"), ("guerra civil", "civil war"),
    ("guerra", "war"), ("paz", "peace"), ("accidente", "accident"),
    ("siniestro", "crash"), ("rescate", "rescue"), ("seguridad", "safety"),
    ("investigacion", "investigation"), ("cientifico", "scientific"),
    ("exploracion", "exploration"), ("turismo", "tourism"),
    # categorías del archivo
    ("nacimiento", "born"), ("fundacion", "founded"), ("conmemoracion", "commemoration"),
]

MAPA = {}
for es, en in PARES:
    a, b = normaliza(es), normaliza(en)
    if not a or not b:
        continue
    MAPA.setdefault(a, set()).add(b)
    MAPA.setdefault(b, set()).add(a)
    MAPA.setdefault(raiz(a), set()).add(raiz(b))
    MAPA.setdefault(raiz(b), set()).add(raiz(a))

VACIAS = set("""a al ante bajo con contra de del desde durante en entre hacia hasta
la las el los un una unos unas y o u e que como por para se su sus le les lo
mas pero sin sobre tras es son fue fueron ha han habia ser esta este estos estas
aqui alli cuando donde quien quienes todo toda todos todas cada otro otra
the of and in on to for with from at by as is was were be been it its an
this that these those after before during over under about into than then""".split())


# ---------------------------------------------------------------- índice

class Corpus:
    def __init__(self, ruta):
        self.ruta = Path(ruta)
        self.posts = []
        self.por_slug = {}
        self.por_fecha_slug = {}
        for f in sorted(self.ruta.glob("*.md")):
            m = FECHA_ARCHIVO.match(f.name)
            if not m:
                continue
            texto = f.read_text(encoding="utf-8", errors="ignore")
            cm = re.search(r"^categories:\s*\[([^\]]*)\]", texto, re.M)
            cats = [c.strip() for c in cm.group(1).split(",") if c.strip()] if cm else []
            catpath = "/".join(cats)
            tm = re.search(r"^title:\s*\"?(.*?)\"?\s*$", texto, re.M)
            titulo = tm.group(1) if tm else f.stem
            cuerpo = texto.split("---", 2)[-1] if texto.startswith("---") else texto
            post = {
                "archivo": f.name,
                "fecha": m.group("f"),
                "slug": m.group("slug"),
                "cat": cats[0] if cats else "",
                "cats": cats,
                "catpath": catpath,
                "titulo": titulo,
                "texto": normaliza(titulo + " " + re.sub(r"<[^>]+>", " ", cuerpo)),
                "url": f"{SITIO}/{catpath}/{m.group('f').replace('-', '/')}/{m.group('slug')}.html",
            }
            self.posts.append(post)
            self.por_slug.setdefault(post["slug"], []).append(post)
            self.por_fecha_slug[(post["fecha"], post["slug"])] = post

    def resolver(self, cat, fecha, slug):
        exacto = self.por_fecha_slug.get((fecha, slug))
        if exacto:
            if exacto["catpath"] != cat:
                etiqueta = ", ".join(exacto["cats"]) or "(sin categoría)"
                return exacto, ("categoria", f"el destino es de categoría [{etiqueta}]")
            return exacto, None
        otros = self.por_slug.get(slug, [])
        if otros:
            fechas = ", ".join(p["fecha"] for p in otros)
            return otros[0], ("fecha", f"existe ese slug, pero fechado el {fechas}")
        return None, ("inexistente", "no hay ningún post con ese slug en el corpus")


# ---------------------------------------------------------------- validación

def urls_internas(texto):
    return sorted({m.group(0) for m in re.finditer(
        r"https://www\.efemeridesdeaviacion\.com/[^\")\s]+", texto)})


def http_status(url, timeout=25):
    req = urllib.request.Request(url, method="GET",
                                 headers={"User-Agent": "Mozilla/5.0 (verifica-enlaces)"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return 0


def revisa_uno(post, corpus, args=None, verboso=True):
    """Devuelve (fallos, avisos, líneas)."""
    texto = post.read_text(encoding="utf-8", errors="ignore")
    m = FECHA_ARCHIVO.match(post.name)
    propio = corpus.por_fecha_slug.get((m.group("f"), m.group("slug"))) if m else None

    urls = urls_internas(texto)
    fallos = avisos = 0
    lineas = []
    if verboso:
        lineas.append(f"POST: {post.name}")
        lineas.append(f"  corpus: {corpus.ruta} ({len(corpus.posts)} posts)")
        lineas.append(f"  enlaces internos: {len(urls)}\n")
    vistos = set()
    for u in urls:
        mm = PATRON.match(u)
        if not mm:
            lineas.append(f"  [FALLO] Fuera del patrón canónico: {u}")
            fallos += 1
            continue
        cat = mm.group("cat")
        fecha = f"{mm.group('y')}-{mm.group('m')}-{mm.group('d')}"
        slug = mm.group("slug")
        destino, motivo = corpus.resolver(cat, fecha, slug)

        if propio and destino and destino["archivo"] == propio["archivo"]:
            lineas.append(f"  [FALLO] El post se enlaza a sí mismo: {u}")
            fallos += 1
            continue
        if u in vistos:
            lineas.append(f"  [AVISO] Enlace repetido en el cuerpo: {u}")
            avisos += 1
        vistos.add(u)

        if motivo:
            tipo, detalle = motivo
            if tipo == "categoria":
                lineas.append(f"  [FALLO] Prefijo /{cat}/ incorrecto: {detalle}. Canónica: {destino['url']}")
            elif tipo == "fecha":
                canonica = f"{SITIO}/{destino['catpath']}/{destino['fecha'].replace('-', '/')}/{slug}.html"
                lineas.append(f"  [FALLO] La fecha {fecha} no coincide: {detalle}. Canónica: {canonica}")
            else:
                lineas.append(f"  [FALLO] Enlace muerto: {detalle} ({slug})")
            fallos += 1
            continue

        if getattr(args, "http", False):
            code = http_status(u)
            if code == 200:
                lineas.append(f"  [OK] {u} → HTTP 200")
            else:
                lineas.append(f"  [FALLO] {u} → HTTP {code}")
                fallos += 1
        else:
            lineas.append(f"  [OK] {u} → {destino['fecha']} [{destino['catpath']}] {destino['titulo'][:58]}")
    return fallos, avisos, lineas


def validar(args):
    post = Path(args.post)
    corpus = Corpus(args.corpus)
    fallos, avisos, lineas = revisa_uno(post, corpus, args)
    print("\n".join(lineas))
    print()
    if fallos:
        print(f"SALIDA: FALLOS ({fallos} fallo(s), {avisos} aviso(s))")
        return 1
    print(f"SALIDA: LIMPIO ({avisos} aviso(s))")
    return 0


def auditar_todos(args):
    corpus = Corpus(args.corpus)
    total = fallos_tot = avisos_tot = 0
    for f in sorted(corpus.ruta.glob("*.md")):
        total += 1
        fallos, avisos, lineas = revisa_uno(f, corpus, args, verboso=False)
        fallos_tot += fallos
        avisos_tot += avisos
        if fallos or (avisos and args.avisos):
            print(f"\n{f.name}")
            print("\n".join(lineas))
    print(f"\nPOSTS: {total} · FALLOS: {fallos_tot} · AVISOS: {avisos_tot}")
    return 1 if fallos_tot else 0


# ---------------------------------------------------------------- buscador

def expande(terminos):
    """Devuelve [(término, peso, es_frase)] con traducción y descomposición."""
    salida = []
    for bruto in terminos:
        n = normaliza(bruto)
        if not n:
            continue
        if " " in n:                                   # frase: se busca entera…
            salida.append((n, 2.2, True))
            for w in n.split():                        # …y por piezas
                if w not in VACIAS and len(w) > 2:
                    salida.append((w, 0.7, False))
                    for par in MAPA.get(w, ()):
                        salida.append((par, 0.5, False))
                    for par in MAPA.get(raiz(w), ()):
                        salida.append((par, 0.4, False))
            for par in MAPA.get(n, ()):                # traducción de la frase entera
                salida.append((par, 1.6, True))
        else:
            salida.append((n, 1.0, False))
            for par in MAPA.get(n, ()):
                salida.append((par, 0.85, bool(" " in par)))
            for par in MAPA.get(raiz(n), ()):
                salida.append((par, 0.65, bool(" " in par)))
    # depura duplicados conservando el peso mayor
    mejor = {}
    for t, peso, frase in salida:
        clave = (t, frase)
        if clave not in mejor or mejor[clave] < peso:
            mejor[clave] = peso
    return [(t, peso, frase) for (t, frase), peso in mejor.items()]


def busca_termino(texto, titulo_compacto, termino, frase):
    if frase or " " in termino:
        encontrado = termino in texto
        return 1 if encontrado else 0, encontrado
    r = raiz(termino)
    patron = r"(?<![a-z0-9])" + re.escape(r) + r"[a-z]{0,3}(?![a-z0-9])"
    apariciones = len(re.findall(patron, texto))
    en_titulo = r in titulo_compacto
    return apariciones, en_titulo


def puntua(post, terminos, idf=None):
    texto = " " + post["texto"] + " "
    titulo_compacto = normaliza(post["titulo"]).replace(" ", "")
    puntos = 0.0
    aciertos = []
    for termino, peso, frase in terminos:
        if idf is not None:
            peso = peso * idf.get((termino, frase), 1.0)
        apariciones, en_titulo = busca_termino(texto, titulo_compacto, termino, frase)
        if not apariciones and not en_titulo:
            continue
        puntos += peso * (1.5 if frase else 1.0)
        if apariciones:
            puntos += peso * min(apariciones, 6) * (0.6 if frase else 0.3)
        if en_titulo:
            puntos += peso * 2.0
        if len(termino) > 2 and termino not in aciertos:
            aciertos.append(termino)
    return puntos, aciertos


def ranking(args, terminos, exclusion=None):
    corpus = Corpus(args.corpus)
    excluir = {Path(exclusion).name} if exclusion else set()
    ya = set()
    if exclusion:
        try:
            ya = set(urls_internas(Path(exclusion).read_text(encoding="utf-8", errors="ignore")))
        except FileNotFoundError:
            pass
    # IDF: cuánto distingue cada término dentro de este corpus
    import math
    total = max(len(corpus.posts), 1)
    idf = {}
    for termino, peso, frase in terminos:
        clave = (termino, frase)
        if clave in idf:
            continue
        df = 0
        for post in corpus.posts:
            texto = " " + post["texto"] + " "
            compacto = normaliza(post["titulo"]).replace(" ", "")
            a, en_titulo = busca_termino(texto, compacto, termino, frase)
            if a or en_titulo:
                df += 1
        idf[clave] = math.log(1 + total / (1 + df)) * 2.0

    filas = []
    for post in corpus.posts:
        if post["archivo"] in excluir:
            continue
        puntos, aciertos = puntua(post, terminos, idf)
        if post["url"] in ya:
            puntos *= 0.10                   # ya enlazado: se hunde, no se oculta
        if puntos > 0:
            filas.append((puntos, aciertos, post, post["url"] in ya))
    filas.sort(key=lambda x: (-x[0], x[2]["fecha"]))
    return filas[: args.max]


def imprime(filas, cabecera):
    print(cabecera)
    for puntos, aciertos, post, ya in filas:
        marca = " ·ya enlazado" if ya else ""
        print(f"  {puntos:6.1f}  {post['fecha']}  [{post['catpath'][:11]:11}] {post['titulo'][:70]}{marca}")
        print(f"          {post['url']}")
        if aciertos:
            print(f"          coincide por: {', '.join(aciertos[:6])}")


def buscar(args):
    if not args.terminos:
        print("ERROR: indica al menos un término de búsqueda.")
        return 2
    terminos = expande(args.terminos)
    filas = ranking(args, terminos, args.desde)
    cab = f"CANDIDATOS ({len(filas)}) para: {' / '.join(args.terminos)}"
    if args.desde:
        cab += f"\n  desde: {Path(args.desde).name} (los ya enlazados se hunden al final)"
    imprime(filas, cab)
    return 0


def sugerir(args):
    post = Path(args.post)
    texto = post.read_text(encoding="utf-8", errors="ignore")
    cuerpo = re.sub(r"<[^>]+>", " ", texto.split("---", 2)[-1])
    tm = re.search(r"^title:\s*\"?(.*?)\"?\s*$", texto, re.M)
    titulo = tm.group(1) if tm else ""
    palabras = []
    for w in re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ][A-Za-zÁÉÍÓÚÜÑáéíóúüñ]{4,}", titulo + " " + cuerpo):
        n = normaliza(w)
        if n in VACIAS or len(n) < 5:
            continue
        if n in normaliza(post.stem[11:]):
            continue
        palabras.append(n)
    frecuencia = {}
    for w in palabras:
        frecuencia[w] = frecuencia.get(w, 0) + 1
    clave = [w for w, _ in sorted(frecuencia.items(), key=lambda x: (-x[1], x[0]))[:14]]
    filas = ranking(args, expande(clave), args.post)
    imprime(filas, f"SUGERENCIAS para {post.name}\n  términos usados: {', '.join(clave)}")
    return 0


# ---------------------------------------------------------------- CLI

def main():
    ap = argparse.ArgumentParser(description="Auditoría de enlaces internos y buscador de candidatos.")
    ap.add_argument("--corpus", default=None)
    sub = ap.add_subparsers(dest="cmd", required=True)
    # --corpus se admite también tras el subcomando (SUPPRESS: no pisa el valor previo)
    _subs = []

    v = sub.add_parser("validar"); _subs.append(v)
    v.add_argument("post")
    v.add_argument("--http", action="store_true")
    v.add_argument("--max", type=int, default=12)
    v.set_defaults(func=validar)

    b = sub.add_parser("buscar"); _subs.append(b)
    b.add_argument("terminos", nargs="+")
    b.add_argument("--desde", default=None)
    b.add_argument("--max", type=int, default=12)
    b.set_defaults(func=buscar)

    a = sub.add_parser("auditar-todos", help="audita los enlaces internos de todo el corpus")
    a.add_argument("--avisos", action="store_true", help="muestra también los posts con avisos")
    a.add_argument("--max", type=int, default=12)
    a.set_defaults(func=auditar_todos)

    s = sub.add_parser("sugerir"); _subs.append(s)
    s.add_argument("post")
    s.add_argument("--max", type=int, default=12)
    s.set_defaults(func=sugerir)

    for _sp in _subs:
        _sp.add_argument("--corpus", default=argparse.SUPPRESS)
    args = ap.parse_args()
    if args.corpus is None:
        args.corpus = "_posts" if Path("_posts").is_dir() else "corpus/_posts"
    if not Path(args.corpus).is_dir():
        print(f"ERROR: no encuentro el corpus en {args.corpus}")
        return 2
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
