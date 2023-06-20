from machine import ADC
from time import sleep

tempsensor = ADC(4)
conversion_factor = 3.3 / (65535) # 3.3V / 2^16

while True:
    current_voltage = tempsensor.read_u16() * conversion_factor
    temperature = 27 - (current_voltage - 0.706)/0.001721
    print(str(current_voltage) + " : " + str(temperature))
    sleep(2)