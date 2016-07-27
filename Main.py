import RPi.GPIO as GPIO
from LEDs import red, green, yellow, LED
from Buttons import button, is_reset, get_code

class Main:

    def __int__(self, stoplight):
        self.stoplight = stoplight

    def bootstrap(self):
        print ("bootstrapping GPIO")
        GPIO.setup(GPIO.BCM)
        GPIO.setup(button, GPIO.IN)
        GPIO.setup(LED, GPIO.OUT)
        self.__bootstrap_callbacks()

        yellow()

    def __boostrap_callback(self):
        print("bootstrapping callbacks")
        GPIO.add_event_detect(button, GPIO.FALLING, callback=self.click_callback, bouncetime=200)

    def click_callback(self, channel):
        print ("Channel " + channel + "clicked")
        if is_reset(channel):
            print ("Resetting")
            yellow()
            self.stoplight.reset()
        else:
            value = get_code(channel)
            print ("Pushing value " + value)
            self.stoplight.push(value)
            valid = self.stoplight.validate()

            if valid:
                green()
            else:
                red()


