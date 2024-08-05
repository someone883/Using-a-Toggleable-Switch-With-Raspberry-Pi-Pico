import machine
import utime
button = machine.Pin(14, machine.Pin.IN)
while True:
    if button.value() == 0:
        print("ON")
        utime.sleep(1)
    else:
        print("OFF")
        utime.sleep(1)