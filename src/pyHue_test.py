# Simple Philips Hue demo using phue library
# Bjoern Heller <tec(att)sixtopia.net>

from phue import Bridge
import time

def turn_lights_on(bridge):
    bridge.set_group(1, 'on', True)

def turn_lights_off(bridge):
    bridge.set_group(1, 'on', False)

def main():
    # Replace 'your_bridge_ip' with the IP address of your Hue Bridge
    bridge_ip = '10.100.6.170'
    bridge = Bridge(bridge_ip)

    # If this is your first time connecting to the bridge, press the button on the bridge and run this once
    # bridge.connect()

    # Initialize the bridge
    bridge.connect()

    # Turn the lights on
    turn_lights_on(bridge)
    time.sleep(2)  # Wait for 2 seconds

    # Turn the lights off
    turn_lights_off(bridge)

if __name__ == "__main__":
    main()