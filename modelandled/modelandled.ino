  int switch1 = 2;    
  int switch2 = 3;   
  int switch3 = 4; 
  int rbpin = 5;     
  
  int relePins[] = { 0, 8, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7 };
  
  int arrayState[]  = {0,0,0};

  int sw1 = 0;
  int sw2 = 0;
  int sw3 = 0;

  int atr = 0; 

  void setup() {
    
    Serial.begin(9600);
    
    pinMode(switch1, INPUT);  
    pinMode(switch2, INPUT);   
    pinMode(switch3, INPUT); 
    
    pinMode(5, OUTPUT);   
    pinMode(6, OUTPUT);   
    pinMode(7, OUTPUT); 
    pinMode(8, OUTPUT); 

    pinMode(rbpin, OUTPUT);  
    digitalWrite(rbpin, HIGH);
    
    digitalWrite(5, HIGH);
    digitalWrite(6, HIGH);
    digitalWrite(7, HIGH);
    digitalWrite(8, HIGH);
    
    arrayState[0] = 0;
    arrayState[1] = 0;
    arrayState[2] = 0;
    
    sw1 = digitalRead(switch3);
    sw2 = digitalRead(switch2);
    sw3 = digitalRead(switch1);

    Serial.print(sw1);
    Serial.print(sw2);
    Serial.print(sw3);
        
    int atr = 0; 
    
  }
        
     
  void loop() {
    String codigo = "";
    
    sw1 = digitalRead(switch3);
    sw2 = digitalRead(switch2);
    sw3 = digitalRead(switch1);

    delay(200);

    if ( arrayState[0] != sw1){
       arrayState[0] = sw1;
       atr = 1;
    }

    if (arrayState[1]!= sw2){
       arrayState[1] = sw2;
       atr = 1;
   }
   
    if (arrayState[2]!= sw3){
       arrayState[2] = sw3;
       atr = 1;  
   }
   
    if(atr == 1){ 
        digitalWrite(rbpin,LOW);
        delay(100);
        digitalWrite(rbpin,HIGH);
        atr = 0;        
    }
    
    while(Serial.available() > 0){
      char ch = Serial.read();
      if (isDigit(ch)) { //Filtrado de entrada solo deja numeros 0 al 9
        codigo += ch;
      } 
    } 
    int data = codigo.toInt();

    if(data == 99){ 
        digitalWrite(rbpin,HIGH);
        Serial.print(arrayState[0]);
        Serial.print(arrayState[1]);
        Serial.print(arrayState[2]);
        //Serial.println();
        
 
    } else if (data < 99){
      if (data % 2 == 0){
        int auxpar = (data/2);
        digitalWrite(relePins[auxpar],HIGH); 
      }
      else if (data % 2 != 0) {
        int auximpar = ((data + 1)/2);
        digitalWrite(relePins[auximpar],LOW);
      }  
    }
 
  }
