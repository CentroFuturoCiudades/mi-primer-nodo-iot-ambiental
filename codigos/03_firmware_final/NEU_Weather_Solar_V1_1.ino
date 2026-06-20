// =====================================================================
// NEU_Weather_Solar_V1.1_Taller.ino
// version 1.1.0 - Workshop Update
//
// Solar Air-Quality Node — Blues Swan + Notecarrier F
// SEN55 (PM/VOC/NOx/T/RH) + optional SCD41 (CO2) + optional LC709203F
//
// Updated for workshop:
// - ProductUID configured
// - TEAM_ID added
// - LoRa templates include port numbers
// - DEBUG_MODE sends notes with sync:true
// - Missing optional sensors do not stop the program
// =====================================================================


// --------- OPTIONS ---------
#define ProductUID "mx.tec.alanromero:arroyo_vivo"

// Cambiar por equipo: 1, 2, 3, ... 10
#define TEAM_ID 1

// 1 = SCD41 installed, 0 = not installed
#define useSCD4x 1

// 0 = Cellular Notecard, 1 = Notecard LoRa
#define NOTECARD_LORA 1

// 1 = workshop/debug mode.
// 0 = deployment mode with low-power sleep.
#define DEBUG_MODE 1

#define BATT_LOW_ENTER 20
#define BATT_LOW_EXIT  30

// For workshop/debug. Each cycle includes 45 seconds of SEN55 warm-up.
#define DEBUG_CYCLE_SECONDS 180

// Battery status codes sent in battery.qo
#define BATT_STATUS_LOW       0
#define BATT_STATUS_RESTORED  1
#define BATT_STATUS_POWERON   2

#if DEBUG_MODE
  #define RECHARGE_INTERVAL_MS (DEBUG_CYCLE_SECONDS * 1000UL)
#else
  #define RECHARGE_INTERVAL_MS 3600000UL
#endif
// --------- OPTIONS END ---------


#include <Arduino.h>
#include <Wire.h>
#include <Notecard.h>
#include <SensirionI2CSen5x.h>
#include <Adafruit_LC709203F.h>

#if !DEBUG_MODE
  #include <STM32LowPower.h>
#endif

#if useSCD4x
  #include <SensirionI2cScd4x.h>
#endif


#define usbSerial Serial

static char errorMessage[256];
static int16_t error;
static int16_t scd_error;

Notecard notecard;
SensirionI2CSen5x sen5x;
Adafruit_LC709203F lc;

#if useSCD4x
  SensirionI2cScd4x scd4x;
#endif

bool hasSEN55 = false;
bool hasFuelGauge = false;

#if useSCD4x
bool hasSCD41 = false;
#else
bool hasSCD41 = false;
#endif

int prevInboundTime  = -1;
int prevOutboundTime = -1;


// --------- Low-power helper ---------
void enterLowPower(uint32_t ms) {
#if DEBUG_MODE
  delay(ms);
#else
  Serial.flush();
  Wire.end();
  LowPower.deepSleep(ms);
  Wire.begin();
#endif
}


// --------- Environment variable helper ---------
const char* getEnvVar(const char* varName, const char* defaultValue) {
  char* result = NULL;

  J* req = notecard.newRequest("env.get");
  if (req != NULL) {
    JAddStringToObject(req, "name", varName);

    J* rsp = notecard.requestAndResponse(req);
    if (rsp != NULL) {
      const char* value = JGetString(rsp, "text");
      if (value != NULL && strlen(value) > 0) {
        result = strdup(value);
      }
      notecard.deleteResponse(rsp);
    }
  }

  return result ? result : strdup(defaultValue);
}


