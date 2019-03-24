import usocket
from logic import make_decision
import gc


def listen(host="0.0.0.0", port=5000):
    s = usocket.socket(usocket.AF_INET,
                       usocket.SOCK_STREAM)
    try:
        s.setsockopt(usocket.SOL_SOCKET, usocket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(1)
        conn, addr = s.accept()
        data = conn.recv(64)
        if len(data) > 0:
            print('Received signal: {}'.format(data))
            make_decision(data)
    except:
        print('Error with socket connection')
    finally:
        s.close()
