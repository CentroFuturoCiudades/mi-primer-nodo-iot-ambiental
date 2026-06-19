import React from 'react';
import Link from '@docusaurus/Link';

export default function ActivityCard({number, tag, title, description, to}) {
  return (
    <div className="activityCard">
      <div className="activityTop">
        <span className="activityNumber">{number}</span>
        <span className="activityTag">{tag}</span>
      </div>

      <h3>{title}</h3>
      <p>{description}</p>

      <Link className="activityButton" to={to}>
        Consultar actividad
      </Link>
    </div>
  );
}
