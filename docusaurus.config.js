// @ts-check

const config = {
  title: 'Mi primer nodo IoT ambiental',
  tagline: 'De la arena al sensor inteligente',
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
      title: 'Mi primer nodo IoT ambiental',
      items: [
        {
          to: '/',
          label: 'Inicio',
          position: 'left',
        },
        {
          to: '/slides/',
          label: 'Historia visual',
          position: 'left',
        },
        {
          to: '/actividades/antes-de-empezar',
          label: 'Actividades',
          position: 'left',
        },
        {
          to: '/actividades/ayuda',
          label: 'Ayuda',
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
              label: 'Historia visual',
              to: '/slides/',
            },
            {
              label: 'Actividades',
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
