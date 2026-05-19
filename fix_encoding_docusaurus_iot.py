

from pathlib import Path

ROOT = Path.cwd()

def write(rel_path: str, content: str):
    path = ROOT / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"OK: {rel_path}")

# ---------------------------------------------------------------------
# Configuración de Docusaurus
# ---------------------------------------------------------------------
write("docusaurus.config.js", r"""
// @ts-check

const config = {
  title: 'Mi primer nodo IoT ambiental',
  tagline: 'De la arena al sensor inteligente',
  favicon: 'img/favicon.ico',

  // Cambia estos datos cuando publiques en GitHub Pages.
  url: 'https://TU_USUARIO_GITHUB.github.io',
  baseUrl: '/mi-primer-nodo-iot-ambiental/',

  organizationName: 'TU_USUARIO_GITHUB',
  projectName: 'mi-primer-nodo-iot-ambiental',

  onBrokenLinks: 'throw',

  i18n: {
    defaultLocale: 'es',
    locales: ['es'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.js',
          routeBasePath: '/actividades',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      },
    ],
  ],

  themeConfig: {
    navbar: {
      title: 'Mi primer nodo IoT ambiental',
      items: [
        {
          to: '/',
          label: 'Inicio',
          position: 'left',
        },
        {
          to: '/slides/',
          label: 'Historia visual',
          position: 'left',
        },
        {
          to: '/actividades/antes-de-empezar',
          label: 'Actividades',
          position: 'left',
        },
        {
          to: '/actividades/ayuda',
          label: 'Ayuda',
          position: 'left',
        },
      ],
    },

    footer: {
      style: 'dark',
      links: [
        {
          title: 'Taller',
          items: [
            {
              label: 'Inicio',
              to: '/',
            },
            {
              label: 'Historia visual',
              to: '/slides/',
            },
            {
              label: 'Actividades',
              to: '/actividades/antes-de-empezar',
            },
          ],
        },
      ],
      copyright: `Centro para el Futuro de las Ciudades — ${new Date().getFullYear()}`,
    },
  },
};

export default config;
""")

write("sidebars.js", r"""
const sidebars = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Antes de empezar',
      items: ['antes-de-empezar'],
    },
    {
      type: 'category',
      label: 'Actividades',
      items: [
        'hola-mundo',
        'primer-parpadeo',
        'tiempo-dentro-del-chip',
        'sensor-simulado',
        'medir-co2',
        'medir-particulas',
      ],
    },
    {
      type: 'category',
      label: 'Apoyo',
      items: ['ayuda'],
    },
  ],
};

export default sidebars;
""")

# ---------------------------------------------------------------------
# Componentes React
# ---------------------------------------------------------------------
write("src/components/CoursePath.jsx", r"""
import React from 'react';

const steps = [
  'Materia',
  'Chip',
  'Código',
  'LED',
  'Sensor',
  'Ciudad',
];

export default function CoursePath() {
  return (
    <div className="coursePath">
      {steps.map((step, index) => (
        <React.Fragment key={step}>
          <div className="pathItem">
            <span>{index + 1}</span>
            <p>{step}</p>
          </div>
          {index < steps.length - 1 && <div className="pathArrow">→</div>}
        </React.Fragment>
      ))}
    </div>
  );
}
""")

write("src/components/ActivityCard.jsx", r"""
import React from 'react';
import Link from '@docusaurus/Link';

export default function ActivityCard({number, tag, title, description, to}) {
  return (
    <div className="activityCard">
      <div className="activityTop">
        <span className="activityNumber">{number}</span>
        <span className="activityTag">{tag}</span>
      </div>

      <h3>{title}</h3>
      <p>{description}</p>

      <Link className="activityButton" to={to}>
        Abrir actividad
      </Link>
    </div>
  );
}
""")

