import React from 'react';
import Layout from '@theme/Layout';

import SessionCard from '../components/SessionCard';
import sessions from '../data/sessions';

export default function SessionsPage() {
  return (
    <Layout
      title="Sesiones"
      description="Sesiones del taller Ciencia, tecnologia y arte para el cuidado del Arroyo Vivo"
    >
      <main>
        <section className="sessionsHero">
          <div>
            <p className="heroKicker">Ruta completa</p>
            <h1>Sesiones y materiales</h1>
            <p>
              Aqui se concentran las guias, presentaciones, codigos y productos
              esperados de cada encuentro.
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
