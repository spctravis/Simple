import RPi.GPIO as GPIO

__green = 23

__yellow = 24

__red = 18

LED = [__green, __red, __yellow]

def __off(LEDs):
    GPIO.output(LED, GPIO.LOW)

def __on(LEDs):
    GPIO.output(LED, GPIO.HIGH)

def red():
    __off(__green)
    __off(__yellow)
    __on(__red)

def yellow():
    __off(__green)
    __off(__red)
    __on(__yellow)

def green():
    __off(__red)
    __off(__yellow)
    __on(__green)

