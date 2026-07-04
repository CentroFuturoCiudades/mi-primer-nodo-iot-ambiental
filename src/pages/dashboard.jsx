import React, {useCallback, useEffect, useMemo, useRef, useState} from 'react';
import Layout from '@theme/Layout';
import useBaseUrl from '@docusaurus/useBaseUrl';
import {
  CategoryScale,
  Chart as ChartJS,
  Filler,
  Legend,
  LinearScale,
  LineElement,
  PointElement,
  Title,
  Tooltip,
} from 'chart.js';
import {Line} from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  Filler,
  Legend,
  LinearScale,
  LineElement,
  PointElement,
  Title,
  Tooltip,
);

const API_BASE =
  'https://arroyo-vivo-ingest-enbvbvh3b9f8azc3.westus2-01.azurewebsites.net/api';

const LEAFLET_CSS = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css';
const LEAFLET_JS = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js';

const FALLBACK_DEVICES = [
  {
    device_uid: 'dev:0080e115004531d4',
    name: 'Colibrí',
    type: 'sensor',
    team_id: 1,
    latitude: 25.638386524771192,
    longitude: -100.30466820974594,
    location_name: 'Arroyo Vivo / Sensor ambiental',
    description: 'Nodo ambiental SEN55 + Notecard LoRa',
    last_measurement: null,
  },
  {
    device_uid: 'dev:mariposa-demo',
    name: 'Mariposa',
    type: 'sensor',
    team_id: 2,
    latitude: 25.63824,
    longitude: -100.30479,
    location_name: 'Arroyo Vivo / Sensor ambiental',
    description: 'Nodo ambiental SEN55 + Notecard LoRa',
    last_measurement: null,
  },
  {
    device_uid: 'gateway:rak2287-arroyo-vivo',
    name: 'Gateway LoRaWAN',
    type: 'gateway',
    team_id: null,
    latitude: 25.637859359865796,
    longitude: -100.30491257705157,
    location_name: 'Arroyo Vivo / Gateway',
    description: 'RAK2287 conectado a TTN',
    last_measurement: null,
  },
];

const chartBaseOptions = {
  responsive: true,
  maintainAspectRatio: false,
  interaction: {
    intersect: false,
    mode: 'index',
  },
  plugins: {
    legend: {
      align: 'end',
      labels: {
        boxHeight: 10,
        boxWidth: 18,
        color: '#24433e',
        font: {
          family: 'inherit',
          weight: 800,
        },
      },
    },
    tooltip: {
      backgroundColor: '#062b27',
      padding: 12,
      titleFont: {
        weight: 900,
      },
    },
  },
  scales: {
    x: {
      grid: {
        display: false,
      },
      ticks: {
        color: '#61716e',
        maxRotation: 0,
        autoSkipPadding: 22,
      },
    },
    y: {
      beginAtZero: true,
      grid: {
        color: 'rgba(16, 67, 78, 0.09)',
      },
      ticks: {
        color: '#61716e',
      },
    },
  },
};

async function fetchDevices() {
  const response = await fetch(`${API_BASE}/devices`);

  if (!response.ok) {
    throw new Error(`Respuesta ${response.status}`);
  }

  return response.json();
}

async function fetchMeasurements(teamId) {
  const response = await fetch(
    `${API_BASE}/devices/team/${encodeURIComponent(teamId)}/measurements?limit=200`,
  );

  if (!response.ok) {
    throw new Error(`Respuesta ${response.status}`);
  }

  return response.json();
}

function normalizeText(value = '') {
  return value
    .toString()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase();
}

function getDeviceBadge(device) {
  if (device?.type === 'gateway') {
    return 'GW';
  }

  const name = normalizeText(device?.name);

  if (device?.team_id === 1 || name.includes('colibri')) {
    return 'CO';
  }

  if (device?.team_id === 2 || name.includes('mariposa')) {
    return 'MA';
  }

  return device?.team_id ? `T${device.team_id}` : 'SN';
}

function getDeviceMarkerColor(device) {
  if (device?.type === 'gateway') {
    return '#52677a';
  }

  const name = normalizeText(device?.name);

  if (device?.team_id === 1 || name.includes('colibri')) {
    return '#2f9b73';
  }

  if (device?.team_id === 2 || name.includes('mariposa')) {
    return '#1188a0';
  }

  return '#1188a0';
}

