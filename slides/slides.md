---
theme: seriph
title: Entendiendo el origen y fundamentos de los microcontroladores
info: |
  Taller práctico para bachillerato.
  Historia visual del curso Mi primer nodo IoT ambiental.
class: deck
drawings:
  persist: false
transition: fade
mdc: true
---

<div class="cover">
  <p class="eyebrow">Mi primer nodo IoT ambiental</p>
  <h1>Entendiendo el origen y fundamentos de los microcontroladores</h1>
  <a href="../actividades/antes-de-empezar" target="_top" class="quiet-link">Ir a actividades</a>
</div>


---
class: image-story
---

<img class="image-story__img" src="./assets/imagenes/mineria-tierras-raras.png" alt="Minería relacionada con materiales electrónicos" />

<div class="image-story__panel">
  <p class="eyebrow">Escena 2</p>
  <h1>Comenzamos con las tierras raras</h1>
  <p>En el mundo existen tierras raras con minerales que son la base de los microcontroladores.</p>
  <div class="path">
    <span>tierras raras</span>
    <span>minerales</span>
    <span>chips</span>
  </div>
</div>

---
class: image-story materials-story
---

<img class="image-story__img" src="./assets/imagenes/periodic_table.png" alt="Tabla periodica" />

<div class="image-story__panel material-panel">
  <p class="eyebrow">Escena 3</p>
  <h1>Existen 3 tipos de materiales</h1>

  <div class="three-cols">
    <div>
      <span class="symbol">+</span>
      <h2>Conductor</h2>
      <p>Deja pasar corriente con facilidad.</p>
      <strong>Cobre, aluminio, oro.</strong>
    </div>
    <div>
      <span class="symbol">-</span>
      <h2>Aislante</h2>
      <p>Dificulta el paso de corriente.</p>
      <strong>Plástico, vidrio, cerámica.</strong>
    </div>
    <div class="accent">
      <span class="symbol">0/1</span>
      <h2>Semiconductor</h2>
      <p>Puede cambiar si lo controlamos.</p>
      <strong>Silicio.</strong>
    </div>
  </div>

  <p class="takeaway">La clave de un chip no es tener electricidad: es poder controlarla.</p>
</div>

---
class: transistor-story
---

<img class="image-story__img transistor-story__img" src="./assets/imagenes/transitors.png" alt="Transistores sobre una superficie metálica" />

<p class="eyebrow">Escena 4</p>

# El transistor: un semiconductor que podemos controlar

<div class="transistor-grid">
  <div class="transistor-explain">
    <h2>La unidad fundamental de los chips</h2>
    <p>Un transistor es un interruptor hecho con semiconductores. Una señal pequeña en la compuerta decide si la corriente se bloquea o puede pasar.</p>
  </div>
  <div class="transistor-visual">
    <div class="transistor-demo" aria-label="Animación de un transistor bloqueando y dejando pasar corriente">
      <div class="terminal">
        <strong>Fuente</strong>
        <small>entrada</small>
      </div>
      <div class="chip-channel">
        <div class="gate-plate">compuerta</div>
        <div class="channel">
          <span class="electron"></span>
          <span class="electron"></span>
          <span class="electron"></span>
        </div>
        <div class="state off">0 bloquea</div>
        <div class="state on">1 conduce</div>
      </div>
      <div class="terminal">
        <strong>Drenaje</strong>
        <small>salida</small>
      </div>
    </div>
    <div class="transistor-symbol" aria-label="Esquemático de transistor">
      <p>símbolo</p>
      <svg viewBox="0 0 220 220" role="img">
        <line class="schematic-line" x1="110" y1="30" x2="110" y2="72" />
        <line class="schematic-line" x1="110" y1="148" x2="110" y2="190" />
        <line class="schematic-line" x1="78" y1="74" x2="78" y2="146" />
        <line class="schematic-line" x1="110" y1="72" x2="78" y2="94" />
        <line class="schematic-line" x1="78" y1="126" x2="110" y2="148" />
        <line class="schematic-gate" x1="38" y1="110" x2="68" y2="110" />
        <line class="schematic-gate" x1="68" y1="78" x2="68" y2="142" />
        <path class="schematic-arrow" d="M101 141 L116 148 L105 160" />
        <text x="117" y="27">D</text>
        <text x="116" y="207">S</text>
        <text x="23" y="116">G</text>
      </svg>
      <div class="symbol-caption">
        <span>G: compuerta</span>
        <span>D/S: corriente</span>
      </div>
    </div>
  </div>
