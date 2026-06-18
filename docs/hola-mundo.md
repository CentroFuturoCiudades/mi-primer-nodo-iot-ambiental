---
title: 2. Leer SEN55 por I2C
---

# Actividad 2 - Leer SEN55 por I2C

En esta practica vas a conectar la **Blues Swan R5** con el sensor **SEN55**
por I2C. El objetivo es aislar una sola parte del nodo ambiental:

```text
Swan MCU -> I2C -> SEN55 -> Serial Monitor
```

Todavia no usaremos Notecard, LoRa, SCD41 ni almacenamiento de datos. Primero
queremos comprobar que el microcontrolador puede iniciar el bus I2C, reconocer
el sensor y mostrar mediciones en la computadora.

## Objetivo

Leer por I2C las variables principales del SEN55:

| Variable | Que representa |
|---|---|
| PM1.0, PM2.5, PM4.0, PM10 | Particulas suspendidas en el aire |
| Temperatura | Temperatura del aire cerca del sensor |
| Humedad | Humedad relativa |
| VOC Index | Indicador de compuestos organicos volatiles |
| NOx Index | Indicador de oxidos de nitrogeno |

## Material

- Blues Swan R5 configurada.
- Sensor SEN55 o SEN5x compatible.
- Cables para I2C y alimentacion.
- Arduino IDE.
- Cable USB de datos.
- Serial Monitor configurado a `115200 baud`.

## Librerias necesarias

En Arduino IDE abre:

```text
Sketch -> Include Library -> Manage Libraries...
```

Busca e instala:

```text
Sensirion I2C SEN5X
```

Si Arduino IDE lo solicita, instala tambien:

```text
Sensirion Core
```

## Conexion I2C

I2C usa dos lineas de comunicacion:

| Linea | Funcion |
|---|---|
| `SDA` | Transporta datos |
| `SCL` | Transporta el reloj que coordina la lectura |

Conecta el sensor siguiendo la alimentacion indicada por tu modulo SEN55. En
la Swan, usa los pines marcados como `SDA` y `SCL`.

:::caution Antes de energizar
Revisa voltaje, tierra y orientacion de cables antes de conectar la tarjeta por
USB. Si hay duda, pide revision antes de encender.
:::

## Codigo base

Abre el archivo:

```text
static/codigos/02_sen55_i2c/02_sen55_i2c.ino
```

<a href="../codigos/02_sen55_i2c/02_sen55_i2c.ino" class="button button--secondary">Abrir codigo SEN55</a>

O copia este sketch en Arduino IDE:

```cpp
#include <Wire.h>
#include <SensirionI2CSen5x.h>

SensirionI2CSen5x sen5x;

char errorMessage[256];
uint16_t error;

void setup() {
  Serial.begin(115200);

  while (!Serial && millis() < 5000) {
  }

  Serial.println("Iniciando SEN55...");

  Wire.begin();
  sen5x.begin(Wire);

  error = sen5x.deviceReset();
  if (error) {
    Serial.print("Error en deviceReset(): ");
    errorToString(error, errorMessage, 256);
    Serial.println(errorMessage);

    while (1) {
      delay(1000);
    }
  }

  Serial.println("SEN55 listo.");
  Serial.println("----------------------------");
}

void loop() {
  float pm1p0;
  float pm2p5;
  float pm4p0;
  float pm10p0;
  float humidity;
  float temperature;
  float vocIndex;
  float noxIndex;

  Serial.println("Iniciando medicion SEN55...");

  error = sen5x.startMeasurement();
  if (error) {
    Serial.print("Error en startMeasurement(): ");
    errorToString(error, errorMessage, 256);
    Serial.println(errorMessage);
    delay(5000);
    return;
  }

  Serial.println("Ventilador encendido, esperando estabilizacion...");

  // Para medicion real usa 45000 ms.
  // Para pruebas rapidas de clase puedes usar 5000 ms.
  delay(45000);

  error = sen5x.readMeasuredValues(
    pm1p0,
    pm2p5,
    pm4p0,
    pm10p0,
    humidity,
    temperature,
    vocIndex,
    noxIndex
  );

  sen5x.stopMeasurement();

  if (error) {
    Serial.print("Error en readMeasuredValues(): ");
    errorToString(error, errorMessage, 256);
    Serial.println(errorMessage);
  } else {
    Serial.println("Datos SEN55:");

    Serial.print("PM1.0: ");
    Serial.print(pm1p0);
    Serial.println(" ug/m3");

    Serial.print("PM2.5: ");
    Serial.print(pm2p5);
    Serial.println(" ug/m3");

    Serial.print("PM4.0: ");
    Serial.print(pm4p0);
    Serial.println(" ug/m3");

    Serial.print("PM10: ");
    Serial.print(pm10p0);
    Serial.println(" ug/m3");

    Serial.print("Temperatura: ");
    Serial.print(temperature);
    Serial.println(" C");

    Serial.print("Humedad: ");
    Serial.print(humidity);
    Serial.println(" %");

    Serial.print("VOC Index: ");
    Serial.println(vocIndex);

    Serial.print("NOx Index: ");
    Serial.println(noxIndex);

    Serial.println("----------------------------");
  }

  delay(10000);
}
```