function createMapMarkerIcon(L, {label, color, selected}) {
  return L.divIcon({
    className: '',
    html: `
      <div class="avMapMarker ${selected ? 'isSelected' : ''}" style="--marker-color:${color}">
        <div class="avMapMarkerPin"><span>${label}</span></div>
      </div>
    `,
    iconSize: [44, 56],
    iconAnchor: [22, 56],
    popupAnchor: [0, -54],
  });
}

function normalizeDevice(device) {
  if (device?.type !== 'sensor') {
    return device;
  }

  const name = normalizeText(device.name);

  if (name.includes('colibri')) {
    return {
      ...device,
      team_id: 1,
    };
  }

  if (name.includes('mariposa')) {
    return {
      ...device,
      team_id: 2,
    };
  }

  return device;
}

function getDeviceLabel(device) {
  if (device?.type === 'gateway') {
    return 'GW';
  }

  if (device?.team_id) {
    return `T${device.team_id}`;
  }

  return 'SN';
}

function getPm25Status(value) {
  if (typeof value !== 'number') {
    return {
      label: 'Sin lectura',
      tone: 'muted',
    };
  }

  if (value < 12) {
    return {
      label: 'Bueno',
      tone: 'good',
    };
  }

  if (value <= 35) {
    return {
      label: 'Moderado',
      tone: 'moderate',
    };
  }

  return {
    label: 'Alto',
    tone: 'high',
  };
}

function formatNumber(value, digits = 1) {
  if (typeof value !== 'number') {
    return '--';
  }

  return new Intl.NumberFormat('es-MX', {
    maximumFractionDigits: digits,
    minimumFractionDigits: digits,
  }).format(value);
}

function formatTime(value) {
  if (!value) {
    return '--';
  }

  return new Date(value).toLocaleTimeString('es-MX', {
    hour: '2-digit',
    minute: '2-digit',
  });
}

function formatDateTime(value) {
  if (!value) {
    return 'Sin lectura registrada';
  }

  return new Date(value).toLocaleString('es-MX');
}

function buildChartData(measurements) {
  const labels = measurements.map((row) => formatTime(row.time));

  return {
    particles: {
      labels,
      datasets: [
        {
          label: 'PM2.5',
          data: measurements.map((row) => row.pm25),
          borderColor: '#2f9b73',
          backgroundColor: 'rgba(47, 155, 115, 0.12)',
          borderWidth: 3,
          pointRadius: 0,
          pointHoverRadius: 4,
          tension: 0.32,
          fill: true,
        },
        {
          label: 'PM10',
          data: measurements.map((row) => row.pm10),
          borderColor: '#1188a0',
          backgroundColor: 'rgba(17, 136, 160, 0.08)',
          borderWidth: 3,
          pointRadius: 0,
          pointHoverRadius: 4,
          tension: 0.32,
          fill: true,
        },
      ],
    },
    climate: {
      labels,
      datasets: [
        {
          label: 'Temperatura',
          data: measurements.map((row) => row.temperature),
          borderColor: '#f5b041',
          backgroundColor: 'rgba(245, 176, 65, 0.12)',
          borderWidth: 3,
          pointRadius: 0,
          pointHoverRadius: 4,
          tension: 0.32,
          yAxisID: 'temperature',
        },
        {
          label: 'Humedad',
          data: measurements.map((row) => row.humidity),
          borderColor: '#c65b83',
          backgroundColor: 'rgba(198, 91, 131, 0.10)',
          borderWidth: 3,
          pointRadius: 0,
          pointHoverRadius: 4,
          tension: 0.32,
          yAxisID: 'humidity',
        },
      ],
    },
  };
}

function getStats(measurements, key) {
  const values = measurements
    .map((row) => row[key])
    .filter((value) => typeof value === 'number');

  if (values.length === 0) {
    return {
      min: null,
      max: null,
      avg: null,
    };
  }

  return {
    min: Math.min(...values),
    max: Math.max(...values),
    avg: values.reduce((sum, value) => sum + value, 0) / values.length,
  };
}

