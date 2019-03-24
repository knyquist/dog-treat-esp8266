import machine
import time


def led_on():
    print('Performing action: turn LED 2 on')
    pin = machine.Pin(2, machine.Pin.OUT)
    pin.value(0)

def led_off():
    print('Performing action: turn LED 2 off')
    pin = machine.Pin(2, machine.Pin.OUT)
    pin.value(1)

# 0, 4, 5, 16

def motor_fwd(cycles=512):
    print('Performing action: rotate motor forward')
    in4 = machine.Pin(0, machine.Pin.OUT)
    in3 = machine.Pin(4, machine.Pin.OUT)
    in2 = machine.Pin(5, machine.Pin.OUT)
    in1 = machine.Pin(16, machine.Pin.OUT)

    for i in range(0, cycles):
        in4.value(1)
        in3.value(1)
        in2.value(0)
        in1.value(0)
        time.sleep(0.0021)

        in4.value(0)
        in3.value(1)
        in2.value(1)
        in1.value(0)
        time.sleep(0.0021)

        in4.value(0)
        in3.value(0)
        in2.value(1)
        in1.value(1)
        time.sleep(0.0021)

        in4.value(1)
        in3.value(0)
        in2.value(0)
        in1.value(1)
        time.sleep(0.0021)

def motor_rev(cycles=512):
    print('Performing action: rotate motor reverse')
    in4 = machine.Pin(0, machine.Pin.OUT)
    in3 = machine.Pin(4, machine.Pin.OUT)
    in2 = machine.Pin(5, machine.Pin.OUT)
    in1 = machine.Pin(16, machine.Pin.OUT)

    for i in range(0, cycles):
        in4.value(0)
        in3.value(0)
        in2.value(1)
        in1.value(1)
        time.sleep(0.0021)

        in4.value(0)
        in3.value(1)
        in2.value(1)
        in1.value(0)
        time.sleep(0.0021)

        in4.value(1)
        in3.value(1)
        in2.value(0)
        in1.value(0)
        time.sleep(0.0021)

        in4.value(1)
        in3.value(0)
        in2.value(0)
        in1.value(1)
        time.sleep(0.0021)
