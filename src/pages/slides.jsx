import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useBaseUrl from '@docusaurus/useBaseUrl';

export default function SlidesPage() {
  const presentacionUrl = useBaseUrl('/presentacion/index.html');

  return (
    <Layout
      title="Historia visual"
      description="Presentación visual del taller Mi primer nodo IoT ambiental"
    >
      <main className="slidesPage">
        <section className="slidesHeader">
          <p className="heroKicker">Historia visual</p>

          <h1>De la arena al sensor inteligente</h1>

          <p>
            Esta historia visual sirve como apoyo para explicar, de forma
            sencilla, cómo pasamos de la materia y los transistores a un
            microcontrolador capaz de ejecutar código, controlar un LED y leer
            sensores ambientales.
          </p>

          <div className="slidesActions">
            <a
              className="slidesFullButton"
              href={presentacionUrl}
              target="_blank"
              rel="noreferrer"
            >
              Abrir en pantalla completa
            </a>

            <Link
              className="slidesSecondaryButton"
              to="/actividades/antes-de-empezar"
            >
              Ir a actividades
            </Link>
          </div>
        </section>

        <section className="slidesFrameWrapper">
          <iframe
            className="slidesFrame"
            src={presentacionUrl}
            title="Historia visual del taller"
            allowFullScreen
          />
        </section>
      </main>
    </Layout>
  );
}
