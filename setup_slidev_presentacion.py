# setup_slidev_presentacion.py
# Configura Slidev dentro del proyecto Docusaurus del taller.
#
# Ejecutar desde la raíz del proyecto:
#   cd C:\Users\A01649591\Documents\mi-primer-nodo-iot-ambiental
#   python .\setup_slidev_presentacion.py
#   npm install
#   npm run slides:dev
#
# Para integrar el resultado en Docusaurus:
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

# De la arena al sensor inteligente

Una historia sobre materia, electricidad, chips, código y ciudades que aprenden a observarse.

<div class="mt-10 flex gap-4 justify-center">
  <a href="../actividades/antes-de-empezar" class="btn-main">Ir a actividades</a>
</div>

---
layout: center
class: scene-dark
---

<p class="kicker">Acto 1 — La materia</p>

# Antes del dato, hubo materia

<v-clicks>

- Antes del sensor, hubo silicio.
- Antes del código, hubo transistores.
- Antes de una ciudad inteligente, hubo una pregunta:

</v-clicks>

## <span class="accent">¿cómo puede un chip observar el mundo?</span>

<!--
Para usar video de fondo en esta escena, coloca:
slides/assets/videos/desierto.mp4

Y cambia esta diapositiva por algo como:

<video class="bg-video" autoplay muted loop playsinline>
  <source src="./assets/videos/desierto.mp4" type="video/mp4" />
</video>
<div class="shade"></div>
<div class="content-front">
  ...contenido...
</div>
-->

---

<p class="kicker">Pregunta de arranque</p>

# ¿De qué está hecho un chip?

<v-clicks>

- No empieza en una aplicación.
- No empieza en Arduino.
- Empieza en materiales que podemos transformar y organizar.

</v-clicks>

## <span class="accent">Materia organizada para controlar electricidad.</span>

---

<p class="kicker">Silicio</p>

# El silicio es especial

No es simplemente un conductor.  
No es simplemente un aislante.

<v-click>

## Es un <span class="accent">semiconductor</span>.

</v-click>

---

<p class="kicker">Controlar la electricidad</p>

# Tres materiales, tres comportamientos

<div class="three-col">
  <div class="concept-card">
    <div class="icon">⚡</div>
    <h2>Conductor</h2>
    <p>Deja pasar electricidad con facilidad.</p>
    <strong>Ejemplo: cobre</strong>
  </div>

  <div class="concept-card">
    <div class="icon">■</div>
    <h2>Aislante</h2>
    <p>Dificulta el paso de electricidad.</p>
    <strong>Ejemplo: plástico</strong>
  </div>

  <div class="concept-card highlight">
    <div class="icon">◐</div>
    <h2>Semiconductor</h2>
    <p>Puede comportarse de una forma u otra según cómo se controle.</p>
    <strong>Ejemplo: silicio</strong>
  </div>
</div>

<v-click>

> La computación no nace solo de la electricidad. Nace de poder controlarla.

</v-click>

---

<p class="kicker">Información física</p>

# Controlar corriente permite representar información

<div class="binary-strip">
  <span>no pasa corriente</span>
  <b>0</b>
  <span>pasa corriente</span>
  <b>1</b>
</div>

<v-click>

Con muchos elementos capaces de representar 0 y 1 podemos construir lógica digital.

</v-click>

---

<p class="kicker">Acto 2 — El transistor</p>

# Un transistor es un interruptor microscópico

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

Con millones de interruptores así, podemos construir memoria, cálculo y control.

</v-click>

<!--
Para usar un GIF real:
![Transistor como interruptor](./assets/gifs/transistor.gif)
-->

---

<p class="kicker">De uno a millones</p>

# Un transistor solo decide poco

<v-clicks>

- Muchos transistores pueden formar reglas.
- Muchas reglas pueden formar memoria y cálculo.
- La complejidad aparece al repetir piezas simples.

</v-clicks>

---

<p class="kicker">Acto 3 — Funciones digitales</p>

# De transistores a compuertas lógicas

<div class="logic-flow">
  <div>Transistores</div>
  <div>→</div>
  <div>Compuertas</div>
  <div>→</div>
  <div>Bloques digitales</div>
  <div>→</div>
  <div>Microcontrolador</div>
</div>

<v-click>