// --------- Note templates ---------
void registerTemplates() {

  // ---- sensors.qo ----
  J* req = notecard.newRequest("note.template");
  JAddStringToObject(req, "file", "sensors.qo");

#if NOTECARD_LORA
  JAddStringToObject(req, "format", "compact");
  JAddNumberToObject(req, "port", 10);
#endif

  J* b = JAddObjectToObject(req, "body");
  if (b) {
    JAddNumberToObject(b, "team_id", TUINT8);
    JAddNumberToObject(b, "timestamp", TUINT32);

    JAddNumberToObject(b, "PM10",  TFLOAT32);
    JAddNumberToObject(b, "PM25",  TFLOAT32);
    JAddNumberToObject(b, "PM40",  TFLOAT32);
    JAddNumberToObject(b, "PM100", TFLOAT32);

    JAddNumberToObject(b, "vocIndex", TFLOAT32);
    JAddNumberToObject(b, "noxIndex", TFLOAT32);
    JAddNumberToObject(b, "temp",     TFLOAT32);
    JAddNumberToObject(b, "humidity", TFLOAT32);

    JAddNumberToObject(b, "scd_co2",   TUINT16);
    JAddNumberToObject(b, "scd_temp",  TFLOAT32);
    JAddNumberToObject(b, "scd_humid", TFLOAT32);

    JAddNumberToObject(b, "fuelgauge_percent", TFLOAT32);

#if !NOTECARD_LORA
    JAddStringToObject(b, "ID", TSTRING(32));
    JAddNumberToObject(b, "voltage", TFLOAT32);
    JAddNumberToObject(b, "fuelgauge_voltage", TFLOAT32);
    JAddNumberToObject(b, "fuelgauge_celltemp", TFLOAT32);
    JAddNumberToObject(b, "inboundTime",  TUINT16);
    JAddNumberToObject(b, "outboundTime", TUINT16);
    JAddNumberToObject(b, "readingInterval", TUINT16);
#endif
  }

  Serial.println("Registering template: sensors.qo");
  notecard.sendRequest(req);


  // ---- battery.qo ----
  J* req2 = notecard.newRequest("note.template");
  JAddStringToObject(req2, "file", "battery.qo");

#if NOTECARD_LORA
  JAddStringToObject(req2, "format", "compact");
  JAddNumberToObject(req2, "port", 11);
#endif

  J* b2 = JAddObjectToObject(req2, "body");
  if (b2) {
    JAddNumberToObject(b2, "team_id",     TUINT8);
    JAddNumberToObject(b2, "batt_v",      TFLOAT32);
    JAddNumberToObject(b2, "batt_pct",    TFLOAT32);
    JAddNumberToObject(b2, "batt_status", TUINT8);
  }

  Serial.println("Registering template: battery.qo");
  notecard.sendRequest(req2);
}


// --------- Helper to queue a battery.qo note ---------
void sendBatteryNote(float v, float pct, int statusCode, bool sync) {
  J* req = notecard.newRequest("note.add");
  if (req) {
    JAddStringToObject(req, "file", "battery.qo");

    if (sync) {
      JAddBoolToObject(req, "sync", true);
    }

    J* body = JAddObjectToObject(req, "body");
    if (body) {
      JAddNumberToObject(body, "team_id",     TEAM_ID);
      JAddNumberToObject(body, "batt_v",      v);
      JAddNumberToObject(body, "batt_pct",    pct);
      JAddNumberToObject(body, "batt_status", statusCode);
    }

    notecard.sendRequest(req);
  }
}


