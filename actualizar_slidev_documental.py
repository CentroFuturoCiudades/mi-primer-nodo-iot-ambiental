# actualizar_slidev_documental.py
# Reemplaza slides/slides.md por una versión más documental, visual y editable.
#
# Ejecuta desde la raíz del proyecto:
#   cd C:\Users\A01649591\Documents\mi-primer-nodo-iot-ambiental
#   python .\actualizar_slidev_documental.py
#   npm run slides:dev
#
# Cuando te guste:
#   npm run slides:build
#   npm start

from pathlib import Path

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

1. Cada diapositiva está separada por:
   ---

2. Para poner una imagen:
   ![Texto alternativo](./assets/imagenes/mi-imagen.jpg)

3. Para poner un GIF:
   ![Animación](./assets/gifs/transistor.gif)

4. Para poner video:
   <video controls class="media-video">
     <source src="./assets/videos/desierto.mp4" type="video/mp4" />
   </video>

5. Para que un enlace salga del recuadro de Docusaurus:
   target="_top"
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
layout: center
class: desert-scene
---

<div class="content-front">

<p class="kicker">Escena 2 — La Tierra</p>

# Un chip empieza lejos del laboratorio

<v-clicks>

- Empieza en materiales.
- En minerales.
- En estructuras que podemos transformar.
- En una idea poderosa: controlar la electricidad.

</v-clicks>

</div>

<!--
Si tienes video de desierto, reemplaza esta diapositiva por:
<video class="bg-video" autoplay muted loop playsinline>
  <source src="./assets/videos/desierto.mp4" type="video/mp4" />
</video>
<div class="shade"></div>
<div class="content-front">
  <p class="kicker">Escena 2 — La Tierra</p>
  <h1>Un chip empieza lejos del laboratorio</h1>
</div>
-->

---

<p class="kicker">Escena 3 — Tres comportamientos</p>

# No todos los materiales tratan igual a la electricidad

<div class="three-col">
  <div class="concept-card">
    <div class="icon">⚡</div>
    <h2>Conductor</h2>
    <p>Deja pasar electricidad con facilidad.</p>
    <strong>Cobre</strong>
  </div>

  <div class="concept-card">
    <div class="icon">■</div>
    <h2>Aislante</h2>
    <p>Dificulta el paso de electricidad.</p>
    <strong>Plástico</strong>
  </div>

  <div class="concept-card highlight">
    <div class="icon">◐</div>
    <h2>Semiconductor</h2>
    <p>Puede dejar pasar o bloquear electricidad según cómo se controle.</p>
    <strong>Silicio</strong>
  </div>
</div>

<v-click>

> La computación no nace solo de tener electricidad. Nace de poder controlarla.

</v-click>

---

<p class="kicker">Escena 4 — Silicio</p>

# El silicio es útil porque puede cambiar de comportamiento

<div class="big-quote">
  No se trata solo de encender o apagar.  
  Se trata de construir decisiones.
</div>

<v-click>

## <span class="accent">Y una decisión física puede convertirse en información.</span>

</v-click>

---

<p class="kicker">Escena 5 — Información física</p>

# El cero y el uno no son magia

<div class="binary-strip">
  <span>No pasa corriente</span>
  <b>0</b>
  <span>Pasa corriente</span>
  <b>1</b>
</div>

<v-clicks>

- El microcontrolador trabaja con señales.
- Las señales representan información.
- Muchísimas señales juntas pueden guardar datos, ejecutar instrucciones y controlar el mundo físico.

</v-clicks>

---

<p class="kicker">Escena 6 — Transistor</p>

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

<!-- Para usar GIF: ![Transistor](./assets/gifs/transistor.gif) -->

---

<p class="kicker">Escena 7 — La idea más importante</p>

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

<p class="kicker">Escena 8 — Compuertas</p>

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

<p class="kicker">Escena 9 — Memoria</p>

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

<p class="kicker">Escena 10 — ALU</p>

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

<p class="kicker">Escena 11 — Oblea y chip</p>

# Una ciudad microscópica

<div class="wafer-visual"></div>

<v-clicks>

- En una oblea se fabrican muchos chips.
- En cada chip hay regiones que recuerdan, calculan y se comunican.
- Un circuito integrado es una ciudad construida a escala microscópica.

</v-clicks>

<!-- Para imagen real: ![Oblea de silicio](./assets/imagenes/oblea.jpg) -->

---

