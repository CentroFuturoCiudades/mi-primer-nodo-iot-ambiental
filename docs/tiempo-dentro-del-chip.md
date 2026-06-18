---
title: 1. Algoritmo, memoria y tiempo visible
---

# Actividad 1 — Algoritmo, memoria y tiempo visible

En esta actividad vas a usar el LED de la **Blues Swan R5** como una ventana al
microcontrolador. La meta no es solo parpadear: la meta es entender cómo un
algoritmo se guarda en memoria, cómo la CPU lo ejecuta paso a paso y cómo el
reloj interno permite convertir ciclos eléctricos en tiempo visible.

## Objetivo

Construir señales con el LED y explicarlas usando cuatro ideas:

```text
algoritmo → instrucciones en Flash → ciclo de ejecución → tiempo medido
```

## Material

- Blues Swan R5 configurada.
- Arduino IDE.
- Cable USB de datos.
- Cronómetro de celular, opcional.
- Libreta o documento para tus respuestas.

:::tip Antes de cargar
Si Arduino IDE no logra cargar el programa, repite la secuencia **BOOT + RESET**
de la Swan y vuelve a presionar **Upload**.
:::

## 1. Mapa mental rápido

Un **algoritmo** es una lista finita de pasos para resolver una tarea. En código
aparecen tres estructuras básicas:

| Estructura | Qué significa | Ejemplo |
|---|---|---|
| Secuencia | ejecutar pasos en orden | prender → esperar → apagar |
| Decisión | elegir según una condición | `if (boton == 1)` |
| Repetición | ejecutar varias veces | `while`, `for`, `loop()` |

Completa en una frase:

| Pregunta | Tu respuesta |
|---|---|
| ¿Qué parte del programa se repite para siempre? | |
| ¿Dónde queda guardado el programa después de cargarlo? | |
| ¿Qué bloque interno mide el tiempo? | |
| ¿Qué bloque cambia el voltaje del LED? | |

## 2. Programa base: una señal visible

Carga este programa:

```cpp
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);

  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
```

Explica el recorrido:

```text
digitalWrite → registro GPIO → voltaje en la patita → LED
delay        → temporizador → contador de milisegundos → espera
```

## 3. Mision: senal de ayuda con LED

Crea una señal de ayuda:

```text
3 pulsos cortos + pausa larga
```

Usa esta base:

```cpp
void pulsoCorto() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(120);
  digitalWrite(LED_BUILTIN, LOW);
  delay(120);
}

void pausaLarga() {
  delay(900);
}

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  pulsoCorto();
  pulsoCorto();
  pulsoCorto();
  pausaLarga();
}
```

Ahora modifica el código para crear una señal propia:

| Señal | Patrón propuesto | Tu patrón |
|---|---|---|
| Ayuda | corto, corto, corto, pausa | |
| Latido | corto, pausa corta, corto, pausa larga | |
| Alerta ambiental | dos pulsos rápidos, pausa, un pulso largo | |

Pregunta: ¿por qué crear funciones como `pulsoCorto()` ayuda a describir mejor
el algoritmo?

## 4. Experimento: cuando el parpadeo parece continuo

Cambia los dos tiempos del programa base y observa:

| Prueba | Encendido | Apagado | ¿Se distingue el parpadeo? |
|---|---:|---:|---|
| A | 1000 ms | 1000 ms | |
| B | 250 ms | 250 ms | |
| C | 80 ms | 80 ms | |
| D | 30 ms | 30 ms | |

Después prueba ciclos de trabajo distintos:

| Encendido | Apagado | ¿Cómo cambia el brillo percibido? |
|---:|---:|---|
| 100 ms | 900 ms | |
| 500 ms | 500 ms | |
| 900 ms | 100 ms | |

Idea técnica: el **ciclo de trabajo** es la fracción del periodo en la que la
salida permanece encendida.

## 5. Reto: construir y medir un retardo manual

`delay(1000)` usa una base de tiempo mantenida por temporizadores. En este reto
vas a construir otra forma de espera: una rutina que gasta ciclos de CPU de
manera controlada. La meta no es reemplazar `delay()`, sino comparar tres cosas:
lo que predice la teoría, lo que genera el programa compilado y lo que observas
en la tarjeta.

La Swan R5 trabaja con un microcontrolador STM32L4R5 basado en Cortex-M4. En la
documentación de Blues, la Swan v3.0 aparece con **120 MHz** de reloj, es decir:

```text
F_CPU = 120 000 000 ciclos/s
1 ciclo ≈ 8.33 ns
```

