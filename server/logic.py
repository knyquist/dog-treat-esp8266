import commands as cmd


def make_decision(data):
    if data == b'LON':
        cmd.led_on()  # turn LED 2 on
    elif data == b'LOFF':
        cmd.led_off()  # turn LED 2 off
    else:
        print('Error: Input data not in allowed commands')
