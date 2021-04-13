import uuid
from bluetooth import *
import RPi.GPIO as GPIO
from time import sleep

led = 18
buz = 17


GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(buz, GPIO.OUT)

server_socket=BluetoothSocket(RFCOMM)
server_socket.bind(("", PORT_ANY))
server_socket.listen(1)
port = server_socket.getsockname()[1]
service_id = str(uuid.uuid4())

advertise_service(server_socket, "LEDServer",
                  service_id = service_id,
                  service_classes = [service_id, SERIAL_PORT_CLASS],
                  profiles = [SERIAL_PORT_PROFILE])

client_dict = { 'a':"btn_led_on", 'b':"btn_buz_on", 'c':"btn_led_off", 
                'd':"btn_buz_off", 'e':"btn_bebebe", 'f':"btn_buz_led"}

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
                if data == client_dict['a']:
                    GPIO.output(led, GPIO.HIGH)
                    print("Turn on the light")
                elif data == client_dict['b']:
                    GPIO.output(buz, GPIO.HIGH)
                    print("Turn on the buzzer")
                elif data == client_dict['c']:
                    GPIO.output(led, GPIO.LOW)
                    print("Turn off the light")
                elif data == client_dict['d']:
                    GPIO.output(buz, GPIO.LOW)
                    print("Turn off the buzzer")
                elif data == client_dict['e']:
                    for x in range(0, 10):
                        if x<10:
                            GPIO.output(buz, GPIO.HIGH)
                            sleep(0.1)
                            GPIO.output(buz, GPIO.LOW)
                            sleep(0.1)
                        else:
                            GPIO.output(buz, GPIO.LOW)
                    print("Click the BeBeBe button")
                elif data == client_dict['f']:
                    for i in range(0, 10):
                        if i < 10:
                            GPIO.output(led, GPIO.HIGH)
                            GPIO.output(buz, GPIO.HIGH)
                            sleep(0.1)
                            GPIO.output(led, GPIO.LOW)
                            GPIO.output(buz, GPIO.LOW)
                            sleep(0.1)
                        else:
                            GPIO.output(led, GPIO.LOW)
                            GPIO.output(buz, GPIO.LOW)
                    print("Click the BeBeBe button")
                else:
                    print('Unknown Command: {}'.format(data))
        except IOError:
            pass
        client_socket.close()
        print("Stop Connection")
except KeyboardInterrupt:
    print("Close!!")
finally:
    if 'client_socket' in vars():
        client_socket.close()
    server_socket.close()
    GPIO.cleanup()
    print("Stop Connection")
