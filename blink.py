import machine
import time

# Set up the LED
led = machine.Pin(25, machine.Pin.OUT)

# Blink the LED
while True:
    led.toggle()
    time.sleep(0.5)

# Save the file and run it on the Pico. The LED should blink on and off every half second.
