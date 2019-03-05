def do_connect(essid, password):
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to wifi network...')
        wlan.connect(essid, password)
        while not wlan.isconnected():
            pass
    print('Network config: {}'.format(wlan.ifconfig()))