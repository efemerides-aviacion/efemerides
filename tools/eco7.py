#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
eco7.py — Detector de ecos de 7-gramas de prosa.

Recreación del 24-sep-2026, incorporada al repositorio el 25-sep-2026. El original (SHA-256
bd71d9b2a3efd1fb201adc15875d738975290cc1d184abc656da5340da14fa24) se perdió
con el reset del workspace y no estaba versionado; esta versión implementa el
criterio documentado en el ESTADO-Y-PENDIENTES-102 (sección «Fotografía
actual»), con dos decisiones de tokenización documentadas en esta misma
cabecera:

  - Tokenización: un tramo de 2 o más palabras consecutivas con inicial
    mayúscula (nombre propio o denominación institucional, p. ej.
    «Escuela de Aviación Militar de Chile», «National Air and Space Museum»)
    cuenta como UN solo token (entidad). Así los nombres propios no
    constituyen prosa y no generan ni reciben ecos; los nombres de una sola
    palabra se tokenizan como palabra común minúscula.
  - Los 7-gramas se calculan sobre esos tokens (minúsculas), bloque a
    bloque: un grama nunca cruza párrafo, cabecera ni sección.
  - Excluidos:
      a) gramos de plantilla: front matter YAML, comentarios HTML, líneas de
         cabecera Markdown, <hr> y la sección «Referencias Verificadas» y la
         de «Metadatos de Control» (texto estructural, no prosa narrativa).
      b) gramos 100 % vocabulario no narrativo: gramos cuyo 7 tokens no
         contiene ninguna palabra del vocabulario común español (lista
         integrada NARRATIVE); p. ej. solo cifras, fechas y nombres propios.
      c) gramos extendidos a 2 o más posts del corpus (material común del
         repositorio, no eco puntual).
  - Eco de contenido = grama no estructural compartida con exactamente 1
    otro post del corpus.
  - exit 0 = limpio (0 ecos); exit 1 = hay ecos (se imprimen uno a uno,
    con el post compañero).

Uso:
  python3 tools/eco7.py <post.md> [--corpus DIR]

  <post.md>   post a auditar (dentro o fuera del corpus)
  --corpus    directorio del corpus (por defecto <raíz-del-repo>/_posts)

El post auditado se excluye del corpus. La salida es determinista (orden
alfabético de gramos). Calibración exigida por el estado: los dos posts
1924-09-28 (circunnavegación y Lagreze) dan 0 ecos.
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys

N = 7
DEFAULT_CORPUS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "_posts"))

