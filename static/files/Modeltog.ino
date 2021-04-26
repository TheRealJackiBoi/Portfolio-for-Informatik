#define styrepin 4 // DCC out
#define dirpin 2 // inputpin for forward/reverse



unsigned char preample1; // global variabel for preample part 1
unsigned char preample2; // global variabel for preample part 2
unsigned char lokoadr; // global variabel for loko adresse
unsigned char data; // global variabel for kommando
unsigned char checksum; // global variabel for checksum
int Hastighed;
int Has1 = 0;
int Has2 = 79;
boolean a = false;


void setup()
{
  // put your setup code here, to run once:
  Serial.begin(115200);
  preample1 = 255; // preample 11111111
  preample2 = 255; // preample 11111111
  lokoadr = 11; // lokoadresse
  data = 0x79; // hastighed og retning, rew speed = 4
  // data =0x64; // forward speed = 4
  pinMode(styrepin,OUTPUT);// enable styrepin som output
  pinMode(dirpin,INPUT_PULLUP); // dirpin som input

  pinMode(A0,INPUT);
  Hastighed = analogRead(A0);
}

void loop()
{
  
  Hastighed = analogRead(A0)/31;
  /*put your main code here, to run repeatedly:
  if((digitalRead(dirpin)==HIGH))
  data = 0x64;
  else
  data = 0x44;*/

  
  
  if (Hastighed < 17) {Has1 = Hastighed; a = true;}
  if (Hastighed > 17) {Has1 = Hastighed; a = false;}

  
  Serial.print(Has1);
  Serial.print(" ");
  Serial.print(" ");
  Serial.print(" ");


  
  Has2 = Has1+100; 
  data = Has2;
  
  // Nu sendes hele “pakken” til toget
  // Den skal overholde DCC protokollen


  
  sendbyte(preample1); // send 11111111
  sendbyte(preample2); // send 11111111
  sendbit(0); // send 0 seperator
  sendbyte(lokoadr); // send adresse
  sendbit(0); // send 0 seperator
  sendbyte(data); // send data (command)
  sendbit(0); // send 0 seperator
  checksum=lokoadr^data; // make checksum
  sendbyte(checksum); // send checksum
  sendbit(1); // send stopbit
  sendbit(1); // send stopbit
  //Serial.println();
}
void sendbyte(unsigned char uch)
  { // sender byte bit for bit
  int a;
  for(a=128;a>0;a=a/2)
  { // pakker byte ud bit for bit
  if((uch&a)==0)
  sendbit(0);
  else
  sendbit(1);
  }
}

void sendbit(int b)
  {
  // sender 0 eller 1
  if(b==0)
  {
  digitalWrite(styrepin,HIGH);
  delayMicroseconds(116);
  digitalWrite(styrepin,LOW);
  delayMicroseconds(116);
  }
  else
  {
  digitalWrite(styrepin,HIGH);
  delayMicroseconds(58);
  digitalWrite(styrepin,LOW);
  delayMicroseconds(58);
  }
}
