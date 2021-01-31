/*
   Created by ArduinoGetStarted.com

   This example code is in the public domain

   Tutorial page: https://arduinogetstarted.com/tutorials/arduino-http-request
*/

#include <SPI.h>
#include <Ethernet.h>
#include <Wire.h>
#include <Adafruit_PN532.h>

#define PN532_IRQ  9

Adafruit_PN532 nfc(PN532_IRQ, 100);

// replace the MAC address below by the MAC address printed on a sticker on the Arduino Shield 2
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };

EthernetClient client;

int    HTTP_PORT   = 4567;
String HTTP_METHOD = "GET"; // or POST
char   HOST_NAME[] = "192.168.1.153";
String ROUTE   = "/read";
String answer() {
  String ans = "";
  while (client.connected()) {
    if (client.available()) {
      char c = client.read();
      ans += c;
    }
  }
  return ans;
}

void sendargs(String argname, String arg) {
  Serial.println();
  if (client.connect(HOST_NAME, HTTP_PORT)) {
    Serial.println("Connected to server");

    client.println(HTTP_METHOD + " " + ROUTE + argname + "?=" + arg + " HTTP/1.1");
    client.println("Host: " + String(HOST_NAME));
    client.println("Connection: close");
    client.println();
    answer();

    client.stop();
    Serial.println();
    Serial.println("disconnected");
  } else {// if not connected:
    Serial.println("connection failed");
  }


}

void setup() {
  Serial.begin(9600);

  // initialize the Ethernet shield using DHCP:
  if (Ethernet.begin(mac) == 0) {
    Serial.println("Failed to obtaining an IP address using DHCP");
    while (true);
  }

  nfc.begin();
  int versiondata = nfc.getFirmwareVersion();
  if (!versiondata) {
    Serial.print("Didn't find RFID/NFC reader");
    while (1) {
    }
  }

  Serial.println("Found RFID/NFC reader");
  // настраиваем модуль
  nfc.SAMConfig();
  Serial.println("Waiting for a card ...");

}

void loop() {
  uint8_t success;
  uint8_t uid[4];
  uint8_t uidLength;
  success = nfc.readPassiveTargetID(PN532_MIFARE_ISO14443A, uid, &uidLength);
  if (success) {
    String ID = stringID(uid);
    sendargs("card", ID);
  }
   
}
String stringID(uint8_t f[]) {
  String CardID = "";
  for (byte i = 0; i < 4; i++)
    CardID += String(f[i], HEX);
  return CardID;
}
//bool функция проверки ответа получаящая на вход ответ
//функция открытия/закрытия дверей