import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useBaseUrl from '@docusaurus/useBaseUrl';

import SessionCard from '../components/SessionCard';
import sessions from '../data/sessions';

export default function Home() {
  const arroyoImage = useBaseUrl('/img/arroyo-vivo.jpg');
  const topLogos = useBaseUrl('/img/arroyo-vivo-dgeti-logos.png');
  const institutionLogos = useBaseUrl('/img/institution-logos.png');

  return (
    <Layout
      title="Ciencia, tecnologia y arte para el cuidado del Arroyo Vivo"
      description="Taller Ciencia, tecnologia y arte para el cuidado del Arroyo Vivo"
    >
      <main>
        <section className="homeCover">
          <div className="homeCoverInner">
            <img
              className="coverTopLogos"
              src={topLogos}
              alt="Arroyo Vivo y DGETI"
            />

            <div className="coverMain">
              <div className="coverText">
                <p className="coverKicker">Taller</p>

                <h1>
                  Ciencia, tecnologia y arte para el cuidado del Arroyo Vivo
                </h1>

                <p className="coverMeta">
                  13 de junio al 4 de julio de 2026
                </p>

            <p className="coverDescription">
                  Agendas, presentaciones, codigos, bitacoras y productos de
                  las cuatro sesiones del taller.
                </p>

                <div className="heroActions">
                  <Link className="mainButton" to="/sesiones/">
                    Ver sesiones
                  </Link>

                  <Link
                    className="outlineButton"
                    to="/actividades/repositorio-materiales"
                  >
                    Materiales
                  </Link>
                </div>
              </div>

              <figure className="coverPhoto">
                <img src={arroyoImage} alt="Arroyo Vivo" />
              </figure>
            </div>

            <img
              className="coverInstitutionLogos"
              src={institutionLogos}
              alt="Tecnologico de Monterrey, Centro para el Futuro de las Ciudades, MIT y Northeastern University"
            />
          </div>
        </section>

        <section className="pageSection">
          <div className="sectionIntro">
            <p className="sectionKicker">Programa completo</p>
            <h2>Cuatro sesiones conectadas</h2>
            <p>
              La sesion 1 abre el problema ambiental. La sesion 2 construye el
              nodo de medicion. Las sesiones 3 y 4 cruzan esas dos piezas:
              interpretar datos, visualizarlos y preparar propuestas.
            </p>
          </div>

          <div className="sessionGrid">
            {sessions.map((session) => (
              <SessionCard key={session.number} session={session} />
            ))}
          </div>
        </section>

        <section className="pageSection bandSection">
          <div className="sectionIntro">
            <p className="sectionKicker">Material disponible</p>
            <h2>Recursos del taller</h2>
            <p>
              Cada sesion concentra sus presentaciones, actividades y productos
              esperados para que los equipos puedan consultar el material antes,
              durante y despues del taller.
            </p>
          </div>

          <div className="repoGrid">
            <Link className="repoItem" to="/actividades/repositorio-materiales">
              <strong>Materiales del taller</strong>
              <span>Presentaciones, hojas de trabajo, bitacoras y enlaces.</span>
            </Link>

            <Link className="repoItem" to="/actividades/sesion-2">
              <strong>Actividades tecnicas</strong>
              <span>Arduino, LED, serial, sensores, LoRa y mediciones.</span>
            </Link>

            <Link className="repoItem" to="/actividades/sesion-3">
              <strong>Datos y visualizacion</strong>
              <span>Organizacion de mediciones, analisis y dashboard.</span>
            </Link>
          </div>
        </section>

        <section className="pageSection">
          <h2>Resultado del taller</h2>

          <p>Al final podrás explicar con tus palabras:</p>

          <ul>
            <li>Que problema ambiental quieren observar y por que importa.</li>
            <li>Como un nodo IoT mide variables del entorno.</li>
            <li>Como registrar y comparar datos entre equipos.</li>
            <li>Como transformar mediciones en visualizaciones comprensibles.</li>
            <li>Como defender una propuesta basada en evidencia.</li>
          </ul>
        </section>
      </main>
    </Layout>
  );
}
