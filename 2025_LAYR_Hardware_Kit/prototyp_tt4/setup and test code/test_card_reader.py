# SPDX-FileCopyrightText: 2024 Fabio Ramirez Stern
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Put this on the RPi Pico controlling the RFID reader, not the RP2040 on the TT04 dev board!
"""
 This script checks for the presence of an NFC Card and prints out the UID if it finds any.
 Use this to check that RFID reader and NFC card are working.
"""

import board
import busio
import digitalio

from adafruit_pn532.spi import PN532_SPI

spi = busio.SPI(board.GP2, board.GP3, board.GP4) # SPI0 inteface standard pins
cs_pin = digitalio.DigitalInOut(board.GP5)
pn532 = PN532_SPI(spi, cs_pin, debug=False)

ic, ver, rev, support = pn532.firmware_version
print("Found PN532 with firmware version: {0}.{1}".format(ver, rev))

led = digitalio.DigitalInOut(board.LED) # setup
led.direction = digitalio.Direction.OUTPUT

pn532.SAM_configuration()

while True:
    # Check if a card is available to read
    uid = pn532.read_passive_target(timeout=0.5)
    # Try again if no card is available.
    if uid is None:
        led.value = False
        print(".", end="")
        continue
    else:
        print(uid.hex())
        led.value = True
