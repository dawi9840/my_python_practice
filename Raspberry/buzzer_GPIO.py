import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
pin_b = 17
GPIO.setup(pin_b, GPIO.OUT)

try:
 print("Ctrl + C to close")
 GPIO.output(pin_b, True)
 sleep(0.1)
 GPIO.output(pin_b, False)
 sleep(0.1)
except  KeyboardInterrupt:
 print("close!!")
finally:
 GPIO.cleanup()
