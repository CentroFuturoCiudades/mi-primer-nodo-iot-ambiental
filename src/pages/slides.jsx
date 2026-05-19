import React from 'react';
import Layout from '@theme/Layout';
import useBaseUrl from '@docusaurus/useBaseUrl';

export default function SlidesPage() {
  const historiaUrl = useBaseUrl('/historia/index.html');

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
            Esta es la presentación narrativa del taller. Úsala para guiar la
            sesión antes de pasar a las actividades prácticas.
          </p>
        </section>

        <section className="slidesFrameWrapper">
          <iframe
            className="slidesFrame"
            src={historiaUrl}
            title="Historia visual del taller"
            allowFullScreen
          />
        </section>
      </main>
    </Layout>
  );
}