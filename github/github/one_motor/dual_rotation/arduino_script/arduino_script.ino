#include <Stepper.h>

Stepper motor(200, 3, 5, 9, 11);

void setup() {
Serial.begin(9600);
Serial.write("ready");
}

void loop() {
if (Serial.available() > 0){
const byte value = Serial.read();
Serial.write(value);
motor.setSpeed(100);
motor.step(value);
delay(1000);
motor.step(-value);
delay(1000);
}

}
