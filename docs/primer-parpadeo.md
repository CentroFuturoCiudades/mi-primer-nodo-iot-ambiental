---
title: 2. Primer parpadeo
---

# Actividad 2 — Primer parpadeo

## Objetivo

Hacer que la tarjeta encienda y apague un LED.

```text
Código → patita de salida → voltaje → LED
```

## Código

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

## ¿Qué significa?

| Línea | Idea sencilla |
|---|---|
| `pinMode()` | Prepara una patita de la tarjeta |
| `digitalWrite(HIGH)` | Enciende la salida |
| `delay(1000)` | Espera un segundo |
| `digitalWrite(LOW)` | Apaga la salida |

## Reto 1

Haz que el LED parpadee más rápido.

## Reto 2

Crea una señal de emergencia:

```text
3 parpadeos rápidos + 1 pausa larga
```

## Reflexión

¿Cómo sabe el microcontrolador que ya pasó un segundo?
