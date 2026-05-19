import React from 'react';

const steps = [
  'Materia',
  'Chip',
  'Código',
  'LED',
  'Sensor',
  'Ciudad',
];

export default function CoursePath() {
  return (
    <div className="coursePath">
      {steps.map((step, index) => (
        <React.Fragment key={step}>
          <div className="pathItem">
            <span>{index + 1}</span>
            <p>{step}</p>
          </div>
          {index < steps.length - 1 && <div className="pathArrow">→</div>}
        </React.Fragment>
      ))}
    </div>
  );
}
