---
title: 3. Comunicar mediciones del sensor por LoRa
pagination_next: null
---

# Actividad 3 - Comunicar mediciones del sensor por LoRa

En esta actividad se relaciona el código con la arquitectura revisada en la
presentación:

```text
Swan -> I2C -> Notecard -> LoRa -> pasarela -> Notehub
```

El propósito no es memorizar todo el firmware, sino reconocer cómo el programa
prepara la secuencia de comunicación, construye una nota y solicita su
sincronización.

## Objetivo

Interpretar el código como una arquitectura de comunicación por capas:

| Elemento de código | Función en el sistema |
|---|---|
| `Wire.begin()` | abre el canal I2C local |
| `hub.set` | registra el ProductUID y modo de conexión |
| `note.template` | define la forma compacta del mensaje |
| `note.add` | crea una nota con valores |
| `hub.sync` | solicita enviar hacia Notehub |
| `delay(...)` | espera antes del siguiente ciclo |

## 1. Prueba mínima con datos simulados

Consulta el programa de referencia para realizar una prueba mínima de
comunicación con datos simulados.

<a href="../codigos/03_notecard_lora_quick_test/03_notecard_lora_quick_test.ino" class="button button--secondary">Consultar programa de prueba</a>

Este programa utiliza datos simulados para comprobar la comunicación antes de
integrar sensores reales.

### Bloque A: preparación de Swan y Notecard

```cpp
Wire.begin();
notecard.begin();
notecard.setDebugOutputStream(Serial);
```

La Swan se comunica con la Notecard por I2C. `Serial` se utiliza únicamente
para observar el comportamiento del programa.

### Bloque B: asociación con el proyecto

```cpp
J *req = notecard.newRequest("hub.set");
JAddStringToObject(req, "product", ProductUID);
JAddStringToObject(req, "mode", "continuous");
notecard.sendRequest(req);
```

`hub.set` indica a la Notecard a qué proyecto pertenece el nodo.

### Bloque C: declaración de la forma del mensaje

```cpp
req = notecard.newRequest("note.template");
JAddStringToObject(req, "file", "sensors.qo");
JAddStringToObject(req, "format", "compact");
JAddNumberToObject(req, "port", 10);
```

La plantilla funciona como un molde: antes de enviar, define qué campos
existirán y de qué tipo serán. Esto es importante en LoRa, porque los mensajes
deben mantenerse pequeños y bien estructurados.

### Bloque D: creación de la nota

```cpp
req = notecard.newRequest("note.add");
JAddStringToObject(req, "file", "sensors.qo");

J *body = JAddObjectToObject(req, "body");
JAddNumberToObject(body, "counter", counter);
JAddNumberToObject(body, "temp", 25.5);
JAddNumberToObject(body, "humidity", 55.0);
JAddNumberToObject(body, "battery", 3.7);
```

Esta es la misma idea presentada en la diapositiva: una nota `sensors.qo`
contiene campos con valores concretos.

### Bloque E: solicitud de sincronización

```cpp
req = notecard.newRequest("hub.sync");
notecard.sendRequest(req);
```

La nota puede quedar en cola. `hub.sync` solicita una oportunidad para enviarla
hacia Notehub.

## 2. Mini-reto: modificación del paquete

Cambia los valores simulados:

```cpp
JAddNumberToObject(body, "temp", 28.0);
JAddNumberToObject(body, "humidity", 62.0);
JAddNumberToObject(body, "battery", 3.9);
```

Después cambia temporalmente el intervalo de prueba:

```cpp
delay(15000);
```

Pregunta de verificación: ¿por qué un nodo real no debería enviar datos cada pocos
segundos durante todo el día?

## 3. Lectura del firmware final por capas

Consulta el firmware final del nodo ambiental. El análisis no debe hacerse como
una lectura lineal, sino como una revisión por capas funcionales.

<a href="../codigos/03_firmware_final/NEU_Weather_Solar_V1_1.ino" class="button button--secondary">Consultar firmware final</a>

Analízalo por capas:

| Capa | Elementos por identificar |
|---|---|
| Identidad | `ProductUID` |
| Comunicación | `Wire`, `Notecard`, `hub.set`, `hub.sync` |
| Plantillas | `sensors.qo`, `battery.qo`, `note.template` |
| Sensores | SEN55, SCD41, batería |
| Decisión | `if (...)`, batería baja, errores |
| Repetición | `loop()`, espera, bajo consumo |

## Mapa de lectura

Completa la tabla:

| Pregunta | Respuesta |
|---|---|
| ¿Qué se configura una sola vez en `setup()`? | |
| ¿Qué se repite en `loop()`? | |
| ¿Qué campos viajan dentro de `sensors.qo`? | |
| ¿Dónde aparece una condición booleana? | |
| ¿Qué parte conecta con Notehub? | |

## Entregable

Entrega una nota breve con:

- Evidencia de una nota enviada, o de un intento de envío, en el monitor serial.
- Explicación de `note.template` en tus palabras.
- Explicación de `note.add` en tus palabras.
- Una condición booleana encontrada en el código.
- Un diagrama breve de la secuencia: Swan -> Notecard -> LoRa -> Notehub.