### 5.1 Primera estimación: ciclo de espera ideal

Un retardo manual mínimo puede pensarse como un ciclo que repite tres acciones:

| Acción de máquina | Costo típico en Cortex-M4 | Papel en el ciclo |
|---|---:|---|
| No hacer operación útil | 1 ciclo | consume una marca de reloj |
| Restar 1 al contador | 1 ciclo | actualiza las vueltas restantes |
| Saltar si el contador no llegó a 0 | 1 ciclo si no salta; `1 + P` si salta | repite el ciclo |

En el manual técnico del Cortex-M4, `NOP` aparece como una instrucción de 1
ciclo; muchas operaciones aritméticas simples también toman 1 ciclo; y los
saltos condicionales dependen del relleno de la tubería de ejecución, por eso se
modelan como `1 + P`.

Para una estimación de laboratorio podemos usar:

```text
ciclos_por_vuelta ≈ 1 + 1 + 3 = 5 ciclos/vuelta
```

Entonces, para aproximar 1 segundo:

```text
vueltas ≈ tiempo × F_CPU / ciclos_por_vuelta
vueltas ≈ 1 s × 120 000 000 ciclos/s / 5 ciclos
vueltas ≈ 24 000 000
```

Este no será el valor final. Es una hipótesis técnica inicial.

### 5.2 Programa de prueba

Prueba este código. La función `__NOP()` significa **No Operation**: la CPU
ejecuta una operación que no cambia el estado lógico del programa, pero sí
consume tiempo de reloj.

```cpp
#include <Arduino.h>

void esperaManual(volatile unsigned long vueltas) {
  while (vueltas > 0) {
    __NOP();
    vueltas--;
  }
}

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  esperaManual(800000);

  digitalWrite(LED_BUILTIN, LOW);
  esperaManual(800000);
}
```

Empieza con un valor calculado, por ejemplo `24000000`, y observa si el LED se
acerca a 1 segundo encendido y 1 segundo apagado. Si tarda demasiado, reduce el
valor; si tarda muy poco, auméntalo.

### 5.3 Comparación analítica vs. empírica

Llena esta tabla. Puedes medir con cronómetro contando 10 parpadeos completos y
dividiendo el tiempo entre 10.

| Prueba | Vueltas | Ciclos/vuelta supuestos | Tiempo teórico por espera | Tiempo medido por espera | Error aproximado |
|---|---:|---:|---:|---:|---:|
| A | 12 000 000 | 5 | 0.50 s | | |
| B | 24 000 000 | 5 | 1.00 s | | |
| C | 36 000 000 | 5 | 1.50 s | | |

Usa esta fórmula:

```text
tiempo ≈ vueltas × ciclos_por_vuelta / frecuencia_del_reloj
```

Después despeja el costo real observado:

```text
ciclos_por_vuelta_medido ≈ tiempo_medido × F_CPU / vueltas
```

Pregunta de análisis: ¿tu costo medido se acerca a 5 ciclos por vuelta? Si no,
propón una causa: optimización del compilador, accesos a memoria por `volatile`,
interrupciones del sistema, llamadas a funciones o forma exacta del ciclo.

### 5.4 Cierre técnico

Un retardo por ciclos es útil para aprender arquitectura porque conecta reloj,
instrucciones y flujo de control. En un producto real se prefieren temporizadores
del microcontrolador, porque son más estables y liberan a la CPU para hacer otras
tareas.

Fuentes para el cálculo:

- [Blues Swan Datasheet](https://dev.blues.io/datasheets/swan-datasheet/swan-v3-0/): Swan v3.0, STM32L4R5ZIY6, reloj de 120 MHz.
- [Arm Cortex-M4 Processor Technical Reference Manual](https://documentation-service.arm.com/static/5fce431be167456a35b36ade): tabla de ciclos de instrucciones del Cortex-M4.

## Entregable

Entrega una sola hoja o captura con:

- Tu definición de algoritmo.
- Un diagrama pequeño: Flash → PC → CPU → GPIO/Timer → LED.
- Tu señal de ayuda o alerta.
- La tabla donde indicas cuándo el parpadeo empieza a verse continuo.
- Tu mejor valor de `esperaManual(...)` y cómo lo ajustaste.

## Cierre

El LED parece simple, pero revela mucho: memoria de programa, flujo de control,
GPIO, temporizadores, ciclos de reloj y la diferencia entre esperar con una base
de tiempo y esperar gastando ciclos de CPU.

<a href="./hola-mundo" class="button button--primary">Continuar a Actividad 2: leer SEN55 por I2C</a>
