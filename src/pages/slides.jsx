import React, {useMemo, useRef} from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useBaseUrl from '@docusaurus/useBaseUrl';
import {useLocation} from '@docusaurus/router';

export default function SlidesPage() {
  const iframeRef = useRef(null);
  const location = useLocation();
  const presentacionUrl = useBaseUrl('/presentacion/index.html');
  const presentacionBaseUrl = useBaseUrl('/presentacion/');
  const targetSlide = useMemo(() => {
    const params = new URLSearchParams(location.search);
    const slide = params.get('slide');
    return slide && /^\d+$/.test(slide) ? slide : null;
  }, [location.search]);

  const handleFrameLoad = () => {
    if (!targetSlide || !iframeRef.current?.contentWindow) {
      return;
    }

    const frameWindow = iframeRef.current.contentWindow;
    const targetPath = `${presentacionBaseUrl}${targetSlide}`;

    const goToSlide = () => {
      try {
        frameWindow.history.replaceState(null, '', targetPath);
        frameWindow.dispatchEvent(new PopStateEvent('popstate', {state: null}));
      } catch {
        // If the iframe is not ready yet, keep the regular first slide.
      }
    };

    goToSlide();
    window.setTimeout(goToSlide, 150);
    window.setTimeout(goToSlide, 500);
  };

  const handleFullscreen = () => {
    const frame = iframeRef.current;

    if (frame?.requestFullscreen) {
      frame.requestFullscreen();
      return;
    }

    if (frame?.webkitRequestFullscreen) {
      frame.webkitRequestFullscreen();
      return;
    }

    window.open(presentacionUrl, '_blank', 'noopener,noreferrer');
  };

  return (
    <Layout
      title="Presentacion sesion 2"
      description="Presentacion de apoyo para la sesion 2 del taller Mi primer nodo IoT ambiental"
    >
      <main className="slidesPage">
        <section className="slidesHeader">
          <p className="heroKicker">Sesion 2 · Medir el entorno</p>

          <h1>Presentacion: del chip al nodo ambiental</h1>

          <p>
            Material visual de apoyo para explicar como un microcontrolador
            ejecuta codigo, controla salidas, se comunica con sensores y permite
            construir un nodo IoT ambiental.
          </p>

          <div className="slidesActions">
            <button
              className="slidesFullButton"
              type="button"
              onClick={handleFullscreen}
            >
              Abrir en pantalla completa
            </button>

            <Link
              className="slidesSecondaryButton"
              to="/sesiones/"
            >
              Volver a sesiones
            </Link>
          </div>
        </section>

        <section className="slidesFrameWrapper">
          <iframe
            ref={iframeRef}
            className="slidesFrame"
            src={presentacionUrl}
            title="Presentacion de la sesion 2 del taller"
            onLoad={handleFrameLoad}
            allowFullScreen
          />
        </section>
      </main>
    </Layout>
  );
}
