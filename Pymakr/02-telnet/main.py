# import machine
# import ubinascii
# ubinascii.hexlify(machine.unique_id())

import pycom
from network import WLAN
pycom.wifi_on_boot(True)
pycom.wifi_mode_on_boot(WLAN.AP)