# Vocabulario narrativo español: palabras de clase abierta (sustantivos
# comunes, verbos, adjetivos, adverbios). Un grama es «narrativo» si contiene
# al menos un token (una sola palabra) de esta lista. Las palabras funcionales
# (artículos, preposiciones, conjunciones, pronombres), los numerales, las
# fechas y los nombres propios (tokens-entidad) son vocabulario NO narrativo:
# un grama 100 % no narrativo (p. ej. una cadena de nombres propios y
# preposiciones, o una fecha extensa) se excluye de la búsqueda de ecos.
NARRATIVE = {
    "(dominio", "(infinitivo", "+", "Adjetivos", "Adverbios", "Sustantivos", "Verbos", "abandona",
    "abandonado", "abandonar", "abandono", "abierto", "abre", "abria", "abrio", "abrir", "aca",
    "acepta", "aceptado", "aceptar", "acepte", "aclara", "aclaracion", "aclaraciones",
    "aclaración", "aclarado", "aclarar", "aclare", "acompana", "acompanado", "acompanar",
    "acompañaba", "acompañe", "actual", "actuales", "acuerdo", "acuerdos", "acá", "ademas",
    "además", "administra", "administrado", "administrar", "administró", "aerodromo", "aeronave",
    "aeronaves", "aeropuerto", "aeropuertos", "aeródromo", "afirma", "afirmado", "afirmar",
    "afirmo", "agrega", "agregaba", "agregado", "agregar", "agregue", "ahí", "ala", "alas",
    "alcance", "alcanza", "alcanzado", "alcanzar", "allí", "almacena", "almacenaba", "almacenado",
    "almacenar", "almacené", "almirante", "altitud", "altura", "alturas", "amplia", "ampliado",
    "ampliar", "amplio", "analice", "analiza", "analizado", "analizar", "aniversario",
    "aniversarios", "anos", "anterior", "antes", "antigua", "antiguas", "antiguo", "antiguos",
    "aparato", "aparatos", "apenas", "aplica", "aplicaba", "aplicado", "aplicar", "aplique",
    "aporta", "aportaba", "aportado", "aportar", "aporte", "apoya", "apoyado", "apoyar", "apoye",
    "aprende", "aprender", "aprendido", "aprendio", "aqui", "aquí", "archiva", "archivado",
    "archivar", "archive", "archivo", "archivos", "arquitecto", "arquitectos", "asamblea",
    "ascender", "ascendido", "ascendio", "asciende", "asciendo", "asi", "asigna", "asignaba",
    "asignado", "asignar", "asigne", "aspecto", "aspectos", "asunto", "asuntos", "así", "atender",
    "atendia", "atendido", "aterriza", "aterrizado", "aterrizar", "aterrizo", "atiende", "atiendo",
    "atravesado", "atravesar", "atraveso", "atraviesa", "aumenta", "aumentado", "aumentar",
    "aumento", "aun", "autoridad", "autoridades", "avion", "aviones", "avión", "año", "aún",
    "base", "bases", "bate", "batido", "batir", "batió", "biblioteca", "bibliotecas", "biplano",
    "brigada", "brigadas", "cadete", "cadetes", "calcula", "calculado", "calcular", "calculo",
    "cambio", "campeon", "campeona", "campeones", "campeón", "campo", "capitan", "capitanes",
    "capitán", "caracteristica", "característica", "características", "casi", "caso", "casos",
    "cataloga", "catalogado", "catalogar", "catalogue", "celebra", "celebrado", "celebrar",
    "celebre", "centenario", "centenarios", "centro", "centros", "cerraba", "cerrado", "cerrar",
    "cerro", "cierra", "cierre", "cierta", "ciertas", "cierto", "ciertos", "cita", "citado",
    "citar", "cite", "clasifica", "clasificaba", "clasificado", "clasificar", "clasifique",
    "coleccion", "colecciones", "colección", "coloca", "colocaba", "colocado", "colocar",
    "coloque", "comanda", "comandado", "comandante", "comandar", "comando", "combina", "combinaba",
    "combinado", "combinar", "combine", "combustible", "comenzado", "comenzar", "comenzo",
    "comienza", "comision", "comisiones", "comisión", "comite", "comites", "comité", "comités",
    "completa", "completado", "completar", "completo", "compone", "componer", "compongo",
    "componia", "compra", "comprado", "comprar", "compre", "compuesto", "compuso", "comunicado",
    "comunicados", "concluido", "concluir", "concluye", "concluyo", "conduce", "conducia",
    "conducido", "conducir", "condujo", "configura", "configuraba", "configurado", "configurar",
    "configure", "confirma", "confirmado", "confirmar", "confirmo", "congreso", "conmemora",
    "conmemorado", "conmemorar", "conmemoró", "conoce", "conocer", "conocia", "conocida",
    "conocidas", "conocido", "conocidos", "conocio", "conserva", "conservaba", "conservado",
    "conservar", "conserve", "considera", "considerado", "considerar", "considero", "constituia",
    "constituido", "constituir", "constituye", "constituyo", "construia", "construido",
    "construir", "construye", "construyo", "contado", "contar", "continua", "continuado",
    "continuar", "continue", "continuó", "contraalmirante", "controla", "controlado", "controlar",
    "controlo", "contó", "convenio", "convenios", "coronel", "coroneles", "corregido", "corregir",
    "corrige", "corrigio", "corrijo", "crea", "creaba", "creado", "crear", "cree", "creer",
    "creia", "creido", "creo", "creyó", "cruza", "cruzado", "cruzar", "cruzo", "cuando", "cuenta",
    "cuestion", "cuestiona", "cuestionado", "cuestionar", "cuestiono", "cuestión", "cuida",
    "cuidaba", "cuidado", "cuidar", "cuide", "cuido", "da", "daba", "dado", "dar", "debe", "deber",
    "debia", "debida", "debido", "debio", "decide", "decidido", "decidio", "decidir", "decido",
    "decir", "declaracion", "declaraciones", "declaración", "decreto", "decretos", "dedica",
    "dedicado", "dedicar", "dedique", "defender", "defendia", "defendido", "defendio", "defiende",
    "defiendo", "define", "definido", "definir", "defino", "deja", "dejaba", "dejado", "dejar",
    "dejaron", "dejo", "demostrado", "demostrar", "demostro", "demuestra", "desarrolla",
    "desarrollado", "desarrollar", "desarrollo", "descender", "descendido", "descendio",
    "descenso", "desciende", "desciendo", "describe", "describio", "describir", "descrito",
    "descubierto", "descubre", "descubria", "descubrio", "descubrir", "descubro", "designa",
    "designado", "designar", "designe", "desmonta", "desmontado", "desmontar", "desmonte",
    "despegado", "despegar", "despegue", "despues", "después", "destaca", "destacado", "destacar",
    "destaco", "destina", "destinaba", "destinado", "destinar", "destine", "detalle", "detalles",
    "determina", "determinado", "determinar", "determino", "devolver", "devolvió", "devuelto",
    "devuelve", "devuelvo", "dia", "dias", "dibuja", "dibujaba", "dibujado", "dibujar", "dibujé",
    "dice", "dicho", "diferente", "dijeron", "dijo", "dio", "diputado", "diputados", "dirige",
    "dirigia", "dirigido", "dirigio", "dirigir", "discute", "discutido", "discutir", "discutió",
    "discuto", "disena", "disenado", "disenador", "disenar", "disenó", "disminuido", "disminuir",
    "disminuye", "disminuyo", "distancia", "distingo", "distingue", "distinguia", "distinguido",
    "distinguir", "distinto", "divide", "dividia", "dividido", "dividio", "dividir", "divido",
    "division", "división", "doctor", "doctora", "doctores", "documenta", "documentado",
    "documentar", "documento", "donde", "dura", "duraba", "durado", "durar", "duro", "edifica",
    "edificaba", "edificado", "edificar", "edifico", "edita", "editaba", "editado", "editar",
    "edite", "ejemplo", "ejercito", "ejercitos", "ejército", "elegido", "elegir", "elemento",
    "elementos", "elige", "eligio", "elijo", "empezado", "empezar", "empezó", "empiece", "empieza",
    "emplea", "empleaba", "empleado", "emplear", "empleo", "emprenda", "emprende", "emprender",
    "emprendido", "emprendo", "empresa", "empresas", "encontrado", "encontrar", "encontraron",
    "encontro", "encuentra", "enmendado", "enmendar", "enmendó", "enmienda", "ensambla",
    "ensamblado", "ensamblar", "ensamble", "ensena", "ensenado", "ensenar", "ensene", "enseña",
    "entender", "entendido", "entendio", "entiende", "entiendo", "entonces", "entra", "entraba",
    "entrado", "entrar", "entrega", "entregado", "entregar", "entregue", "entro", "envia",
    "enviaba", "enviado", "enviar", "envió", "epoca", "era", "eran", "erige", "erigia", "erigido",
    "erigir", "erijo", "es", "escapa", "escapado", "escapar", "escapó", "escoge", "escoger",
    "escogido", "escogio", "escojo", "escribe", "escribia", "escribio", "escribir", "escrito",
    "escuela", "especial", "especiales", "especifica", "especificado", "especificar", "especifico",
    "espera", "esperaba", "esperado", "esperar", "espero", "esta", "estaba", "estaban", "estabas",
    "establece", "establecer", "establecido", "establecio", "estan", "estar", "este", "esten",
    "estima", "estimado", "estimar", "estimo", "estimula", "estimulado", "estimular", "estimule",
    "estructura", "estructuraba", "estructurado", "estructurar", "estructure", "estudia",
    "estudiaba", "estudiado", "estudiar", "estudio", "estudios", "estuvieron", "estuvo", "etapa",
    "evalua", "evaluado", "evaluar", "evalúe", "examina", "examinado", "examinar", "examine",
    "excede", "exceder", "excedido", "excedo", "exhibe", "exhibia", "exhibido", "exhibir",
    "exhibo", "explica", "explicado", "explicar", "explico", "expone", "exponer", "expongo",
    "exponia", "expuesto", "expuso", "fabrica", "fabricado", "fabricar", "fabricas", "fabrico",
    "famosa", "famoso", "fecha", "fija", "fijado", "fijar", "fijo", "final", "finales", "finalice",
    "finaliza", "finalizado", "finalizar", "financia", "financiado", "financiar", "financie",
    "firma", "firmado", "firmar", "firme", "fomenta", "fomentado", "fomentar", "fomento", "fondo",
    "fondos", "forma", "formaba", "formado", "formar", "formas", "forme", "formo", "fotografia",
    "fotografias", "fotografía", "fotografías", "frecuentes)", "fue", "fuente", "fuentes",
    "fueron", "fuerza", "fuerzas", "fui", "fuiste", "funda", "fundada", "fundado", "fundar",
    "fundo", "fábrica", "fábricas", "gaceta", "gana", "ganaba", "ganado", "ganar", "gano",
    "general", "generales", "generales)", "gestiona", "gestionado", "gestionar", "gestionó",
    "gobernado", "gobernar", "gobierna", "gobierno", "gobiernos", "gran", "grande", "grandes",
    "guarda", "guardaba", "guardado", "guardar", "guardo", "guerra", "guia", "guiaba", "guiado",
    "guiar", "guide", "haber", "habia", "habido", "habla", "hablaba", "hablado", "hablar", "hable",
    "hace", "hacen", "hacer", "hacia", "haciendo", "hay", "hecho", "hicieron", "historia",
    "historica", "historico", "histórica", "histórico", "hito", "hizo", "homenaje", "homenajea",
    "homenajeado", "homenajear", "homenajes", "homenajeó", "hora", "horas", "hubieron", "hubo",
    "iban", "identifica", "identificaba", "identificado", "identificar", "identifique", "ido",
    "igual", "ilustra", "ilustrado", "ilustrar", "ilustro", "impulsa", "impulsado", "impulsar",
    "impulse", "incluso", "incorpora", "incorporaba", "incorporado", "incorporar", "incorpore",
    "incrementa", "incrementado", "incrementar", "incremento", "indica", "indicado", "indicar",
    "indicaron", "indico", "industria", "industrias", "ingeniera", "ingeniero", "ingenieros",
    "inicia", "iniciado", "iniciar", "inicie", "inspira", "inspirado", "inspirar", "inspire",
    "instala", "instalado", "instalar", "instale", "institucion", "instituciones", "institución",
    "instructor", "instructores", "integra", "integraba", "integrado", "integrar", "integre",
    "internacional", "internacionales", "ir", "ire", "junta", "juntaba", "juntado", "juntar",
    "junte", "kilometro", "kilometros", "laboratorio", "laboratorios", "lado", "lados", "ley",
    "leyes", "lidera", "liderado", "liderar", "lidere", "llega", "llegaba", "llegado", "llegando",
    "llegar", "lleva", "llevaba", "llevado", "llevar", "llevé", "local", "locales", "luego",
    "manera", "mantener", "mantenia", "mantenido", "mantiene", "mantuvo", "marca", "marcado",
    "marcar", "marco", "mas", "material", "materiales", "mayor", "mayores", "medalla", "medallas",
    "medido", "medir", "memoria", "memorial", "menciona", "mencionado", "mencionar", "menciono",
    "menor", "menores", "menos", "mes", "meses", "metro", "metros", "mezcla", "mezclaba",
    "mezclado", "mezclar", "mezcle", "mide", "midio", "mientras", "militar", "militares", "milla",
    "millas", "ministeria", "ministerio", "ministerios", "ministro", "ministros", "minuto",
    "minutos", "misma", "mismas", "mismo", "mismos", "moderna", "modernas", "modernice",
    "moderniza", "modernizado", "modernizar", "moderno", "modernos", "modo", "momento", "momentos",
    "monoplano", "monta", "montado", "montar", "monte", "mostrado", "mostrar", "mostraron",
    "mostro", "motiva", "motivado", "motivar", "motive", "motor", "motores", "mucha", "muchas",
    "mucho", "muchos", "muestra", "museo", "museos", "muy", "más", "nace", "nacer", "nacia",
    "nacido", "nacional", "nacionales", "nació", "navega", "navegaba", "navegado", "navegar",
    "navegue", "nego", "negocia", "negociado", "negociar", "negoció", "nombra", "nombrado",
    "nombrar", "nombre", "nota", "notas", "nudo", "nudos", "nueva", "nuevas", "nuevo", "nuevos",
    "nunca", "obra", "obras", "oficial", "oficiales", "ofrece", "ofrecer", "ofrecia", "ofrecido",
    "ofrezco", "opera", "operado", "operar", "opero", "orden", "ordenanza", "ordenanzas",
    "ordenes", "organice", "organiza", "organizacion", "organizaciones", "organización",
    "organizado", "organizar", "otra", "otras", "otro", "otros", "pacto", "pactos", "pais",
    "paises", "paracaidas", "paracaidista", "paracaidistas", "paracaídas", "parte", "partes",
    "pasa", "pasaba", "pasado", "pasar", "paso", "patrocina", "patrocinado", "patrocinar",
    "patrocinó", "paz", "país", "países", "pensaba", "pensado", "pensar", "pensaron", "penso",
    "perder", "perdia", "perdido", "perdió", "periodico", "periodista", "periodistas", "periodo",
    "periódico", "permanece", "permanecer", "permanecia", "permanecido", "período", "pie",
    "piensa", "pierde", "pies", "pilota", "pilotado", "pilotar", "pilote", "piloto", "pilotos",
    "pinta", "pintado", "pintar", "pinte", "pionera", "pioneras", "pionero", "pioneros", "pista",
    "planea", "planeaba", "planeado", "planear", "planeé", "poca", "pocas", "poco", "pocos",
    "poder", "podia", "podido", "pone", "poner", "ponia", "popular", "populares", "posterior",
    "precisa", "precisado", "precisar", "preciso", "premio", "premios", "prensa", "prepara",
    "preparaba", "preparado", "preparar", "prepare", "presenta", "presentaba", "presentado",
    "presentar", "presente", "presento", "preserva", "preservaba", "preservado", "preservar",
    "preserve", "preside", "presidencia", "presidenta", "presidente", "presidentes", "presidia",
    "presidido", "presidir", "presidió", "primer", "primera", "primero", "principal",
    "principales", "probado", "probar", "probo", "produce", "producia", "producido", "producir",
    "profesor", "profesores", "programa", "programaba", "programado", "programar", "promover",
    "promovido", "promovió", "promueve", "promuevo", "propia", "propias", "propio", "propios",
    "proporciona", "proporcionaba", "proporcionado", "proporcionar", "proporcionase", "proseguido",
    "proseguir", "prosigue", "prosiguió", "protege", "proteger", "protegia", "protegido",
    "protegio", "prototipo", "prototipos", "provee", "proveer", "proveia", "proveo", "provisto",
    "proyecto", "proyectos", "prueba", "publica", "publicaba", "publicado", "publicar", "publique",
    "pudieron", "pudo", "puede", "puesto", "punto", "puntos", "puso", "queda", "quedaba",
    "quedado", "quedar", "quedó", "querer", "queria", "querido", "quiere", "quiso", "radio",
    "rasgo", "rasgos", "realidad", "rechace", "rechaza", "rechazado", "rechazar", "recibe",
    "recibia", "recibido", "recibir", "recibo", "reciente", "recientes", "recoge", "recoger",
    "recogia", "recogido", "recogio", "reconoce", "reconocer", "reconocia", "reconocido",
    "reconocimiento", "reconocimientos", "reconocio", "reconozco", "reconstruido", "reconstruir",
    "reconstruye", "reconstruyo", "recopila", "recopilaba", "recopilado", "recopilar", "recopile",
    "recordaba", "recordado", "recordar", "recuerda", "recuerdo", "reduce", "reducido", "reducir",
    "redujo", "referencia", "referencias", "reforma", "reformado", "reformar", "reforme",
    "regimiento", "regimientos", "region", "regiones", "registra", "registrado", "registrar",
    "registro", "registró", "región", "reglamento", "regresa", "regresado", "regresar", "regresó",
    "relata", "relatado", "relatar", "relate", "remite", "remitia", "remitido", "remitir",
    "remito", "remodela", "remodelado", "remodelar", "remodeledo", "remonta", "remontado",
    "remontar", "remonto", "renovado", "renovar", "renueva", "renuevo", "repara", "reparado",
    "reparar", "repare", "rescata", "rescatado", "rescatar", "rescató", "resolver", "resolvio",
    "restaura", "restaurado", "restaurar", "restituyo", "resuelto", "resuelve", "resuelvo",
    "retoma", "retomado", "retomar", "retome", "retorna", "retornado", "retornar", "reune",
    "reunia", "reunido", "reunio", "reunir", "reuno", "revela", "revelaba", "revelado", "revelar",
    "revele", "revisa", "revisado", "revisar", "revise", "rompe", "romper", "rompo", "roto",
    "sabe", "saber", "sabia", "sabido", "sale", "salia", "salido", "salir", "salva", "salvado",
    "salvar", "salvó", "sargento", "sargentos", "sea", "sean", "seguia", "seguido", "seguir",
    "segunda", "segundo", "segundos", "senado", "senador", "senadores", "senala", "senalar",
    "separa", "separaba", "separado", "separar", "separe", "ser", "sera", "seran", "servia",
    "servido", "servio", "servir", "será", "serán", "señala", "señalado", "señalo", "sido",
    "siempre", "siglo", "siglos", "sigue", "siguiente", "siguió", "similar", "sirve", "sirvo",
    "situa", "situaba", "situado", "situar", "situe", "sobrevive", "sobrevivia", "sobrevivido",
    "sobrevivio", "sobrevivir", "sola", "solas", "soldado", "soldados", "solo", "solos",
    "suboficial", "suboficiales", "subraya", "subrayado", "subrayar", "subrayo", "suma", "sumaba",
    "sumado", "sumar", "sume", "suministra", "suministraba", "suministrar", "suministro", "supera",
    "superado", "superar", "supere", "supieron", "supo", "tambien", "también", "tampoco", "tan",
    "tanto", "tema", "temas", "tener", "tenia", "tenido", "teniendo", "teniente", "tenientes",
    "tercera", "tercero", "termina", "terminado", "terminar", "termino", "territorio", "tiene",
    "tienen", "titulo", "todavía", "toma", "tomaba", "tomado", "tomar", "tomo", "trabaja",
    "trabajaba", "trabajado", "trabajar", "trabajo", "trace", "transporta", "transportaba",
    "transportado", "transportar", "transporte", "traslada", "trasladaba", "trasladar", "traslade",
    "traslado", "tratado", "tratados", "traza", "trazaba", "trazado", "trazar", "tripulacion",
    "tripulaciones", "tripulación", "tuvieron", "tuvo", "título", "títulos", "ubica", "ubicaba",
    "ubicado", "ubicar", "ubique", "ultima", "ultimo", "une", "unia", "unica", "unicas", "unico",
    "unicos", "unidad", "unidades", "unido", "unio", "unir", "uno", "usa", "usaba", "usado",
    "usar", "uso", "utiliza", "utilizaba", "utilizar", "utilize", "utilizo", "va", "varias",
    "varios", "ve", "veces", "velocidad", "vende", "vender", "vendido", "vendo", "ver", "verifica",
    "verificado", "verificar", "verifico", "vez", "viaja", "viajaba", "viajado", "viajar", "viaje",
    "vicealmirante", "vieron", "vio", "visita", "visitado", "visitar", "visite", "visto", "vive",
    "vivia", "vivido", "vivir", "volaba", "volaban", "volado", "volando", "volar", "volver",
    "volvia", "volvió", "vuela", "vuelo", "vuelos", "vuelto", "vuelve", "ya", "época", "órdenes",
    "última", "último", "única", "únicas", "único", "únicos",
}


