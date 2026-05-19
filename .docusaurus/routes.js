import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/mi-primer-nodo-iot-ambiental/markdown-page',
    component: ComponentCreator('/mi-primer-nodo-iot-ambiental/markdown-page', 'd75'),
    exact: true
  },
  {
    path: '/mi-primer-nodo-iot-ambiental/slides',
    component: ComponentCreator('/mi-primer-nodo-iot-ambiental/slides', 'a87'),
    exact: true
  },
  {
    path: '/mi-primer-nodo-iot-ambiental/actividades',
    component: ComponentCreator('/mi-primer-nodo-iot-ambiental/actividades', '7f5'),
    routes: [
      {
        path: '/mi-primer-nodo-iot-ambiental/actividades',
        component: ComponentCreator('/mi-primer-nodo-iot-ambiental/actividades', 'f7a'),
        routes: [
          {
            path: '/mi-primer-nodo-iot-ambiental/actividades',
            component: ComponentCreator('/mi-primer-nodo-iot-ambiental/actividades', '1e8'),
            routes: [
              {
                path: '/mi-primer-nodo-iot-ambiental/actividades/antes-de-empezar',
                component: ComponentCreator('/mi-primer-nodo-iot-ambiental/actividades/antes-de-empezar', '24c'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/mi-primer-nodo-iot-ambiental/actividades/ayuda',
                component: ComponentCreator('/mi-primer-nodo-iot-ambiental/actividades/ayuda', 'f2c'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/mi-primer-nodo-iot-ambiental/actividades/hola-mundo',
                component: ComponentCreator('/mi-primer-nodo-iot-ambiental/actividades/hola-mundo', '32b'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/mi-primer-nodo-iot-ambiental/actividades/intro',
                component: ComponentCreator('/mi-primer-nodo-iot-ambiental/actividades/intro', '15c'),
                exact: true
              },
              {
                path: '/mi-primer-nodo-iot-ambiental/actividades/medir-co2',
                component: ComponentCreator('/mi-primer-nodo-iot-ambiental/actividades/medir-co2', '8c1'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/mi-primer-nodo-iot-ambiental/actividades/medir-particulas',
                component: ComponentCreator('/mi-primer-nodo-iot-ambiental/actividades/medir-particulas', 'a16'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/mi-primer-nodo-iot-ambiental/actividades/primer-parpadeo',
                component: ComponentCreator('/mi-primer-nodo-iot-ambiental/actividades/primer-parpadeo', '7fa'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/mi-primer-nodo-iot-ambiental/actividades/sensor-simulado',
                component: ComponentCreator('/mi-primer-nodo-iot-ambiental/actividades/sensor-simulado', '762'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/mi-primer-nodo-iot-ambiental/actividades/tiempo-dentro-del-chip',
                component: ComponentCreator('/mi-primer-nodo-iot-ambiental/actividades/tiempo-dentro-del-chip', 'f52'),
                exact: true,
                sidebar: "tutorialSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '/mi-primer-nodo-iot-ambiental/',
    component: ComponentCreator('/mi-primer-nodo-iot-ambiental/', '183'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
