# Simple Philips Hue script for alerting when a device does not respond to ping requests anymore
# Bjoern Heller <tec(att)sixtopia.net>

from phue import Bridge
import time
import subprocess

def set_lights_red(bridge):
    red = [0.675, 0.322]
    brightness = 254  # Max brightness
    bridge.set_group(1, 'on', True)
    bridge.set_group(1, 'bri', brightness)
    bridge.set_group(1, 'xy', red)

def turn_lights_off(bridge):
    bridge.set_group(1, 'on', False)

def ping_host(host):
    try:
        subprocess.check_output(["ping", "-c", "1", "-W", "1", host])  # -W 1 sets the timeout to 1 second
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    # Replace 'your_bridge_ip' with the IP address of your Hue Bridge
    bridge_ip = '10.100.6.170'
    bridge = Bridge(bridge_ip)

    # If this is your first time connecting to the bridge, press the button on the bridge and run this once
    # bridge.connect()

    # Initialize the bridge
    bridge.connect()

    # Set the initial lights state to off
    turn_lights_off(bridge)
    lights_on = False

    while True:
        if not ping_host("10.100.6.182"):
            set_lights_red(bridge)
            lights_on = True
            time.sleep(0.2)  # Turn the light on for 500ms
            turn_lights_off(bridge)
            lights_on = False
            time.sleep(0.1)  # Wait for 500ms before checking ping again
        else:
            if lights_on:
                turn_lights_off(bridge)
                lights_on = False
        time.sleep(0.1)  # Wait for 100ms between ping checks

if __name__ == "__main__":
    main()
