import machine


def led_on():
    print('Performing action: turn LED 2 on')
    machine.Pin(2, machine.Pin.OUT)

def led_off():
    print('Performing action: turn LED 2 off')
    machine.Pin(2, machine.Pin.IN)