function loadLeaflet() {
  if (typeof window === 'undefined') {
    return Promise.resolve(null);
  }

  if (window.L) {
    return Promise.resolve(window.L);
  }

  if (!document.querySelector(`link[href="${LEAFLET_CSS}"]`)) {
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = LEAFLET_CSS;
    document.head.appendChild(link);
  }

  const existingScript = document.querySelector(`script[src="${LEAFLET_JS}"]`);

  if (existingScript) {
    return new Promise((resolve, reject) => {
      existingScript.addEventListener('load', () => resolve(window.L), {
        once: true,
      });
      existingScript.addEventListener('error', reject, {once: true});
    });
  }

  return new Promise((resolve, reject) => {
    const script = document.createElement('script');
    script.src = LEAFLET_JS;
    script.async = true;
    script.onload = () => resolve(window.L);
    script.onerror = reject;
    document.body.appendChild(script);
  });
}

function MetricCard({label, value, unit, tone, status}) {
  return (
    <article className={`dashboardMetric dashboardMetric--${tone}`}>
      <div>
        <p>{label}</p>
        {status && <span className={`pmStatus pmStatus--${status.tone}`}>{status.label}</span>}
      </div>
      <strong>{formatNumber(value)}</strong>
      <small>{unit}</small>
    </article>
  );
}

function StatCard({label, stats, unit, tone}) {
  return (
    <article className={`historyStat historyStat--${tone}`}>
      <p>{label}</p>
      <strong>{formatNumber(stats.avg)}</strong>
      <span>Promedio {unit}</span>
      <dl>
        <div>
          <dt>Mín.</dt>
          <dd>{formatNumber(stats.min)}</dd>
        </div>
        <div>
          <dt>Máx.</dt>
          <dd>{formatNumber(stats.max)}</dd>
        </div>
      </dl>
    </article>
  );
}

