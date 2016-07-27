import RPi.GPIO as GPIO


__buttonA = 5
__buttonB = 6
__buttonC = 13
__buttonReset = 26

button = [__buttonA, __buttonB, __buttonC, __buttonReset]


GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN)

pushedButtons = []
x = button()
GPIO.add_event_detect(button, GPIO.FALLING, callback=x, bouncetime=200)
pushedButtons.inputs.append(x)
print pushedButtons
