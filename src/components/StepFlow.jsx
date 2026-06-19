import React from 'react';

const steps = [
  {
    title: '1. Comprender',
    text: 'Primero se establece el concepto técnico mediante esquemas, ejemplos y preguntas de observación.',
  },
  {
    title: '2. Verificar',
    text: 'Después se carga un programa breve en la tarjeta para observar un comportamiento controlado.',
  },
  {
    title: '3. Modificar',
    text: 'Luego se modifica el código para comparar el efecto de cada decisión de programación.',
  },
  {
    title: '4. Reflexionar',
    text: 'Finalmente se relaciona la observación experimental con el funcionamiento interno del microcontrolador.',
  },
];

export default function StepFlow() {
  return (
    <div className="stepGrid">
      {steps.map((step) => (
        <div className="stepCard" key={step.title}>
          <h3>{step.title}</h3>
          <p>{step.text}</p>
        </div>
      ))}
    </div>
  );
}
