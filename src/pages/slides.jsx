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
            <button
              className="slidesFullButton"
              type="button"
              onClick={handleFullscreen}
            >
              Abrir en pantalla completa
            </button>

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
            ref={iframeRef}
            className="slidesFrame"
            src={presentacionUrl}
            title="Historia visual del taller"
            onLoad={handleFrameLoad}
            allowFullScreen
          />
        </section>
      </main>
    </Layout>
  );
}