export default function Dashboard() {
  const logo = useBaseUrl('/img/arroyo-vivo-dgeti-logos.png');
  const mapElementRef = useRef(null);
  const mapRef = useRef(null);
  const markerLayerRef = useRef(null);
  const selectedDeviceRef = useRef(null);

  const [devices, setDevices] = useState([]);
  const [selectedDevice, setSelectedDevice] = useState(null);
  const [measurements, setMeasurements] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [lastUpdated, setLastUpdated] = useState(null);

  useEffect(() => {
    selectedDeviceRef.current = selectedDevice;
  }, [selectedDevice]);

  const loadDashboard = useCallback(async ({silent = false} = {}) => {
    if (!silent) {
      setLoading(true);
    }

    let nextSelection = null;

    try {
      const apiDevices = await fetchDevices();
      const nextDevices = Array.isArray(apiDevices)
        ? apiDevices.map(normalizeDevice)
        : [];
      console.log('devices from API', nextDevices);

      const previousSelection = selectedDeviceRef.current;
      const sensor = nextDevices.find((device) => device.type === 'sensor');
      nextSelection =
        nextDevices.find(
          (device) => device.device_uid === previousSelection?.device_uid,
        ) ||
        nextDevices.find(
          (device) =>
            previousSelection?.type === 'sensor' &&
            device.type === 'sensor' &&
            device.team_id === previousSelection.team_id,
        ) ||
        sensor ||
        nextDevices[0] ||
        null;

      setDevices(nextDevices);
      setSelectedDevice(nextSelection);
      setError('');
      setLastUpdated(new Date());
    } catch (caughtError) {
      console.error('No se pudo actualizar el dashboard.', {
        endpoint: `${API_BASE}/devices`,
        error: caughtError,
      });

      setError(caughtError.message || 'Error de red o CORS');
      setDevices((currentDevices) =>
        currentDevices.length > 0 ? currentDevices : FALLBACK_DEVICES,
      );
      setSelectedDevice((currentSelection) => currentSelection || FALLBACK_DEVICES[0]);
      setMeasurements([]);
      setLoading(false);
      return;
    }

    if (nextSelection?.type === 'sensor' && nextSelection.team_id != null) {
      try {
        const history = await fetchMeasurements(nextSelection.team_id);
        setMeasurements(Array.isArray(history) ? history : []);
      } catch (caughtError) {
        console.error('No se pudo cargar el histórico del nodo.', {
          endpoint: `${API_BASE}/devices/team/${encodeURIComponent(
            nextSelection.team_id,
          )}/measurements?limit=200`,
          error: caughtError,
        });
        setError(caughtError.message || 'Error al cargar mediciones');
        setMeasurements([]);
      }
    } else {
      setMeasurements([]);
    }

    setLoading(false);
  }, []);

  const selectDevice = useCallback(async (device) => {
    setSelectedDevice(device);
    setError('');

    if (device.type !== 'sensor') {
      setMeasurements([]);
      return;
    }

    if (device.team_id == null) {
      setError('El sensor seleccionado no tiene team_id para consultar histórico');
      setMeasurements([]);
      return;
    }

    setLoading(true);

    try {
      const history = await fetchMeasurements(device.team_id);
      setMeasurements(Array.isArray(history) ? history : []);
      setLastUpdated(new Date());
    } catch (caughtError) {
      console.error('No se pudo cargar el histórico del nodo.', {
        endpoint: `${API_BASE}/devices/team/${encodeURIComponent(
          device.team_id,
        )}/measurements?limit=200`,
        error: caughtError,
      });
      setError(caughtError.message || 'Error al cargar mediciones');
      setMeasurements([]);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadDashboard();
    const timer = window.setInterval(() => loadDashboard({silent: true}), 60000);

    return () => window.clearInterval(timer);
  }, [loadDashboard]);

  useEffect(() => {
    let cancelled = false;

    async function renderMap() {
      const L = await loadLeaflet();

      if (!L || cancelled || !mapElementRef.current) {
        return;
      }

      const locatedDevices = devices.filter(
        (device) =>
          typeof device.latitude === 'number' &&
          typeof device.longitude === 'number',
      );

      if (!mapRef.current) {
        mapRef.current = L.map(mapElementRef.current, {
          zoomControl: true,
          scrollWheelZoom: true,
        }).setView([25.63815, -100.30479], 18);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          maxZoom: 21,
          attribution: '&copy; OpenStreetMap contributors',
        }).addTo(mapRef.current);

        markerLayerRef.current = L.layerGroup().addTo(mapRef.current);
      }

      markerLayerRef.current.clearLayers();

      locatedDevices.forEach((device) => {
        const isSelected = device.device_uid === selectedDevice?.device_uid;
        const icon = createMapMarkerIcon(L, {
          label: getDeviceBadge(device),
          color: getDeviceMarkerColor(device),
          selected: isSelected,
        });
        const popupType =
          device.type === 'gateway' ? 'Gateway LoRaWAN' : 'Nodo sensor';
        const popupTeam =
          device.type === 'sensor' && device.team_id != null
            ? `<p><span>Team ID</span><strong>${device.team_id}</strong></p>`
            : '';
        const popupAction =
          device.type === 'sensor'
            ? '<button type="button" class="avPopupButton">Ver mediciones</button>'
            : '';

        L.marker([device.latitude, device.longitude], {icon})
          .addTo(markerLayerRef.current)
          .on('click', () => selectDevice(device))
          .bindPopup(`
            <div class="avMapPopup">
              <h3>${device.name}</h3>
              <p><span>Tipo</span><strong>${popupType}</strong></p>
              ${popupTeam}
              ${popupAction}
            </div>
          `);
      });

      if (locatedDevices.length > 1) {
        const bounds = L.latLngBounds(
          locatedDevices.map((device) => [device.latitude, device.longitude]),
        );
        mapRef.current.fitBounds(bounds, {padding: [72, 72], maxZoom: 18});
      } else if (locatedDevices.length === 1) {
        mapRef.current.setView(
          [locatedDevices[0].latitude, locatedDevices[0].longitude],
          18,
        );
      }

      window.setTimeout(() => mapRef.current?.invalidateSize(), 50);
    }

    renderMap();

    return () => {
      cancelled = true;
    };
  }, [devices, selectedDevice, selectDevice]);

  useEffect(() => {
    return () => {
      mapRef.current?.remove();
      mapRef.current = null;
      markerLayerRef.current = null;
    };
  }, []);

  const selectedMeasurement = selectedDevice?.last_measurement || {};
  const selectedIsSensor = selectedDevice?.type === 'sensor';
  const activeSensors = devices.filter((device) => device.type === 'sensor');
  const activeGateways = devices.filter((device) => device.type === 'gateway');
  const pm25Status = getPm25Status(selectedMeasurement.pm25);
  const chartData = useMemo(() => buildChartData(measurements), [measurements]);
  const historyStats = useMemo(
    () => ({
      pm25: getStats(measurements, 'pm25'),
      temperature: getStats(measurements, 'temperature'),
      humidity: getStats(measurements, 'humidity'),
    }),
    [measurements],
  );

  const particleChartOptions = useMemo(
    () => ({
      ...chartBaseOptions,
      plugins: {
        ...chartBaseOptions.plugins,
        title: {
          display: false,
        },
      },
      scales: {
        ...chartBaseOptions.scales,
        y: {
          ...chartBaseOptions.scales.y,
          title: {
            display: true,
            text: 'µg/m³',
          },
        },
      },
    }),
    [],
  );

  const climateChartOptions = useMemo(
    () => ({
      ...chartBaseOptions,
      scales: {
        x: chartBaseOptions.scales.x,
        temperature: {
          type: 'linear',
          position: 'left',
          grid: {
            color: 'rgba(16, 67, 78, 0.09)',
          },
          ticks: {
            color: '#8a5b00',
          },
          title: {
            display: true,
            text: '°C',
          },
        },
        humidity: {
          type: 'linear',
          position: 'right',
          grid: {
            drawOnChartArea: false,
          },
          ticks: {
            color: '#8a1f3f',
          },
          title: {
            display: true,
            text: '% humedad',
          },
        },
      },
    }),
    [],
  );

  return (
    <Layout
      title="Dashboard Arroyo Vivo"
      description="Dashboard de datos ambientales del nodo Colibrí en Arroyo Vivo"
    >
      <main className="dashboardPage">
        <section className="dashboardHero">
          <img src={logo} alt="Arroyo Vivo y DGETI" />

          <div className="dashboardHeroText">
            <p className="dashboardKicker">Monitoreo ambiental</p>
            <h1>Dashboard Arroyo Vivo</h1>
            <p>
              Datos del nodo Colibrí, ubicación del gateway LoRaWAN e histórico
              de mediciones para la demo del taller.
            </p>
          </div>

          <div className="dashboardHeroActions">
            <div
              className="dashboardStatus"
              data-status={error ? 'error' : loading ? 'loading' : 'ready'}
            >
              <span />
              {error ? 'Respaldo local' : loading ? 'Cargando datos...' : 'Datos en vivo'}
            </div>
            <button
              className="refreshButton"
              type="button"
              onClick={() => loadDashboard()}
              disabled={loading}
            >
              Actualizar ahora
            </button>
          </div>
        </section>

        <section className="dashboardLayout">
          <section className="dashboardPanel mapPanel">
            <div className="panelHeader">
              <div>
                <p className="dashboardKicker">Ubicación</p>
                <h2>Arroyo Vivo</h2>
                <p className="mapSummary">
                  {activeSensors.length} sensores · {activeGateways.length} gateway
                </p>
              </div>
              <a
                className="mapLink"
                href="https://www.openstreetmap.org/"
                target="_blank"
                rel="noreferrer"
              >
                OpenStreetMap
              </a>
            </div>

            <div
              ref={mapElementRef}
              className="dashboardMap"
              aria-label="Mapa de ubicación del nodo Colibrí y Gateway LoRaWAN"
            />
          </section>

          <aside className="dashboardPanel nodeOverview">
            <div className="selectedNodeHeader">
              <div className={`nodeInitial nodeInitial--${selectedDevice?.type || 'sensor'}`}>
                {getDeviceBadge(selectedDevice)}
              </div>
              <div>
                <p className="dashboardKicker">
                  {selectedDevice?.type === 'gateway'
                    ? 'Infraestructura'
                    : 'Nodo seleccionado'}
                </p>
                <h2>{selectedDevice?.name || 'Colibrí'}</h2>
                <p>{selectedDevice?.description || 'Nodo ambiental SEN55 + Notecard LoRa'}</p>
              </div>
            </div>

            <dl className="nodeDetails">
              <div>
                <dt>Última lectura</dt>
                <dd>{formatDateTime(selectedMeasurement.recorded_at)}</dd>
              </div>
              <div>
                <dt>ID del dispositivo</dt>
                <dd>{selectedDevice?.device_uid || 'Cargando dispositivo...'}</dd>
              </div>
              <div>
                <dt>Ubicación</dt>
                <dd>{selectedDevice?.location_name || 'Arroyo Vivo'}</dd>
              </div>
              <div>
                <dt>Equipo</dt>
                <dd>
                  {selectedDevice?.type === 'sensor' && selectedDevice?.team_id != null
                    ? `Team ${selectedDevice.team_id}`
                    : selectedDevice?.type === 'gateway'
                      ? 'Infraestructura'
                      : 'Sin asignar'}
                </dd>
              </div>
              <div>
                <dt>Última actualización</dt>
                <dd>{lastUpdated ? formatDateTime(lastUpdated) : 'Pendiente'}</dd>
              </div>
            </dl>

            <div className="activeDevices">
              <p className="dashboardKicker">Dispositivos activos</p>
              <div className="activeDeviceList">
                {devices.map((device) => (
                  <button
                    key={device.device_uid}
                    className={`activeDeviceButton ${
                      device.device_uid === selectedDevice?.device_uid
                        ? 'activeDeviceButton--selected'
                        : ''
                    }`}
                    type="button"
                    onClick={() => selectDevice(device)}
                  >
                    <span>{getDeviceBadge(device)}</span>
                    <strong>{device.name}</strong>
                    <small>{getDeviceLabel(device)}</small>
                  </button>
                ))}
              </div>
            </div>

            {error && (
              <p className="dashboardError">
                No se pudo consultar la API desde el navegador. Se conserva la
                ubicación local de respaldo. Detalle: {error}
              </p>
            )}
          </aside>
        </section>

        <section className="metricGrid" aria-label="Lecturas ambientales actuales">
          <MetricCard
            label="PM2.5"
            value={selectedMeasurement.pm25}
            unit="µg/m³"
            tone="green"
            status={pm25Status}
          />
          <MetricCard
            label="PM10"
            value={selectedMeasurement.pm10}
            unit="µg/m³"
            tone="blue"
          />
          <MetricCard
            label="Temperatura"
            value={selectedMeasurement.temperature}
            unit="°C"
            tone="amber"
          />
          <MetricCard
            label="Humedad"
            value={selectedMeasurement.humidity}
            unit="%"
            tone="pink"
          />
        </section>

        <section className="historySection">
          <div className="historyHeader">
            <div>
              <p className="dashboardKicker">Líneas de tiempo</p>
              <h2>Histórico ambiental</h2>
              <p>
                {selectedIsSensor
                  ? `Últimas ${measurements.length} mediciones registradas por ${
                      selectedDevice?.name || 'el nodo'
                    }${
                      selectedDevice?.team_id != null
                        ? `, equipo ${selectedDevice.team_id}.`
                        : '.'
                    }`
                  : 'Selecciona el nodo Colibrí en el mapa para consultar mediciones históricas.'}
              </p>
            </div>
            {loading && <span className="loadingPill">Cargando datos...</span>}
          </div>

          {selectedIsSensor ? (
            <>
              <div className="historyStatsGrid">
                <StatCard
                  label="PM2.5"
                  stats={historyStats.pm25}
                  unit="µg/m³"
                  tone="green"
                />
                <StatCard
                  label="Temperatura"
                  stats={historyStats.temperature}
                  unit="°C"
                  tone="amber"
                />
                <StatCard
                  label="Humedad"
                  stats={historyStats.humidity}
                  unit="%"
                  tone="pink"
                />
              </div>

              <div className="chartGrid">
                <article className="dashboardPanel chartPanel">
                  <div className="panelHeader">
                    <div>
                      <p className="dashboardKicker">Partículas suspendidas</p>
                      <h3>PM2.5 y PM10</h3>
                    </div>
                  </div>
                  <div className="chartFrame">
                    {measurements.length > 0 ? (
                      <Line data={chartData.particles} options={particleChartOptions} />
                    ) : (
                      <p className="emptyChart">Sin mediciones históricas disponibles.</p>
                    )}
                  </div>
                </article>

                <article className="dashboardPanel chartPanel">
                  <div className="panelHeader">
                    <div>
                      <p className="dashboardKicker">Microclima</p>
                      <h3>Temperatura y humedad</h3>
                    </div>
                  </div>
                  <div className="chartFrame">
                    {measurements.length > 0 ? (
                      <Line data={chartData.climate} options={climateChartOptions} />
                    ) : (
                      <p className="emptyChart">Sin mediciones históricas disponibles.</p>
                    )}
                  </div>
                </article>
              </div>
            </>
          ) : (
            <div className="dashboardPanel gatewayNotice">
              <p className="dashboardKicker">Gateway LoRaWAN</p>
              <h3>Infraestructura de comunicación</h3>
              <p>
                Este punto recibe los paquetes LoRaWAN del nodo ambiental. No
                genera series de PM2.5, PM10, temperatura o humedad.
              </p>
            </div>
          )}
        </section>
      </main>
    </Layout>
  );
}
