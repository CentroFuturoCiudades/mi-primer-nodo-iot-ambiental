void setup() {
  Serial.begin(115200);

  while (!Serial && millis() < 5000) {
  }

  Serial.println("Hola mundo IoT");
  Serial.println("La tarjeta está funcionando");
}

void loop() {
  Serial.println("El programa sigue corriendo");
  delay(1000);
}
