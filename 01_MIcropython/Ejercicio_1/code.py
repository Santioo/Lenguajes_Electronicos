from machine import Pin
from utime import sleep

print("Hello, ESP32!")

espera = 1

led = Pin(15, Pin.OUT)
led2 = Pin(2, Pin.OUT)

while True:
  led.on()
  sleep(espera)
  led.off()
  led2.on()
  sleep(espera)
  led2.off()