</div>

---
class: circuit-complexity
---

<img class="circuit-complexity__img" src="./assets/imagenes/ALU.png" alt="Diagrama técnico de una ALU" />

<p class="eyebrow">Escena 5</p>

# La complejidad de los circuitos lógicos digitales

<div class="bit-examples">
  <div class="bit-panel latch-panel">
    <div class="bit-panel__head">
      <span>memoria</span>
      <h2>Biestable SR de 1 bit</h2>
      <p>Dos inversores acoplados por realimentación cruzada conservan un estado lógico estable.</p>
    </div>
    <svg class="logic-diagram latch-schematic" viewBox="0 0 560 280" role="img" aria-label="Biestable SR de un bit con transistores cruzados">
      <path class="wire rail-hot" d="M48 32H512" />
      <path class="wire rail-gnd" d="M48 248H512" />
      <text x="48" y="23">+5 V</text>
      <text x="48" y="268">GND</text>
      <path class="wire" d="M150 32V70" />
      <path class="wire" d="M410 32V70" />
      <path class="resistor" d="M150 70l-10 8 20 12-20 12 20 12-10 8v22" />
      <path class="resistor" d="M410 70l-10 8 20 12-20 12 20 12-10 8v22" />
      <text x="112" y="92">R1</text>
      <text x="424" y="92">R4</text>
      <circle class="node-out node-low" cx="150" cy="144" r="22" />
      <circle class="node-out node-high" cx="410" cy="144" r="22" />
      <text x="136" y="151">Q̅=0</text>
      <text x="396" y="151">Q=1</text>
      <path class="wire feedback-a" d="M172 144C230 96 318 96 388 144" />
      <path class="wire feedback-b" d="M388 144C318 198 230 198 172 144" />
      <circle class="transistor off" cx="150" cy="205" r="34" />
      <circle class="transistor on" cx="410" cy="205" r="34" />
      <path class="gate-line" d="M125 185v40" />
      <path class="gate-line" d="M385 185v40" />
      <path class="wire" d="M150 166v5M150 239v9M410 166v5M410 239v9" />
      <text x="134" y="210">Q1</text>
      <text x="394" y="210">Q2</text>
      <path class="wire input-wire" d="M250 248V214" />
      <path class="wire input-wire active" d="M310 248V214" />
      <rect class="input-key" x="226" y="180" width="48" height="34" rx="6" />
      <rect class="input-key active" x="286" y="180" width="48" height="34" rx="6" />
      <text x="244" y="202">R</text>
      <text x="304" y="202">S</text>
      <circle class="signal signal-latch-a" cx="172" cy="144" r="5" />
      <circle class="signal signal-latch-b" cx="388" cy="144" r="5" />
      <rect class="state-label" x="202" y="50" width="156" height="32" rx="16" />
      <text class="state-text" x="220" y="71">estado estable: Q=1</text>
    </svg>
  </div>
  <div class="bit-panel alu-panel">
    <div class="bit-panel__head">
      <span>cálculo</span>
      <h2>Sumador completo de 1 bit</h2>
      <p>Una red combinacional implementa S = A ⊕ B ⊕ Cin y Cout = AB + Cin(A ⊕ B).</p>
    </div>
    <svg class="logic-diagram adder-schematic" viewBox="0 0 560 280" role="img" aria-label="Sumador completo de un bit con compuertas XOR AND y OR">
      <text x="34" y="62">A=1</text>
      <text x="34" y="112">B=1</text>
      <text x="34" y="192">Cin=0</text>
      <path class="wire active" d="M86 58H168" />
      <path class="wire active" d="M86 108H168" />
      <path class="wire muted" d="M86 188H246" />
      <path class="gate xor" d="M168 38C218 38 244 58 258 84C244 110 218 130 168 130C188 104 188 64 168 38Z" />
      <path class="gate-shadow" d="M154 38C174 64 174 104 154 130" />
      <text x="198" y="90">XOR</text>
      <path class="wire active" d="M258 84H318" />
      <path class="wire muted" d="M246 188H318" />
      <path class="gate xor" d="M318 64C368 64 394 84 408 110C394 136 368 156 318 156C338 130 338 90 318 64Z" />
      <path class="gate-shadow" d="M304 64C324 90 324 130 304 156" />
      <text x="348" y="116">XOR</text>
      <path class="wire muted" d="M408 110H500" />
      <text x="508" y="116">S=0</text>
      <path class="wire active" d="M116 58V166H184" />
      <path class="wire active" d="M116 108V206H184" />
      <path class="gate and" d="M184 154H220C246 154 262 166 262 180C262 194 246 206 220 206H184Z" />
      <text x="203" y="184">AND</text>
      <path class="wire active" d="M262 180H370" />
      <path class="wire active" d="M258 84V226H184" />
      <path class="wire muted" d="M246 188V246H184" />
      <path class="gate and" d="M184 214H220C246 214 262 226 262 240C262 254 246 266 220 266H184Z" />
      <text x="203" y="244">AND</text>
      <path class="wire muted" d="M262 240H370" />
      <path class="gate or" d="M370 166C420 166 450 186 466 210C450 234 420 254 370 254C392 228 392 192 370 166Z" />
      <text x="407" y="216">OR</text>
      <path class="wire active" d="M466 210H500" />
      <text x="508" y="216">Cout=1</text>
      <circle class="signal signal-adder-a" cx="86" cy="58" r="5" />
      <circle class="signal signal-adder-b" cx="86" cy="108" r="5" />
      <circle class="signal signal-adder-c" cx="466" cy="210" r="5" />
    </svg>
  </div>
