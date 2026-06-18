#include <Wire.h>
#include <SensirionI2CSen5x.h>

SensirionI2CSen5x sen5x;

char errorMessage[256];
uint16_t error;

void setup() {
  Serial.begin(115200);

  while (!Serial && millis() < 5000) {
  }

  Serial.println("Iniciando SEN55...");

  Wire.begin();
  sen5x.begin(Wire);

  error = sen5x.deviceReset();
  if (error) {
    Serial.print("Error en deviceReset(): ");
    errorToString(error, errorMessage, 256);
    Serial.println(errorMessage);

    while (1) {
      delay(1000);
    }
  }

  Serial.println("SEN55 listo.");
  Serial.println("----------------------------");
}

void loop() {
  float pm1p0;
  float pm2p5;
  float pm4p0;
  float pm10p0;
  float humidity;
  float temperature;
  float vocIndex;
  float noxIndex;

  Serial.println("Iniciando medicion SEN55...");

  error = sen5x.startMeasurement();
  if (error) {
    Serial.print("Error en startMeasurement(): ");
    errorToString(error, errorMessage, 256);
    Serial.println(errorMessage);
    delay(5000);
    return;
  }

  Serial.println("Ventilador encendido, esperando estabilizacion...");

  // Para medicion real usa 45000 ms.
  // Para pruebas rapidas de clase puedes usar 5000 ms.
  delay(45000);

  error = sen5x.readMeasuredValues(
    pm1p0,
    pm2p5,
    pm4p0,
    pm10p0,
    humidity,
    temperature,
    vocIndex,
    noxIndex
  );

  sen5x.stopMeasurement();

  if (error) {
    Serial.print("Error en readMeasuredValues(): ");
    errorToString(error, errorMessage, 256);
    Serial.println(errorMessage);
  } else {
    Serial.println("Datos SEN55:");

    Serial.print("PM1.0: ");
    Serial.print(pm1p0);
    Serial.println(" ug/m3");

    Serial.print("PM2.5: ");
    Serial.print(pm2p5);
    Serial.println(" ug/m3");

    Serial.print("PM4.0: ");
    Serial.print(pm4p0);
    Serial.println(" ug/m3");

    Serial.print("PM10: ");
    Serial.print(pm10p0);
    Serial.println(" ug/m3");

    Serial.print("Temperatura: ");
    Serial.print(temperature);
    Serial.println(" C");

    Serial.print("Humedad: ");
    Serial.print(humidity);
    Serial.println(" %");

    Serial.print("VOC Index: ");
    Serial.println(vocIndex);

    Serial.print("NOx Index: ");
    Serial.println(noxIndex);

    Serial.println("----------------------------");
  }

  delay(10000);
}
