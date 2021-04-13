import uuid
from bluetooth import *
from gpiozero import LED, Buzzer, LightSensor
from time import sleep

led = LED(18)
buz = Buzzer(17)
light = LightSensor(4)

server_socket=BluetoothSocket(RFCOMM)
server_socket.bind(("", PORT_ANY))
server_socket.listen(1)
port = server_socket.getsockname()[1]
service_id = str(uuid.uuid4())

advertise_service(server_socket, "LEDServer",
                  service_id = service_id,
                  service_classes = [service_id, SERIAL_PORT_CLASS],
                  profiles = [SERIAL_PORT_PROFILE])

c_dict = {'a':"btn_led_on", 'b':"btn_buz_on", 'c':"btn_led_off", 
          'd':"btn_buz_off", 'e':"btn_bebebe", 'f':"btn_buz_led",
          'g':"btn_light_on", 'h':"btn_lihght_ctl_led_buz"}

try:
  print("Ctrl + C to close!")
  while True:
    print('Wait RFCOMM Channel {} for Connection'.format(port))
    client_socket, client_info = server_socket.accept()
    print('Receive connection from {}'.format(client_info))
    try:
      while True:
        data = client_socket.recv(1024).decode().lower()
        if len(data) == 0:
          break
        if data == c_dict['a']:
          led.on()
          print("LED on")
        elif data == c_dict['b']:
          buz.on()
          print("Buzzer on")
        elif data == c_dict['c']:
          led.off()
          print("LED off")
        elif data == c_dict['d']:
          buz.off()
          print("Buzzer off")
        elif data == c_dict['e']:
          for i in range(0, 10):
            if i < 10:
              buz.on()
              sleep(0.1)
              buz.off()
              sleep(0.1)
            else:
              buz.off()
          print("BeBe call")
        elif data == c_dict['f']:
          for x in range(0,10):
            if x < 10:
              led.on()
              buz.on()
              sleep(0.1)
              led.off()
              buz.off()
              sleep(0.1)
            else:
              led.off()
              buz.off()
          print("BeBe call with LED")
        elif data == c_dict['g']:
          print("light value: ", light.value)          
        elif data == c_dict['h']:
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
          print("value <= 0.96: LED and Buzzer On")
        else:
          print('Unknown Command: {}'.format(data))
except KeyboardInterrupt:
  print("Close!!")
finally:
  if 'client_socket' in vars():
      client_socket.close()
    server_socket.close()
    led.close()
    buz.close()
    print("Stop Connection")

