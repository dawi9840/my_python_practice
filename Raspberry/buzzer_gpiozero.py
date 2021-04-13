from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(17)

try:
 print("Ctrl + C to close")
 while True:
  buzzer.on()
  sleep(0.1)
  buzzer.off()
  sleep(0.1)
except KeyboardInterrupt:
 print("\n close")
finally:
 buzzer.close()
