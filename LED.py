from machine import Pin
from time import sleep

pin = Pin(15, Pin.OUT)

while True:
    pin.on()
    sleep(.001)
    pin.off()
    sleep(.005)