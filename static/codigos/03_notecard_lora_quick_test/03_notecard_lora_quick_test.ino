#include <Arduino.h>
#include <Wire.h>
#include <Notecard.h>

#define ProductUID "mx.tec.alanromero:arroyo_vivo"
#define TEAM_ID 1   // Cambiar por equipo: 1, 2, 3, ... 10

Notecard notecard;
int counter = 0;

void setup() {
  Serial.begin(115200);
  delay(5000);

  Wire.begin();
  notecard.begin();
  notecard.setDebugOutputStream(Serial);

  Serial.println();
  Serial.println("=================================");
  Serial.println("RAK2287 LoRa quick test");
  Serial.print("TEAM_ID: ");
  Serial.println(TEAM_ID);
  Serial.println("ProductUID: mx.tec.alanromero:arroyo_vivo");
  Serial.println("=================================");

  J *req = notecard.newRequest("hub.set");
  if (req != NULL) {
    JAddStringToObject(req, "product", ProductUID);
    JAddStringToObject(req, "mode", "continuous");
    JAddNumberToObject(req, "outbound", 1);
    JAddNumberToObject(req, "inbound", 60);
    JAddBoolToObject(req, "sync", true);

    Serial.println("Enviando hub.set...");
    notecard.sendRequest(req);
  }

  delay(2000);

  req = notecard.newRequest("note.template");
  if (req != NULL) {
    JAddStringToObject(req, "file", "sensors.qo");
    JAddStringToObject(req, "format", "compact");
    JAddNumberToObject(req, "port", 10);

    J *body = JAddObjectToObject(req, "body");
    if (body != NULL) {
      JAddNumberToObject(body, "team_id", TUINT8);
      JAddNumberToObject(body, "counter", TUINT32);
      JAddNumberToObject(body, "temp", TFLOAT32);
      JAddNumberToObject(body, "humidity", TFLOAT32);
      JAddNumberToObject(body, "battery", TFLOAT32);
    }

    Serial.println("Enviando note.template...");
    notecard.sendRequest(req);
  }

  delay(2000);

  Serial.println("Setup listo.");
}

void loop() {
  counter++;

  Serial.println();
  Serial.print("Enviando nota #");
  Serial.println(counter);

  J *req = notecard.newRequest("note.add");
  if (req != NULL) {
    JAddStringToObject(req, "file", "sensors.qo");
    JAddBoolToObject(req, "sync", true);

    J *body = JAddObjectToObject(req, "body");
    if (body != NULL) {
      JAddNumberToObject(body, "team_id", TEAM_ID);
      JAddNumberToObject(body, "counter", counter);
      JAddNumberToObject(body, "temp", 25.5);
      JAddNumberToObject(body, "humidity", 55.0);
      JAddNumberToObject(body, "battery", 3.7);
    }

    Serial.println("Enviando note.add...");
    notecard.sendRequest(req);
  }

  delay(2000);

  req = notecard.newRequest("hub.sync");
  if (req != NULL) {
    Serial.println("Forzando hub.sync...");
    notecard.sendRequest(req);
  }

  Serial.println("Esperando 60 segundos...");
  delay(60000);
}