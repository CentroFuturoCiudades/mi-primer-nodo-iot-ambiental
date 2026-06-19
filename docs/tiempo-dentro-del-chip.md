---
title: 1. Controlar un LED / Mi primer programa
pagination_next: null
pagination_prev: null
---

# Actividad 1 - Controlar un LED / Mi primer programa

En esta actividad se utiliza el LED de la **Blues Swan R5** para observar una
idea fundamental: un programa es una secuencia de instrucciones almacenadas en
memoria que la CPU ejecuta de manera ordenada y repetitiva.

```text
código -> memoria Flash -> CPU -> GPIO -> LED
```

## Objetivo

Construir una señal visible con el LED y explicar el programa mediante tres
conceptos básicos de programación embebida:

| Idea | En el código |
|---|---|
| Secuencia | instrucciones en orden |
| Repetición | `loop()` se ejecuta continuamente |
| Tiempo | `delay(...)` espera cierta cantidad de milisegundos |

## Material

- Blues Swan R5 configurada.
- Arduino IDE.
- Cable USB de datos.
- Libreta o documento para anotar respuestas.

:::tip Antes de cargar
Si Arduino IDE no logra cargar el programa, repite la secuencia **BOOT + RESET**
de la Swan y vuelve a presionar el botón de carga.
:::

## 1. Programa base: parpadeo del LED

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

Interpreta el código como una secuencia de instrucciones:

| Línea | Función |
|---|---|
| `pinMode(...)` | prepara el pin del LED como salida |
| `digitalWrite(..., HIGH)` | entrega voltaje al LED |
| `delay(1000)` | espera 1000 ms |
| `digitalWrite(..., LOW)` | apaga el LED |

Pregunta de verificación: ¿qué parte se ejecuta una sola vez y qué parte se
repite?

## 2. Modificar la base de tiempo

Modifica los dos `delay(1000)` y registra el comportamiento del LED:

| Prueba | Encendido | Apagado | Observación |
|---|---:|---:|---|
| A | 1000 ms | 1000 ms | |
| B | 250 ms | 250 ms | |
| C | 80 ms | 80 ms | |

Cuando el tiempo baja mucho, el parpadeo puede parecer casi continuo. Eso
ocurre porque el ojo ya no distingue cada cambio individual.

## 3. Definir una señal mediante funciones

Una función permite agrupar varias instrucciones bajo un nombre descriptivo. De
esta manera, el programa expresa mejor la intención del algoritmo.

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

Modifica el patrón para diseñar una señal propia:

| Señal | Patrón |
|---|---|
| Ayuda | tres pulsos cortos y pausa |
| Latido | dos pulsos y pausa larga |
| Alerta | pulso largo, pausa, dos pulsos cortos |

Pregunta de verificación: ¿por qué `pulsoCorto()` hace más legible el
algoritmo?

## 4. Mini-reto: incorporar una decisión

Agrega una condición para modificar la señal según el valor de una variable:

```cpp
bool alerta = true;

void loop() {
  if (alerta) {
    pulsoCorto();
    pulsoCorto();
    pausaLarga();
  } else {
    pulsoCorto();
    pausaLarga();
  }
}
```

Una condición booleana solo puede tomar dos caminos: verdadero o falso. Esta
misma idea aparecerá después cuando el programa decida si hubo error, si un
sensor respondió o si una medición rebasa un umbral.

## Entregable

Entrega una captura o nota breve con:

- Tu patrón final de LED.
- Una frase que explique qué hace `loop()`.
- Una frase que explique qué hace `delay(...)`.
- Una condición booleana escrita por ti.

## Cierre

Aunque el LED es un elemento sencillo, permite estudiar principios esenciales
del firmware: instrucciones, repetición, tiempo, funciones y decisiones.

<nav class="pagination-nav" aria-label="Siguiente paso">
  <a class="pagination-nav__link pagination-nav__link--next" href="../slides/?slide=10">
    <div class="pagination-nav__sublabel">Siguiente</div>
    <div class="pagination-nav__label">Comunicación local, GPIO y sensores</div>
  </a>
</nav>
