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
    <p class="mcu-board-note">Para el taller usaremos la <strong>Blues Swan R5</strong>: prepara Arduino IDE, puerto COM y modo de carga.</p>
    <a href="../actividades/antes-de-empezar" target="_top" class="mcu-prepare-link" aria-label="Abrir la actividad Antes de empezar para preparar la Blues Swan R5">
      <span class="mcu-prepare-kicker">Siguiente paso</span>
      <strong>Preparar mi tarjeta Swan</strong>
      <small>IDE + COM + carga</small>
      <span class="mcu-prepare-arrow">-&gt;</span>
    </a>
  </div>
  <figure class="mcu-board">
    <img src="./assets/imagenes/atmega2560.png" alt="Arduino Mega con partes etiquetadas" />
  </figure>
</div>



---

<p class="eyebrow">Escena 12</p>

# Del algoritmo a instrucciones en memoria

<div class="program-machine">
  <div class="program-source">
    <div class="algorithm-card">
      <b>Algoritmo</b>
      <span>Una receta finita de pasos: inicializar, decidir, repetir y producir una salida.</span>
    </div>
    <div class="source-code">
      <span>digitalWrite(HIGH);</span>
      <span>delay(1000);</span>
      <span>digitalWrite(LOW);</span>
      <span>delay(1000);</span>
    </div>
    <div class="compile-lane" aria-label="Flujo de compilación">
      <span>programa</span>
      <span>compilador</span>
      <span>binario</span>
      <span>Flash</span>
      <i></i>
    </div>
    <div class="control-structures" aria-label="Estructuras de control">
      <div><b>secuencia</b><span>paso 1 → paso 2</span></div>
      <div><b>if</b><span>elegir un camino</span></div>
      <div><b>while / for</b><span>repetir mientras se cumpla una condición</span></div>
    </div>
    <p>El programa se traduce a instrucciones binarias y queda guardado en Flash. La CPU las lee en orden, salvo cuando una condición o un ciclo cambia el flujo.</p>
  </div>

  <div class="mcu-core-map" aria-label="Animación de bloques internos del microcontrolador">
    <div class="core-block flash"><b>Memoria de programa</b><small>guarda el código</small></div>
    <div class="core-block pc"><b>Contador de programa</b><small>PC: siguiente dirección</small></div>
    <div class="core-block decoder"><b>Decodificador</b><small>entiende la instrucción</small></div>
    <div class="core-block regs"><b>Registros</b><small>datos inmediatos</small></div>
    <div class="core-block alu"><b>Unidad lógica</b><small>ALU: calcula y compara</small></div>
    <div class="core-block ram"><b>Memoria de datos</b><small>RAM: variables</small></div>
    <div class="core-block gpio"><b>Entradas y salidas</b><small>GPIO: voltaje al LED</small></div>
    <span class="fetch-dot"></span>
    <span class="execute-dot"></span>
    <span class="io-dot"></span>
  </div>

  <div class="machine-caption">
    <b>Ciclo de ejecución</b>
    <span>buscar instrucción → decodificar → ejecutar → actualizar registros o salidas → avanzar, saltar o repetir</span>
  </div>
</div>

---
class: delay-slide
---

<p class="eyebrow">Escena 13</p>

# Qué pasa durante `delay(1000)`