write("src/components/StepFlow.jsx", r"""
import React from 'react';

const steps = [
  {
    title: '1. Entender',
    text: 'Primero explicamos la idea con dibujos, ejemplos y preguntas.',
  },
  {
    title: '2. Probar',
    text: 'Después cargamos un código pequeño en la tarjeta.',
  },
  {
    title: '3. Cambiar',
    text: 'Luego modificamos el código para ver qué ocurre.',
  },
  {
    title: '4. Reflexionar',
    text: 'Al final conectamos lo que pasó con el funcionamiento del chip.',
  },
];

export default function StepFlow() {
  return (
    <div className="stepGrid">
      {steps.map((step) => (
        <div className="stepCard" key={step.title}>
          <h3>{step.title}</h3>
          <p>{step.text}</p>
        </div>
      ))}
    </div>
  );
}
""")

# ---------------------------------------------------------------------
# Portada
# ---------------------------------------------------------------------
write("src/pages/index.jsx", r"""
import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';

import CoursePath from '../components/CoursePath';
import ActivityCard from '../components/ActivityCard';
import StepFlow from '../components/StepFlow';

export default function Home() {
  return (
    <Layout
      title="Mi primer nodo IoT ambiental"
      description="Taller práctico de microcontroladores, sensores e IoT ambiental para bachillerato"
    >
      <main>
        <section className="heroSection">
          <div className="heroContent">
            <p className="heroKicker">Taller práctico para bachillerato</p>

            <h1>De la arena al sensor inteligente</h1>

            <p className="heroSubtitle">
              Una experiencia para descubrir cómo un pequeño microcontrolador
              puede prender un LED, leer sensores ambientales y convertir el
              mundo físico en datos útiles para entender una ciudad.
            </p>

            <div className="heroActions">
              <Link className="mainButton" to="/slides/">
                Ver historia visual
              </Link>

              <Link className="secondaryButton" to="/actividades/antes-de-empezar">
                Prepararme para empezar
              </Link>
            </div>
          </div>
        </section>

        <section className="pageSection">
          <h2>Ruta del taller</h2>
          <CoursePath />
        </section>

        <section className="pageSection">
          <h2>Actividades principales</h2>

          <div className="activityGrid">
            <ActivityCard
              number="01"
              tag="Mensaje"
              title="Hola mundo"
              description="La tarjeta enviará su primer mensaje a la computadora. Aquí aprenderás a usar el monitor de mensajes."
              to="/actividades/hola-mundo"
            />

            <ActivityCard
              number="02"
              tag="LED"
              title="Primer parpadeo"
              description="El microcontrolador encenderá y apagará un LED. Es la primera señal física que produce el chip."
              to="/actividades/primer-parpadeo"
            />

            <ActivityCard
              number="03"
              tag="Tiempo"
              title="El tiempo dentro del chip"
              description="Verás cómo una espera en el código se relaciona con el reloj interno del microcontrolador."
              to="/actividades/tiempo-dentro-del-chip"
            />

            <ActivityCard
              number="04"
              tag="Aire"
              title="Medir el ambiente"
              description="Conectaremos sensores para medir CO₂, temperatura, humedad y partículas en el aire."
              to="/actividades/medir-co2"
            />
          </div>
        </section>

        <section className="pageSection">
          <h2>¿Cómo se trabaja cada actividad?</h2>
          <StepFlow />

          <div className="importantBox">
            <strong>Idea importante:</strong>
            <p>
              No se trata solo de copiar código. Cada actividad está diseñada
              para que entiendas qué parte del microcontrolador estás usando.
            </p>
          </div>
        </section>

        <section className="pageSection">
          <h2>Resultado del taller</h2>

          <p>Al final podrás explicar con tus palabras:</p>

          <ul>
            <li>Qué es un microcontrolador.</li>
            <li>Cómo se comunica con la computadora.</li>
            <li>Cómo controla una salida física como un LED.</li>
            <li>Cómo mide datos del ambiente usando sensores.</li>
            <li>Cómo esos datos pueden ayudar a entender espacios reales de una ciudad.</li>
          </ul>
        </section>
      </main>
    </Layout>
  );
}
""")

