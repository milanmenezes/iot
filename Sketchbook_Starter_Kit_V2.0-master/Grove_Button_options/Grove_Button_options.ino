// Demo for Grove - Starter V2.0
// Author: Loovee  2013-3-10

// Uses the Grove - Button to control the Grove - LED.
// Connect the Grove - Button to the socket marked D3
// Connect the Grove - LED to D7

// Defines the pins to which the button and LED are connected.
const int pinButton = 3;
const int pinLight = A2;
//const int pinLed   = 7;
int thresholdvalue = 300;
const int pinSound = A3;
int thresholdValue1 = 700;
int count=0;
bool flag=0;

int speakerPin = 7;                  // Grove Buzzer connect to D3


int length = 15; // the number of notes
char notes[] = "ccggaagffeeddc "; // a space represents a rest
int beats[] = { 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 4 };
int tempo = 300;

void playTone(int tone, int duration) {
    for (long i = 0; i < duration * 1000L; i += tone * 2) {
        digitalWrite(speakerPin, HIGH);
        delayMicroseconds(tone);
        digitalWrite(speakerPin, LOW);
        delayMicroseconds(tone);
    }
}

void playNote(char note, int duration) {
    char names[] = { 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'C' };
    int tones[] = { 1915, 1700, 1519, 1432, 1275, 1136, 1014, 956 };

    // play the tone corresponding to the note name
    for (int i = 0; i < 8; i++) {
        if (names[i] == note) {
            playTone(tones[i], duration);
        }
    }
}


void setup()
{
    // Configure the button's pin for input signals.
    pinMode(pinButton, INPUT);
     pinMode(speakerPin, OUTPUT);
    Serial.begin(9600);

    // Configure the LED's pin for output.
//    pinMode(pinLed, OUTPUT);
}

void loop()
{
    
    if(digitalRead(pinButton))
    {
        // When the button is pressed, turn the LED on.
//        digitalWrite(pinLed, HIGH);
        count+=1;
//        Serial.println("success1");
        delay(300);

    }
    else
    {
        // Otherwise, turn the LED off.
//        digitalWrite(pinLed, LOW);
//Serial.println("success2");
      if(count<=3){
        flag=1;
      }
      
    }
    
    
    if((millis()%5000)==0){
    if(!flag){
      Serial.println("long");
      count=0;
    }
    if(count==1){
      int sensorValue = analogRead(pinLight);
      if(sensorValue > thresholdvalue)
    {
      Serial.println("light detected");
    }
    else {
      Serial.println("light not detected");
    }
    }
    if(count==2){
      Serial.println("success2");
      for (int i = 0; i < length; i++) 
    {
        if (notes[i] == ' ')
        {
            delay(beats[i] * tempo); // rest
        }
        else
        {
            playNote(notes[i], beats[i] * tempo);
        }

        // pause between notes
        delay(tempo / 2);
    }
    }
    if(count==3){
      int sensorValue = analogRead(pinSound);
      if(sensorValue > thresholdValue1){
      Serial.println("Sound sensed");
      }
      else{
        Serial.println("Sound not sensed");
      }
    }
    
//    Serial.println(count);
    count=0;
    }
}

