# actualizar_presentacion_slidev_completa.py
# Actualiza la presentación Slidev completa con una versión documental.
#
# Uso:
#   cd C:\Users\A01649591\Documents\mi-primer-nodo-iot-ambiental
#   python .\actualizar_presentacion_slidev_completa.py
#   npm install
#   npm run slides:dev
#
# Para integrar en Docusaurus:
#   npm run slides:build
#   npm start

from pathlib import Path
import json

ROOT = Path.cwd()

def write(path, content):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"OK: {path}")

def ensure_dir(path):
    p = ROOT / path
    p.mkdir(parents=True, exist_ok=True)
    gitkeep = p / ".gitkeep"
    if not gitkeep.exists():
        gitkeep.write_text("", encoding="utf-8")
    print(f"OK: {path}")

ensure_dir("slides/assets/imagenes")
ensure_dir("slides/assets/gifs")
ensure_dir("slides/assets/videos")

svg_conductores = r'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#041816"/>
      <stop offset="55%" stop-color="#073b36"/>
      <stop offset="100%" stop-color="#1f2c1d"/>
    </linearGradient>
    <linearGradient id="card" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.14"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0.06"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="18" stdDeviation="20" flood-color="#000000" flood-opacity="0.35"/>
    </filter>
    <style>
      .title{font-family:Inter,Segoe UI,Arial,sans-serif;font-size:68px;font-weight:900;fill:#fff;letter-spacing:-2px}
      .subtitle{font-family:Inter,Segoe UI,Arial,sans-serif;font-size:30px;font-weight:500;fill:#c8d8d4}
      .kicker{font-family:Inter,Segoe UI,Arial,sans-serif;font-size:25px;font-weight:900;fill:#f5b041;letter-spacing:7px}
      .cardTitle{font-family:Inter,Segoe UI,Arial,sans-serif;font-size:38px;font-weight:900;fill:#fff}
      .cardText{font-family:Inter,Segoe UI,Arial,sans-serif;font-size:25px;font-weight:500;fill:#dbe9e5}
      .small{font-family:Inter,Segoe UI,Arial,sans-serif;font-size:21px;font-weight:700;fill:#f5b041}
      .zeroone{font-family:Inter,Segoe UI,Arial,sans-serif;font-size:46px;font-weight:900;fill:#00b894}
      .caption{font-family:Inter,Segoe UI,Arial,sans-serif;font-size:25px;font-weight:800;fill:#fff}
    </style>
  </defs>
  <rect width="1600" height="900" fill="url(#bg)"/>
  <circle cx="1290" cy="120" r="230" fill="#f5b041" opacity="0.10"/>
  <circle cx="250" cy="780" r="260" fill="#00b894" opacity="0.10"/>
  <text x="80" y="95" class="kicker">MATERIALES ELECTRÓNICOS</text>
  <text x="80" y="175" class="title">Conductores, aislantes y semiconductores</text>
  <text x="80" y="225" class="subtitle">La diferencia clave no es “tener electricidad”, sino poder controlar su paso.</text>
  <g transform="translate(80,300)" filter="url(#shadow)">
    <rect width="440" height="430" rx="36" fill="url(#card)" stroke="#ffffff" stroke-opacity="0.18"/>
    <text x="42" y="70" class="cardTitle">Conductor</text>
    <text x="42" y="115" class="small">La corriente pasa con facilidad</text>
    <path d="M65 230 C140 150, 240 310, 355 210" fill="none" stroke="#f5b041" stroke-width="16" stroke-linecap="round"/>
    <circle cx="90" cy="210" r="18" fill="#f5b041"/>
    <circle cx="175" cy="205" r="18" fill="#f5b041"/>
    <circle cx="260" cy="245" r="18" fill="#f5b041"/>
    <circle cx="340" cy="215" r="18" fill="#f5b041"/>
    <text x="42" y="345" class="cardText">Ejemplos: cobre, aluminio, oro.</text>
    <text x="42" y="383" class="cardText">Se usa para cables y contactos.</text>
  </g>
  <g transform="translate(580,300)" filter="url(#shadow)">
    <rect width="440" height="430" rx="36" fill="url(#card)" stroke="#00b894" stroke-opacity="0.9"/>
    <text x="42" y="70" class="cardTitle">Semiconductor</text>
    <text x="42" y="115" class="small">La corriente se puede controlar</text>
    <rect x="85" y="177" width="270" height="92" rx="22" fill="#0b4c46" stroke="#00b894" stroke-width="5"/>
    <text x="150" y="237" class="zeroone">0 / 1</text>
    <path d="M82 310 L358 310" stroke="#00b894" stroke-width="12" stroke-linecap="round" stroke-dasharray="24 18"/>
    <text x="42" y="345" class="cardText">Ejemplo: silicio.</text>
    <text x="42" y="383" class="cardText">Base para transistores y chips.</text>
  </g>
  <g transform="translate(1080,300)" filter="url(#shadow)">
    <rect width="440" height="430" rx="36" fill="url(#card)" stroke="#ffffff" stroke-opacity="0.18"/>
    <text x="42" y="70" class="cardTitle">Aislante</text>
    <text x="42" y="115" class="small">La corriente casi no pasa</text>
    <rect x="105" y="185" width="230" height="90" rx="18" fill="#f5f1df"/>
    <rect x="130" y="170" width="28" height="120" rx="10" fill="#b87948"/>
    <rect x="200" y="170" width="28" height="120" rx="10" fill="#b87948"/>
    <rect x="270" y="170" width="28" height="120" rx="10" fill="#b87948"/>
    <line x1="95" y1="230" x2="345" y2="230" stroke="#2a1a10" stroke-width="10" stroke-linecap="round"/>
    <text x="42" y="345" class="cardText">Ejemplos: plástico, vidrio, cerámica.</text>
    <text x="42" y="383" class="cardText">Se usa para proteger y separar.</text>
  </g>
  <g transform="translate(210,785)">
    <rect width="1180" height="72" rx="36" fill="#00b894" opacity="0.18" stroke="#00b894" stroke-opacity="0.55"/>
    <text x="55" y="47" class="caption">Un semiconductor permite construir decisiones: bloquear corriente o dejarla pasar. Esa es la base del transistor.</text>
  </g>
</svg>'''
write("slides/assets/imagenes/conductores_semiconductores_aislantes.svg", svg_conductores)

svg_tierra = r'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#51351f"/>
      <stop offset="100%" stop-color="#080604"/>
    </linearGradient>
    <linearGradient id="soil" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#c58a3a"/>
      <stop offset="50%" stop-color="#8b5a27"/>
      <stop offset="100%" stop-color="#3d2818"/>
    </linearGradient>
    <style>
      .kicker{font-family:Inter,Segoe UI,Arial,sans-serif;font-size:26px;font-weight:900;fill:#f5b041;letter-spacing:7px}
      .title{font-family:Inter,Segoe UI,Arial,sans-serif;font-size:78px;font-weight:900;fill:#fff;letter-spacing:-3px}
      .text{font-family:Inter,Segoe UI,Arial,sans-serif;font-size:32px;font-weight:600;fill:#eadfd3}
      .label{font-family:Inter,Segoe UI,Arial,sans-serif;font-size:26px;font-weight:900;fill:#061716}
      .chip{font-family:Inter,Segoe UI,Arial,sans-serif;font-size:28px;font-weight:900;fill:#00b894}
    </style>
  </defs>
  <rect width="1600" height="900" fill="url(#sky)"/>
  <path d="M0 610 C180 500 300 650 470 555 C640 460 820 620 1000 500 C1200 360 1370 480 1600 330 L1600 900 L0 900 Z" fill="url(#soil)"/>
  <path d="M0 705 C180 650 320 740 480 680 C680 610 770 710 970 630 C1150 560 1350 590 1600 500 L1600 900 L0 900 Z" fill="#5b351c" opacity=".78"/>
  <circle cx="1270" cy="130" r="260" fill="#f5b041" opacity=".12"/>
  <circle cx="380" cy="760" r="260" fill="#00b894" opacity=".10"/>
  <text x="90" y="115" class="kicker">DE LA TIERRA AL CHIP</text>
  <text x="90" y="215" class="title">Antes del sensor, hubo materiales</text>
  <text x="90" y="278" class="text">Los microcontroladores están hechos de materia transformada con precisión.</text>
  <g transform="translate(120,420)">
    <rect width="360" height="90" rx="45" fill="#f5b041"/>
    <text x="55" y="57" class="label">minerales</text>
  </g>
  <path d="M520 465 L690 465" stroke="#eadfd3" stroke-width="8" stroke-linecap="round"/>
  <path d="M670 440 L700 465 L670 490" fill="none" stroke="#eadfd3" stroke-width="8" stroke-linecap="round"/>
  <g transform="translate(720,420)">
    <rect width="360" height="90" rx="45" fill="#00b894"/>
    <text x="45" y="57" class="label">materiales electrónicos</text>
  </g>
  <path d="M1120 465 L1290 465" stroke="#eadfd3" stroke-width="8" stroke-linecap="round"/>
  <path d="M1270 440 L1300 465 L1270 490" fill="none" stroke="#eadfd3" stroke-width="8" stroke-linecap="round"/>
  <g transform="translate(1320,385)">
    <rect width="170" height="160" rx="24" fill="#061716" stroke="#00b894" stroke-width="7"/>
    <rect x="34" y="42" width="102" height="76" rx="12" fill="#0b4c46" stroke="#f5b041" stroke-width="4"/>
    <text x="38" y="145" class="chip">chip</text>
  </g>
  <text x="105" y="790" class="text">Silicio, cobre, aluminio y otros materiales permiten construir circuitos, conexiones y sensores.</text>
</svg>'''
write("slides/assets/imagenes/de_la_tierra_al_chip.svg", svg_tierra)

slides_md = r'''---
theme: default
title: De la arena al sensor inteligente
info: |
  Taller práctico para bachillerato.
  Historia visual del curso Mi primer nodo IoT ambiental.
class: text-center
drawings:
  persist: false
transition: fade
mdc: true
---

<!--
GUÍA RÁPIDA PARA EDITAR
- Cada diapositiva está separada por ---
- Imágenes: ![Texto](./assets/imagenes/archivo.jpg)
- GIFs: ![Animación](./assets/gifs/archivo.gif)
- Videos:
  <video controls class="media-video">
    <source src="./assets/videos/archivo.mp4" type="video/mp4" />
  </video>
-->

<div class="cover-scene">
  <p class="kicker">Taller IoT ambiental</p>

  <h1>De la arena al sensor inteligente</h1>

  <p class="subtitle">
    Una historia sobre materia, electricidad, microcontroladores y ciudades que aprenden a observarse.
  </p>

  <div class="mt-10 flex gap-4 justify-center">
    <a href="../actividades/antes-de-empezar" target="_top" class="btn-main">Ir a actividades</a>
  </div>
</div>

---
layout: center
class: scene-dark
---

<p class="kicker">Escena 1 — La pregunta</p>

# Antes del dato, hubo materia

<v-clicks>

- Antes del sensor, hubo silicio.
- Antes del código, hubo transistores.
- Antes del LED parpadeando, hubo millones de decisiones microscópicas.

</v-clicks>

## <span class="accent">¿Cómo puede un chip observar el mundo?</span>

---
layout: image-right
image: ./assets/imagenes/de_la_tierra_al_chip.svg
class: image-right-readable
---

<p class="kicker">Escena 2 — De la Tierra al chip</p>

# Minerales, elementos y materiales electrónicos

Un microcontrolador no aparece de la nada. Está hecho con materiales que vienen de la Tierra y que luego se transforman con mucha precisión.

<v-clicks>

- **No todo mineral sirve para hacer chips.**
- De algunos minerales se obtienen elementos importantes para la electrónica.
- El **silicio** es clave para fabricar semiconductores.
- Otros materiales ayudan en conexiones, baterías, pantallas y sensores.

</v-clicks>

<div class="note-box">
  Idea para recordar: un chip es materia organizada con muchísima precisión.
</div>

---

<p class="kicker">Precisión importante</p>

# ¿Son “tierras raras” todos los materiales de un chip?

No exactamente.

<div class="two-col">
  <div class="concept-card">
    <h2>Silicio</h2>
    <p>
      Es la base más común de muchos chips. Se obtiene a partir de minerales ricos en sílice
      y se purifica para fabricar obleas.
    </p>
  </div>

  <div class="concept-card">
    <h2>Tierras raras</h2>
    <p>
      Son elementos usados en varias tecnologías como imanes, pantallas y motores.
      Son importantes, pero no son “la base” de todos los chips.
    </p>
  </div>
</div>

<v-click>

## <span class="accent">Hoy seguiremos el camino: minerales → materiales electrónicos → microcontrolador.</span>

</v-click>

---
layout: image-right
image: ./assets/imagenes/conductores_semiconductores_aislantes.svg
class: image-right-readable
---

<p class="kicker">Escena 3 — Tres comportamientos eléctricos</p>

# Conductores, aislantes y semiconductores

Para construir electrónica necesitamos entender cómo se comportan los materiales frente a la electricidad.

<v-clicks>

- Un **conductor** deja pasar corriente con facilidad.
- Un **aislante** dificulta el paso de corriente.
- Un **semiconductor** puede cambiar su comportamiento si lo controlamos.

</v-clicks>

<div class="note-box">
  La clave no es solo tener electricidad: la clave es poder controlar su paso.
</div>

---

<p class="kicker">Escena 4 — La idea que conecta todo</p>

# Un semiconductor permite construir decisiones

<div class="binary-strip">
  <span>bloquea corriente</span>
  <b>0</b>
  <span>deja pasar corriente</span>
  <b>1</b>
</div>

<v-clicks>

- Con un comportamiento controlable podemos representar ceros y unos.
- Con ceros y unos podemos construir instrucciones.
- Con instrucciones podemos prender un LED, esperar un segundo o leer un sensor.

</v-clicks>

## <span class="accent">Aquí empieza el camino hacia el transistor.</span>

---

<p class="kicker">Escena 5 — Transistor</p>

# El transistor: un interruptor microscópico

<div class="switch-demo">
  <div class="switch-state off">
    0
    <small>apagado</small>
  </div>

  <div class="arrow">→</div>

  <div class="switch-state on">
    1
    <small>encendido</small>
  </div>
</div>

<v-click>

Un transistor decide poco. Millones de transistores pueden construir una computadora.

</v-click>

---

<p class="kicker">Escena 6 — La idea más importante</p>

# La complejidad nace por repetición

<div class="logic-flow">
  <div>1 transistor</div>
  <div>→</div>
  <div>muchos transistores</div>
  <div>→</div>
  <div>reglas</div>
  <div>→</div>
  <div>memoria y cálculo</div>
</div>

<v-clicks>

- Una pieza simple no parece inteligente.
- Muchas piezas simples, conectadas con orden, pueden hacer tareas complejas.
- Así se construye la lógica digital.

</v-clicks>

---

<p class="kicker">Escena 7 — Compuertas</p>

# Las compuertas son pequeñas reglas

<div class="truth-table">
  <div class="head">Entrada A</div>
  <div class="head">Entrada B</div>
  <div class="head">Salida</div>

  <div>0</div><div>0</div><div>0</div>
  <div>0</div><div>1</div><div>0</div>
  <div>1</div><div>0</div><div>0</div>
  <div>1</div><div>1</div><div class="on">1</div>
</div>

<v-click>

Con reglas simples podemos construir decisiones más grandes.

</v-click>

---

<p class="kicker">Escena 8 — Memoria</p>

# Algunos circuitos pueden recordar

<div class="memory-visual">
  <div>0</div>
  <div class="active">1</div>
  <div>0</div>
  <div class="active">1</div>
  <div class="active">1</div>
  <div>0</div>
  <div>0</div>
  <div class="active">1</div>
</div>

<v-clicks>

- Un bit guarda un estado.
- Muchos bits guardan números, textos, instrucciones y mediciones.
- En un microcontrolador, la memoria es esencial.

</v-clicks>

---

<p class="kicker">Escena 9 — ALU</p>

# La ALU es el taller de cálculo

<div class="alu-demo">
  <div>A = 7</div>
  <div class="alu">ALU<br><small>suma, compara, decide</small></div>
  <div>B = 3</div>
</div>

<v-click>

Cuando escribimos una condición como `if (co2 > 1000)`, la tarjeta debe comparar valores.

</v-click>

---

<p class="kicker">Escena 10 — Oblea y chip</p>

# Una ciudad microscópica

<div class="wafer-visual"></div>

<v-clicks>

- En una oblea se fabrican muchos chips.
- En cada chip hay regiones que recuerdan, calculan y se comunican.
- Un circuito integrado es una ciudad construida a escala microscópica.

</v-clicks>

---

<p class="kicker">Escena 11 — Analogía principal</p>

# El microcontrolador como una ciudad

<div class="city-grid">
  <div><b>CPU</b><span>centro de control</span></div>
  <div><b>ALU</b><span>taller de cálculo</span></div>
  <div><b>Flash</b><span>biblioteca del programa</span></div>
  <div><b>RAM</b><span>mesa de trabajo</span></div>
  <div><b>Reloj</b><span>metrónomo de la ciudad</span></div>
  <div><b>GPIO</b><span>puertas al exterior</span></div>
</div>

---

<p class="kicker">Escena 12 — Dentro del microcontrolador</p>

# ¿Qué vive dentro del chip?

<div class="mcu-map">
  <div class="flash">Flash<br><span>programa</span></div>
  <div class="cpu">CPU<br><span>lee y ejecuta</span></div>
  <div class="gpio">GPIO<br><span>mundo físico</span></div>
  <div class="ram">RAM<br><span>variables</span></div>
  <div class="alu">ALU<br><span>cálculo</span></div>
  <div class="clock">Reloj<br><span>ritmo</span></div>
</div>

<v-click>

Esto es lo que hace que la tarjeta sea algo más que un simple circuito.

</v-click>

---

<p class="kicker">Escena 13 — Cargar un programa</p>

# Cuando cargamos código, no solo copiamos texto

<div class="program-flow">
  <div>Código Arduino</div>
  <div>→</div>
  <div>Compilación</div>
  <div>→</div>
  <div>Instrucciones</div>
  <div>→</div>
  <div>Memoria Flash</div>
</div>

<v-click>

El programa queda guardado en la tarjeta, por eso puede seguir funcionando aunque la desconectes y la vuelvas a conectar.

</v-click>

---

<p class="kicker">Escena 14 — Programa</p>

# Un programa es una lista ordenada de instrucciones

<v-clicks>

- La CPU no entiende “toda la historia” al mismo tiempo.
- Lee una instrucción.
- La interpreta.
- La ejecuta.
- Avanza a la siguiente.

</v-clicks>

---

<p class="kicker">Escena 15 — Contador de programa</p>

# ¿Cómo sabe cuál instrucción sigue?

<div class="instruction-scene">
  <div class="memory-list">
    <div class="instruction active">1. pinMode(...)</div>
    <div class="instruction">2. digitalWrite(HIGH)</div>
    <div class="instruction">3. delay(1000)</div>
    <div class="instruction">4. digitalWrite(LOW)</div>
    <div class="instruction">5. delay(1000)</div>
  </div>

  <div class="cpu-card">
    CPU<br>
    <span>leer → interpretar → ejecutar → avanzar</span>
  </div>
</div>

<v-click>

El contador de programa funciona como un dedo que señala la siguiente instrucción.

</v-click>

---

<p class="kicker">Escena 16 — Sin entrar en ensamblador</p>

# Arduino es una forma humana de escribir instrucciones

```cpp
digitalWrite(LED_BUILTIN, HIGH);
delay(1000);
```

<v-clicks>

- Nosotros escribimos algo fácil de leer.
- El compilador lo transforma en pasos más pequeños.
- El microcontrolador ejecuta esos pasos con su CPU.

</v-clicks>

---

<p class="kicker">Escena 17 — Reloj</p>

# El microcontrolador tiene ritmo

<div class="clock-wave">
  <span></span><span></span><span></span><span></span><span></span><span></span>
</div>

<v-clicks>

- El oscilador genera pulsos.
- Los pulsos marcan el ritmo interno.
- No todo ocurre al mismo tiempo: la tarjeta avanza paso a paso.

</v-clicks>

---

<p class="kicker">Escena 18 — Delay</p>

# `delay(1000)` no es magia

<div class="delay-flow">
  <div>Reloj</div>
  <div>→</div>
  <div>Temporizador</div>
  <div>→</div>
  <div>1000 ms</div>
  <div>→</div>
  <div>Siguiente instrucción</div>
</div>

<v-click>

Cuando cambias `1000` por `100`, cambias cuánto espera la tarjeta antes de continuar.

</v-click>

<div class="mt-8">
  <a href="../actividades/tiempo-dentro-del-chip" target="_top" class="btn-main">Actividad: tiempo dentro del chip</a>
</div>

---

<p class="kicker">Escena 19 — GPIO</p>

# El LED no entiende código

<v-clicks>

- El LED responde a voltaje.
- El microcontrolador traduce instrucciones en señales físicas.
- Esa traducción ocurre por las patitas de entrada/salida.

</v-clicks>

---

<p class="kicker">Escena 20 — Primer parpadeo</p>

# Una instrucción puede cambiar el mundo físico

<div class="gpio-flow">
  <div>CPU ejecuta</div>
  <div>→</div>
  <div>registro de salida</div>
  <div>→</div>
  <div>GPIO cambia voltaje</div>
  <div>→</div>
  <div>LED prende</div>
</div>

```cpp
pinMode(LED_BUILTIN, OUTPUT);
digitalWrite(LED_BUILTIN, HIGH);
```

<div class="mt-8">
  <a href="../actividades/primer-parpadeo" target="_top" class="btn-main">Actividad: primer parpadeo</a>
</div>

---

<p class="kicker">Escena 21 — Variables</p>

# Una variable es un dato temporal

```cpp
int co2 = 900;
```

<v-clicks>

- La variable vive en la memoria de trabajo.
- Puede cambiar mientras el programa corre.
- Nos permite tomar decisiones.

</v-clicks>

---

<p class="kicker">Escena 22 — Decisiones</p>

# La tarjeta también puede decidir

```cpp
if (co2 > 1000) {
  // activar alerta
}
```

<v-clicks>

- La RAM guarda el valor.
- La ALU compara.
- La CPU decide qué camino seguir.

</v-clicks>

---

<p class="kicker">Escena 23 — Sensores</p>

# Un sensor convierte el ambiente en números

<div class="sensor-flow">
  <div>Aire</div>
  <div>→</div>
  <div>Sensor</div>
  <div>→</div>
  <div>Tarjeta</div>
  <div>→</div>
  <div>Datos</div>
  <div>→</div>
  <div>Decisión</div>
</div>

<v-click>

CO₂, temperatura, humedad y partículas pueden convertirse en mediciones.

</v-click>

<div class="mt-8">
  <a href="../actividades/medir-co2" target="_top" class="btn-main">Actividad: medir CO₂</a>
</div>

---

<p class="kicker">Escena 24 — Ciudad</p>

# Un dato pequeño puede contar una historia grande

<v-clicks>

- Un LED nos enseña a controlar una salida.
- Un sensor nos enseña a leer el ambiente.
- Muchas mediciones pueden ayudar a entender espacios reales de una ciudad.

</v-clicks>

---

layout: center
class: text-center scene-dark
---

<p class="kicker">Cierre</p>

# De la arena al sensor inteligente

<v-clicks>

- Materia.
- Transistores.
- Microcontrolador.
- Código.
- Señales.
- Sensores.
- Ciudad.

</v-clicks>

<div class="mt-10 flex gap-4 justify-center">
  <a href="../actividades/antes-de-empezar" target="_top" class="btn-main">Comenzar actividades</a>
  <a href="../" target="_top" class="btn-ghost">Volver al inicio</a>
</div>
'''
write("slides/slides.md", slides_md)

style_css = r''':root {
  --teal: #00b894;
  --amber: #f5b041;
  --dark: #031917;
}

.slidev-layout {
  font-family: "Inter", "Nunito Sans", system-ui, sans-serif;
}

.cover-scene {
  min-height: 100%;
  display: grid;
  place-items: center;
  text-align: center;
  background:
    radial-gradient(circle at 85% 20%, rgba(245,176,65,.20), transparent 28%),
    radial-gradient(circle at 12% 14%, rgba(0,184,148,.28), transparent 30%),
    linear-gradient(120deg, #020303, #063a37);
  color: white;
  padding: 3rem;
  margin: -1rem;
}

.cover-scene h1 {
  font-size: 4.8rem;
  line-height: .92;
  max-width: 1050px;
  font-weight: 900;
  letter-spacing: -0.06em;
}

.subtitle {
  color: rgba(255,255,255,.72);
  font-size: 1.35rem;
  max-width: 900px;
  margin: 1.5rem auto;
}

.kicker {
  color: var(--amber);
  text-transform: uppercase;
  letter-spacing: 0.16em;
  font-size: 0.78rem;
  font-weight: 900;
  margin-bottom: 1rem;
}

.accent {
  color: var(--teal);
}

.btn-main, .btn-ghost {
  display: inline-block;
  border-radius: 999px;
  padding: 0.7rem 1.1rem;
  font-weight: 900;
  text-decoration: none;
}

.btn-main {
  background: var(--teal);
  color: #041212;
}

.btn-ghost {
  border: 1px solid rgba(255,255,255,.35);
  color: white;
}

.scene-dark {
  background:
    radial-gradient(circle at top right, rgba(245,176,65,.18), transparent 30%),
    linear-gradient(120deg, #020303, #063a37);
  color: white;
}

.image-right-readable h1 {
  font-size: 2.2rem;
  line-height: 1.05;
}

.image-right-readable p,
.image-right-readable li {
  font-size: 1.05rem;
}

.note-box {
  margin-top: 1.3rem;
  padding: 0.85rem 1rem;
  border-radius: 1rem;
  border: 1px solid rgba(0, 184, 148, 0.45);
  background: rgba(0, 184, 148, 0.12);
  color: rgba(255,255,255,0.88);
  font-weight: 800;
}

.two-col {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.1rem;
  margin-top: 2rem;
}

.two-col .concept-card p {
  font-size: 1rem;
  line-height: 1.35;
}

.three-col {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-top: 2rem;
}

.concept-card, .city-grid div, .mcu-map div {
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.16);
  border-radius: 1.1rem;
  padding: 1rem;
}

.concept-card h2 {
  font-size: 1.4rem;
}

.concept-card p {
  font-size: .95rem;
}

.concept-card strong {
  color: var(--amber);
}

.concept-card.highlight {
  border-color: var(--teal);
  box-shadow: 0 0 35px rgba(0,184,148,.25);
}

.icon {
  font-size: 2rem;
}

.binary-strip, .logic-flow, .program-flow, .delay-flow, .gpio-flow, .sensor-flow {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: .7rem;
  margin: 2rem 0;
}

.binary-strip span, .logic-flow div, .program-flow div, .delay-flow div, .gpio-flow div, .sensor-flow div {
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.15);
  border-radius: 999px;
  padding: .6rem .9rem;
  font-weight: 800;
}

.binary-strip b {
  color: var(--teal);
  font-size: 2rem;
}

.switch-demo {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  margin: 2rem 0;
}

.switch-state {
  width: 170px;
  height: 170px;
  border-radius: 1.4rem;
  display: grid;
  place-items: center;
  font-size: 3rem;
  font-weight: 900;
}

.switch-state small {
  display: block;
  font-size: .9rem;
  color: rgba(255,255,255,.7);
}

.switch-state.off {
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.18);
}

.switch-state.on {
  background: rgba(0,184,148,.22);
  border: 1px solid var(--teal);
}

.arrow {
  color: var(--amber);
  font-size: 3rem;
}

.truth-table {
  display: grid;
  grid-template-columns: repeat(3, 150px);
  justify-content: center;
  margin-top: 1rem;
}

.truth-table div {
  border: 1px solid rgba(255,255,255,.2);
  padding: .5rem;
}

.truth-table .head {
  background: rgba(0,184,148,.2);
  color: var(--teal);
  font-weight: 900;
}

.truth-table .on {
  color: var(--amber);
  font-weight: 900;
}

.memory-visual {
  display: grid;
  grid-template-columns: repeat(8, 76px);
  justify-content: center;
  gap: .55rem;
  margin: 2rem 0;
}

.memory-visual div {
  height: 76px;
  display: grid;
  place-items: center;
  border-radius: .9rem;
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.15);
  font-weight: 900;
}

.memory-visual .active {
  background: rgba(0,184,148,.22);
  border-color: var(--teal);
}

.alu-demo {
  display: grid;
  grid-template-columns: 1fr 1.4fr 1fr;
  gap: 1rem;
  align-items: center;
  max-width: 920px;
  margin: 2rem auto;
}

.alu-demo > div {
  border-radius: 1.2rem;
  padding: 1rem;
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.16);
  font-weight: 900;
}

.alu-demo .alu {
  background: rgba(245,176,65,.16);
  color: var(--amber);
}

.wafer-visual {
  width: 360px;
  height: 360px;
  border-radius: 50%;
  margin: 1rem auto;
  background:
    repeating-radial-gradient(circle, rgba(255,255,255,.16) 0 2px, transparent 2px 18px),
    conic-gradient(from 20deg, rgba(0,184,148,.24), rgba(245,176,65,.18), rgba(80,180,255,.16), rgba(0,184,148,.24));
  animation: rotateWafer 30s linear infinite;
}

@keyframes rotateWafer {
  from { transform: rotate(0); }
  to { transform: rotate(360deg); }
}

.city-grid, .mcu-map {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  max-width: 1000px;
  margin: 2rem auto;
}

.city-grid span, .mcu-map span {
  display: block;
  color: rgba(255,255,255,.72);
  font-size: .9rem;
}

.mcu-map .cpu {
  border-color: var(--teal);
  box-shadow: 0 0 35px rgba(0,184,148,.18);
}

.instruction-scene {
  display: grid;
  grid-template-columns: 1.1fr .9fr;
  gap: 1.2rem;
  max-width: 1000px;
  margin: 2rem auto;
  align-items: center;
}

.memory-list {
  display: grid;
  gap: .4rem;
}

.instruction {
  text-align: left;
  padding: .6rem .8rem;
  border-radius: .8rem;
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.14);
  font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
}

.instruction.active {
  border-color: var(--amber);
  color: var(--amber);
}

.cpu-card {
  border-radius: 1.2rem;
  padding: 1.4rem;
  background: rgba(0,184,148,.16);
  border: 1px solid rgba(0,184,148,.3);
  color: var(--teal);
  font-weight: 900;
}

.cpu-card span {
  display: block;
  margin-top: .5rem;
  color: rgba(255,255,255,.72);
}

.clock-wave {
  display: flex;
  justify-content: center;
  align-items: flex-end;
  gap: .25rem;
  height: 180px;
  margin: 2rem 0;
}

.clock-wave span {
  width: 72px;
  height: 120px;
  border-top: 10px solid var(--teal);
  border-left: 10px solid var(--teal);
  border-right: 10px solid var(--teal);
  animation: pulseGlow 1.8s ease-in-out infinite;
}

.clock-wave span:nth-child(even) {
  transform: translateY(60px);
  border-top-color: var(--amber);
  border-left-color: var(--amber);
  border-right-color: var(--amber);
}

@keyframes pulseGlow {
  0%, 100% { opacity: .45; }
  50% { opacity: 1; }
}

.media-video {
  width: 85%;
  max-height: 60vh;
  border-radius: 1rem;
}
'''
write("slides/style.css", style_css)
write("style.css", style_css)

global_top = r'''<template>
  <button class="exit-course-button" @click="exitToCourse">
    Salir al curso
  </button>
</template>

<script setup>
import { onMounted, onBeforeUnmount } from 'vue'

function getExitUrl() {
  if (window.location.hostname === 'localhost' && window.location.port === '3030') {
    return 'http://localhost:3000/mi-primer-nodo-iot-ambiental/slides/'
  }
  return '../slides/'
}

function exitToCourse() {
  window.top.location.href = getExitUrl()
}

function handleKeydown(event) {
  if (event.key === 'Escape') {
    exitToCourse()
  }
}

onMounted(() => {
  window.addEventListener('keydown', handleKeydown)
})

onBeforeUnmount(() => {
  window.removeEventListener('keydown', handleKeydown)
})
</script>

<style>
.exit-course-button {
  position: fixed;
  top: 18px;
  right: 22px;
  z-index: 9999;
  border: 1px solid rgba(255,255,255,0.22);
  border-radius: 999px;
  background: rgba(0,0,0,0.55);
  color: white;
  padding: 0.45rem 0.85rem;
  font-size: 0.85rem;
  font-weight: 800;
  cursor: pointer;
  backdrop-filter: blur(8px);
}
.exit-course-button:hover {
  background: #00b894;
  color: #041212;
  border-color: #00b894;
}
@media print {
  .exit-course-button {
    display: none;
  }
}
</style>'''
write("slides/global-top.vue", global_top)

pkg_path = ROOT / "package.json"
if pkg_path.exists():
    pkg = json.loads(pkg_path.read_text(encoding="utf-8"))
else:
    pkg = {"scripts": {}, "devDependencies": {}}

pkg.setdefault("scripts", {})
pkg["scripts"]["slides:dev"] = "slidev slides/slides.md --open"
pkg["scripts"]["slides:build"] = "slidev build slides/slides.md --base /mi-primer-nodo-iot-ambiental/presentacion/ --out ../static/presentacion"
pkg.setdefault("devDependencies", {})
pkg["devDependencies"].setdefault("@slidev/cli", "^52.0.0")
pkg["devDependencies"].setdefault("@slidev/theme-default", "^0.25.0")
pkg_path.write_text(json.dumps(pkg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("OK: package.json actualizado")

assets_readme = r'''# Recursos visuales de la presentación

Archivos generados por este script:

```text
slides/assets/imagenes/de_la_tierra_al_chip.svg
slides/assets/imagenes/conductores_semiconductores_aislantes.svg
```

Puedes reemplazar `de_la_tierra_al_chip.svg` por una foto real de minería con el mismo nombre.
'''
write("slides/assets/README.md", assets_readme)

print("\nLISTO.")
print("Ahora ejecuta:")
print("  npm install")
print("  npm run slides:dev")
print("\nPara integrar en Docusaurus:")
print("  npm run slides:build")
print("  npm start")
