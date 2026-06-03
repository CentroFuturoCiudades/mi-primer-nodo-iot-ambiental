---
title: 2. Primer parpadeo
---

# Actividad 2 — Primer parpadeo

Ahora que ya entendiste el recorrido interno del programa, vas a usar esa teoría
para controlar algo visible: el LED de la tarjeta.

La meta no es solo “hacer que parpadee”. La meta es comprobar que cambiar código
cambia instrucciones, esas instrucciones cambian registros de salida, y esos
registros cambian voltaje en una patita.

## Objetivo

Programar diferentes patrones de parpadeo y relacionarlos con tres ideas:

```text
instrucción → salida digital → tiempo visible
```

## Material

- Blues Swan R5 conectada por USB.
- Arduino IDE configurado.
- Puerto COM correcto seleccionado.
- Método de carga en modo DFU, si estás cargando sin STLINK-V3MINI.

:::tip Antes de cargar
Si Arduino IDE no logra cargar el programa, repite la secuencia **BOOT + RESET**
de la Swan y vuelve a presionar **Upload**.
:::

## Parte A — Programa base

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

Resultado esperado:

```text
LED encendido 1 segundo → LED apagado 1 segundo → se repite
```

## Parte B — Traduce cada línea

Completa la tabla antes de modificar el programa.

| Línea | Qué le pedimos a Arduino | Qué ocurre físicamente |
|---|---|---|
| `pinMode(LED_BUILTIN, OUTPUT)` | | |
| `digitalWrite(LED_BUILTIN, HIGH)` | | |
| `delay(1000)` | | |
| `digitalWrite(LED_BUILTIN, LOW)` | | |
| `delay(1000)` | | |

Palabras que deben aparecer en tus respuestas: **salida**, **voltaje**,
**temporizador**, **LED**.

## Parte C — Cambia el ritmo

Modifica los tiempos y registra qué observas:

| Prueba | Código | Predicción | Observación |
|---|---|---|---|
| Lento | `delay(1500);` y `delay(1500);` | | |
| Normal | `delay(1000);` y `delay(1000);` | | |
| Rápido | `delay(250);` y `delay(250);` | | |
| Muy rápido | `delay(80);` y `delay(80);` | | |

Pregunta: ¿tu predicción coincidió con lo que viste?

## Parte D — Encendido y apagado no tienen que durar lo mismo

Ahora prueba este patrón:

```cpp
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(100);

  digitalWrite(LED_BUILTIN, LOW);
  delay(900);
}
```

Este programa no solo parpadea más rápido o más lento. Cambia la proporción de
tiempo encendido contra tiempo apagado.

Completa:

| Tiempo encendido | Tiempo apagado | Porcentaje aproximado encendido |
|---:|---:|---:|
| 100 ms | 900 ms | |
| 250 ms | 750 ms | |
| 500 ms | 500 ms | |
| 900 ms | 100 ms | |

:::info Idea técnica
Esa proporción se llama **ciclo de trabajo**. En palabras sencillas: de todo el
ciclo completo, qué parte del tiempo la salida está encendida.
:::

## Parte E — Señal con significado

Construye una señal de emergencia:

```text
3 parpadeos rápidos + 1 pausa larga
```

Puedes empezar con esta versión:

```cpp
void pulsoRapido() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(120);
  digitalWrite(LED_BUILTIN, LOW);
  delay(120);
}

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  pulsoRapido();
  pulsoRapido();
  pulsoRapido();

  delay(900);
}
```

Observa que ahora creamos una función propia: `pulsoRapido()`. No es una
instrucción nueva del microcontrolador; es una forma humana de agrupar varias
instrucciones para reutilizarlas.

## Parte F — Reto técnico

Haz una señal tipo “latido”:

```text
parpadeo corto + pausa corta + parpadeo corto + pausa larga
```

Ejemplo de tiempos:

```text
80 ms encendido
120 ms apagado
80 ms encendido
800 ms apagado
```

Después responde:

| Pregunta | Respuesta |
|---|---|
| ¿Qué líneas cambian el voltaje del LED? | |
| ¿Qué líneas controlan el tiempo visible? | |
| ¿Qué parte del programa se repite para siempre? | |
| ¿Dónde aparece la idea de temporizador vista en la slide? | |

## Diagnóstico rápido

| Síntoma | Posible causa | Qué revisar |
|---|---|---|
| El LED no cambia | El programa no se cargó | Repite BOOT + RESET y carga otra vez. |
| Carga, pero no ves parpadeo | Los tiempos son muy pequeños | Prueba con `delay(1000)`. |
| Arduino IDE marca error de puerto | Puerto COM incorrecto | Revisa Administrador de dispositivos. |
| Error de compilación | Llaves o punto y coma faltante | Revisa `{}`, `()` y `;`. |

## Cierre

En esta actividad el LED fue nuestro “osciloscopio humano”: una forma visible de
notar que el microcontrolador ejecuta instrucciones en orden y usa el tiempo
interno para producir cambios en el mundo físico.

<a href="./hola-mundo" class="button button--primary">Continuar a Actividad 3: hola mundo</a>
