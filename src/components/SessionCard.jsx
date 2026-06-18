import React from 'react';
import Link from '@docusaurus/Link';

export default function SessionCard({session}) {
  return (
    <article className="sessionCard">
      <div className="sessionCardTop">
        <span className="sessionNumber">Sesion {session.number}</span>
        <span className="sessionStatus">{session.status}</span>
      </div>

      <p className="sessionDate">{session.date}</p>
      <h3>{session.title}</h3>
      <p className="sessionSubtitle">{session.subtitle}</p>
      <p>{session.description}</p>

      <div className="sessionFocus" aria-label="Temas de la sesion">
        {session.focus.map((item) => (
          <span key={item}>{item}</span>
        ))}
      </div>

      <div className="sessionActions">
        <Link className="activityButton" to={session.docsTo}>
          Ver guia
        </Link>
        <Link className="resourceButton" to={session.materialsTo}>
          Materiales
        </Link>
      </div>
    </article>
  );
}
