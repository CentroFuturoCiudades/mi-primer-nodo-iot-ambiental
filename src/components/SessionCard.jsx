import React from 'react';
import Link from '@docusaurus/Link';

export default function SessionCard({session}) {
  return (
    <article className={`sessionCard sessionCard--${session.color || 'blue'}`}>
      <div className="sessionCardTop">
        <span className="sessionNumber">Sesión {session.number}</span>
        <span className="sessionStatus">{session.status}</span>
      </div>

      <p className="sessionDate">{session.date}</p>
      <h3>{session.title}</h3>
      <p className="sessionSubtitle">{session.subtitle}</p>
      <p>{session.description}</p>

      <div className="sessionFocus" aria-label="Temas de la sesión">
        {session.focus.map((item) => (
          <span key={item}>{item}</span>
        ))}
      </div>

      <div className="sessionActions">
        <Link className="activityButton" to={session.docsTo}>
          Ver guía
        </Link>
        <Link className="resourceButton" to={session.materialsTo}>
          Materiales
        </Link>
      </div>
    </article>
  );
}
