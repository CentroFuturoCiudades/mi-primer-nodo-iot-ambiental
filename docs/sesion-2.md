---
title: Sesión 2. Tecnología para medir el entorno
---

# Sesión 2 — Tecnología para medir el entorno

**Fecha:** 20 de junio de 2026  
**Horario:** 9:00 am - 1:00 pm

## Propósito

Construir la base técnica del nodo IoT: microcontrolador, programación,
sensores, visualización local y comunicación.

Cada práctica sigue una secuencia común: fundamento técnico, armado del sistema
y programación guiada. La codificación por color permite reconocer con rapidez
el tipo de trabajo de cada bloque.

<div class="activityLegend" aria-label="Código de color de las prácticas">
  <span class="activityBadge activityBadge--a1">A1</span>
  <p><strong>Mi primer programa.</strong> Control de un LED como salida observable del microcontrolador.</p>
  <span class="activityBadge activityBadge--a2">A2</span>
  <p><strong>Lectura ambiental.</strong> Obtención de mediciones del sensor mediante I2C.</p>
  <span class="activityBadge activityBadge--c1">C1</span>
  <p><strong>Comunicación del nodo.</strong> Envío de mediciones mediante Notecard y LoRa.</p>
</div>

## Agenda

<table class="coloredAgenda">
  <thead>
    <tr>
      <th>Hora</th>
      <th>Bloque</th>
      <th>Actividad</th>
      <th>Recurso</th>
    </tr>
  </thead>
  <tbody>
    <tr class="agendaRow agendaRow--a1">
      <td>9:30 - 10:00</td>
      <td><span class="activityBadge activityBadge--a1">A1</span></td>
      <td>Fundamento técnico: señal digital, programa y control de LED.</td>
      <td>Presentación</td>
    </tr>
    <tr class="agendaRow agendaRow--a1">
      <td>10:00 - 10:10</td>
      <td><span class="activityBadge activityBadge--a1">A1</span></td>
      <td>Armado de hardware para observar una salida digital.</td>
      <td>Manual de hardware</td>
    </tr>
    <tr class="agendaRow agendaRow--a1">
      <td>10:10 - 10:30</td>
      <td><span class="activityBadge activityBadge--a1">A1</span></td>
      <td>Programación en Arduino IDE: primer programa y patrón del LED.</td>
      <td>Arduino IDE</td>
    </tr>
    <tr class="agendaRow agendaRow--a2">
      <td>10:30 - 11:00</td>
      <td><span class="activityBadge activityBadge--a2">A2</span></td>
      <td>Fundamento técnico: sensor SEN55, bus I2C y lectura de variables ambientales.</td>
      <td>Presentación</td>
    </tr>
    <tr class="agendaRow agendaRow--pause">
      <td>11:00 - 11:15</td>
      <td></td>
      <td>Pausa.</td>
      <td></td>
    </tr>
    <tr class="agendaRow agendaRow--a2">
      <td>11:20 - 11:30</td>
      <td><span class="activityBadge activityBadge--a2">A2</span></td>
      <td>Armado de hardware para conectar alimentación, SDA, SCL y tierra.</td>
      <td>Manual de hardware</td>
    </tr>
    <tr class="agendaRow agendaRow--a2">
      <td>11:30 - 11:50</td>
      <td><span class="activityBadge activityBadge--a2">A2</span></td>
      <td>Programación en Arduino IDE: lectura del sensor y registro en monitor serial.</td>
      <td>Arduino IDE</td>
    </tr>
    <tr class="agendaRow agendaRow--c1">
      <td>11:50 - 12:10</td>
      <td><span class="activityBadge activityBadge--c1">C1</span></td>
      <td>Fundamento técnico: comunicación del nodo, Notecard, LoRa y Notehub.</td>
      <td>Presentación</td>
    </tr>
    <tr class="agendaRow agendaRow--c1">
      <td>12:10 - 12:30</td>
      <td><span class="activityBadge activityBadge--c1">C1</span></td>
      <td>Armado de hardware para integrar comunicación y medición ambiental.</td>
      <td>Manual de hardware</td>
    </tr>
    <tr class="agendaRow agendaRow--c1">
      <td>12:30 - 12:55</td>
      <td><span class="activityBadge activityBadge--c1">C1</span></td>
      <td>Programación en Arduino IDE: nota, plantilla y sincronización.</td>
      <td>Arduino IDE</td>
    </tr>
    <tr class="agendaRow agendaRow--shared">
      <td>12:55 - 1:00</td>
      <td></td>
      <td>Cierre.</td>
      <td>Ejemplos</td>
    </tr>
  </tbody>
</table>

## Materiales principales

- [Presentación visual de la sesión 2](/slides)
- [Manual de hardware](/materiales/sesion-02/Manual%20Sensor%20Ambiental-3.pdf)
- [Antes de empezar](./antes-de-empezar)
- [A1. Mi primer programa](./tiempo-dentro-del-chip)
- [A2. Lectura ambiental con SEN55](./hola-mundo)
- [C1. Comunicación del nodo ambiental](./sensor-simulado)

## Producto de la sesión

- Nodo o prototipo con lectura inicial.
- Prueba de comunicación con Notecard/LoRa.
- Plan de medición: qué medir, dónde y cuándo.
- Bitácora de datos y observaciones.
- Propuesta de carcasa con materiales reciclados o reutilizados.
