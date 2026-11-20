'''
boot.py is executed automatically on every boot before main.py is run. 

It is used to set up the network connection and initialize the onboard LED.
'''

import machine
import network
# import webrepl
import json




def do_connect():
    wlan = network.WLAN()
    if not wlan.isconnected():
        wlan.active(True)
        print('Connecting to network...')

        # Open and load the JSON configuration file
        try:
            with open("config.json", "r") as file:
                config = json.load(file)
            # Access the values using key dictionary lookup
            wifi_ssid = config["WIFI_SSID"]
            wifi_password = config["WIFI_PASSWORD"]
            print("Successfully loaded config for SSID:", wifi_ssid)
            wlan.connect(wifi_ssid, wifi_password)
        except OSError:
            print("Error: config.json file not found on the Pico filesystem.")
        except ValueError:
            print("Error: config.json contains invalid JSON syntax.")
        while not wlan.isconnected():
            machine.idle()
    print('Connection established.\n')
    print('Network config:', wlan.ipconfig('addr4'))
    # webrepl.start()


# Initialize onboard LED
led = machine.Pin('LED', machine.Pin.OUT)
# Turn on the LED to indicate power and successful connection
led.off()
do_connect()
led.on()