def strip_front_matter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:].lstrip("\n")
    return text


COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
URL_RE = re.compile(r"(https?://\S+|www\.\S+)")
LIQUID_RE = re.compile(r"\{\{.*?\}\}")
TAG_RE = re.compile(r"<[^>]+>")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
WORD_RE = re.compile(r"[A-Za-zÀ-ÿ0-9]+")

EXCLUDED_H2 = {"referencias verificadas", "metadatos de control"}


def prose_blocks(text: str):
    """Yield bloques de prosa (texto con HTML ya depurado), bloque a bloque.

    Excluye front matter, comentarios HTML, líneas de cabecera Markdown,
    <hr>, y el contenido de las secciones EXCLUDED_H2 (plantilla/estructural).
    """
    text = strip_front_matter(text)
    text = COMMENT_RE.sub(" ", text)
    current_h2 = None
    for block in re.split(r"\n\s*\n", text):
        lines = []
        for line in block.splitlines():
            s = line.strip()
            if not s:
                continue
            m = HEADING_RE.match(s)
            if m:
                if len(m.group(1)) == 2:
                    current_h2 = m.group(2).strip().lower()
                continue
            if s.startswith("<hr") or s == "---":
                continue
            if current_h2 in EXCLUDED_H2:
                continue
            s = URL_RE.sub(" ", s)
            s = LIQUID_RE.sub(" ", s)
            s = TAG_RE.sub(" ", s)
            s = s.replace("*", " ").replace("_", " ").replace("`", " ")
            lines.append(s)
        if lines:
            yield " ".join(lines)


