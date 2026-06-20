---
title: C1. Comunicación del nodo ambiental
pagination_next: null
---

# C1. Comunicación del nodo ambiental

En esta actividad se relaciona el código con la arquitectura revisada en la
presentación:

```text
Swan -> I2C -> Notecard -> LoRa -> Gateway -> Notehub
```


## Objetivo

Interpretar elementos clave de los algoritmos revisados en esta sección:

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

Una nota `sensors.qo`
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

## 3. Lectura del firmware final

Consulta el firmware final del nodo ambiental e identifica los elementos clave.

<a href="../codigos/03_firmware_final/NEU_Weather_Solar_V1_1.ino" class="button button--secondary">Consultar firmware final</a>

Elementos clave:

| Bloque | Elementos por identificar |
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


