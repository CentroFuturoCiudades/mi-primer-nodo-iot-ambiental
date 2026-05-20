# actualizar_historia_visual.py
# Reescribe la historia visual del taller en UTF-8.
# Ejecuta desde la raíz del proyecto Docusaurus:
#   python .\actualizar_historia_visual.py
#
# Luego prueba:
#   npm start
#   http://localhost:3000/mi-primer-nodo-iot-ambiental/slides/

from pathlib import Path

ROOT = Path.cwd()

def write(path, content):
    path = ROOT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"OK: {path}")

slides_html = r'''<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>De la arena al sensor inteligente</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/theme/black.css">
  <link rel="stylesheet" href="slides.css">
</head>

<body>
<div class="reveal">
  <div class="slides">

    <!-- PORTADA -->
    <section data-background-gradient="linear-gradient(120deg, #020303, #063a37)">
      <p class="eyebrow">Taller IoT ambiental</p>
      <h1>De la arena al sensor inteligente</h1>
      <p class="subtitle">
        Una historia visual para entender cómo un chip puede prender un LED,
        leer sensores y transformar el ambiente en datos.
      </p>
      <div class="button-row">
        <a class="lab-button" href="../actividades/antes-de-empezar">Ir a actividades</a>
        <a class="ghost-button" href="../">Volver al inicio</a>
      </div>
    </section>

    <!-- ACTO 1: MATERIA -->
    <section class="cinematic-scene desert-scene">
      <div class="scene-overlay"></div>
      <div class="scene-content">
        <p class="eyebrow">Acto 1 — La materia</p>
        <h2>Antes del dato, hubo materia.</h2>
        <p class="fragment">Antes del sensor, hubo silicio.</p>
        <p class="fragment">Antes del código, hubo transistores.</p>
        <p class="fragment">Y antes de una ciudad inteligente, hubo una pregunta:</p>
        <h3 class="fragment question">¿cómo puede un chip observar el mundo?</h3>
      </div>
    </section>

    <!-- Para usar video real como fondo, coloca static/slides/videos/desierto.mp4
    <section
      data-background-video="videos/desierto.mp4"
      data-background-video-loop
      data-background-video-muted
      data-background-opacity="0.42"
    >
      <p class="eyebrow">Acto 1 — La materia</p>
      <h2>Antes del dato, hubo materia.</h2>
      <p class="fragment">Antes del sensor, hubo silicio.</p>
      <p class="fragment">Antes del código, hubo transistores.</p>
    </section>
    -->

    <section>
      <p class="eyebrow">Pregunta de arranque</p>
      <h2>¿De qué está hecho un chip?</h2>
      <p class="fragment">No empieza en una aplicación.</p>
      <p class="fragment">No empieza en Arduino.</p>
      <p class="fragment">Empieza en materiales que podemos transformar y organizar.</p>
      <p class="fragment big-idea">Materia organizada para controlar electricidad.</p>
    </section>

    <section data-background-gradient="linear-gradient(120deg, #21160e, #050505)">
      <p class="eyebrow">Silicio</p>
      <h2>El silicio es especial porque permite controlar la electricidad.</h2>
      <p class="fragment">No es simplemente un conductor.</p>
      <p class="fragment">No es simplemente un aislante.</p>
      <p class="fragment big-idea">Es un semiconductor.</p>
    </section>

    <!-- ACTO 2: CONDUCTORES, AISLANTES Y SEMICONDUCTORES -->
    <section>
      <p class="eyebrow">Controlar la electricidad</p>
      <h2>Tres materiales, tres comportamientos.</h2>

      <div class="three-columns">
        <div class="concept-card">
          <div class="concept-icon">⚡</div>
          <h3>Conductor</h3>
          <p>Deja pasar electricidad con facilidad.</p>
          <p class="example">Ejemplo: cobre</p>
        </div>

        <div class="concept-card">
          <div class="concept-icon">■</div>
          <h3>Aislante</h3>
          <p>Dificulta el paso de electricidad.</p>
          <p class="example">Ejemplo: plástico</p>
        </div>

        <div class="concept-card highlight">
          <div class="concept-icon">◐</div>
          <h3>Semiconductor</h3>
          <p>Puede comportarse de una forma u otra según cómo se controle.</p>
          <p class="example">Ejemplo: silicio</p>
        </div>
      </div>

      <p class="fragment reflection">
        La computación no nace solo de la electricidad. Nace de poder controlarla.
      </p>
    </section>

    <section>
      <p class="eyebrow">Idea clave</p>
      <h2>Controlar corriente permite representar información.</h2>
      <div class="binary-strip">
        <span>no pasa</span>
        <strong>0</strong>
        <span>pasa</span>
        <strong>1</strong>
      </div>
      <p class="fragment">
        Con muchos elementos capaces de representar 0 y 1 podemos construir lógica digital.
      </p>
    </section>

    <!-- ACTO 3: TRANSISTOR -->
    <section data-background-gradient="linear-gradient(120deg, #050505, #102d2a)">
      <p class="eyebrow">Acto 2 — El transistor</p>
      <h2>Un transistor es un interruptor microscópico.</h2>

      <div class="switch-demo">
        <div class="switch-state off">
          0
          <span>apagado</span>
        </div>

        <div class="switch-arrow">→</div>

        <div class="switch-state on">
          1
          <span>encendido</span>
        </div>
      </div>

      <p class="fragment">
        Con millones de interruptores así, podemos construir memoria, cálculo y control.
      </p>
    </section>

    <!-- Para usar GIF real, coloca static/slides/gifs/transistor.gif
    <section>
      <p class="eyebrow">Transistor</p>
      <h2>El interruptor microscópico.</h2>
      <img class="gif-frame" src="gifs/transistor.gif" alt="Animación de transistor">
      <p class="fragment">Apagado o encendido. Cero o uno.</p>
    </section>
    -->

    <section>
      <p class="eyebrow">De uno a millones</p>
      <h2>Un transistor solo decide poco.</h2>
      <p class="fragment">Muchos transistores pueden formar reglas.</p>
      <p class="fragment">Muchas reglas pueden formar memoria y cálculo.</p>
      <p class="fragment big-idea">La complejidad aparece al repetir piezas simples.</p>
    </section>

    <!-- ACTO 4: COMPUERTAS Y FUNCIONES DIGITALES -->
    <section>
      <p class="eyebrow">Acto 3 — Funciones digitales</p>
      <h2>De transistores a compuertas lógicas.</h2>

      <div class="logic-flow">
        <div>Transistores</div>
        <div>→</div>
        <div>Compuertas</div>
        <div>→</div>
        <div>Bloques digitales</div>
        <div>→</div>
        <div>Microcontrolador</div>
      </div>

      <p class="fragment">
        Las compuertas son pequeñas reglas que combinan ceros y unos.
      </p>
    </section>

    <section>
      <p class="eyebrow">Ejemplo simple</p>
      <h2>Una regla con dos entradas.</h2>
      <div class="truth-table">
        <div class="truth-head">Entrada A</div>
        <div class="truth-head">Entrada B</div>
        <div class="truth-head">Salida</div>

        <div>0</div><div>0</div><div>0</div>
        <div>0</div><div>1</div><div>0</div>
        <div>1</div><div>0</div><div>0</div>
        <div>1</div><div>1</div><div class="truth-on">1</div>
      </div>
      <p class="fragment">
        Con reglas simples podemos construir decisiones más grandes.
      </p>
    </section>

    <section>
      <p class="eyebrow">Memoria</p>
      <h2>Algunos circuitos pueden recordar estados.</h2>
      <div class="memory-visual">
        <div class="bit-cell">0</div>
        <div class="bit-cell active">1</div>
        <div class="bit-cell">0</div>
        <div class="bit-cell active">1</div>
        <div class="bit-cell active">1</div>
        <div class="bit-cell">0</div>
        <div class="bit-cell">0</div>
        <div class="bit-cell active">1</div>
      </div>
      <p class="fragment">
        Muchos bits organizados permiten guardar datos e instrucciones.
      </p>
    </section>

    <section>
      <p class="eyebrow">ALU</p>
      <h2>La ALU es el taller de cálculo.</h2>
      <div class="alu-demo">
        <div class="alu-input">A = 7</div>
        <div class="alu-box">ALU<br><span>suma, compara, decide</span></div>
        <div class="alu-input">B = 3</div>
      </div>
      <p class="fragment">
        Cuando el programa pregunta <code>if (co2 &gt; 1000)</code>,
        el microcontrolador necesita comparar valores.
      </p>
    </section>

    <!-- ACTO 5: MICROCONTROLADOR COMO CIUDAD -->
    <section class="wafer-scene">
      <div class="scene-overlay"></div>
      <div class="scene-content">
        <p class="eyebrow">Acto 4 — El chip</p>
        <h2>Un circuito integrado es una ciudad microscópica.</h2>
        <p class="fragment">Algunas zonas recuerdan.</p>
        <p class="fragment">Otras calculan.</p>
        <p class="fragment">Otras se comunican con el exterior.</p>
      </div>
    </section>

    <!-- Para usar imagen real de oblea, coloca static/slides/imagenes/oblea.jpg
    <section data-background-image="imagenes/oblea.jpg" data-background-opacity="0.35">
      <p class="eyebrow">Oblea de silicio</p>
      <h2>En una oblea se fabrican muchos chips al mismo tiempo.</h2>
    </section>
    -->

    <section>
      <p class="eyebrow">Analogía</p>
      <h2>El microcontrolador como una ciudad.</h2>

      <div class="city-grid">
        <div><strong>CPU</strong><span>centro de control</span></div>
        <div><strong>ALU</strong><span>taller de cálculo</span></div>
        <div><strong>Flash</strong><span>biblioteca del programa</span></div>
        <div><strong>RAM</strong><span>mesa de trabajo</span></div>
        <div><strong>Reloj</strong><span>metrónomo de la ciudad</span></div>
        <div><strong>GPIO</strong><span>puertas al exterior</span></div>
      </div>
    </section>

    <section>
      <p class="eyebrow">Microcontrolador</p>
      <h2>Una computadora pequeña dentro de un chip.</h2>

      <div class="mcu-map">
        <div class="mcu-cell flash">Flash<br><span>programa</span></div>
        <div class="mcu-cell cpu">CPU<br><span>lee y ejecuta</span></div>
        <div class="mcu-cell gpio">GPIO<br><span>mundo físico</span></div>
        <div class="mcu-cell ram">RAM<br><span>variables</span></div>
        <div class="mcu-cell alu">ALU<br><span>cálculo</span></div>
        <div class="mcu-cell clock">Reloj<br><span>ritmo</span></div>
      </div>
    </section>

    <!-- ACTO 6: PROGRAMA E INSTRUCCIONES -->
    <section data-background-gradient="linear-gradient(120deg, #020303, #063a37)">
      <p class="eyebrow">Acto 5 — El programa</p>
      <h2>Un programa es una lista ordenada de instrucciones.</h2>
      <p class="fragment">Nosotros escribimos código fácil de leer.</p>
      <p class="fragment">La tarjeta ejecuta instrucciones mucho más pequeñas.</p>
    </section>

    <section>
      <p class="eyebrow">Secuencia</p>
      <h2>La CPU avanza paso a paso.</h2>

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

      <p class="fragment">
        El contador de programa señala cuál instrucción toca ejecutar.
      </p>
    </section>

    <section>
      <p class="eyebrow">Sin entrar en ensamblador</p>
      <h2>Arduino es una forma humana de escribir instrucciones.</h2>
      <pre><code data-trim>
digitalWrite(LED_BUILTIN, HIGH);
delay(1000);
      </code></pre>
      <p class="fragment">
        Antes de ejecutarse, estas líneas se traducen a pasos pequeños que el procesador sí puede realizar.
      </p>
    </section>

    <!-- ACTO 7: RELOJ Y DELAY -->
    <section>
      <p class="eyebrow">Acto 6 — El tiempo dentro del chip</p>
      <h2>¿Cómo sabe esperar?</h2>
      <div class="clock-wave">
        <span></span><span></span><span></span><span></span><span></span><span></span>
      </div>
      <p class="fragment">
        El oscilador genera pulsos. Esos pulsos marcan el ritmo interno.
      </p>
    </section>

    <section>
      <p class="eyebrow">delay(1000)</p>
      <h2>Esperar es contar tiempo.</h2>

      <div class="delay-flow">
        <div>Reloj</div>
        <div>→</div>
        <div>Temporizador</div>
        <div>→</div>
        <div>1000 ms</div>
        <div>→</div>
        <div>Siguiente instrucción</div>
      </div>

      <p class="fragment">
        Si cambiamos <code>1000</code> por <code>100</code>, el mundo físico cambia:
        el LED parpadea más rápido.
      </p>

      <a class="lab-button" href="../actividades/tiempo-dentro-del-chip">
        Ir a la actividad del tiempo
      </a>
    </section>

    <!-- ACTO 8: GPIO Y LED -->
    <section>
      <p class="eyebrow">Acto 7 — Puertas al mundo</p>
      <h2>El LED no entiende código.</h2>
      <p class="fragment">El LED responde a voltaje.</p>
      <p class="fragment">El microcontrolador traduce instrucciones en señales físicas.</p>
    </section>

    <section>
      <p class="eyebrow">GPIO</p>
      <h2>Una patita de entrada o salida.</h2>

      <div class="gpio-flow">
        <div>CPU ejecuta</div>
        <div>→</div>
        <div>Registro de salida</div>
        <div>→</div>
        <div>GPIO cambia voltaje</div>
        <div>→</div>
        <div>LED prende</div>
      </div>

      <pre><code data-trim>
pinMode(LED_BUILTIN, OUTPUT);
digitalWrite(LED_BUILTIN, HIGH);
      </code></pre>

      <a class="lab-button" href="../actividades/primer-parpadeo">
        Ir a primer parpadeo
      </a>
    </section>

    <!-- ACTO 9: VARIABLES, DECISIONES Y SENSORES -->
    <section>
      <p class="eyebrow">Acto 8 — Variables y decisiones</p>
      <h2>Una variable es un dato temporal en la mesa de trabajo.</h2>

      <pre><code data-trim>
int co2 = 900;

if (co2 > 1000) {
  // alerta
}
      </code></pre>

      <p class="fragment">
        La RAM guarda el valor. La ALU compara. La CPU decide qué instrucción sigue.
      </p>
    </section>

    <section>
      <p class="eyebrow">Sensores</p>
      <h2>Un sensor convierte el ambiente en números.</h2>

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

      <p class="fragment">
        CO₂, temperatura, humedad y partículas pueden convertirse en mediciones.
      </p>

      <a class="lab-button" href="../actividades/medir-co2">
        Ir a medir CO₂
      </a>
    </section>

    <!-- CIERRE -->
    <section data-background-gradient="linear-gradient(120deg, #020303, #063a37)">
      <p class="eyebrow">Cierre</p>
      <h2>Un dato pequeño puede contar una historia grande.</h2>
      <p class="fragment">De la materia al transistor.</p>
      <p class="fragment">Del transistor al microcontrolador.</p>
      <p class="fragment">Del microcontrolador al LED.</p>
      <p class="fragment">Del sensor a la ciudad.</p>

      <div class="button-row">
        <a class="lab-button" href="../actividades/antes-de-empezar">Comenzar actividades</a>
        <a class="ghost-button" href="../">Volver al inicio</a>
      </div>
    </section>

  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.js"></script>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/highlight/highlight.js"></script>

<script>
  Reveal.initialize({
    hash: true,
    slideNumber: true,
    transition: 'fade',
    backgroundTransition: 'fade',
    plugins: [ RevealHighlight ]
  });
</script>
</body>
</html>'''

