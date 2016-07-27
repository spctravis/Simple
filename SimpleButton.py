import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(18, GPIO.OUT)
prev_input = 0
x = []
GPIO.output(18, 0)

def printFuntion(channel):
    print("Button 1 Pressed")
    GPIO.add_event_detect(13, GPIO.FALLING, callback=printFuntion, bouncetime = 300)

while True:
    input = GPIO.input(13)
    if not input:
        start_time = time.time()
        GPIO.output(18, True)
        while not input:
            input = GPIO.input(13)
        else:
            end_time = time.time()
            GPIO.output(18, False)
            x.append({'start':start_time, 'end':end_time})
print x

GPIO.cleanup()