# ---------------------------------------------------------------------
# Estilos
# ---------------------------------------------------------------------
write("src/css/custom.css", r"""
:root {
  --ifm-color-primary: #00897b;
  --ifm-color-primary-dark: #00796b;
  --ifm-color-primary-darker: #00695c;
  --ifm-color-primary-darkest: #004d40;
  --ifm-color-primary-light: #26a69a;
  --ifm-color-primary-lighter: #4db6ac;
  --ifm-color-primary-lightest: #80cbc4;

  --course-teal: #00897b;
  --course-dark: #062b27;
  --course-amber: #f5b041;
  --course-soft: #f2fbf9;
}

.heroSection {
  min-height: 76vh;
  display: flex;
  align-items: center;
  background:
    radial-gradient(circle at 85% 20%, rgba(245, 176, 65, 0.22), transparent 28%),
    radial-gradient(circle at 15% 10%, rgba(0, 137, 123, 0.28), transparent 30%),
    linear-gradient(135deg, #061716, #073b35 55%, #0a1f1e);
  color: white;
  padding: 5rem 1.5rem;
}

.heroContent {
  max-width: 1050px;
  margin: 0 auto;
  width: 100%;
}

.heroKicker {
  color: var(--course-amber);
  text-transform: uppercase;
  font-weight: 900;
  letter-spacing: 0.14em;
  font-size: 0.9rem;
}

.heroSection h1 {
  font-size: clamp(3rem, 8vw, 6.5rem);
  line-height: 0.96;
  letter-spacing: -0.06em;
  max-width: 900px;
  margin: 1rem 0;
}

.heroSubtitle {
  font-size: clamp(1.15rem, 2vw, 1.55rem);
  line-height: 1.55;
  max-width: 820px;
  color: rgba(255, 255, 255, 0.82);
}

.heroActions {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  margin-top: 2rem;
}

.mainButton,
.secondaryButton,
.activityButton {
  display: inline-block;
  border-radius: 999px;
  font-weight: 900;
  text-decoration: none !important;
}

.mainButton {
  background: var(--course-amber);
  color: #201200 !important;
  padding: 0.9rem 1.25rem;
}

.secondaryButton {
  border: 2px solid rgba(255, 255, 255, 0.55);
  color: white !important;
  padding: 0.78rem 1.15rem;
}

.pageSection {
  max-width: 1050px;
  margin: 0 auto;
  padding: 3.5rem 1.5rem;
}

.pageSection h2 {
  font-size: clamp(2rem, 4vw, 3rem);
  letter-spacing: -0.04em;
  margin-bottom: 1.5rem;
}

.coursePath {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.7rem;
}

.pathItem {
  min-width: 105px;
  text-align: center;
  padding: 1rem 0.8rem;
  border-radius: 1.2rem;
  background: rgba(0, 137, 123, 0.08);
  border: 1px solid rgba(0, 137, 123, 0.16);
}

.pathItem span {
  display: inline-grid;
  place-items: center;
  width: 2.1rem;
  height: 2.1rem;
  border-radius: 999px;
  background: var(--course-teal);
  color: white;
  font-weight: 900;
  margin-bottom: 0.35rem;
}

.pathItem p {
  margin: 0;
  font-weight: 800;
  color: var(--course-dark);
}

.pathArrow {
  color: var(--course-teal);
  font-weight: 900;
  font-size: 1.5rem;
}

.activityGrid {
  display: grid;
  grid-template-columns: repeat(2, minmax(240px, 1fr));
  gap: 1.2rem;
}

.activityCard {
  padding: 1.5rem;
  border-radius: 1.4rem;
  background: white;
  border: 1px solid rgba(0,0,0,0.08);
  box-shadow: 0 14px 36px rgba(0,0,0,0.07);
  min-height: 270px;
}

.activityCard:hover {
  transform: translateY(-4px);
  transition: 0.18s ease;
  box-shadow: 0 20px 50px rgba(0,0,0,0.11);
}

.activityTop {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.activityNumber {
  color: var(--course-teal);
  background: rgba(0, 137, 123, 0.10);
  border-radius: 999px;
  font-weight: 900;
  padding: 0.28rem 0.7rem;
}

.activityTag {
  color: #7a4b00;
  background: rgba(245, 176, 65, 0.18);
  border-radius: 999px;
  font-weight: 900;
  padding: 0.28rem 0.7rem;
  font-size: 0.85rem;
}

.activityCard h3 {
  color: var(--course-dark);
  font-size: 1.45rem;
  margin-top: 1.1rem;
}

.activityCard p {
  line-height: 1.6;
  min-height: 5.5rem;
}

.activityButton {
  background: var(--course-teal);
  color: white !important;
  padding: 0.72rem 1.05rem;
}

.stepGrid {
  display: grid;
  grid-template-columns: repeat(4, minmax(130px, 1fr));
  gap: 1rem;
}

.stepCard {
  background: rgba(245, 176, 65, 0.13);
  border: 1px solid rgba(245, 176, 65, 0.28);
  border-radius: 1.2rem;
  padding: 1rem;
}

.stepCard h3 {
  color: #7a4b00;
  margin-top: 0;
}

.importantBox {
  margin-top: 2rem;
  padding: 1.2rem;
  border-radius: 1.1rem;
  background: rgba(0, 137, 123, 0.08);
  border: 1px solid rgba(0, 137, 123, 0.25);
}

.importantBox p {
  margin-bottom: 0;
}

html[data-theme='dark'] .activityCard {
  background: #151f1f;
  border-color: rgba(255,255,255,0.12);
}

html[data-theme='dark'] .activityCard h3,
html[data-theme='dark'] .pathItem p {
  color: #80cbc4;
}

html[data-theme='dark'] .pathItem {
  background: rgba(0, 137, 123, 0.16);
}

html[data-theme='dark'] .stepCard {
  background: rgba(245, 176, 65, 0.12);
}

@media (max-width: 850px) {
  .activityGrid {
    grid-template-columns: 1fr;
  }

  .stepGrid {
    grid-template-columns: repeat(2, 1fr);
  }

  .pathArrow {
    display: none;
  }
}

@media (max-width: 520px) {
  .stepGrid {
    grid-template-columns: 1fr;
  }
}
""")

