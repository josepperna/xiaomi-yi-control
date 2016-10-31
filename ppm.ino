int ch1;
int ch2;

void setup() {
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(12, INPUT);
  pinMode(7, INPUT);
  Serial.begin(9600);
}

void loop() {

  ch2 = pulseIn(7, HIGH, 25000);
  ch1 = pulseIn(12, HIGH, 25000);
  if (ch1 > 1600){
    Serial.println("foto");
    digitalWrite (9, 1);
    delay (1000);
    digitalWrite (9, 0);
  }
    
  if (ch2 > 1600){
    Serial.println("inici video");
    digitalWrite (10, 1);
    delay (1000);
    digitalWrite (10,0);
  }
  if (ch2 > 1400 && ch2 < 1600){
    Serial.println("final video");
    digitalWrite (3, 1);
    delay (1000);
    digitalWrite (3,0);
  }
}