</div>


---
class: microprocessor-intro
---

<p class="eyebrow">Escena 6</p>

# El microprocesador

<div class="micro-grid">
  <div class="micro-copy">
    <h2>Intel 4004, 1971</h2>
    <p>El Intel 4004 fue el primer microprocesador comercial en un solo chip: una unidad central de procesamiento implementada como circuito integrado.</p>
    <div class="micro-facts">
      <span>4 bits</span>
      <span>≈ 2 300 transistores</span>
      <span>CPU en un encapsulado</span>
    </div>
  </div>
  <figure class="chip-photo">
    <img src="./assets/imagenes/mc4004.png" alt="Microprocesador Intel 4004" />
    <figcaption>Encapsulado físico</figcaption>
  </figure>
  <figure class="die-photo">
    <img src="./assets/imagenes/circuitMC.png" alt="Interior del Intel 4004 con regiones funcionales" />
    <figcaption>Circuito integrado por dentro</figcaption>
  </figure>
  <figure class="block-photo">
    <img src="./assets/imagenes/blockDiagramMC.png" alt="Diagrama de bloques de un microprocesador" />
    <figcaption>Modelo de bloques: memoria, registros, ALU, control e I/O</figcaption>
  </figure>
</div>


---
class: microcontroller-slide
---

<p class="eyebrow">Escena 7</p>

