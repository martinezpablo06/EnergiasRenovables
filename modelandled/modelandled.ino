  int const cantRele = 3;
  int const cantSwitch = 3;
  int const cantArray = 3; 
  
  int rbpin = 5;     
  int swAux = 0;
  int data = 0;
  int auxPar = 0;
  int auxImpar= 0;
  
  int switchPins[] = { 0, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
                       
  int relePins[] = { 0, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
  
  int arrayState[]  = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

  void setup() {

    Serial.begin(9600);

    for (int i=1; i <= cantSwitch; i++){ 
      pinMode(switchPins[i], INPUT);
    } 
    for (int i=1; i <= cantRele; i++){ 
      pinMode(relePins[i],OUTPUT);
    } 
    for (int i=1; i <= cantRele; i++){ 
      digitalWrite(relePins[i],HIGH);
    } 
    pinMode(rbpin, OUTPUT);   
    digitalWrite(rbpin, HIGH);

    for (int i=1; i <= cantArray; i++){ 
      arrayState[i] = 0;
    }     
  }
             
  void loop() {

    for (int i=1; i <= cantSwitch; i++){ 
      swAux = digitalRead(switchPins[i]);

      if(swAux == 0){
        digitalWrite(relePins[i],HIGH);
      }
      
      if (arrayState[i] != swAux){
          arrayState[i] = swAux;
          for (int i=1; i <= cantArray; i++){
            Serial.print(arrayState[i]);
          }
          digitalWrite(rbpin,LOW);
          delay(200);
          digitalWrite(rbpin,HIGH);     
      }    
    }
    
    String codigo = ""; 
    
    while(Serial.available() > 0){
      char ch = Serial.read();
      if (isDigit(ch)) { 
        codigo += ch;
      } 
    } 

    data = codigo.toInt();

    if(data == 99){ 
       Serial.print(arrayState[1]);
       Serial.print(arrayState[2]);
       Serial.print(arrayState[3]);    
    } 
    if (data < 99){
      if (data % 2 == 0){
        auxPar = (data/2);
        digitalWrite(relePins[auxPar],HIGH); 
      }
      else if (data % 2 != 0) {
        auxImpar = ((data + 1)/2);
        digitalWrite(relePins[auxImpar],LOW);
      }  
    }
  }