# ---------------------------------------------------------------------
# Documentos
# ---------------------------------------------------------------------
write("docs/antes-de-empezar.md", r"""
---
title: Antes de empezar
---

# Antes de empezar

En esta sección revisaremos que todo esté listo antes de cargar el primer código.

## Lo que necesitas

- Una tarjeta Swan.
- Cable USB.
- Arduino IDE instalado.
- STM32CubeProgrammer instalado.
- La tarjeta configurada en Arduino IDE.
- Librerías de sensores instaladas si vas a usar SCD41 o SEN55.

## Revisión rápida

Antes de comenzar, verifica:

- Puedes conectar la tarjeta por USB.
- Puedes cargar un programa sencillo.
- Puedes abrir el monitor de mensajes.
- Sabes seleccionar la velocidad de `115200`.

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
""")

write("docs/hola-mundo.md", r"""
---
title: 1. Hola mundo
---

# Actividad 1 — Hola mundo

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
""")

write("docs/primer-parpadeo.md", r"""
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
""")

write("docs/tiempo-dentro-del-chip.md", r"""
---
title: 3. El tiempo dentro del chip
---

# Actividad 3 — El tiempo dentro del chip

Cuando escribimos `delay(1000)`, la tarjeta no espera por magia. Usa su reloj interno para contar el tiempo.

```text
Reloj interno → conteo → espera → siguiente instrucción
```

## Objetivo

Modificar el tiempo de parpadeo del LED y observar qué ocurre.

## Reto

Cambia el tiempo de espera y observa cuándo el parpadeo empieza a verse casi continuo.
""")

write("docs/sensor-simulado.md", r"""
---
title: 4. Sensor simulado
---

# Actividad 4 — Sensor simulado

Antes de conectar un sensor real, podemos simular un dato.

## Idea

Un valor inventado nos permite probar decisiones sin depender todavía del hardware.

```cpp
int co2 = 900;
```

## Reto

Crea una alerta si el valor simulado pasa de 1000.
""")

write("docs/medir-co2.md", r"""
---
title: 5. Medir CO₂
---

# Actividad 5 — Medir CO₂

En esta actividad conectaremos el sensor SCD41 para medir CO₂, temperatura y humedad.

## Pregunta inicial

¿Qué crees que pasa con el CO₂ cuando varias personas se acercan al sensor?

## Reto

Compara una medición cerca de personas y otra en un lugar más ventilado.
""")

