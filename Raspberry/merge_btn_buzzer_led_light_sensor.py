from gpiozero import LED, Button, Buzzer, LightSensor
from time import sleep

led = LED(18)
btn = Button(2) 
buz = Buzzer(17)
light = LightSensor(4)

try:
 print("Ctrl + C to close!")
 while True:
  print("light value: ", light.value)
  if btn.wait_for_press():
   for i in range(0, 10):
    if i <10 and light.value <= 0.96:
     led.on()
     buz.on()
     sleep(0.1)
     led.off()
     buz.off()
     sleep(0.1)
    else:
     led.off()
     buz.off()
except KeyboardInterrupt:
 print("Close!!")
finally:
 led.close()
 btn.close()
 buz.close()
 light.close()
