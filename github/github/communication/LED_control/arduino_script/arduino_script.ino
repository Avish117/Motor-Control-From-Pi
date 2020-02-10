
void setup() {
Serial.begin(9600);
Serial.write("ready");
}

void loop() {
if (Serial.available() > 0){

const byte response = Serial.read();
Serial.write(response);

digitalWrite(LED_BUILTIN, HIGH);
delay(1000);
digitalWrite(LED_BUILTIN, LOW);

}
}
