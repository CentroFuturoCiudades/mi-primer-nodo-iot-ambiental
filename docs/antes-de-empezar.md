---
title: Antes de empezar
pagination_next: null
---

# Antes de empezar

Antes de cargar el primer programa, deja lista tu computadora, Arduino IDE y la
tarjeta **Blues Swan R5**. Esta página resume los pasos oficiales de Blues Swan
Quickstart en español y los organiza como una lista de preparación para el
taller.

![Tarjeta Blues Swan](https://res.cloudinary.com/blues-wireless/image/fetch/f_auto%2Cc_limit%2Cw_640%2Cq_auto/https%3A//dev.blues.io/_next/static/media/swan-small.e6f51b50.png)

## Lo que necesitas

- Una tarjeta **Blues Swan R5**.
- Cable USB de datos, no solo de carga.
- Arduino IDE instalado.
- STM32CubeCLT instalado.
- La tarjeta configurada en Arduino IDE.
- Librerías de sensores instaladas si vas a usar SCD41 o SEN55.

:::tip Antes de conectar
Si tu computadora no detecta la tarjeta, prueba con otro cable USB. Muchos
cables sirven para cargar energía, pero no transfieren datos.
:::

## 1. Instala los programas necesarios

Antes de trabajar con firmware en Arduino IDE, instala estas herramientas:

| Herramienta | Para que sirve | Enlace |
|---|---|---|
| Arduino IDE | Es el programa donde escribirás y cargarás el código. | [Descargar Arduino IDE](https://www.arduino.cc/en/software/) |
| STM32CubeCLT | Permite que Arduino IDE compile y cargue código en microcontroladores STM32, como la Swan. | [Descargar STM32CubeCLT](https://www.st.com/en/development-tools/stm32cubeclt.html) |

Blues también menciona como alternativa instalar STM32CubeIDE y
STM32CubeProgrammer, pero para este taller usaremos el camino más directo:
**Arduino IDE + STM32CubeCLT**.

## 2. Agrega STM32duino a Arduino IDE

Arduino IDE no conoce la Swan por defecto. Para agregarla:

1. Abre **Arduino IDE**.
2. Entra a **File > Preferences** o **Archivo > Preferencias**.
3. Busca el campo **Additional boards manager URLs**.
4. Agrega esta URL:

```text
https://github.com/stm32duino/BoardManagerFiles/raw/main/package_stmicroelectronics_index.json
```

5. Presiona **OK** para guardar.
6. Cierra y vuelve a abrir Arduino IDE.

## 3. Instala las tarjetas STM32

Ahora instala el paquete de tarjetas:

1. En Arduino IDE, abre **Boards Manager**.
2. Busca **STM32 MCU based boards**.
3. Instala la versión **2.9.0 o superior**.
4. Reinicia Arduino IDE al terminar.

:::info Versión mínima
La guía oficial de Blues pide STM32duino versión **2.9.0 o mayor** para trabajar
con Swan R5.
:::

## 4. Selecciona la tarjeta Swan R5

Con el paquete instalado, configura Arduino IDE asi:

1. Ve a **Tools > Board**.
2. Selecciona **STM32 MCU based boards**.
3. Luego selecciona **Blues boards**.
4. Ve a **Tools > Board part number**.
5. Selecciona **Swan R5**.
6. Si aparece la opción **Tools > USB support**, selecciona:

```text
CDC (generic 'Serial' supersede U(S)ART)
```

Esta opción prepara el puerto USB de la Swan para comunicarse con la
computadora.

## 5. Revisa el puerto COM en Windows

Antes de cargar el primer programa, revisa que Windows detecte la tarjeta:

1. Conecta la Swan a tu computadora con un cable USB de datos.
2. Abre el **Administrador de dispositivos** de Windows.
3. Busca la sección **Puertos (COM y LPT)**.
4. Verifica que aparezca algo como **USB Serial Device (COMx)**.
5. Anota el número de puerto, por ejemplo `COM3`, `COM5` o `COM12`.
6. En Arduino IDE, ve a **Tools > Port** y selecciona ese mismo puerto COM.

Si no aparece ningún puerto, prueba con otro cable USB o desconecta y vuelve a
conectar la tarjeta.

## 6. Prepara la carga sin STLINK-V3MINI

Para programar la Swan usando solo el cable USB:

1. En Arduino IDE, ve a **Tools > Upload method**.
2. Selecciona:

```text
STM32CubeProgrammer (DFU)
```

3. Conecta el puerto **Micro USB** de la Swan a tu computadora.
4. Mantén presionado el botón **BOOT** de la Swan.
5. Sin soltar **BOOT**, presiona y suelta **RESET**.
6. Suelta **BOOT**.

Esta secuencia hace que la Swan entre al bootloader. Debes repetirla cada vez
que quieras cargar firmware nuevo a la tarjeta.

## 7. Primer programa de prueba

Esta prueba confirma que Arduino IDE, STM32CubeCLT, la tarjeta, el método de
carga y el puerto quedaron bien configurados.

1. En Arduino IDE, abre **File > New Sketch**.
2. Borra el contenido inicial.
3. Copia este programa:

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

4. Verifica que sigan seleccionados:

```text
Board: Blues boards
Board part number: Swan R5
Upload method: STM32CubeProgrammer (DFU)
Port: el COM que viste en Administrador de dispositivos
```

5. Presiona **Upload**.
6. Si la carga falla porque la tarjeta no está en modo bootloader, repite la
   secuencia **BOOT + RESET** y vuelve a presionar **Upload**.

Si el LED de la Swan prende y apaga cada segundo, tu entorno está listo para el
taller.

## Lenguaje del taller

Durante el taller usaremos palabras sencillas:

| Palabra sencilla | Nombre técnico |
|---|---|
| Tarjeta | Placa de desarrollo |
| Código | Sketch o programa |
| Monitor de mensajes | Serial Monitor |
| Patita de entrada/salida | GPIO |
| Cargar programa | Upload |
| Programa de la tarjeta | Firmware |

## Fuentes

- [Blues Swan Quickstart](https://dev.blues.io/quickstart/swan-quickstart/)
- [Arduino IDE](https://www.arduino.cc/en/software/)
- [STM32CubeCLT](https://www.st.com/en/development-tools/stm32cubeclt.html)
