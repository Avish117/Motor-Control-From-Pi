
void setup() {
Serial.begin(9600);
Serial.write("ready");
}

void loop() {
if (Serial.available() > 0){
	const byte value = Serial.read();
	Serial.write(value);
}
}
