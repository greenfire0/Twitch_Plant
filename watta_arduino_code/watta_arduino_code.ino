int RxedByte = 0;

void setup() {
  pinMode(A1, OUTPUT); // Set analog pin A0 as output
  Serial.begin(9600); // Initialize serial communication at 9600 baud rate
}

void loop() {
  if (Serial.available() > 0) {
    RxedByte = Serial.read(); // Read the incoming byte
        digitalWrite(A1, HIGH); // Turn on the LED connected to analog pin A0
        delay(1000); // Wait for 1 second
        digitalWrite(A1, LOW); // Turn off the LED connected to analog pin A0

    }
  }