## Que observar

Abre el Serial Monitor a `115200 baud`. Si la comunicacion funciona, veras un
flujo parecido a este:

```text
Iniciando SEN55...
SEN55 listo.
----------------------------
Iniciando medicion SEN55...
Ventilador encendido, esperando estabilizacion...
Datos SEN55:
PM1.0: 2.10 ug/m3
PM2.5: 3.40 ug/m3
PM4.0: 4.00 ug/m3
PM10: 4.70 ug/m3
Temperatura: 24.60 C
Humedad: 48.20 %
VOC Index: 104.00
NOx Index: 1.00
----------------------------
```

Los numeros exactos no tienen que coincidir. Lo importante es que aparezcan
valores numericos y que el programa no se quede detenido en un error.

## Tiempo de estabilizacion

El SEN55 enciende un ventilador interno y necesita tiempo para estabilizar la
lectura. En una medicion mas seria se recomienda esperar:

```cpp
delay(45000);
```

Para una prueba rapida en clase puedes cambiar temporalmente a:

```cpp
delay(5000);
```

La lectura de 5 segundos sirve para verificar conexion y flujo de datos. Para
comparar mediciones entre equipos conviene volver a usar el tiempo largo.

## Mini-reto: alerta por PM2.5

Despues de imprimir los datos, agrega una regla sencilla:

```cpp
if (pm2p5 > 25) {
  Serial.println("ALERTA: PM2.5 elevado.");
} else {
  Serial.println("PM2.5 en nivel bajo para esta prueba.");
}
```

Ahora conecta la alerta al LED integrado. En `setup()` agrega:

```cpp
pinMode(LED_BUILTIN, OUTPUT);
```

Y despues de leer `pm2p5`, agrega:

```cpp
if (pm2p5 > 25) {
  digitalWrite(LED_BUILTIN, HIGH);
} else {
  digitalWrite(LED_BUILTIN, LOW);
}
```

## Tabla de registro

Llena una fila por medicion:

| Prueba | Lugar | PM2.5 | PM10 | Temperatura | Humedad | Observacion |
|---|---|---:|---:|---:|---:|---|
| A | | | | | | |
| B | | | | | | |
| C | | | | | | |

## Preguntas de cierre

- Que lineas fisicas usa I2C?
- Por que el sensor necesita una direccion dentro del bus?
- Que diferencia hay entre comprobar que el sensor responde y hacer una
  medicion ambiental confiable?
- Que variable cambiaria mas si hay polvo, movimiento o ventilacion cerca?

## Entregable

Entrega una captura o foto del Serial Monitor con:

- Al menos una lectura completa del SEN55.
- La tabla con una medicion.
- Una frase explicando por que I2C permite conectar sensores al mismo bus.

<a href="./sensor-simulado" class="button button--primary">Continuar a Actividad 3: sensor simulado</a>
