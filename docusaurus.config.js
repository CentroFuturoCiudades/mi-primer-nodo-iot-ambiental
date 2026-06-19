// @ts-check

const config = {
  title: 'Ciencia, tecnología y arte para el cuidado del Arroyo Vivo',
  tagline: 'Taller Arroyo Vivo',
  favicon: 'img/favicon.ico',

  // Cambia estos datos cuando publiques en GitHub Pages.
  url: 'https://CentroFuturoCiudades.github.io',
  baseUrl: '/mi-primer-nodo-iot-ambiental/',

  organizationName: 'CentroFuturoCiudades',
  projectName: 'mi-primer-nodo-iot-ambiental',

  onBrokenLinks: 'throw',

  i18n: {
    defaultLocale: 'es',
    locales: ['es'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.js',
          routeBasePath: '/actividades',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      },
    ],
  ],

  themeConfig: {
    navbar: {
      items: [
        {
          to: '/',
          label: 'Inicio',
          position: 'left',
        },
        {
          to: '/actividades/antes-de-empezar',
          label: 'Guía académica',
          position: 'left',
        },
        {
          to: '/actividades/ayuda',
          label: 'Soporte',
          position: 'left',
        },
      ],
    },

    footer: {
      style: 'dark',
      links: [
        {
          title: 'Taller',
          items: [
            {
              label: 'Inicio',
              to: '/',
            },
            {
              label: 'Guía académica',
              to: '/actividades/antes-de-empezar',
            },
          ],
        },
      ],
      copyright: `Centro para el Futuro de las Ciudades — ${new Date().getFullYear()}`,
    },
  },
};

export default config;