write("docs/medir-particulas.md", r"""
---
title: 6. Medir partículas
---

# Actividad 6 — Medir partículas

En esta actividad usaremos el sensor SEN55 para observar partículas en el aire.

## Idea

Algunas partículas no se ven, pero pueden medirse.

## Reto

Observa si el valor cambia cerca de polvo, movimiento o ventilación.
""")

write("docs/ayuda.md", r"""
---
title: Ayuda
---

# Ayuda

## No veo mensajes

El panel de salida solo muestra compilación. Para ver mensajes debes abrir el monitor de mensajes.

## Error al cargar el programa

Revisa que la tarjeta esté conectada y en el modo correcto.

## Falta una librería

Instala la librería desde el administrador de librerías de Arduino IDE.
""")

# ---------------------------------------------------------------------
# Códigos Arduino
# ---------------------------------------------------------------------
write("static/codigos/01_hola_mundo/01_hola_mundo.ino", r"""
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
""")

write("static/codigos/02_primer_parpadeo/02_primer_parpadeo.ino", r"""
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);

  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
""")

# ---------------------------------------------------------------------
# Historia visual básica
# ---------------------------------------------------------------------
write("static/slides/index.html", r"""
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>De la arena al sensor inteligente</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/theme/black.css">

  <style>
    :root {
      --teal: #00b894;
      --amber: #f5b041;
    }

    .reveal h1,
    .reveal h2 {
      text-transform: none;
      letter-spacing: -0.04em;
    }

    .eyebrow {
      color: var(--amber);
      text-transform: uppercase;
      letter-spacing: 0.16em;
      font-size: 0.55em;
      font-weight: 800;
    }

    .lab-button {
      display: inline-block;
      margin-top: 1rem;
      padding: 0.7rem 1rem;
      border-radius: 999px;
      background: var(--teal);
      color: #041212 !important;
      font-weight: 800;
      text-decoration: none;
      font-size: 0.55em;
    }
  </style>
</head>

<body>
<div class="reveal">
  <div class="slides">

    <section data-background-gradient="linear-gradient(120deg, #020303, #063a37)">
      <p class="eyebrow">Taller IoT ambiental</p>
      <h1>De la arena al sensor inteligente</h1>
      <p>Materia, chips, código y ciudades que aprenden a observarse.</p>
      <a class="lab-button" href="../actividades/antes-de-empezar">Ir a actividades</a>
    </section>

    <section data-background-gradient="linear-gradient(120deg, #3b2f1e, #050505)">
      <p class="eyebrow">Escena 1</p>
      <h2>Antes del dato, hubo materia.</h2>
      <p class="fragment">Antes del sensor, hubo silicio.</p>
      <p class="fragment">Antes del código, hubo transistores.</p>
    </section>

    <section>
      <h2>El viaje</h2>
      <p>Materia → Chip → Código → LED → Sensor → Ciudad</p>
    </section>

    <section>
      <h2>El microcontrolador habla</h2>
      <p>Primero veremos texto en el monitor de mensajes.</p>
      <a class="lab-button" href="../actividades/hola-mundo">Abrir actividad</a>
    </section>

    <section>
      <h2>El chip manda una señal</h2>
      <pre><code>
digitalWrite(LED_BUILTIN, HIGH);
delay(1000);
digitalWrite(LED_BUILTIN, LOW);
delay(1000);
      </code></pre>
      <a class="lab-button" href="../actividades/primer-parpadeo">Abrir actividad</a>
    </section>

  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.js"></script>
<script>
  Reveal.initialize({
    hash: true,
    slideNumber: true,
    transition: 'fade'
  });
</script>
</body>
</html>
""")

# Borra documentos de ejemplo de Docusaurus si existen.
for path in [
    "docs/tutorial-basics",
    "docs/tutorial-extras",
    "docs/intro.md",
    "blog",
]:
    target = ROOT / path
    if target.is_dir():
        import shutil
        shutil.rmtree(target)
        print(f"REMOVED: {path}")
    elif target.is_file():
        target.unlink()
        print(f"REMOVED: {path}")

print("\nListo. Ahora ejecuta:")
print("  npm start")
print("\nSi el navegador ya estaba abierto, recarga con Ctrl + F5.")
