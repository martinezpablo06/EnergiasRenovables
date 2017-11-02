int const cantRele = 20;
int const cantSwitch = 20;
int const cantArray = 20;

int rbpin = 7;
int swAux = 0;
int data = 0;
int auxPar = 0;
int auxImpar = 0;
int flag = 0;
int flag2 = 0;

int switchPins[] = { 0, 48, 46, 52, 53, 50, 29, 23, 31, 25, 27,
                     35, 37, 33, 39, 41, 45, 49, 43, 51, 47
                   };

int relePins[] = { 0, 38, 40, 42, 44, 8, 3, 4, 5, 9, 2,
                   10, 11, 22, 24, 26, 28, 30, 32, 34, 36
                 };

int arrayState[]  = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                    };

void setup() {

  Serial.begin(9600);

  for (int i = 1; i <= cantSwitch; i++) {
    pinMode(switchPins[i], INPUT);
  }

  for (int i = 1; i <= cantRele; i++) {
    pinMode(relePins[i], OUTPUT);
  }
  for (int i = 1; i <= cantRele; i++) {
    digitalWrite(relePins[i], HIGH);
  }
  pinMode(rbpin, OUTPUT);
  digitalWrite(rbpin, HIGH);

  for (int i = 1; i <= cantArray; i++) {
    arrayState[i] = 0;
  }
}

void loop() {

  for (int i = 1; i <= cantSwitch; i++) {
    swAux = digitalRead(switchPins[i]);
    if (swAux == 0) {
      digitalWrite(relePins[i], HIGH);
    }
    if (arrayState[i] != swAux) {
      arrayState[i] = swAux;
      Serial.print('#');
      for (int i = 0; i <= cantArray; i++) {
        Serial.print(arrayState[i]);
      }
      Serial.print('*');
      Serial.print('\n');
      
      digitalWrite(rbpin, LOW);
      delay(100);
      digitalWrite(rbpin, HIGH);
      }
  }

  /*
  if (flag == 1) {
 
    flag = 0;
  }
  */
  
  String codigo = "";
  while (Serial.available() > 0) {
    char ch = Serial.read();
    if (isDigit(ch)) {
      codigo += ch;
    }
  }
  delay(100);
  data = codigo.toInt();

  if (data == 99) {
    
      Serial.print('#');
      for (int i = 0; i <= cantArray; i++) {
        Serial.print(arrayState[i]);
      }
      Serial.print('*');
      Serial.print('\n');
      
  }else if(data < 99){

      if (data % 2 == 0) {
        auxPar = (data / 2);
        digitalWrite(relePins[auxPar], HIGH);
      }
      
      if (data % 2 != 0) {
         auxImpar = ((data + 1) / 2);
         digitalWrite(relePins[auxImpar], LOW);
      }
  }

}
