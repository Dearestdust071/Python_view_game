int led[4] = {2,3,4,5};
int boton[4] = {8,9,10,11};
int power=12;
int estadoLed = LOW;
int puntuacion = 0;
unsigned long tiempoInicio;
bool juegoActivo = false;
int modoJuego = 0;
int puntuacionObjetivo;
int retardo=0;
unsigned long tiempoLimite;
int ultimoLed = -1; // Variable para almacenar el último LED encendido
int numLeds=0;
const int TIEMPO=30; //SEGUNDOS
String  msgboton;
bool mostrarlogs = true;

void setup() {
  pinMode(power, OUTPUT);
  for (int i = 0; i < 4; i++) {
    pinMode(led[i], OUTPUT);
  }
  for (int i = 0; i < 4; i++) {
    pinMode(boton[i], INPUT_PULLUP);
  }
  Serial.begin(9600);
  seleccionarModo();
}
void loop() {
  if (juegoActivo) {
    inicializar();
    while (juegoActivo) {
      jugar();
    }
  }
}

void seleccionarModo() {
  bool ModoRecibido = false;
  if(mostrarlogs){
    Serial.println("Selecciona el modo de juego:");
    Serial.println("0: Fácil");
    Serial.println("1: Medio");
    Serial.println("2: Difícil");
  }  
  while (Serial.available() == 0) {} // Espera a que el usuario ingrese un valor
  modoJuego = Serial.parseInt();
  switch (modoJuego) {
    case 0:
      puntuacionObjetivo = 25;
      tiempoLimite = TIEMPO*1000; // 1 minuto
      juegoActivo = true;
      retardo=20;
      break;
    case 1:
      puntuacionObjetivo = 50;
      tiempoLimite = TIEMPO*1000; // JUGAMOS CONE EL TIEMPO Y ESTA FACIL
      juegoActivo = true;
      retardo=15;
      break;
    case 2:
      puntuacionObjetivo = 75;
      tiempoLimite = TIEMPO*1000; // 30 SEGUNDOS
      juegoActivo = true;
      retardo=10;
      break;
    default:
      break;
  }
}
void inicializar() {
  puntuacion = 0;
  tiempoInicio = millis(); // Marca el tiempo inicial del juego
  //Serial.println("Comienza el juego");
}

void jugar() {
  if (millis() - tiempoInicio >= tiempoLimite) {
    terminarJuego(); // Si el tiempo se ha agotado, termina el juego inmediatamente
    return;
  }
  int ledAleatorio;
  do {
    ledAleatorio = random(0, 4);
  } while (ledAleatorio == ultimoLed); // Repite hasta que sea diferente al último LED
  numLeds++;
  ultimoLed = ledAleatorio; // Almacena el LED actual como el último LED encendido
  digitalWrite(led[ledAleatorio], HIGH);
  if(mostrarlogs){
    Serial.print("LED encendido: ");
    Serial.println(ledAleatorio + 1);
  }
  
  // CICLO PARA ESPERAR PRESIONADO DE BOTÓN
  int tiempo = 0;
  int botonPress = HIGH;
  bool acierto = false;
  // Espera hasta que se presione el botón o se acabe el tiempo límite de 1 segundo
  while (tiempo < retardo) {
    botonPress = digitalRead(boton[ledAleatorio]);
    if (botonPress == LOW) {
      acierto = true;
      break;
    }
    delay(50); // Espera 50 ms para verificar si hay cambios (Necesito ver si hay cambios)
    tiempo++;
  }
  digitalWrite(led[ledAleatorio], LOW); // Apaga el LED cuando termina el tiempo o se presiona el botón
  if (acierto) {
    puntuacion++; // Incrementa la puntuación si se presionó el botón a tiempo
    msgboton = "¡Acierto! Puntuación +1";
  } else {
    msgboton = "Fallaste. No se presionó a tiempo.";
  }
  if(mostrarlogs){
    Serial.println(msgboton);
    Serial.print("Puntuación actual: ");
    Serial.println(puntuacion);
  }
  
  if (millis() - tiempoInicio >= tiempoLimite) {
    terminarJuego(); // Termina el juego si se acabó el tiempo límite
  }
}

void terminarJuego() {
  juegoActivo = false; // Desactiva el juego
  float resultado;
  resultado=((float)puntuacion/(float)numLeds)*1000.0;//necesito convertirlo
  if(mostrarlogs){
    Serial.println(numLeds); 
    Serial.println(puntuacion);  
    Serial.print("Juego terminado. Puntuación final: ");
    Serial.println((int)resultado);
  }  
  Serial.write(modoJuego); //Envia la dificultad
  Serial.write((int)resultado); //Envia el score hacia RaspBerry PI
  seleccionarModo();
}
