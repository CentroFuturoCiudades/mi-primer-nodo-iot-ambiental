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
      title="Ciencia, Tecnología y Arte para el cuidado del Arroyo Vivo"
      description="Taller Ciencia, tecnología y arte para el cuidado del Arroyo Vivo"
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
                  Ciencia, Tecnología y Arte para el cuidado del Arroyo Vivo
                </h1>

                <p className="coverMeta">
                  13 de junio al 4 de julio de 2026
                </p>

                <p className="coverDescription">
                  Repositorio, presentaciones, prácticas
                  de laboratorio, bitácoras y productos de aprendizaje de las
                  cuatro sesiones.
                </p>

                <div className="heroActions">
                  <Link className="mainButton" to="/sesiones/">
                    Consultar sesiones
                  </Link>

                  <Link
                    className="outlineButton"
                    to="/actividades/repositorio-materiales"
                  >
                    Recursos del taller
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
              alt="Tecnológico de Monterrey, Centro para el Futuro de las Ciudades, MIT y Northeastern University"
            />
          </div>
        </section>

        <section className="pageSection">
          <div className="sectionIntro">
            <p className="sectionKicker">Ruta formativa</p>
            <h2>Cuatro sesiones</h2>
            <p>
              La primera sesión define el problema ambiental y las preguntas de
              observación. La segunda sesión introduce el nodo de medición. Las
              sesiones tercera y cuarta integran ambas dimensiones: ordenar
              datos, interpretarlos y formular propuestas sustentadas.
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
            <p className="sectionKicker">Repositorio de consulta</p>
            <h2>Material del taller</h2>
            <p>
              Cada sesión reúne sus presentaciones, prácticas y productos esperados. El material está organizado para
              consulta previa, trabajo en aula y revisión posterior.
            </p>
          </div>

          <div className="repoGrid">
            <Link className="repoItem" to="/actividades/repositorio-materiales">
              <strong>Materiales del taller</strong>
              <span>Presentaciones, hojas de trabajo, bitácoras y recursos de apoyo.</span>
            </Link>

            <Link className="repoItem" to="/actividades/sesion-2">
              <strong>Prácticas de laboratorio</strong>
              <span>Microcontrolador, señales digitales, sensores, comunicación y medición ambiental.</span>
            </Link>

            <Link className="repoItem" to="/actividades/sesion-3">
              <strong>Análisis de datos</strong>
              <span>Organización de mediciones, interpretación comparativa y visualización.</span>
            </Link>
          </div>
        </section>

        <section className="pageSection">
          <h2>Resultados de aprendizaje</h2>

          <p>Al finalizar el taller, cada equipo podrá explicar:</p>

          <ul>
            <li>Qué problema ambiental desea observar y por qué es relevante.</li>
            <li>Cómo un nodo IoT mide variables del entorno.</li>
            <li>Cómo registrar, comparar e interpretar datos entre equipos.</li>
            <li>Cómo transformar mediciones en visualizaciones comprensibles.</li>
            <li>Cómo presentar una propuesta sustentada en evidencia.</li>
          </ul>
        </section>
      </main>
    </Layout>
  );
}
