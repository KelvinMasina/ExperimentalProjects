// Define pin numbers for ultrasonic sensor
const int trigPin = 12;
const int echoPin = 13;

// Variables for duration and distance calculation
long duration;
int distance;
int maxDistance = 14; // Maximum distance in centimeters, adjust according to your sensor's specifications

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Set ultrasonic sensor pins as input and output
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  // Send a short pulse to trigger the sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Measure the duration of the echo signal
  duration = pulseIn(echoPin, HIGH);

  // Calculate distance based on duration
  distance = duration * 0.034 / 2; // Speed of sound in air is approximately 0.034 cm/microsecond

  // Map distance to a percentage scale
  int levelPercentage = map(distance, 0, maxDistance, 100, 0);
  levelPercentage = constrain(levelPercentage, 0, 100); // Ensure the percentage is within 0-100 range

  // Print garbage level percentage to serial monitor
  Serial.print("Garbage Level: ");
  Serial.print(levelPercentage);
  Serial.println("%");

  Serial.print("{\"Lev\":");
  Serial.print(levelPercentage);
  Serial.println("}");

  delay(5000); // Delay between measurements
}
