  
  int relePins[] = { 0, 8, 7, 6 };                     
                     
  int llavePins[] = { 0, 2, 3, 4 };                 
  
  int arrayState[]  = { 0, 0, 0, 0};

  int const cantRele = 3;
  int const cantLlave = 3;
  int rbpin = 5; 
  int swAux = 0;
  int flag = 0; 
  int data = 0;
  int auxPar = 0;
  int auxImpar = 0;

  void setup() {
    
    Serial.begin(9600);

    for (int i=1; i <= cantLlave; i++){ 
      pinMode( llavePins[i], INPUT);
    } 
    for (int i=1; i <= cantRele; i++){ 
      pinMode( relePins[i],OUTPUT);
    } 
    for (int i=1; i <= cantRele; i++){ 
      digitalWrite(relePins[i],HIGH);
    } 
    pinMode(rbpin, OUTPUT);   
    digitalWrite(rbpin, HIGH);
    
    
  }
     
  void loop() {
    
  
    for (int i=1; i <= cantLlave; i++){
      swAux = digitalRead(llavePins[i]);
      
      if(swAux == 0){
        digitalWrite(relePins[i],HIGH);
      }
      /*
      if(swAux == 1){
        digitalWrite(relePins[i],LOW);
      }
      */
      if ( arrayState[i] != swAux){
        arrayState[i] = swAux;
        digitalWrite(rbpin,LOW);
        delay(200);
        digitalWrite(rbpin,HIGH);
        for (int i=1; i <= cantLlave; i++){
          Serial.print(arrayState[i]);
       }
      }

    }
    Serial.println();
       String codigo = "";
    
    while(Serial.available() > 0){
      char ch = Serial.read();
      if (isDigit(ch)) { 
        codigo += ch;
      } 
    } 

    data = codigo.toInt();
    if ((data<100) && (data>0)){
   
      Serial.println("hola");
      Serial.println(data);

      if (data % 2 == 0){
        auxPar = (data/2);
        //arrayState[auxPar] = 0;
        digitalWrite(relePins[auxPar],HIGH); 
      }
      if (data % 2 != 0) {
        auxImpar = ((data + 1)/2);
        //arrayState[auxImpar] = 1;
        if (arrayState[auxImpar] == 1){
          digitalWrite(relePins[auxImpar],LOW);
        }
      } 

      
      delay(500);
      
    }


 }

    
