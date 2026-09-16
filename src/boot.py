'''
boot.py is executed automatically on every boot before main.py is run. 

It is used to set up the network connection and initialize the onboard LED.
'''

import machine
import network
import config
import webrepl

def do_connect():
    wlan = network.WLAN()
    if not wlan.isconnected():
        wlan.active(True)
        print('Connecting to network...')
        wlan.connect(config.WIFI_SSID, config.WIFI_PASSWORD)
        while not wlan.isconnected():
            machine.idle()
    print('Connection established.\n')
    print('Network config:', wlan.ipconfig('addr4'))
    webrepl.start()


# Initialize onboard LED
led = machine.Pin('LED', machine.Pin.OUT)
# Turn on the LED to indicate power and successful connection
led.off()
do_connect()
led.on()
