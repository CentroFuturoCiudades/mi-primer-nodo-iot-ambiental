import React from 'react';

const steps = [
  {
    title: '1. Entender',
    text: 'Primero explicamos la idea con dibujos, ejemplos y preguntas.',
  },
  {
    title: '2. Probar',
    text: 'Después cargamos un código pequeño en la tarjeta.',
  },
  {
    title: '3. Cambiar',
    text: 'Luego modificamos el código para ver qué ocurre.',
  },
  {
    title: '4. Reflexionar',
    text: 'Al final conectamos lo que pasó con el funcionamiento del chip.',
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
