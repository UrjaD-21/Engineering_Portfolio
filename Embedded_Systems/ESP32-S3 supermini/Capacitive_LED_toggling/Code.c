#define TOUCH_PIN 4
#define LED_PIN 5

bool ledState = false;
bool lastTouchState = false;

void setup() {
  pinMode(TOUCH_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  bool currentTouchState = digitalRead(TOUCH_PIN);

  // Detect rising edge (touch just happened)
  if (currentTouchState == HIGH && lastTouchState == LOW) {
    ledState = !ledState;              // Toggle LED state
    digitalWrite(LED_PIN, ledState);   // Update LED
    delay(200); // simple debounce
  }

  lastTouchState = currentTouchState;
}

