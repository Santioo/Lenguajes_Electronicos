from machine import Pin
from utime import sleep

print("Hello, ESP32!")

led = Pin(15, Pin.OUT)
led2 = Pin(2, Pin.OUT)

while True:
  led.on()
  sleep(1)
  led.off()
  led2.on()
  sleep(1)
  led2.off()
