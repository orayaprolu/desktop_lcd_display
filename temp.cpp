#include <WiFi.h>
#include <AsyncTCP.h>
#include <ESPAsyncWebServer.h>
#include <HTTPClient.h>


const char* ssid = "Snapple";
const char* password = "Shinsuke0531";
const String flaskServer = "http://192.168.254.161:4000";
const int ledPin = 13;  // Change this to the actual pin number where your LED is connected

AsyncWebServer server(80);

void setup() {
  Serial.begin(115200);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Configure LED pin
  pinMode(ledPin, OUTPUT);

  // Route for turning on LED
  server.on("/on", HTTP_GET, [](AsyncWebServerRequest *request){
    String message;
    if (trigger_action("H")) {
      message = "Turned on LED on ESP32";
    } else {
      message = "Failed to turn on LED on ESP32";
    }
    request->send(200, "text/plain", message);
  });

  // Route for turning off LED
  server.on("/off", HTTP_GET, [](AsyncWebServerRequest *request){
    String message;
    if (trigger_action("L")) {
      message = "Turned off LED on ESP32";
    } else {
      message = "Failed to turn off LED on ESP32";
    }
    request->send(200, "text/plain", message);
  });

  // Endpoint to receive the trigger from Flask server
  server.on("/receive_image", HTTP_GET, [](AsyncWebServerRequest *request){
    Serial.println("Received trigger from Flask server");

    // Make a GET request to the Flask server's /get_image endpoint to fetch the image
    HTTPClient http;
    http.begin(flaskServer + "/get_image"); // Replace with your Flask server's /get_image endpoint
    int httpResponseCode = http.GET();

    if (httpResponseCode == HTTP_CODE_OK) {
      Serial.println("Image fetched successfully");

      // Supposed to recieve a bitmap image from /get_image and I want to save that image locally on my esp32
      response = ... 
      
    } else {
      Serial.print("Failed to fetch image. Response code: ");
      Serial.println(httpResponseCode);
    }

    http.end();
    request->send(200, "text/plain", "Image received and processed");
  });

  // Start server
  server.begin();
}

void loop() {
  // Other code in loop if needed
}

bool trigger_action(String action) {
  if (action == "H") {
    digitalWrite(ledPin, HIGH);
  }
  else if (action == "L") {
    digitalWrite(ledPin, LOW);
  } else {
    return false;
  }

  return true; // Return true if action succeeded, false otherwise
}