slides_css = r''':root {
  --teal: #00b894;
  --teal-dark: #063a37;
  --amber: #f5b041;
  --muted: #b9c7c3;
  --soft-white: rgba(255,255,255,0.86);
}

.reveal h1,
.reveal h2,
.reveal h3 {
  text-transform: none;
  letter-spacing: -0.04em;
}

.reveal h1 {
  font-size: 2.7em;
  line-height: 0.95;
}

.reveal h2 {
  font-size: 2.0em;
  line-height: 1.05;
}

.reveal h3 {
  font-size: 1.15em;
}

.reveal p {
  line-height: 1.45;
}

.reveal code {
  font-size: 0.75em;
}

.eyebrow {
  color: var(--amber);
  text-transform: uppercase;
  letter-spacing: 0.16em;
  font-size: 0.52em;
  font-weight: 900;
}

.subtitle {
  color: var(--muted);
  max-width: 900px;
  margin: auto;
}

.big-idea {
  color: var(--teal);
  font-weight: 900;
  font-size: 1.35em;
}

.question {
  color: var(--amber);
  margin-top: 1.2rem;
}

.reflection {
  margin-top: 1.2rem;
  color: var(--soft-white);
}

.button-row {
  display: flex;
  justify-content: center;
  gap: 0.8rem;
  flex-wrap: wrap;
  margin-top: 1rem;
}

.lab-button,
.ghost-button {
  display: inline-block;
  margin-top: 1rem;
  padding: 0.72rem 1.05rem;
  border-radius: 999px;
  font-weight: 900;
  text-decoration: none;
  font-size: 0.55em;
}

.lab-button {
  background: var(--teal);
  color: #041212 !important;
}

.ghost-button {
  border: 1px solid rgba(255,255,255,0.36);
  color: white !important;
}

/* Escenas cinematográficas sin video real */

.cinematic-scene {
  position: relative;
  overflow: hidden;
}

.desert-scene {
  background:
    radial-gradient(circle at 20% 10%, rgba(245, 176, 65, 0.30), transparent 28%),
    radial-gradient(circle at 80% 80%, rgba(0, 184, 148, 0.12), transparent 30%),
    linear-gradient(120deg, #3b2a18, #050505 70%);
}

.desert-scene::before {
  content: "";
  position: absolute;
  inset: -20%;
  background: radial-gradient(circle, rgba(245,176,65,0.22) 0 2px, transparent 3px);
  background-size: 42px 42px;
  animation: drift 18s linear infinite;
  opacity: 0.25;
}

.wafer-scene {
  position: relative;
  overflow: hidden;
  background:
    radial-gradient(circle at 50% 50%, rgba(150, 220, 255, 0.18), transparent 24%),
    radial-gradient(circle at 50% 50%, rgba(255,255,255,0.10), transparent 34%),
    linear-gradient(135deg, #071111, #061716);
}

.wafer-scene::before {
  content: "";
  position: absolute;
  width: 640px;
  height: 640px;
  border-radius: 50%;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  background:
    repeating-radial-gradient(circle, rgba(255,255,255,0.16) 0 2px, transparent 2px 18px),
    conic-gradient(from 20deg, rgba(0,184,148,0.24), rgba(245,176,65,0.18), rgba(80,180,255,0.16), rgba(0,184,148,0.24));
  opacity: 0.28;
  animation: slowRotate 32s linear infinite;
}

.scene-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, rgba(0,0,0,0.74), rgba(0,0,0,0.20));
}

.scene-content {
  position: relative;
  z-index: 2;
  max-width: 1050px;
  margin: auto;
}

@keyframes drift {
  from { transform: translate3d(0, 0, 0); }
  to { transform: translate3d(80px, 80px, 0); }
}

@keyframes slowRotate {
  from { transform: translate(-50%, -50%) rotate(0deg); }
  to { transform: translate(-50%, -50%) rotate(360deg); }
}

/* Conceptos */

.three-columns {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-top: 2rem;
}

.concept-card {
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.16);
  border-radius: 1.15rem;
  padding: 1rem;
  min-height: 245px;
}

.concept-card h3 {
  color: white;
  font-size: 0.95em;
  margin-bottom: 0.5rem;
}

.concept-card p {
  font-size: 0.52em;
}

.concept-card .example {
  color: var(--amber);
  font-weight: 800;
}

.concept-card.highlight {
  border-color: var(--teal);
  box-shadow: 0 0 35px rgba(0,184,148,0.25);
}

.concept-icon {
  font-size: 1.35em;
  margin-bottom: 0.4rem;
}

.binary-strip,
.logic-flow,
.delay-flow,
.gpio-flow,
.sensor-flow {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 0.7rem;
  margin: 2rem 0;
}

.binary-strip span,
.logic-flow div,
.delay-flow div,
.gpio-flow div,
.sensor-flow div {
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.15);
  border-radius: 999px;
  padding: 0.6rem 0.9rem;
  font-size: 0.55em;
  font-weight: 800;
}

.binary-strip strong {
  color: var(--teal);
  font-size: 1.5em;
}

/* Transistor */

.switch-demo {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  margin: 2rem 0;
}

.switch-state {
  width: 180px;
  height: 180px;
  border-radius: 1.4rem;
  display: grid;
  place-items: center;
  font-size: 2em;
  font-weight: 900;
}

.switch-state span {
  display: block;
  font-size: 0.28em;
  color: rgba(255,255,255,0.72);
}

.switch-state.off {
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.18);
}

.switch-state.on {
  background: rgba(0,184,148,0.22);
  border: 1px solid var(--teal);
  box-shadow: 0 0 38px rgba(0,184,148,0.22);
}

.switch-arrow {
  color: var(--amber);
  font-size: 2em;
  font-weight: 900;
}

/* Tablas y bloques */

.truth-table {
  display: grid;
  grid-template-columns: repeat(3, 150px);
  justify-content: center;
  margin-top: 1.2rem;
}

.truth-table div {
  border: 1px solid rgba(255,255,255,0.20);
  padding: 0.45rem;
  font-size: 0.55em;
}

.truth-head {
  background: rgba(0,184,148,0.20);
  color: var(--teal);
  font-weight: 900;
}

.truth-on {
  color: var(--amber);
  font-weight: 900;
}

.memory-visual {
  display: grid;
  grid-template-columns: repeat(8, 76px);
  justify-content: center;
  gap: 0.55rem;
  margin: 2rem 0;
}

.bit-cell {
  height: 76px;
  display: grid;
  place-items: center;
  border-radius: 0.9rem;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.15);
  font-weight: 900;
  font-size: 1.0em;
}

.bit-cell.active {
  background: rgba(0,184,148,0.22);
  border-color: var(--teal);
}

.alu-demo {
  display: grid;
  grid-template-columns: 1fr 1.4fr 1fr;
  align-items: center;
  gap: 1rem;
  max-width: 920px;
  margin: 2rem auto;
}

.alu-input,
.alu-box {
  border-radius: 1.2rem;
  padding: 1rem;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.16);
  font-size: 0.75em;
  font-weight: 900;
}

.alu-box {
  background: rgba(245,176,65,0.16);
  border-color: rgba(245,176,65,0.35);
  color: var(--amber);
}

.alu-box span {
  display: block;
  font-size: 0.6em;
  color: rgba(255,255,255,0.75);
}

.city-grid,
.mcu-map {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  max-width: 1000px;
  margin: 2rem auto;
}

.city-grid div,
.mcu-cell {
  border-radius: 1.1rem;
  padding: 1rem;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.15);
  min-height: 120px;
}

.city-grid strong,
.mcu-cell {
  color: var(--amber);
  font-weight: 900;
}

.city-grid span,
.mcu-cell span {
  display: block;
  color: rgba(255,255,255,0.72);
  font-size: 0.52em;
  margin-top: 0.35rem;
}

.mcu-cell.cpu {
  border-color: var(--teal);
  box-shadow: 0 0 35px rgba(0,184,148,0.18);
}

.instruction-scene {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  align-items: center;
  gap: 1.2rem;
  max-width: 1000px;
  margin: 2rem auto;
}

.memory-list {
  display: grid;
  gap: 0.4rem;
}

.instruction {
  text-align: left;
  padding: 0.6rem 0.8rem;
  border-radius: 0.8rem;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.14);
  font-size: 0.55em;
  font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
}

.instruction.active {
  border-color: var(--amber);
  color: var(--amber);
  box-shadow: 0 0 28px rgba(245,176,65,0.18);
}

.cpu-card {
  border-radius: 1.2rem;
  padding: 1.4rem;
  background: rgba(0,184,148,0.16);
  border: 1px solid rgba(0,184,148,0.30);
  color: var(--teal);
  font-weight: 900;
}

.cpu-card span {
  display: block;
  margin-top: 0.5rem;
  color: rgba(255,255,255,0.72);
  font-size: 0.55em;
}

/* Reloj */

.clock-wave {
  display: flex;
  justify-content: center;
  align-items: flex-end;
  gap: 0.25rem;
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
  0%, 100% { opacity: 0.45; }
  50% { opacity: 1; }
}

/* Multimedia */

.media-frame {
  width: min(900px, 85vw);
  max-height: 60vh;
  border-radius: 1.2rem;
  box-shadow: 0 20px 60px rgba(0,0,0,0.45);
  border: 1px solid rgba(255,255,255,0.18);
  background: #000;
}

.gif-frame {
  width: min(760px, 80vw);
  max-height: 55vh;
  object-fit: contain;
  border-radius: 1.2rem;
  box-shadow: 0 20px 60px rgba(0,0,0,0.45);
  border: 1px solid rgba(255,255,255,0.18);
}

.caption {
  font-size: 0.5em;
  color: rgba(255,255,255,0.65);
  margin-top: 0.6rem;
}
'''

