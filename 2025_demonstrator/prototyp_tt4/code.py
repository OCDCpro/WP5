# SPDX-FileCopyrightText: 2024 Fabio Ramirez Stern
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Put this on the RPi Pico controlling the RFID chip, not the RP2040 on the TT04 dev board!

# IMPORTS
import board
import busio
import digitalio

from adafruit_pn532.spi import PN532_SPI

# SPI-Interface & PN532 SETUP
spi = busio.SPI(board.GP2, board.GP3, board.GP4) # SPI0 inteface standard pins
cs_pin = digitalio.DigitalInOut(board.GP5)
pn532 = PN532_SPI(spi, cs_pin, debug=False)
ic, ver, rev, support = pn532.firmware_version
print("Found PN532 with firmware version: {0}.{1}".format(ver, rev))
pn532.SAM_configuration()


# LED SETUP
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# TT04 BOARD SETUP
"""
tt04_unlocked = digitalio.DigitalInOut(board.)
"""


previous = False

while True:
    # Check if a card is available to read
    uid = pn532.read_passive_target(timeout=0.5)
    # Try again if no card is available.
    if uid is None:
        led.value = False
        print(".", end="")
        previous = False
        continue
    else:
        if previous != uid:
            print(uid.hex())
            if uid.hex() == "f7f93600":
                print("Match!")
                led.value = True
        previous = uid