def tokenize(block: str):
    """Tokeniza conservando mayúsculas para detectar entidades: un tramo de
    2 o más palabras consecutivas con inicial mayúscula es UN token (nombre
    propio / denominación institucional); el resto, palabras minúsculas."""
    words = WORD_RE.findall(block)
    tokens = []
    i = 0
    n = len(words)
    while i < n:
        w = words[i]
        if w[0].isupper():
            j = i
            while j + 1 < n and words[j + 1][0].isupper():
                j += 1
            if j > i:
                tokens.append(" ".join(words[i:j + 1]).lower())
                i = j + 1
                continue
        tokens.append(w.lower())
        i += 1
    return tokens


def grams7(tokens):
    if len(tokens) < N:
        return set()
    return {tuple(tokens[i:i + N]) for i in range(len(tokens) - N + 1)}


def post_grams(path: str):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    grams = set()
    for block in prose_blocks(text):
        grams |= grams7(tokenize(block))
    return grams


def is_narrative(gram) -> bool:
    """Narrativo = contiene al menos un token de una sola palabra del
    vocabulario de clase abierta. Tokens-entidad (nombres propios) no
    cuentan; palabras funcionales tampoco."""
    return any(len(t.split(" ")) == 1 and t in NARRATIVE for t in gram)


def main() -> int:
    ap = argparse.ArgumentParser(description="Detector de ecos de 7-gramas de prosa")
    ap.add_argument("post", help="post a auditar")
    ap.add_argument("--corpus", default=DEFAULT_CORPUS,
                    help=f"directorio del corpus (def. {DEFAULT_CORPUS})")
    args = ap.parse_args()

    target = os.path.abspath(args.post)
    if not os.path.isfile(target):
        print(f"ERROR: no existe {target}", file=sys.stderr)
        return 2

    corpus = [p for p in sorted(glob.glob(os.path.join(args.corpus, "*.md")))
              if os.path.abspath(p) != target]
    if not corpus:
        print("ERROR: corpus vacío", file=sys.stderr)
        return 2

    # Pasa 1: contar cuántos posts distintos del corpus contienen cada grama.
    cnt = {}
    for p in corpus:
        for g in post_grams(p):
            cnt[g] = cnt.get(g, 0) + 1

    # Gramas del post auditado.
    tgrams = post_grams(target)
    narr = {g for g in tgrams if is_narrative(g)}
    nonnarr = tgrams - narr
    unique = {g for g in narr if cnt.get(g, 0) == 0}
    common = {g for g in narr if cnt.get(g, 0) >= 2}
    candidates = {g for g in narr if cnt.get(g, 0) == 1}

    # Pasa 2: resolver con qué post se comparte cada candidato.
    echoes = {}
    pending = set(candidates)
    for p in corpus:
        if not pending:
            break
        pg = post_grams(p)
        for g in (pg & pending):
            echoes[g] = os.path.basename(p)
            pending.discard(g)

    name = os.path.basename(target)
    print(f"ECO7 {name}")
    print(f"  corpus: {len(corpus)} posts")
    print(f"  gramos únicos: {len(tgrams)} (narrativos: {len(narr)}; "
          f"excluidos 100% no-narrativos: {len(nonnarr)})")
    print(f"  narrativos: exclusivos {len(unique)} | comunes a >=2 posts "
          f"(excluidos) {len(common)} | compartidos con 1 post: {len(candidates)}")
    if echoes:
        print(f"  ECOS DE CONTENIDO: {len(echoes)}")
        for g in sorted(echoes, key=lambda x: " ".join(x)):
            disp = " ".join(g)
            print(f'    - "{disp}"  <->  {echoes[g]}')
        print("SALIDA: ECOS (exit 1)")
        return 1
    print("  ecos de contenido: 0")
    print("SALIDA: LIMPIO (exit 0)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