# El microcontrolador
<div class="mcu-layout">
  <div class="mcu-copy">
    <h2>Microprocesador vs. microcontrolador</h2>
    <p>Un microprocesador concentra la CPU. Un microcontrolador integra CPU, memoria, temporizadores y puertos de entrada/salida en el mismo circuito integrado.</p>
    <div class="mcu-contrast">
      <div>
        <b>Microprocesador</b>
        <span>necesita memoria y periféricos externos</span>
      </div>
      <div>
        <b>Microcontrolador</b>
        <span>incluye recursos para controlar el mundo físico</span>
      </div>
    </div>
    <div class="mcu-chip-map" aria-label="Bloques internos de un microcontrolador">
      <span class="core">CPU</span>
      <span>Flash</span>
      <span>RAM</span>
      <span>Timers</span>
      <span>GPIO</span>
      <span>ADC</span>
      <span>UART/I2C/SPI</span>
    </div>
    <p class="mcu-board-note">En la tarjeta Arduino Mega, el <strong>ATmega2560</strong> es el microcontrolador.</p>
  </div>
  <figure class="mcu-board">
    <img src="./assets/imagenes/atmega2560.png" alt="Arduino Mega con partes etiquetadas" />
    <figcaption>Arduino Mega: el ATmega2560 es el microcontrolador; la placa facilita alimentación, USB y conexiones.</figcaption>
  </figure>
</div>

---

<p class="eyebrow">Escena 12</p>

# Cargar un programa

Cuando cargamos código, no solo copiamos texto.

<div class="timeline compact">
  <span>Código Arduino</span>
  <span>compilación</span>
  <span>instrucciones</span>
  <span>Flash</span>
</div>

<p class="takeaway">El programa queda guardado y se ejecuta cuando encendemos la tarjeta.</p>

---

<p class="eyebrow">Escena 13</p>

# Un programa es una lista de instrucciones

<div class="instruction-grid">
  <div>
    <div class="instruction active">1. pinMode(...)</div>
    <div class="instruction">2. digitalWrite(HIGH)</div>
    <div class="instruction">3. delay(1000)</div>
    <div class="instruction">4. digitalWrite(LOW)</div>
    <div class="instruction">5. delay(1000)</div>
  </div>
  <div class="cpu-box">
    CPU
    <small>leer -> interpretar -> ejecutar -> avanzar</small>
  </div>
</div>

---

<p class="eyebrow">Escena 14</p>

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

<p class="eyebrow">Escena 15</p>

# El microcontrolador tiene ritmo

<div class="clock-wave">
  <span></span><span></span><span></span><span></span><span></span><span></span>
</div>

<v-clicks>

- El oscilador genera pulsos.
- Los pulsos marcan el ritmo interno.
- La tarjeta avanza paso a paso.

</v-clicks>

---

<p class="eyebrow">Escena 16</p>

# `delay(1000)` no es magia

<div class="timeline compact">
  <span>reloj</span>
  <span>temporizador</span>
  <span>1000 ms</span>
  <span>siguiente instrucción</span>
</div>

<a href="../actividades/tiempo-dentro-del-chip" target="_top" class="quiet-link">Actividad: tiempo dentro del chip</a>

---

<p class="eyebrow">Escena 17</p>

# El LED no entiende código

<div class="timeline compact">
  <span>CPU ejecuta</span>
  <span>registro de salida</span>
  <span>GPIO cambia voltaje</span>
  <span>LED prende</span>
</div>

```cpp
pinMode(LED_BUILTIN, OUTPUT);
digitalWrite(LED_BUILTIN, HIGH);
```

<a href="../actividades/primer-parpadeo" target="_top" class="quiet-link">Actividad: primer parpadeo</a>

---

<p class="eyebrow">Escena 18</p>

# Variables y decisiones

```cpp
int co2 = 900;

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

<p class="eyebrow">Escena 19</p>

# Un sensor convierte el ambiente en números

<div class="timeline compact">
  <span>aire</span>
  <span>sensor</span>
  <span>tarjeta</span>
  <span>datos</span>
  <span>decisión</span>
</div>

<a href="../actividades/medir-co2" target="_top" class="quiet-link">Actividad: medir CO2</a>

---
layout: center
class: statement
---

<p class="eyebrow">Cierre</p>

# Un dato pequeño puede contar una historia grande

<v-clicks>

- Un LED enseña a controlar una salida.
- Un sensor enseña a leer el ambiente.
- Muchas mediciones ayudan a entender espacios reales.

</v-clicks>

<a href="../actividades/antes-de-empezar" target="_top" class="quiet-link">Comenzar actividades</a>
