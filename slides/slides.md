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
layout: center
---

<p class="eyebrow">Escena 5</p>

# Un semiconductor permite construir decisiones

<div class="binary-choice">
  <div>
    <span>0</span>
    <p>bloquea corriente</p>
  </div>
  <b></b>
  <div class="on">
    <span>1</span>
    <p>deja pasar corriente</p>
  </div>
</div>

<v-clicks>

- Con estados controlables representamos ceros y unos.
- Con ceros y unos construimos instrucciones.
- Con instrucciones prendemos un LED o leemos un sensor.

</v-clicks>

---

<p class="eyebrow">Escena 6</p>

# El transistor

<div class="split">
  <div>
    <h2>Un interruptor microscópico</h2>
    <p>Un transistor decide poco. Millones de transistores conectados con orden pueden construir una computadora.</p>
  </div>
  <div class="switch">
    <span>0</span>
    <span class="active">1</span>
  </div>
</div>

---

<p class="eyebrow">Escena 7</p>

# La complejidad nace por repetición

<div class="timeline">
  <span>1 transistor</span>
  <span>muchos transistores</span>
  <span>reglas</span>
  <span>memoria y cálculo</span>
</div>

<v-clicks>

- Una pieza simple no parece inteligente.
- Muchas piezas simples pueden hacer tareas complejas.
- Así se construye la lógica digital.

</v-clicks>

---

<p class="eyebrow">Escena 8</p>

# Compuertas lógicas

Las compuertas son reglas pequeñas que combinan ceros y unos.

<div class="truth-table">
  <div class="head">A</div><div class="head">B</div><div class="head">Salida</div>
  <div>0</div><div>0</div><div>0</div>
  <div>0</div><div>1</div><div>0</div>
  <div>1</div><div>0</div><div>0</div>
  <div>1</div><div>1</div><div class="on">1</div>
</div>

---

<p class="eyebrow">Escena 9</p>

# Memoria

## Algunos circuitos pueden recordar

<div class="memory-row">
  <span>0</span><span class="on">1</span><span>0</span><span class="on">1</span>
  <span class="on">1</span><span>0</span><span>0</span><span class="on">1</span>
</div>

<v-clicks>

- Un bit guarda un estado.
- Muchos bits guardan números, textos, instrucciones y mediciones.
- En un microcontrolador, la memoria es esencial.

</v-clicks>

---

<p class="eyebrow">Escena 10</p>

# ALU

<div class="alu">
  <span>A = 7</span>
  <strong>ALU</strong>
  <span>B = 3</span>
</div>

<p class="takeaway">Cuando escribimos `if (co2 > 1000)`, la tarjeta compara valores.</p>

---

<p class="eyebrow">Escena 11</p>

# El microcontrolador como una ciudad

<div class="city-grid">
  <div><b>CPU</b><span>centro de control</span></div>
  <div><b>ALU</b><span>cálculo y comparación</span></div>
  <div><b>Flash</b><span>programa guardado</span></div>
  <div><b>RAM</b><span>mesa de trabajo</span></div>
  <div><b>Reloj</b><span>ritmo interno</span></div>
  <div><b>GPIO</b><span>puertas al exterior</span></div>
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
