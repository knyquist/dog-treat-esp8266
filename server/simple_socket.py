import usocket
from logic import make_decision


def start_listening(host="0.0.0.0", port=5000):
    s = usocket.socket(usocket.AF_INET,
                       usocket.SOCK_STREAM)
    s.setsockopt(usocket.SOL_SOCKET, usocket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        data = conn.recv(64)
        if len(data) > 0:
            print('Received signal: {}'.format(data))
            s.close()
            make_decision(data)
            start_listening(host=host, port=port)