// --------- SETUP ---------
void setup() {
  delay(3000);

  Serial.begin(115200);
  delay(5000);

  Serial.println();
  Serial.println("=================================");
  Serial.println("NEU Weather Solar Node - Workshop");
  Serial.print("TEAM_ID: ");
  Serial.println(TEAM_ID);
  Serial.print("ProductUID: ");
  Serial.println(ProductUID);
  Serial.println("=================================");

  Wire.begin();
  delay(1000);

  notecard.begin();
  notecard.setDebugOutputStream(Serial);

  Serial.println("Start Setup");

#if !DEBUG_MODE
  LowPower.begin();
#endif

  // ---- Env vars ----
  const char* inboundTimeStr  = getEnvVar("inboundTime", "60");
  const char* outboundTimeStr = getEnvVar("outboundTime", "60");

  int inboundTime  = atoi(inboundTimeStr);
  int outboundTime = atoi(outboundTimeStr);

  free((void*)inboundTimeStr);
  free((void*)outboundTimeStr);

  prevInboundTime  = inboundTime;
  prevOutboundTime = outboundTime;


  // ---- Enable outboard DFU for STM32 host ----
  J* dfu = NoteNewRequest("card.dfu");
  JAddStringToObject(dfu, "name", "stm32");
  JAddBoolToObject(dfu, "on", true);
  notecard.sendRequest(dfu);


  // ---- Configure Notehub ----
  J* req1 = NoteNewRequest("hub.set");
  JAddStringToObject(req1, "product", ProductUID);
  JAddStringToObject(req1, "mode", "periodic");
  JAddNumberToObject(req1, "outbound", outboundTime);
  JAddNumberToObject(req1, "inbound", inboundTime);
  JAddBoolToObject(req1, "sync", true);
  notecard.sendRequest(req1);


  // ---- Register templates ----
  registerTemplates();


  // ---- Configure Notecard battery reporting ----
  J* volt = NoteNewRequest("card.voltage");
  JAddStringToObject(volt, "mode", "lipo");
  notecard.sendRequest(volt);


  // ---- SEN55 ----
  Serial.println("Initializing SEN55...");
  sen5x.begin(Wire);

  unsigned char productName[32];
  uint8_t productNameSize = 32;

  error = sen5x.getProductName(productName, productNameSize);
  if (error) {
    Serial.print("SEN55 getProductName() error: ");
    errorToString(error, errorMessage, 256);
    Serial.println(errorMessage);
    Serial.println("Continuing without SEN55.");
    hasSEN55 = false;
  } else {
    error = sen5x.deviceReset();
    if (error) {
      Serial.print("SEN55 deviceReset() error: ");
      errorToString(error, errorMessage, 256);
      Serial.println(errorMessage);
      Serial.println("Continuing without SEN55.");
      hasSEN55 = false;
    } else {
      hasSEN55 = true;
      Serial.print("SEN55 detected: ");
      Serial.println((char*)productName);
      Serial.println("done - SEN5X");
    }
  }


  // ---- SCD41 ----
#if useSCD4x
  Serial.println("Initializing SCD41...");
  scd4x.begin(Wire, SCD41_I2C_ADDR_62);

  scd_error = scd4x.wakeUp();
  scd_error = scd4x.stopPeriodicMeasurement();
  scd_error = scd4x.reinit();

  if (scd_error) {
    Serial.print("SCD4x init error: ");
    errorToString(scd_error, errorMessage, 256);
    Serial.println(errorMessage);
    Serial.println("Continuing without SCD41.");
    hasSCD41 = false;
  } else {
    scd4x.powerDown();
    hasSCD41 = true;
    Serial.println("done - SCD4x");
  }
#else
  Serial.println("SCD41 disabled in code.");
  hasSCD41 = false;
#endif


  // ---- LC709203F fuel gauge ----
  Serial.println("Initializing LC709203F fuel gauge...");
  if (!lc.begin()) {
    Serial.println("LC709203F not detected. Continuing without fuel gauge.");
    hasFuelGauge = false;
  } else {
    hasFuelGauge = true;
    Serial.print("LC709203F Version: 0x");
    Serial.println(lc.getICversion(), HEX);

    // closest preset for a 5000 mAh cell
    lc.setPackSize(LC709203F_APA_3000MAH);
    Serial.println("done - LC709203F");
  }

  Serial.println("End Setup");

  // ---- Power-on marker ----
  if (hasFuelGauge) {
    sendBatteryNote(lc.cellVoltage(), lc.cellPercent(), BATT_STATUS_POWERON, true);
  } else {
    sendBatteryNote(0.0, 0.0, BATT_STATUS_POWERON, true);
  }
}