Las compuertas son pequeñas reglas que combinan ceros y unos.

</v-click>

---

<p class="kicker">Ejemplo simple</p>

# Una regla con dos entradas

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

<p class="kicker">Memoria</p>

# Algunos circuitos pueden recordar estados

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

<v-click>

Muchos bits organizados permiten guardar datos e instrucciones.

</v-click>

---

<p class="kicker">ALU</p>

# La ALU es el taller de cálculo

<div class="alu-demo">
  <div>A = 7</div>
  <div class="alu">ALU<br><small>suma, compara, decide</small></div>
  <div>B = 3</div>
</div>

<v-click>

Cuando el programa pregunta `if (co2 > 1000)`, el microcontrolador necesita comparar valores.

</v-click>

---

<p class="kicker">Acto 4 — El chip</p>

# Un circuito integrado es una ciudad microscópica

<v-clicks>

- Algunas zonas recuerdan.
- Otras calculan.
- Otras se comunican con el exterior.

</v-clicks>

<!--
Para usar una imagen:
![Oblea de silicio](./assets/imagenes/oblea.jpg)
-->

---

<p class="kicker">Analogía</p>

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

<p class="kicker">Microcontrolador</p>

# Una computadora pequeña dentro de un chip

<div class="mcu-map">
  <div class="flash">Flash<br><span>programa</span></div>
  <div class="cpu">CPU<br><span>lee y ejecuta</span></div>
  <div class="gpio">GPIO<br><span>mundo físico</span></div>
  <div class="ram">RAM<br><span>variables</span></div>
  <div class="alu">ALU<br><span>cálculo</span></div>
  <div class="clock">Reloj<br><span>ritmo</span></div>
</div>

---

<p class="kicker">Acto 5 — El programa</p>

# Un programa es una lista ordenada de instrucciones

<v-clicks>

- Nosotros escribimos código fácil de leer.
- La tarjeta ejecuta instrucciones mucho más pequeñas.
- La CPU lee, interpreta, ejecuta y avanza.

</v-clicks>

---

<p class="kicker">Secuencia</p>

# La CPU avanza paso a paso

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

El contador de programa señala cuál instrucción toca ejecutar.

</v-click>

---

<p class="kicker">Sin entrar en ensamblador</p>

# Arduino es una forma humana de escribir instrucciones

```cpp
digitalWrite(LED_BUILTIN, HIGH);
delay(1000);
```

<v-click>

Antes de ejecutarse, estas líneas se traducen a pasos pequeños que el procesador sí puede realizar.

</v-click>

---

<p class="kicker">Acto 6 — El tiempo dentro del chip</p>

# ¿Cómo sabe esperar?

<div class="clock-wave">
  <span></span><span></span><span></span><span></span><span></span><span></span>
</div>

<v-click>

El oscilador genera pulsos. Esos pulsos marcan el ritmo interno.

</v-click>

---

<p class="kicker">delay(1000)</p>

# Esperar es contar tiempo

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

Si cambiamos `1000` por `100`, el LED parpadea más rápido.

</v-click>

<div class="mt-8">
  <a href="../actividades/tiempo-dentro-del-chip" class="btn-main">Ir a la actividad del tiempo</a>
</div>

---

<p class="kicker">Acto 7 — Puertas al mundo</p>

# El LED no entiende código

<v-clicks>

- El LED responde a voltaje.
- El microcontrolador traduce instrucciones en señales físicas.

</v-clicks>

---

<p class="kicker">GPIO</p>

# Una patita de entrada o salida

<div class="gpio-flow">
  <div>CPU ejecuta</div>
  <div>→</div>
  <div>Registro de salida</div>
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
  <a href="../actividades/primer-parpadeo" class="btn-main">Ir a primer parpadeo</a>
</div>

---

<p class="kicker">Acto 8 — Variables y decisiones</p>

# Una variable es un dato temporal

```cpp
int co2 = 900;

if (co2 > 1000) {
  // alerta
}
```

<v-click>

La RAM guarda el valor. La ALU compara. La CPU decide qué instrucción sigue.

</v-click>

---

<p class="kicker">Sensores</p>

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
  <a href="../actividades/medir-co2" class="btn-main">Ir a medir CO₂</a>
</div>

---
layout: center
class: text-center
---

