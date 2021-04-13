import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

led = 18
btn = 2 
buz = 17
light = 4

GPIO.setup(led, GPIO.OUT)
GPIO.setup(btn, GPIO.OUT)
GPIO.setup(buz, GPIO.OUT)

def rc_time (light):
    count = 0 
    #Output on the pin for 
    GPIO.setup(light, GPIO.OUT)
    GPIO.output(light, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(light, GPIO.IN)  

    #Count until the pin goes high
    while (GPIO.input(light) == GPIO.LOW):
        count += 1
    return count

light_count = rc_time(light)

try:
 print("Ctrl + C to close!", sep = "\n")
 print('Count: {0:.1f}'.format(light_count))
 while True:
  #print('Count: {0:.1f}'.format(light_count))
  if GPIO.output(btn, True):
   for i in range(0, 10):
    if i <10:
     GPIO.output(led, True)
     GPIO.output(buz, True)
     sleep(0.1)
     GPIO.output(led, False)
     GPIO.output(buz, False)
     sleep(0.1)
    else:
     GPIO.output(led, False)
     GPIO.output(buz, False)
except KeyboardInterrupt:
 print("Close!!")
finally:
 GPIO.cleanup()