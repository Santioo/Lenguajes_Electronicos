from machine import Pin
from utime import sleep

led = Pin(15, Pin.OUT)
led2 = Pin(2, Pin.OUT)

wait = 0.05

while True: 
    led.on()
    sleep(wait)
    led.off()
    led2.on()
    sleep(wait)
    led2.off()

    wait = wait + 0.01

    if wait == 0.2:
        wait = wait - 0.01
    elif wait == 0.05:
        wait = wait + 0.01
  
    
