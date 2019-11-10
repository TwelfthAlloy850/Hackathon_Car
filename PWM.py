import RPi.GPIO as GPIO
import time

escPIN = 17
servoPIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(escPIN, GPIO.OUT)
GPIO.setup(servoPIN, GPIO.OUT)

s = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
e = GPIO.PWM(escPIN, 50) # GPIO 18 for PWM with 50Hz

def RUN():
    e.start(7.5)
    s.start(2.5)
    s.ChangeDutyCycle(7.2)
    e.ChangeDutyCycle(7.5)
    time.sleep(3)
    e.ChangeDutyCycle(8.05)
    time.sleep(1)
    s.ChangeDutyCycle(9.2)
    time.sleep(1)
    s.ChangeDutyCycle(7.2)
    time.sleep(1)
    s.ChangeDutyCycle(5.8)
    time.sleep(1)
    s.ChangeDutyCycle(7.2)
    time.sleep(1)
    e.stop()
    s.stop()

def TEST():
    dcycle = 8
    e.start(7.5)
    s.start(7.0)
    s.ChangeDutyCycle(7.03)
    time.sleep(1)
    for i in range(0,30):
        e.ChangeDutyCycle(7.98)
        time.sleep(0.05)
        e.ChangeDutyCycle(7.5)
        time.sleep(0.07)
        print("run")
    e.stop()
    
        
    
#RUN()
TEST()
