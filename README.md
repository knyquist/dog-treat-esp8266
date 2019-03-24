# ESP8266 w/ MicroPython
This repo contains code for provisioning an esp8266 (thing) with micropython. Using standard libraries, the thing is configured to listen on a websocket and perform actions when fed certain commands. For instructions on how to flash the thing with micropython look [here](https://docs.micropython.org/en/latest/esp8266/tutorial/index.html).

# First time connection over Serial
The serial_connect script provides an example for connecting to the thing over serial connection using picocom.

# Wifi connectivity
The thing can be configured to connect to wifi. To do this type the following commands
```
import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('wifi_name', 'wifi_password')
```

Once that works, connect to the thing over WebREPL for easy file transfer. Clone the [webrepl](https://github.com/micropython/webrepl) repo and open webrepl.html in your browser. Change the IP address in the top left to the IP address of the thing and hit Connect.

Enter your wifi credentials into ssid.info and transfer that file along with the python files in server/ to the thing using the WebREPL interface. Restart the thing by hitting the RST button or by powercycling the device. The thing should auto-connect to the wifi and start listening on port 5000.

# Commands
- `b'LON'` turns the onboard LED on
- `b'LOFF'` turns the onboard LED off
- `b'MFWD'` rotates the connected 28BYJ-48 forward one complete rotation
- `b'MREV'` rotates the connected 28BYJ-48 reverse one complete rotation

# GPIO Pins
My current knowlege of the mapping between micropython API pin IDs (left) and labels printed on each thing (right) is below. These may be specific to the particular models I purchased. No guarantees.

|    MicroPython    | Onboard |
| :---------------: | :-----: |
| `machine.Pin(0)`  | D0      |
| `machine.Pin(2)`  | LED     |
| `machine.Pin(4)`  | D1      |
| `machine.Pin(5)`  | D2      |
| `machine.Pin(16)` | D3      |