<p class="kicker">Escena 12 — Analogía principal</p>

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

<p class="kicker">Escena 13 — Dentro del microcontrolador</p>

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

<p class="kicker">Escena 14 — Cargar un programa</p>

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

<p class="kicker">Escena 15 — Programa</p>

# Un programa es una lista ordenada de instrucciones

<v-clicks>

- La CPU no entiende “toda la historia” al mismo tiempo.
- Lee una instrucción.
- La interpreta.
- La ejecuta.
- Avanza a la siguiente.

</v-clicks>

---

<p class="kicker">Escena 16 — Contador de programa</p>

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

<p class="kicker">Escena 17 — Sin entrar en ensamblador</p>

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

<p class="kicker">Escena 18 — Reloj</p>

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

<p class="kicker">Escena 19 — Delay</p>

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

<p class="kicker">Escena 20 — GPIO</p>

# El LED no entiende código

<v-clicks>

- El LED responde a voltaje.
- El microcontrolador traduce instrucciones en señales físicas.
- Esa traducción ocurre por las patitas de entrada/salida.

</v-clicks>

---

<p class="kicker">Escena 21 — Primer parpadeo</p>

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

<p class="kicker">Escena 22 — Variables</p>

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

<p class="kicker">Escena 23 — Decisiones</p>

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

<p class="kicker">Escena 24 — Sensores</p>

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

<p class="kicker">Escena 25 — Ciudad</p>

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

<style>
:root {
  --teal: #00b894;
  --amber: #f5b041;
  --dark: #031917;
}
.kicker {
  color: var(--amber);
  text-transform: uppercase;
  letter-spacing: 0.16em;
  font-size: 0.78rem;
  font-weight: 900;
}
.accent {
  color: var(--teal);
}
.cover-scene {
  min-height: 100%;
  display: grid;
  place-items: center;
  background:
    radial-gradient(circle at 85% 20%, rgba(245,176,65,.20), transparent 28%),
    radial-gradient(circle at 12% 14%, rgba(0,184,148,.28), transparent 30%),
    linear-gradient(120deg, #020303, #063a37);
  color: white;
  padding: 3rem;
  margin: -1rem;
  border-radius: 0;
}
.cover-scene h1 {
  font-size: 4.8rem;
  line-height: .92;
  max-width: 1000px;
}
.subtitle {
  color: rgba(255,255,255,.72);
  font-size: 1.35rem;
  max-width: 900px;
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
  background: radial-gradient(circle at top right, rgba(245,176,65,.18), transparent 30%),
              linear-gradient(120deg, #020303, #063a37);
}
.desert-scene {
  background:
    radial-gradient(circle at 20% 10%, rgba(245,176,65,.30), transparent 28%),
    radial-gradient(circle at 80% 80%, rgba(0,184,148,.12), transparent 30%),
    linear-gradient(120deg, #3b2a18, #050505 70%);
}
.content-front {
  position: relative;
  z-index: 2;
}
.big-quote {
  font-size: 2rem;
  line-height: 1.25;
  color: rgba(255,255,255,.8);
  margin: 2rem auto;
  max-width: 900px;
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
.bg-video {
  position: fixed;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.shade {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,.55);
}
</style>
'''

assets_readme = r'''# Recursos de la presentación

Coloca aquí tus recursos visuales.

## Imágenes

```text
slides/assets/imagenes/oblea.jpg
slides/assets/imagenes/microcontrolador.jpg
slides/assets/imagenes/sensor.jpg
```

Uso en `slides.md`:

```markdown
![Oblea de silicio](./assets/imagenes/oblea.jpg)
```

## GIFs

```text
slides/assets/gifs/transistor.gif
slides/assets/gifs/reloj.gif
```

Uso:

```markdown
![Transistor](./assets/gifs/transistor.gif)
```

## Videos

```text
slides/assets/videos/desierto.mp4
slides/assets/videos/ciudad.mp4
```

Uso:

```html
<video controls class="media-video">
  <source src="./assets/videos/desierto.mp4" type="video/mp4" />
</video>
```
'''

for d in ["slides/assets/imagenes", "slides/assets/gifs", "slides/assets/videos"]:
    ensure_dir(d)

write("slides/slides.md", slides_md)
write("slides/assets/README.md", assets_readme)

print("\nListo. Ahora ejecuta:")
print("  npm run slides:dev")
print("\nCuando te guste:")
print("  npm run slides:build")
print("  npm start")
