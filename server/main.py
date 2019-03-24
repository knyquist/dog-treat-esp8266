import wifi_connect as wifi
import simple_socket as sock
import gc

with open('ssid.info', 'r') as f:
    wifi_name = f.readline().split('\n')[0]
    wifi_pwd = f.readline().split('\n')[0]

wifi.do_connect(wifi_name, wifi_pwd)

def main():
    # pass
    while True:
        sock.listen()
        gc.collect()

if __name__ == '__main__':
    main()
