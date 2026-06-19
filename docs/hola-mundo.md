---
title: 2. Lectura de mediciones del sensor
pagination_next: null
pagination_prev: null
---

# Actividad 2 - Lectura de mediciones del sensor

En esta actividad se lee el sensor **SEN55** desde la **Blues Swan R5**. El
propósito es vincular los conceptos de I2C y GPIO revisados en la presentación
con un programa real de medición ambiental:

```text
Swan -> SDA/SCL -> SEN55 -> monitor serial
```

En esta etapa no se utiliza Notecard ni LoRa. Primero se verifica que la Swan
puede iniciar el bus I2C, comunicarse con el sensor y convertir la respuesta en
variables del programa.

## Objetivo

Identificar en el código los siguientes elementos:

| Elemento | Función |
|---|---|
| `Wire.begin()` | inicia el bus I2C |
| `sen5x.begin(Wire)` | conecta la biblioteca del sensor al bus |
| `startMeasurement()` | pide iniciar una medición |
| `readMeasuredValues(...)` | llena variables con datos del sensor |
| `if (error)` | decide qué hacer si la comunicación falla |

## Material

- Blues Swan R5 configurada.
- Sensor SEN55 o SEN5x compatible.
- Cables para alimentación, `SDA`, `SCL` y `GND`.
- Arduino IDE.
- Monitor serial configurado a `115200` baudios.

## 1. Preparación de bibliotecas y conexión

En Arduino IDE abre el administrador de bibliotecas:

```text
Sketch -> Include Library -> Manage Libraries...
```

Instala:

```text
Sensirion I2C SEN5X
Sensirion Core
```

I2C utiliza dos líneas principales:

| Línea | Función |
|---|---|
| `SDA` | transporte de datos |
| `SCL` | señal de reloj del bus |

Conecta el sensor a los pines `SDA` y `SCL` de la Swan. Revisa también la
alimentación y la conexión a tierra antes de energizar el circuito.

## 2. Programa de referencia

Consulta el programa de referencia para la lectura del SEN55. El enlace abre el
material preparado para esta práctica.

<a href="../codigos/02_sen55_i2c/02_sen55_i2c.ino" class="button button--secondary">Consultar programa de referencia</a>

El programa puede interpretarse en cuatro momentos:

| Momento | Fragmento | Significado |
|---|---|---|
| Bus | `Wire.begin();` | la Swan activa el bus I2C |
| Sensor | `sen5x.begin(Wire);` | SEN55 queda asociado al bus |
| Medición | `startMeasurement();` | el sensor inicia su proceso interno |
| Lectura | `readMeasuredValues(...)` | los datos llegan a variables `float` |

## 3. Lectura del código por bloques

### Bloque A: inicio de comunicación

```cpp
Wire.begin();
sen5x.begin(Wire);
```

Este bloque corresponde a la diapositiva de I2C: la Swan actúa como
controlador y el SEN55 responde dentro del mismo bus.

### Bloque B: verificación de errores

```cpp
error = sen5x.deviceReset();
if (error) {
  errorToString(error, errorMessage, 256);
  while (1) {
    delay(1000);
  }
}
```

`if (error)` es una condición booleana. Si ocurre un error, el programa detiene
el flujo normal y evita continuar con una lectura inválida.

### Bloque C: almacenamiento de mediciones

```cpp
float pm2p5;
float temperature;
float humidity;
```

Cada variable almacena un número medido. En la Actividad 3, esta misma relación
entre “campo” y “valor” se utilizará para construir una nota dirigida a
Notehub.

## 4. Observación del monitor serial

Abre el monitor serial a `115200` baudios. Deberá aparecer una salida similar a
la siguiente:

```text
Iniciando SEN55...
SEN55 listo.
Iniciando medición SEN55...
Datos SEN55:
PM2.5: 3.40 ug/m3
Temperatura: 24.60 C
Humedad: 48.20 %
```

Los números exactos no tienen que coincidir. Lo importante es que existan
lecturas numéricas y que el programa no se quede detenido en un error.

## 5. Mini-reto: alerta por PM2.5

Después de leer `pm2p5`, agrega una regla de decisión:

```cpp
if (pm2p5 > 25) {
  Serial.println("ALERTA: PM2.5 elevado.");
  digitalWrite(LED_BUILTIN, HIGH);
} else {
  Serial.println("PM2.5 en nivel bajo para esta prueba.");
  digitalWrite(LED_BUILTIN, LOW);
}
```

En `setup()` agrega también:

```cpp
pinMode(LED_BUILTIN, OUTPUT);
```

En este punto se integran dos conceptos: el sensor entrega datos por I2C y el LED se
controla mediante GPIO.

## Registro

Registra al menos una medición:

| Lugar | PM2.5 | PM10 | Temperatura | Humedad | Observación |
|---|---:|---:|---:|---:|---|
| | | | | | |

## Entregable

Entrega los siguientes elementos:

- Una captura del monitor serial.
- Una frase explicando qué función cumplen `SDA` y `SCL`.
- Una frase explicando por qué el código usa `if (error)`.
- Tu resultado del mini-reto de PM2.5.

<nav class="pagination-nav" aria-label="Siguiente paso">
  <a class="pagination-nav__link pagination-nav__link--next" href="../slides/?slide=12">
    <div class="pagination-nav__sublabel">Siguiente</div>
    <div class="pagination-nav__label">Fundamentos de comunicación inalámbrica</div>
  </a>
</nav>
