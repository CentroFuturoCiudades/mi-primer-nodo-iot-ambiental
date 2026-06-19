import React from 'react';
import Layout from '@theme/Layout';

import SessionCard from '../components/SessionCard';
import sessions from '../data/sessions';

export default function SessionsPage() {
  return (
    <Layout
      title="Sesiones"
      description="Guía académica de sesiones del taller Ciencia, tecnología y arte para el cuidado del Arroyo Vivo"
    >
      <main>
        <section className="sessionsHero">
          <div>
            <p className="heroKicker">Guía académica</p>
            <h1>Sesiones, recursos y productos</h1>
            <p>
              Esta sección organiza la ruta de trabajo del taller: objetivos,
              materiales de consulta, prácticas y productos esperados de cada
              encuentro.
            </p>
          </div>
        </section>

        <section className="pageSection">
          <div className="sessionGrid">
            {sessions.map((session) => (
              <SessionCard key={session.number} session={session} />
            ))}
          </div>
        </section>
      </main>
    </Layout>
  );
}
