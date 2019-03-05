import socket

def connect_to_socket(host='192.168.100.145', port=5000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s

def turn_led2_on():
    connect_to_socket().send(b'LON')

def turn_led2_off():
    connect_to_socket().send(b'LOFF')