homepage = r'''import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';

import CoursePath from '../components/CoursePath';
import ActivityCard from '../components/ActivityCard';
import StepFlow from '../components/StepFlow';

export default function Home() {
  return (
    <Layout
      title="Mi primer nodo IoT ambiental"
      description="Taller práctico de microcontroladores, sensores e IoT ambiental para bachillerato"
    >
      <main>
        <section className="heroSection">
          <div className="heroContent">
            <p className="heroKicker">Taller práctico para bachillerato</p>

            <h1>De la arena al sensor inteligente</h1>

            <p className="heroSubtitle">
              Una experiencia para descubrir cómo un pequeño microcontrolador
              puede prender un LED, leer sensores ambientales y convertir el
              mundo físico en datos útiles para entender una ciudad.
            </p>

            <div className="heroActions">
              <Link className="mainButton" to="/slides/">
                Ver historia visual
              </Link>

              <Link className="secondaryButton" to="/actividades/antes-de-empezar">
                Prepararme para empezar
              </Link>
            </div>
          </div>
        </section>

        <section className="pageSection">
          <h2>Ruta del taller</h2>
          <CoursePath />
        </section>

        <section className="pageSection">
          <h2>Actividades principales</h2>

          <div className="activityGrid">
            <ActivityCard
              number="01"
              tag="Mensaje"
              title="Hola mundo"
              description="La tarjeta enviará su primer mensaje a la computadora. Aquí aprenderás a usar el monitor de mensajes."
              to="/actividades/hola-mundo"
            />

            <ActivityCard
              number="02"
              tag="LED"
              title="Primer parpadeo"
              description="El microcontrolador encenderá y apagará un LED. Es la primera señal física que produce el chip."
              to="/actividades/primer-parpadeo"
            />

            <ActivityCard
              number="03"
              tag="Tiempo"
              title="El tiempo dentro del chip"
              description="Verás cómo una espera en el código se relaciona con el reloj interno del microcontrolador."
              to="/actividades/tiempo-dentro-del-chip"
            />

            <ActivityCard
              number="04"
              tag="Aire"
              title="Medir el ambiente"
              description="Conectaremos sensores para medir CO₂, temperatura, humedad y partículas en el aire."
              to="/actividades/medir-co2"
            />
          </div>
        </section>

        <section className="pageSection">
          <h2>¿Cómo se trabaja cada actividad?</h2>
          <StepFlow />

          <div className="importantBox">
            <strong>Idea importante:</strong>
            <p>
              No se trata solo de copiar código. Cada actividad está diseñada
              para que entiendas qué parte del microcontrolador estás usando.
            </p>
          </div>
        </section>

        <section className="pageSection">
          <h2>Resultado del taller</h2>

          <p>Al final podrás explicar con tus palabras:</p>

          <ul>
            <li>Qué es un microcontrolador.</li>
            <li>Cómo se comunica con la computadora.</li>
            <li>Cómo controla una salida física como un LED.</li>
            <li>Cómo mide datos del ambiente usando sensores.</li>
            <li>Cómo esos datos pueden ayudar a entender espacios reales de una ciudad.</li>
          </ul>
        </section>
      </main>
    </Layout>
  );
}
'''

readme_media = '''# Recursos visuales opcionales

Puedes colocar aquí videos, GIFs e imágenes para enriquecer la historia visual.

Rutas recomendadas:

- `static/slides/videos/desierto.mp4`
- `static/slides/gifs/transistor.gif`
- `static/slides/imagenes/oblea.jpg`

En `static/slides/index.html` hay bloques comentados que muestran cómo activar estos recursos.
'''

write("static/slides/index.html", slides_html)
write("static/slides/slides.css", slides_css)
write("src/pages/index.jsx", homepage)
write("static/slides/videos/.gitkeep", "")
write("static/slides/gifs/.gitkeep", "")
write("static/slides/imagenes/.gitkeep", "")
write("static/slides/README_RECURSOS.md", readme_media)

print("\nListo. Ahora ejecuta:")
print("  npm start")
print("y abre:")
print("  http://localhost:3000/mi-primer-nodo-iot-ambiental/slides/")
