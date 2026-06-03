---
title: 3. Hola mundo
---

# Actividad 3 — Hola mundo

## Objetivo

Hacer que la tarjeta envíe su primer mensaje a la computadora.

## ¿Qué parte usamos?

Usamos el monitor de mensajes. Su nombre técnico en Arduino es **Serial Monitor**.

## Código

Abre el archivo:

```text
static/codigos/01_hola_mundo/01_hola_mundo.ino
```

```cpp
void setup() {
  Serial.begin(115200);

  while (!Serial && millis() < 5000) {
  }

  Serial.println("Hola mundo IoT");
  Serial.println("La tarjeta está funcionando");
}

void loop() {
  Serial.println("El programa sigue corriendo");
  delay(1000);
}
```

## Resultado esperado

En el monitor de mensajes deberías ver:

```text
Hola mundo IoT
La tarjeta está funcionando
El programa sigue corriendo
```

## Reto

Cambia el mensaje para que diga el nombre de tu equipo.

## Reflexión

¿Por qué necesitamos iniciar la comunicación antes de mostrar mensajes?
