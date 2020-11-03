import pycom
import time

pycom.heartbeat(False)

while True:
    pycom.rgbled(0x330033)
    time.sleep(1)
    pycom.rgbled(0xFF5733)
    time.sleep(1)    
    pycom.rgbled(0x75FF33)
    time.sleep(1)
