int const cantRele = 20;
int const cantSwitch = 20;
int const cantArray = 24;

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

int llavePins[] = { 0, 1, 2, 3 };    

int relePins[] = { 0, 38, 40, 42, 44, 8, 3, 4, 5, 9, 2,
                   10, 11, 22, 24, 26, 28, 30, 32, 34, 36
                 };

int arrayState[]  = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                    };

int mensaje[]  =    { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
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


  for (int i = 1; i <= cantSwitch; i++) {
    swAux = digitalRead(switchPins[i]);
  
    if (swAux == 0) {
      digitalWrite(relePins[i], HIGH);
    }
    //-------------------------------------------
    /*
    else if (swAux == 1) {
      digitalWrite(relePins[i], LOW);
    }
    */
    //----------------------------------------
    if (arrayState[i] != swAux) {
      flag = 1;
    }
    
  }

  //-------------------------------------------------

    for (int i=0; i <= 3; i++){ 
      int auxa = analogRead(llavePins[i]);
      
      if (auxa > 100){
        auxa = 0;
      }else if (auxa < 100){
         auxa = 1;
      }

      
      if (auxa == 0) {
        if (i == 0) {analogWrite(A4,250);}
        if (i == 1) {analogWrite(A5,250);}
        if (i == 2) {analogWrite(A6,250);}
        if (i == 3) {analogWrite(A7,250);}
      }
      //-------------------------------------------
      /*
      else if (auxa == 1) {
        if (i == 0) {analogWrite(A4,0);}
        if (i == 1) {analogWrite(A5,0);}
        if (i == 2) {analogWrite(A6,0);}
        if (i == 3) {analogWrite(A7,0);}
      }
      */
      //----------------------------------------

      if (arrayState[i+21] != auxa) {
        flag = 1;
        arrayState[i+21] = auxa;
      }
      
    
    } 

  //------------------------------------------------
    
  if (flag == 1) {
     flag = 0;
     Serial.print('#');
     for (int i = 0; i <= cantArray; i++) {
       arrayState[i] = swAux;
       Serial.print(arrayState[i]);
     }
     Serial.print('*');
     Serial.print('\n');
      
     digitalWrite(rbpin, LOW);

  }

}


void loop() {

  

  for (int i = 1; i <= cantSwitch; i++) {
    swAux = digitalRead(switchPins[i]);
    if (swAux == 0) {
      digitalWrite(relePins[i], HIGH);
    }
    //-------------------------------------------
    /*
    else if (swAux == 1) {
      digitalWrite(relePins[i], LOW);
    }
    */
    //-------------------------------------------
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
  

    //-------------------------------------------------

    for (int i=0; i <= 3; i++){ 
      int auxa = analogRead(llavePins[i]);
      
      if (auxa > 100){
        auxa = 0;
      }else if (auxa < 100){
         auxa = 1;
      }

      if (auxa == 0) {
        if (i == 0) {analogWrite(A4,250);}
        if (i == 1) {analogWrite(A5,250);}
        if (i == 2) {analogWrite(A6,250);}
        if (i == 3) {analogWrite(A7,250);}
      }
      //----------------------------------------
      /*
      else if (auxa == 1) {
        if (i == 0) {analogWrite(A4,0);}
        if (i == 1) {analogWrite(A5,0);}
        if (i == 2) {analogWrite(A6,0);}
        if (i == 3) {analogWrite(A7,0);}
      }
      */
      //----------------------------------------


      if (arrayState[i+21] != auxa) {
        arrayState[i+21] = auxa;
        
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

  //------------------------------------------------

  /*
  if (flag == 1) {
 
    flag = 0;
  }
  */
  
  String codigo = "";
  char codigo2[30];
  int ini = 0;
  int fin = 0;

  int index = 0;
  while (Serial.available() > 0) {
    
    char ch = Serial.read();
    codigo2[index] = ch;
    index = index+1;

  }   

  int indice = 0;
  while ((indice < index)&&(fin == 0)) {

      char c = codigo2[indice];

      if (c == '#'){
        ini = 1;
        //Serial.println("encontre #");
      }

      if ((c != '#')&&(c != '*')){
        //Serial.println(c);
        if (ini == 1){
           if (isDigit(c)) {
              codigo+=c;
              mensaje []
           }
           //Serial.println(c);
        }
      }

      if ((c == '*')&&(ini == 1)){
         //Serial.println("encontre *");
         data = codigo.toInt();
         fin = 1;
         ini = 0;
      }

      indice = indice+1;

  }

    delay(100);

    if (fin == 1){
        fin = 0;
        if(data < 88){
           if(data <= 40){
              if (data % 2 == 0) {
                auxPar = (data / 2);
                digitalWrite(relePins[auxPar], HIGH);
              }    
              if (data % 2 != 0) {
                 auxImpar = ((data + 1) / 2);
                 digitalWrite(relePins[auxImpar], LOW);
              }
           }
           if(data > 40){
              data = data-40;
              if (data % 2 == 0) {
                if (data == 2) {analogWrite(A4,250);}
                if (data == 4) {analogWrite(A5,250);}
                if (data == 6) {analogWrite(A6,250);}
                if (data == 8) {analogWrite(A7,250);}
              }    
              if (data % 2 != 0) {
                 if (data == 1) {analogWrite(A4,0);}
                 if (data == 3) {analogWrite(A5,0);}
                 if (data == 5) {analogWrite(A6,0);}
                 if (data == 7) {analogWrite(A7,0);}
              }
           }

            
        }
        if (data == 99) {
          digitalWrite(rbpin, HIGH);
          Serial.print('#');
          for (int i = 0; i <= cantArray; i++) {
            Serial.print(arrayState[i]);
          }
          Serial.print('*');
          Serial.print('\n');
        }
        
        if (data == 88) {
          for (int i = 0; i <= cantArray-4; i++) {
            digitalWrite(relePins[i], HIGH);
          }
          analogWrite(A4,250);
          analogWrite(A5,250);
          analogWrite(A6,250);
          analogWrite(A7,250);

        }

    }


  ini = 0;
  fin = 0;
  index = 0;
  data = 0;
      
}







