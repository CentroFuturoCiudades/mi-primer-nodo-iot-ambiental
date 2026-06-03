---
title: 1. Código, memoria y tiempo
---

# Actividad 1 — Código, memoria y tiempo

En **Antes de empezar** cargaste un programa que prende y apaga el LED. En la
historia visual vimos la idea por dentro: el programa no vive como texto dentro
de la tarjeta, sino como instrucciones guardadas en memoria.

En esta actividad vas a seguir el recorrido del programa como si fueras el
microcontrolador.

## Objetivo

Explicar, con tus propias palabras y con un diagrama, cómo el código Arduino se
convierte en instrucciones, cómo se guarda en memoria y cómo el reloj interno
permite construir esperas como `delay(1000)`.

## Material

- Blues Swan R5 ya configurada.
- Arduino IDE.
- El programa de parpadeo que cargaste en **Antes de empezar**.
- Libreta, hoja o documento para dibujar.
- Cronómetro de celular, opcional.

## Punto de partida

Usaremos este programa como mapa:

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

:::tip Lenguaje del taller
Cuando aparezca una palabra técnica en inglés, úsala como etiqueta, no como
magia. Por ejemplo: **GPIO** significa una patita configurable de entrada o
salida; **Flash** es memoria que conserva el programa aunque apagues la tarjeta.
:::

## Parte A — Del código a la memoria

Completa este recorrido:

```text
código Arduino → compilador → instrucciones de máquina → memoria Flash
```

Ahora responde:

| Pregunta | Tu respuesta |
|---|---|
| ¿Qué escribimos los humanos? | |
| ¿Qué entiende realmente el microcontrolador? | |
| ¿Dónde queda guardado el programa después de cargarlo? | |
| ¿Por qué el programa sigue ahí aunque desconectes la tarjeta? | |

## Parte B — Mapa interno del microcontrolador

Dibuja estos bloques y conéctalos con flechas:

```text
Memoria de programa → Contador de programa → Decodificador
                         ↓
                 Registros / Unidad lógica
                         ↓
              Entradas y salidas → LED
```

Usa esta tabla para completar tu dibujo:

| Bloque | Nombre técnico | Qué hace en palabras sencillas |
|---|---|---|
| Memoria de programa | Flash | Guarda las instrucciones del programa. |
| Contador de programa | PC, de *program counter* | Apunta a la siguiente instrucción. |
| Decodificador | Instruction decoder | Decide qué operación se debe hacer. |
| Registros | Register file | Guardan datos pequeños y rápidos. |
| Unidad lógica | ALU | Calcula, compara y toma decisiones simples. |
| Memoria de datos | RAM | Guarda variables mientras el programa corre. |
| Entradas y salidas | GPIO | Cambian voltajes en las patitas de la tarjeta. |
| Temporizador | Timer | Cuenta pulsos del reloj para medir tiempo. |

## Parte C — Sigue una vuelta del programa

Imagina que el programa está corriendo dentro de `loop()`. Completa qué bloque
participa más en cada paso.

| Paso | Línea de código | Qué ocurre por dentro | Bloque principal |
|---|---|---|---|
| 1 | `digitalWrite(..., HIGH)` | Se cambia un registro de salida para subir el voltaje del LED. | |
| 2 | `delay(1000)` | El programa espera hasta que el contador de tiempo avance 1000 ms. | |
| 3 | `digitalWrite(..., LOW)` | Se cambia el registro de salida para bajar el voltaje del LED. | |
| 4 | `delay(1000)` | Se repite la espera de 1000 ms. | |
| 5 | `loop()` | El programa vuelve al inicio de la función. | |

## Parte D — ¿Qué pasa durante `delay(1000)`?

Una forma útil de pensarlo es esta:

```text
oscilador → ciclos del reloj → temporizador → contador de milisegundos
```

Después, la función `delay(1000)` espera de manera activa:

```text
leer tiempo actual → restar tiempo inicial → comparar con 1000 → repetir si falta
```

Esto no significa que `delay(1000)` sea una sola instrucción del procesador. Es
una función de Arduino que usa una base de tiempo para esperar aproximadamente
un segundo.

:::info Retardo hecho a mano
En ensamblador también se puede crear un retardo con un contador:

```text
repetir:
  restar 1 al contador
  si no llegó a cero, volver a repetir
```

Ese método sirve para aprender ciclos, pero depende mucho de la frecuencia del
reloj, de cuántos ciclos tarda cada instrucción y de si ocurren interrupciones.
:::

## Parte E — Experimento de percepción

Cambia los dos `delay(1000)` por estos valores y observa el LED:

| Prueba | Tiempo encendido | Tiempo apagado | ¿Cómo se ve? |
|---|---:|---:|---|
| A | 1000 ms | 1000 ms | |
| B | 500 ms | 500 ms | |
| C | 200 ms | 200 ms | |
| D | 100 ms | 100 ms | |
| E | 50 ms | 50 ms | |

Pregunta clave: ¿en qué momento deja de sentirse como “prende y apaga” y empieza
a verse casi continuo?

## Entregable

Al terminar, debes tener:

- Un diagrama del recorrido del programa dentro del microcontrolador.
- La tabla de una vuelta de `loop()` completada.
- Una observación sobre qué pasa cuando reduces el tiempo de `delay()`.
- Una explicación breve de por qué `delay(1000)` necesita al reloj interno.

## Cierre

`delay(1000)` parece una instrucción humana muy simple, pero por dentro conecta
varias ideas importantes: memoria, instrucciones, registros, temporizadores y el
ritmo eléctrico del microcontrolador.

<a href="./primer-parpadeo" class="button button--primary">Continuar a Actividad 2: primer parpadeo</a>