<p class="kicker">Cierre</p>

# Un dato pequeño puede contar una historia grande

<v-clicks>

- De la materia al transistor.
- Del transistor al microcontrolador.
- Del microcontrolador al LED.
- Del sensor a la ciudad.

</v-clicks>

<div class="mt-10 flex gap-4 justify-center">
  <a href="../actividades/antes-de-empezar" class="btn-main">Comenzar actividades</a>
  <a href="../" class="btn-ghost">Volver al inicio</a>
</div>

<style>
.kicker {
  color: #f5b041;
  text-transform: uppercase;
  letter-spacing: 0.16em;
  font-size: 0.75rem;
  font-weight: 900;
}
.accent {
  color: #00b894;
}
.btn-main, .btn-ghost {
  display: inline-block;
  border-radius: 999px;
  padding: 0.65rem 1rem;
  font-weight: 900;
  text-decoration: none;
}
.btn-main {
  background: #00b894;
  color: #041212;
}
.btn-ghost {
  border: 1px solid rgba(255,255,255,0.35);
  color: white;
}
.scene-dark {
  background: radial-gradient(circle at top right, rgba(245,176,65,.18), transparent 30%),
              linear-gradient(120deg, #020303, #063a37);
}
.three-col {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-top: 2rem;
}
.concept-card, .city-grid div, .mcu-map div {
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.16);
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
  color: #f5b041;
}
.concept-card.highlight {
  border-color: #00b894;
  box-shadow: 0 0 35px rgba(0,184,148,0.25);
}
.icon {
  font-size: 2rem;
}
.binary-strip, .logic-flow, .delay-flow, .gpio-flow, .sensor-flow {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: .7rem;
  margin: 2rem 0;
}
.binary-strip span, .logic-flow div, .delay-flow div, .gpio-flow div, .sensor-flow div {
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.15);
  border-radius: 999px;
  padding: .6rem .9rem;
  font-weight: 800;
}
.binary-strip b {
  color: #00b894;
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
  border: 1px solid #00b894;
}
.arrow {
  color: #f5b041;
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
  color: #00b894;
  font-weight: 900;
}
.truth-table .on {
  color: #f5b041;
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
  border-color: #00b894;
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
  color: #f5b041;
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
  border-color: #00b894;
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
  border-color: #f5b041;
  color: #f5b041;
}
.cpu-card {
  border-radius: 1.2rem;
  padding: 1.4rem;
  background: rgba(0,184,148,.16);
  border: 1px solid rgba(0,184,148,.3);
  color: #00b894;
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
  border-top: 10px solid #00b894;
  border-left: 10px solid #00b894;
  border-right: 10px solid #00b894;
  animation: pulseGlow 1.8s ease-in-out infinite;
}
.clock-wave span:nth-child(even) {
  transform: translateY(60px);
  border-top-color: #f5b041;
  border-left-color: #f5b041;
  border-right-color: #f5b041;
}
@keyframes pulseGlow {
  0%, 100% { opacity: .45; }
  50% { opacity: 1; }
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
.content-front {
  position: relative;
  z-index: 2;
}
</style>
'''

slides_page = r'''import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useBaseUrl from '@docusaurus/useBaseUrl';

export default function SlidesPage() {
  const presentacionUrl = useBaseUrl('/presentacion/index.html');

  return (
    <Layout
      title="Historia visual"
      description="Presentación visual del taller Mi primer nodo IoT ambiental"
    >
      <main className="slidesPage">
        <section className="slidesHeader">
          <p className="heroKicker">Historia visual</p>

          <h1>De la arena al sensor inteligente</h1>

          <p>
            Esta historia visual sirve como apoyo para explicar, de forma
            sencilla, cómo pasamos de la materia y los transistores a un
            microcontrolador capaz de ejecutar código, controlar un LED y leer
            sensores ambientales.
          </p>

          <div className="slidesActions">
            <a
              className="slidesFullButton"
              href={presentacionUrl}
              target="_blank"
              rel="noreferrer"
            >
              Abrir en pantalla completa
            </a>

            <Link
              className="slidesSecondaryButton"
              to="/actividades/antes-de-empezar"
            >
              Ir a actividades
            </Link>
          </div>
        </section>

        <section className="slidesFrameWrapper">
          <iframe
            className="slidesFrame"
            src={presentacionUrl}
            title="Historia visual del taller"
            allowFullScreen
          />
        </section>
      </main>
    </Layout>
  );
}
'''

css_add = r'''
/* Slidev integrado en Docusaurus */
.slidesPage {
  max-width: 100%;
  margin: 0;
  padding: 0;
}

.slidesHeader {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2.5rem 1.5rem 1.5rem 1.5rem;
}

.slidesHeader h1 {
  font-size: clamp(2.4rem, 6vw, 4.5rem);
  letter-spacing: -0.06em;
  line-height: 1;
}

.slidesHeader p {
  max-width: 850px;
  font-size: 1.1rem;
  line-height: 1.6;
}

.slidesActions {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  margin-top: 1.5rem;
}

.slidesFullButton {
  display: inline-block;
  border-radius: 999px;
  background: #f5b041;
  color: #201200 !important;
  padding: 0.8rem 1.15rem;
  font-weight: 900;
  text-decoration: none !important;
}

.slidesSecondaryButton {
  display: inline-block;
  border-radius: 999px;
  border: 2px solid #00897b;
  color: #00897b !important;
  padding: 0.68rem 1.05rem;
  font-weight: 900;
  text-decoration: none !important;
}

.slidesFrameWrapper {
  width: 100%;
  height: calc(100vh - 235px);
  min-height: 620px;
  border-radius: 0;
  overflow: hidden;
  box-shadow: none;
  border-top: 1px solid rgba(0,0,0,0.12);
  border-bottom: 1px solid rgba(0,0,0,0.12);
}

.slidesFrame {
  width: 100%;
  height: 100%;
  border: 0;
  background: #000;
}

@media (max-width: 800px) {
  .slidesFrameWrapper {
    height: 70vh;
    min-height: 420px;
  }
}
'''

readme = r'''# Presentación Slidev

Edita la presentación en:

```text
slides/slides.md
```

Coloca recursos visuales en:

```text
slides/assets/imagenes/
slides/assets/gifs/
slides/assets/videos/
```

Ejemplos:

```text
slides/assets/videos/desierto.mp4
slides/assets/gifs/transistor.gif
slides/assets/imagenes/oblea.jpg
```

Comandos:

```powershell
npm run slides:dev
npm run slides:build
npm start
```

El comando `slides:build` genera la presentación en:

```text
static/presentacion/
```

Docusaurus la muestra en:

```text
/slides/
```
'''

# Create dirs
for d in ["slides/assets/imagenes", "slides/assets/gifs", "slides/assets/videos"]:
    ensure_dir(d)

write("slides/slides.md", slides_md)
write("slides/README.md", readme)
write("src/pages/slides.jsx", slides_page)

# Update package.json
pkg_path = ROOT / "package.json"
if pkg_path.exists():
    pkg = json.loads(pkg_path.read_text(encoding="utf-8"))
else:
    pkg = {"scripts": {}, "devDependencies": {}}

pkg.setdefault("scripts", {})
pkg["scripts"]["slides:dev"] = "slidev slides/slides.md --open"
pkg["scripts"]["slides:build"] = "slidev build slides/slides.md --base /mi-primer-nodo-iot-ambiental/presentacion/ --out static/presentacion"

pkg.setdefault("devDependencies", {})
pkg["devDependencies"].setdefault("@slidev/cli", "^52.0.0")
pkg["devDependencies"].setdefault("@slidev/theme-default", "^0.25.0")

pkg_path.write_text(json.dumps(pkg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("OK: package.json actualizado")

# Append Docusaurus CSS if not present
css_path = ROOT / "src/css/custom.css"
css_path.parent.mkdir(parents=True, exist_ok=True)
existing = css_path.read_text(encoding="utf-8") if css_path.exists() else ""
if "Slidev integrado en Docusaurus" not in existing:
    css_path.write_text(existing.rstrip() + "\n\n" + css_add.strip() + "\n", encoding="utf-8")
    print("OK: src/css/custom.css actualizado")
else:
    print("OK: src/css/custom.css ya tenía estilos Slidev")

print("\nListo.")
print("Ahora ejecuta:")
print("  npm install")
print("  npm run slides:dev")
print("\nCuando te guste la presentación:")
print("  npm run slides:build")
print("  npm start")
