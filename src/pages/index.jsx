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