// --------- MAIN LOOP ---------
void loop() {

  // ---- Fuel gauge ----
  float battery_voltage = 0.0;
  float battery_percent = 0.0;
  float battery_temp    = 0.0;

  if (hasFuelGauge) {
    battery_voltage = lc.cellVoltage();
    battery_percent = lc.cellPercent();
    battery_temp    = lc.getCellTemperature();
  }


  // ---- Battery hysteresis ----
  if (hasFuelGauge && battery_percent < BATT_LOW_ENTER) {
    Serial.println("Battery low - entering recharge wait.");
    sendBatteryNote(battery_voltage, battery_percent, BATT_STATUS_LOW, true);

    while (battery_percent < BATT_LOW_EXIT) {
      enterLowPower(RECHARGE_INTERVAL_MS);

      battery_voltage = lc.cellVoltage();
      battery_percent = lc.cellPercent();
      battery_temp    = lc.getCellTemperature();

      Serial.print("Recharge wait - battery: ");
      Serial.print(battery_percent);
      Serial.println(" %");

      sendBatteryNote(battery_voltage, battery_percent, BATT_STATUS_LOW, false);
    }

    sendBatteryNote(battery_voltage, battery_percent, BATT_STATUS_RESTORED, true);
    Serial.println("Battery recovered - resuming.");
  }


  // ---- Default values ----
  float pm1p0 = 0.0;
  float pm2p5 = 0.0;
  float pm4p0 = 0.0;
  float pm10p0 = 0.0;
  float ambHum = 0.0;
  float ambTemp = 0.0;
  float voc = 0.0;
  float nox = 0.0;

  uint16_t scdCO2 = 0;
  float scdTemp = 0.0;
  float scdHumidity = 0.0;


  // ---- SEN55 measurement ----
  if (hasSEN55) {
    Serial.println("SEN55: start measurement");
    error = sen5x.startMeasurement();

    if (error) {
      Serial.print("SEN55 startMeasurement() error: ");
      errorToString(error, errorMessage, 256);
      Serial.println(errorMessage);
    } else {

#if useSCD4x
      if (hasSCD41) {
        scd_error = scd4x.wakeUp();
      }
#endif

      Serial.println("SEN55 warm-up: 45 seconds");
      delay(45000);

      error = sen5x.readMeasuredValues(
        pm1p0,
        pm2p5,
        pm4p0,
        pm10p0,
        ambHum,
        ambTemp,
        voc,
        nox
      );

      sen5x.stopMeasurement();

      if (error) {
        Serial.print("SEN55 readMeasuredValues() error: ");
        errorToString(error, errorMessage, 256);
        Serial.println(errorMessage);
      } else {
        Serial.println("SEN55 data:");
        Serial.print("PM2.5: ");
        Serial.print(pm2p5);
        Serial.print(" ug/m3  T: ");
        Serial.print(ambTemp);
        Serial.print(" C  RH: ");
        Serial.print(ambHum);
        Serial.print(" %  VOC: ");
        Serial.print(voc);
        Serial.print("  NOx: ");
        Serial.println(nox);
      }
    }
  } else {
    Serial.println("SEN55 not available. Sending zeros for SEN55 fields.");
    delay(5000);
  }


  // ---- SCD41 measurement ----
#if useSCD4x
  if (hasSCD41) {
    Serial.println("SCD4x: measure");

    scd_error = scd4x.measureSingleShot();
    scd_error = scd4x.measureAndReadSingleShot(scdCO2, scdTemp, scdHumidity);

    if (scd_error) {
      Serial.print("SCD4x measureAndReadSingleShot() error: ");
      errorToString(scd_error, errorMessage, sizeof errorMessage);
      Serial.println(errorMessage);
    } else {
      Serial.println("SCD41 data:");
      Serial.print("CO2: ");
      Serial.print(scdCO2);
      Serial.print(" ppm  T: ");
      Serial.print(scdTemp);
      Serial.print(" C  RH: ");
      Serial.print(scdHumidity);
      Serial.println(" %");
    }

    scd4x.powerDown();
  } else {
    Serial.println("SCD41 not available. Sending zeros for SCD41 fields.");
  }
#endif


  // ---- Timestamp from Notecard ----
  uint32_t timestamp = 0;

  J* timeRsp = notecard.requestAndResponse(notecard.newRequest("card.time"));
  if (timeRsp != NULL) {
    if (!notecard.responseError(timeRsp) && JIsPresent(timeRsp, "time")) {
      timestamp = (uint32_t)JGetNumber(timeRsp, "time");
    } else {
      Serial.println("card.time not set yet.");
    }
    notecard.deleteResponse(timeRsp);
  }


  // ---- Latest env vars ----
  const char* intervalStr = getEnvVar("readingInterval", "1800");
  int readingInterval = atoi(intervalStr);
  free((void*)intervalStr);

  const char* inboundTimeStr  = getEnvVar("inboundTime", "60");
  const char* outboundTimeStr = getEnvVar("outboundTime", "60");

  int inboundTime  = atoi(inboundTimeStr);
  int outboundTime = atoi(outboundTimeStr);

  free((void*)inboundTimeStr);
  free((void*)outboundTimeStr);

#if DEBUG_MODE
  readingInterval = DEBUG_CYCLE_SECONDS;
#endif


#if !NOTECARD_LORA
  // ---- Device ID for cellular diagnostics ----
  char deviceUID[64] = "unknown";
  J* verRsp = notecard.requestAndResponse(notecard.newRequest("card.version"));
  if (verRsp != NULL) {
    const char* uid = JGetString(verRsp, "device");
    if (uid != NULL && strlen(uid) < sizeof(deviceUID)) {
      strcpy(deviceUID, uid);
    }
    notecard.deleteResponse(verRsp);
  }

  // ---- Notecard V+ for cellular diagnostics ----
  double voltage = -1;
  J* vrsp = notecard.requestAndResponse(notecard.newRequest("card.voltage"));
  if (vrsp != NULL) {
    voltage = JGetNumber(vrsp, "value");
    notecard.deleteResponse(vrsp);
  }
#endif


  // ---- Send sensor note ----
  J* req = notecard.newRequest("note.add");
  if (req) {
    JAddStringToObject(req, "file", "sensors.qo");

#if DEBUG_MODE
    // For workshop: force sync so data appears quickly in Notehub.
    JAddBoolToObject(req, "sync", true);
#endif

    J* body = JAddObjectToObject(req, "body");
    if (body) {
      JAddNumberToObject(body, "team_id", TEAM_ID);
      JAddNumberToObject(body, "timestamp", timestamp);

      JAddNumberToObject(body, "PM10",  pm1p0);
      JAddNumberToObject(body, "PM25",  pm2p5);
      JAddNumberToObject(body, "PM40",  pm4p0);
      JAddNumberToObject(body, "PM100", pm10p0);

      JAddNumberToObject(body, "vocIndex", voc);
      JAddNumberToObject(body, "noxIndex", nox);
      JAddNumberToObject(body, "temp",     ambTemp);
      JAddNumberToObject(body, "humidity", ambHum);

      JAddNumberToObject(body, "scd_co2",   scdCO2);
      JAddNumberToObject(body, "scd_temp",  scdTemp);
      JAddNumberToObject(body, "scd_humid", scdHumidity);

      JAddNumberToObject(body, "fuelgauge_percent", battery_percent);

#if !NOTECARD_LORA
      JAddStringToObject(body, "ID", deviceUID);
      JAddNumberToObject(body, "voltage", voltage);
      JAddNumberToObject(body, "fuelgauge_voltage", battery_voltage);
      JAddNumberToObject(body, "fuelgauge_celltemp", battery_temp);
      JAddNumberToObject(body, "inboundTime",  inboundTime);
      JAddNumberToObject(body, "outboundTime", outboundTime);
      JAddNumberToObject(body, "readingInterval", readingInterval);
#endif
    }

    Serial.println("Sending sensors.qo note...");
    notecard.sendRequest(req);
  }


  // ---- Update hub.set if env vars changed ----
  if (inboundTime != prevInboundTime || outboundTime != prevOutboundTime) {
    prevInboundTime  = inboundTime;
    prevOutboundTime = outboundTime;

    J* hubReq = NoteNewRequest("hub.set");
    JAddStringToObject(hubReq, "product", ProductUID);
    JAddStringToObject(hubReq, "mode", "periodic");
    JAddNumberToObject(hubReq, "outbound", outboundTime);
    JAddNumberToObject(hubReq, "inbound", inboundTime);
    JAddBoolToObject(hubReq, "sync", true);

    notecard.sendRequest(hubReq);
    Serial.println("hub.set updated because env vars changed.");
  }


  // ---- Sleep / wait until next reading ----
  Serial.print("Waiting before next reading. Seconds: ");
  Serial.println(readingInterval);

  enterLowPower((uint32_t)readingInterval * 1000UL);

  Serial.println("Wake");
}