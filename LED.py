from machine import Pin, PWM
import time

pwm = PWM(Pin(15))
pwm.freq(1000)

try:
    for i in range(0,10000):
        pwm.duty_u16(i)
        time.sleep_us(100)
    for i in range(20000,0,-1):
        pwm.duty_u16(i)
        time.sleep_us(100)
except:
    pwm.deinit()
    print('PWM deinit')