<div class="timing-deep">
  <div class="timing-code-panel">
    <div class="timing-code-card" aria-label="Código Arduino que controla el LED">
      <span><b>01</b> digitalWrite(LED_BUILTIN, HIGH);</span>
      <span><b>02</b> delay(1000);</span>
      <span><b>03</b> digitalWrite(LED_BUILTIN, LOW);</span>
      <span><b>04</b> delay(1000);</span>
      <i class="code-scan"></i>
    </div>
    <div class="delay-truth">
      <b>Idea clave</b>
      <span>`delay(1000)` no es una sola instrucción del microcontrolador. Es una función que espera hasta que la base de tiempo acumule 1000 milisegundos.</span>
    </div>
    <div class="delay-models" aria-label="Formas de construir una espera">
      <div><b>base de tiempo</b><span>un temporizador actualiza un contador de milisegundos</span><small>Arduino usa esta idea para `delay()`</small></div>
      <div><b>espera activa</b><span>leer → comparar → repetir si todavía falta tiempo</span><small>el procesador permanece ocupado esperando</small></div>
      <div><b>retardo manual</b><span>un `while` o `for` consume ciclos de reloj</span><small>se estima con frecuencia y ciclos por vuelta</small></div>
    </div>
  </div>
  <div class="clock-lab" aria-label="Modelo visual del reloj, temporizador y espera activa">
    <div class="osc-core">
      <b>Oscilador</b>
      <small>marca el ritmo eléctrico</small>
      <span>millones de ciclos por segundo</span>
    </div>
    <div class="wave-scope">
      <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
      <i class="cycle-runner"></i>
    </div>
    <div class="cycle-math">
      <div><b>ciclo</b><span>un latido del reloj interno</span></div>
      <div><b>instrucción</b><span>puede tomar uno o varios ciclos</span></div>
      <div><b>interrupción</b><span>una pausa breve para actualizar el tiempo</span></div>
    </div>
    <div class="delay-engine" aria-label="Ruta del tiempo dentro del microcontrolador">
      <div class="timer-ladder">
        <div><b>reloj</b><span>pulsos muy rápidos</span></div>
        <i></i>
        <div><b>divisor</b><span>baja la velocidad de conteo</span></div>
        <i></i>
        <div><b>temporizador</b><span>avisa cada 1 ms</span></div>
        <i></i>
        <div><b>contador</b><span>0, 1, 2... 1000 ms</span></div>
      </div>
      <div class="wait-loop-card">
        <strong>Mientras tanto, el procesador espera</strong>
        <div><b>leer</b><span>tiempo actual</span></div>
        <div><b>restar</b><span>actual - inicio</span></div>
        <div><b>comparar</b><span>¿ya son 1000?</span></div>
        <div><b>saltar</b><span>si falta tiempo, repetir</span></div>
      </div>
      <div class="manual-delay-card">
        <strong>Retardo hecho a mano</strong>
        <code>while (contador &gt; 0) {<br>&nbsp;&nbsp;NOP(); contador--;<br>}</code>
        <div class="manual-delay-formula">
          <b>tiempo ≈ vueltas × ciclos/vuelta ÷ F_CPU</b>
          <span>120 MHz y 5 ciclos/vuelta → 24 M vueltas ≈ 1 s</span>
        </div>
      </div>
    </div>
    <div class="mcu-prepare-link timing-next-link">
      <span class="mcu-prepare-kicker">Siguiente idea</span>
      <strong>El reloj tambien coordina comunicacion</strong>
      <small>de esperar 1 segundo a leer sensores por I2C, SPI o UART</small>
      <span class="mcu-prepare-arrow">-&gt;</span>
    </div>
  </div>
</div>

---
class: protocol-book-slide
---

<p class="eyebrow">Escena 14</p>

# I2C y UART: dos formas de ordenar una conversacion serial

