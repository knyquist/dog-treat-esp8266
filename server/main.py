import wifi_connect as wifi
import simple_socket as sock
import time

with open('ssid.info', 'r') as f:
    wifi_name = f.readline().split('\n')[0]
    wifi_pwd = f.readline().split('\n')[0]

wifi.do_connect(wifi_name, wifi_pwd)

def main():
    while True:
        sock.start_listening()

if __name__ == '__main__':
    main()