<div class="book-protocol"><p class="book-def"><b>Protocolo de comunicacion.</b> Conjunto de reglas que indica como se representan los bits, que lineas fisicas se emplean, quien inicia la transmision y en que instante debe leerse cada senal electrica.</p><div class="book-panels"><section class="book-panel i2c-panel"><header><b>I2C</b><span>Inter-Integrated Circuit · sincrono</span></header><svg viewBox="0 0 520 205" role="img" aria-label="Bus I2C con SDA, SCL y multiples dispositivos direccionados"><rect class="chip master" x="18" y="76" width="82" height="58" rx="8"/><text x="59" y="100">Swan</text><text x="59" y="119">controlador</text><path class="bus sda" d="M112 82H488"/><path class="bus scl" d="M112 127H488"/><text class="wire-label" x="118" y="74">SDA datos</text><text class="wire-label" x="118" y="151">SCL reloj</text><g class="i2c-device d1"><path d="M192 82V45"/><path d="M192 127V45"/><rect class="chip" x="158" y="18" width="68" height="45" rx="7"/><text x="192" y="76">addr 0x40</text></g><g class="i2c-device d2"><path d="M306 82V45"/><path d="M306 127V45"/><rect class="chip" x="272" y="18" width="68" height="45" rx="7"/><text x="306" y="76">addr 0x64</text></g><g class="i2c-device d3"><path d="M420 82V45"/><path d="M420 127V45"/><rect class="chip" x="386" y="18" width="68" height="45" rx="7"/><text x="420" y="76">addr 0x81</text></g><circle class="pulse address-pulse" cx="192" cy="82" r="6"/><polyline class="clock-wave-svg" points="205,127 216,127 216,111 228,111 228,127 240,127 240,111 252,111 252,127 264,127 264,111 276,111 276,127 288,127 288,111 300,111 300,127"/><text class="caption" x="18" y="188">Un mismo bus puede conectar varios sensores; todos observan el bus, pero responde el dispositivo cuya direccion coincide.</text></svg></section><section class="book-panel uart-panel"><header><b>UART</b><span>Universal Asynchronous Receiver/Transmitter · asincrono</span></header><svg viewBox="0 0 520 205" role="img" aria-label="Comunicacion UART punto a punto con TX RX y trama asincrona"><rect class="chip master uart-chip" x="30" y="65" width="90" height="78" rx="8"/><text x="75" y="99">Swan</text><text x="75" y="119">UART</text><rect class="chip module" x="388" y="65" width="92" height="78" rx="8"/><text x="434" y="99">Modulo</text><text x="434" y="119">UART</text><path class="bus uart-tx" d="M128 82H380"/><path class="bus uart-rx" d="M380 128H128"/><text class="wire-label" x="132" y="74">TX → RX</text><text class="wire-label" x="300" y="150">RX ← TX</text><g class="uart-frame"><text x="176" y="38">trama: inicio · datos · parada</text><path d="M176 50h18v18h18V50h18v18h18V50h18v18h18V50h18v18h18"/></g><rect class="baud" x="183" y="158" width="154" height="25" rx="6"/><text x="260" y="175">baud rate comun</text><circle class="pulse uart-pulse" cx="220" cy="82" r="6"/><text class="caption" x="30" y="188">No viaja una linea de reloj. Cada extremo usa su propio reloj interno y ambos deben acordar la misma velocidad.</text></svg></section></div><div class="book-comparison"><b>Contraste principal</b><span>I2C organiza una conversacion de bus: pocos cables, varios dispositivos y direcciones. UART organiza una conversacion punto a punto: menos estructura de bus, pero mayor dependencia de que ambos extremos conserven el mismo ritmo temporal.</span></div></div>

---
class: swan-pins-book-slide
---

<p class="eyebrow">Escena 14B</p>

# Pines de la Swan: GPIO y funciones de comunicacion

<div class="swan-pin-book"><figure><img src="./assets/imagenes/swan-pinout-feather-v3.png" alt="Pinout oficial de Blues Swan v3.0 en formato Feather" /><figcaption>Pinout oficial Blues Swan v3.0</figcaption></figure><div class="pin-book-copy"><p><b>GPIO</b> significa entrada/salida de proposito general. Un pin configurado como GPIO permite que el programa lea un nivel logico o produzca un voltaje digital. Cuando el pin se asigna a un periferico interno, la misma terminal fisica puede convertirse en parte de un protocolo de comunicacion.</p><div class="pin-book-table"><div><b>Uso general</b><span>D5, D6, D9, D10...</span><small>LED, boton, salida digital, lectura HIGH/LOW.</small></div><div><b>I2C</b><span>SDA + SCL</span><small>Bus sincrono para multiples sensores con direccion.</small></div><div><b>UART</b><span>TX + RX</span><small>Enlace asincrono entre dos extremos con velocidad acordada.</small></div><div><b>SPI</b><span>SCK + MOSI + MISO + CS</span><small>Bus sincrono rapido; el pin CS selecciona el dispositivo activo.</small></div></div><a href="../actividades/hola-mundo" target="_top" class="mcu-prepare-link pin-activity-link" aria-label="Ir a la Actividad 2 Leer SEN55 por I2C"><span class="mcu-prepare-kicker">Siguiente actividad</span><strong>Actividad 2: leer SEN55 por I2C</strong><small>usar SDA y SCL para obtener particulas, temperatura, humedad, VOC y NOx</small><span class="mcu-prepare-arrow">-&gt;</span></a></div></div>

---

<p class="eyebrow">Escena 15</p>

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

<p class="eyebrow">Escena 16</p>

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
